print("----YOU CAN ENCRYPT AND DECRYPT YOUR PRIVATE TEXT HERE----")
message=''
while(True):
        try:
            encrypt_or_decrypt = int(input("\n[*]Select: \n1.Encrypt \n2.Decrypt\n3.Exit\nEnter your choice: "))
            if(encrypt_or_decrypt==1):
                shift_key = int(input('Enter the number of letters that should be shifted: '))
                message=input('Enter the message to encrypt: ')
                # to encrypt data- (x+n)%26
                encrypted_data=''
                for i in message:
                    encrypted_data += chr(ord(i) + shift_key % 26)
                print(f'Encrypted text: {encrypted_data}')
            elif(encrypt_or_decrypt==2):
                shift_key = int(input('Enter the shift key that was used to encrypt the data: '))
                message=input('Enter the message to decrypt: ')
                # to decrypt data- (x-n)%26
                decrypted_data=''
                for i in message:
                    decrypted_data += chr(ord(i) - shift_key % 26)
                print(f'Decrypted text: {decrypted_data}')
            elif(encrypt_or_decrypt==3):
                break
            else:
                 print("Please enter valid input!!")

        except ValueError:
             print('Enter a valid value')






