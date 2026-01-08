import random
import string
import json

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
# asks whether you want to encrypt or decrypt a message
decrypt_or_encrypt = input("Hello! welcome to the encryption program! do you want to encrypt or decrypt a message? (d/e): ")
if decrypt_or_encrypt == "d":
  import fetch
elif decrypt_or_encrypt == "e":
  try:
          with open('last_key.json', 'w') as f:
            json.dump( key, f, indent=4)
            print("The last generated key has been saved to 'last_key.json'.")
  except Exception as e:
    print(f"An error occurred while writing the file: {e}")
        

  #ENCRYPT#
  plain_text = input("Enter a message to encrypt: ")
  cipher_text = ""

  for letter in plain_text:
      index = chars.index(letter)
      cipher_text += key[index]

  print(f"original message : {plain_text}")
  print(f"encrypted message: {cipher_text}")
  view = input ("do you want to share the encryption key? (y/n): ")
if view == "y":
    print ("step one: open the file tab on the left that says last_key .json. step two select all of the text and copy it. step three e-mail that text to the person you want to share it with. to input the new text go back to last_key.json and delete all of the old text and paste in the new ones.")
else:
  print("ERROR!!! wrong input.")
