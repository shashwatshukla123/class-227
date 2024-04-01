print("Welcome! To the of cryptography")

def main():
    print("Choose one option")
    choice=int(input("1. Encryption \n 2. Decryption \n Choose(1,2): "))
    if choice==1:
        encryption()
    elif choice==2:
        decryption()
    else:
        print("Wrong choice.")
    
def encryption():
    print("Encryption")
    msg=input("Enter the meassage: ")
    key=int(input("Enter key(1-94): "))
    encrypted_text=""
    for i in range(len(msg)):
        temp=(ord(msg[i])+key)
        if(temp>126):
            temp=temp-127+32
        encrypted_text+=chr(temp)
    print("Encryption: "+encrypted_text)    
    main()

def decryption():
    print("Decryption")
    print("Message can only be lower or upper case alphabet")
    encryption_msg=input("Enter encrypted text: ")
    decrypted_key=int(input("Enter key(1-94): "))
    decrypted_text=""
    for i in range(len(encryption_msg)):
        temp=(ord(encryption_msg[i])-decrypted_key)
        if(temp<32):
            temp=temp+127-32
        decrypted_text+=chr(temp)
    print("Decrypted: "+decrypted_text)

if __name__=="__main__":
    main()   