import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

print(decrypt("9XB8nsIqRfYeswC", encrypted).decode('utf8'))