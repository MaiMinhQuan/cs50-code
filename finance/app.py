import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

db.execute("""
    CREAT TABLE IF NOT EXITS users(
           id INTERGER PRIMARY KEY AUTOINCREMENT,
           username TEXT NOT NULL,
           hash TEXT NOT NULL,
           cash NUMERIC NOT NULL DEFAULT 10000.00
    )
""")

db.execute("""
    CREAT TABLE IF NOT EXITS transactions(
           id INTERGER PRIMARY KEY AUTOINCREMENT,
           user_id INTEGER NOT NULL
           symbol TEXT NOT NULL,
           shares INTEGER NOT NULL,
           price NUMERIC NOT NULL,
           timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
           FOREIGN KEY (user_id) REFERENCES users (id)
    )
""")

if name == "__main__":
    app.run()
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    rows = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    if len(rows) != 1:
        return apology("user not found", 400)
    cash = rows[0]["cash"]

    stocks = db.execute("SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0",
                        user_id)

    total_value = cash
    for stock in stocks:
        symbol = stock["symbol"]
        shares = stock["total_shares"]
        stock_info = lookup(symbol)
        if stock_info is None:
            return apology("lookup failed", 500)
        stock["name"] = stock_info["name"]
        stock["price"] = stock_info["price"]
        stock["value"] = stock_info["price"] * shares
        total_value += stock["value"]

    return render_template("index.html", stocks = stocks, cash = cash, total_value = total_value)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)
        if not request.form.get("shares"):
            return apology("must provide number of shares", 400)

        stock = lookup(request.form.get("symbol"))
        if stock is None:
            return apology("invalid symbol", 400)

        try:
            shares = int(request.form.get("shares"))
            if shares < 1:
                raise ValueError
        except ValueError:
            return apology("shares must be a positive integer", 400)

        user_id = session["user_id"]
        rows = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        if len(rows) != 1:
            return apology("user not found", 400)
        cash = rows[0]["cash"]

        total_cost = stock["price"] * shares

        if cash < total_cost:
            return apology("insufficient funds", 400)

        updated_cash = cash - total_cost
        result = db.execute("UPDATE users SET cash = ? WHERE id = ?", updated_cash, user_id)
        if not result:
            return apology("purchase failed", 500)

        result = db.execute("INSERT INTO transactions (user_id, symbol, shares, price, timestamp) VALUES (?, ?, ?, ?, ?)",
                            user_id,
                            stock["symbol"],
                            shares,
                            stock["price"],
                            datetime.datetime.now()
                            )
        if not result:
            return apology("purchase failed", 500)

        return redirect("/")
    else:
        return render_template("buy.html")




@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions = db.execute("SELECT symbol, shares, price, timestamp FROM transactions WHERE user_id = ? ORDER BY timestamp DESC", user_id)
    return render_template("history.html", transactions = transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)

        stock = lookup(request.form.get("symbol"))
        if stock is None:
            return apology("invalid symbol", 400)

        return render_template("quoted.html", stock =stock)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
