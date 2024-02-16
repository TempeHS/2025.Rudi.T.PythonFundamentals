def main():
    x = str.lower(input("give me the name of a file"))
    gif = x[-4:]
    jpg = x[-4:]
    jpeg = x[-5:]
    png = x[-4:]
    pdf = x[-4:]
    txt = x[-4:]
    zipz = x[-4:]
    if gif == str(".gif"):
        print("image/gif")
    elif jpg == str(".jpg"):
        print("image/jpeg")
    elif jpeg == str(".jpeg"):
        print("image/jpeg")
    elif png == str(".png"):
        print("image/png")
    elif pdf == str(".pdf"):
        print("application/pdf")
    elif txt == str(".txt"):
        print("text/plain")
    elif zipz == str(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

    
main()
