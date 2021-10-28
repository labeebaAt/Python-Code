# -*- coding: utf-8 -*-
"""Base64DecodingExample.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nNGeU-A7VbvY3l6tHLWVqm4cVvpUsGhT
"""

#Decoding Example

import base64

encodedStr = "aHR0cHM6Ly9naXRodWIuY29tLw=="

# Url Safe Base64 Decoding
decodedBytes = base64.urlsafe_b64decode(encodedStr)
decodedStr = str(decodedBytes, "utf-8")

print(decodedStr) 
print("\nAnother one: \n")
print(decodedBytes)