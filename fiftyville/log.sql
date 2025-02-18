-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT description FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28;

SELECT transcript FROM interviews
WHERE year = 2021 AND month = 7 AND transcript LIKE '%bakery%';

SELECT bakery_security_logs.activity, bakery_security_logs.license_plate, people.name FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE bakery_security_logs.year = 2021
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute >= 15
AND bakery_security_logs.minute <= 25;

SELECT people.name, atm_t.transaction_type FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions AS atm_t ON bank_accounts.account_number = atm_t.account_number
WHERE atm_t.year = 2021
AND atm_t.month = 7
AND atm_t.day = 28
AND atm_t.atm_location = 'Leggett Street'
AND atm_t.transaction_type = 'withdraw';

ALTER TABLE phone_calls
ADD caller_name TEXT;

ALTER TABLE phone_calls
ADD receiver_name TEXT;

SELECT caller, caller_name, receiver, receiver_name FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60;

UPDATE phone_calls
SET caller_name = people.name
FROM people
WHERE people.phone_number = phone_calls.caller;

UPDATE phone_calls
SET receiver_name = people.name
FROM people
WHERE people.phone_number = phone_calls.receiver;

SELECT id, hour, minute, origin_airport_id, destination_airport_id FROM flights
WHERE year = 2021
AND  month = 7
AND day = 29
ORDER BY hour ASC
LIMIT 1;

UPDATE flights
SET origin_airport_id = airports.id
FROM airports
WHERE  flights.origin_airport_id = airports.id;

UPDATE flights
SET destination_airport_id = airports.id
FROM airports
WHERE  flights.destination_airport_id = airports.id;

SELECT airports.city, name, phone_number, license_plate FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON flights.id = passengers.flight_id
JOIN airports ON airports.id = flights.destination_airport_id
WHERE flights.id = 36
ORDER BY flights.hour ASC;

SELECT name from people
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON flights.id = passengers.flight_id
WHERE (flights.year = 2021 AND flights.month = 7 AND flights.day = 28 AND flights.id = 36)
AND name IN
(
    SELECT phone_calls.caller_name FROM phone_calls
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration < 60
)
AND name IN
(
    SELECT people.name FROM people
    JOIN bank_accounts ON people.id = bank_accounts.person_id
    JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
    WHERE atm_transactions.year = 2021
    AND atm_transactions.month = 7
    AND atm_transactions.day = 28
    AND atm_transactions.atm_location = 'Leggett Street'
    AND atm_transactions.transaction_type = 'withdraw'
)
AND name IN
(
    SELECT people.name FROM people
    JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
    WHERE bakery_security_logs.year = 2021
    AND bakery_security_logs.month = 7
    AND bakery_security_logs.day = 28
    AND bakery_security_logs.hour = 10
    AND bakery_security_logs.minute >= 15
    AND bakery_security_logs.minute <= 25
);