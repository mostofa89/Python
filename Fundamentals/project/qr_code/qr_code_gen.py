import qrcode
def generate(path):
    try:
        with open(path, "r") as file:
            lines = file.readlines()

        if len(lines) < 2:
            print("Error: file must be contaion 2 lines.")
            return
        

        
        text = lines[0].strip()
        filename = lines[1].strip()

        qrCode_image = qrcode.make(text)
        qrCode_image.save(filename)
        print(f"QR Code has been saved successfully as {filename} ")


    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")

    except Exception as e:
        print(f"Unexpected error: '{e}'.")


generate("Fundamentals/project/qr_code/file.txt")