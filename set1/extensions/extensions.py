fileName = input("File name: ").lower().strip().rpartition(".")

match fileName[2]:
    case "gif" | "png":
        print("image/" + fileName[2])
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "pdf" | "zip":
        print("application/" + fileName[2])
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")


