s = input("File name: ")
s = s.lower()
if ".gif" in s:
    print("image/gif")
elif ".png" in s:
    print("image/png")
elif ".jpg" in s:
    print("image/jpeg")
elif ".jpeg" in s:
    print("image/jpeg")
elif ".pdf" in s:
    print("application/pdf")
elif ".zip" in s:
    print("application/zip")
elif ".txt" in s:
    print("text/plain")
else:
    print("application/octet-stream")