alphabet = 'abcdefghijklmnopqrstuvwxyz'
cipher1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
cipher2 = "map"

# METHOD 1
def decipherText(cipher):
  shift = 2
  text = []
  for i in cipher:
    pos = alphabet.find(i)
    if (pos >= 0):
      text.append(alphabet[(pos+shift)%26])
    else:
      text.append(i)
  print(''.join(text))

decipherText(cipher1)
decipherText(cipher2)

# METHOD 2
b = 'cdefghijklmnopqrstuvwxyzab'
myTable = str.maketrans(alphabet, b)
print(cipher1.translate(myTable))
print(cipher2.translate(myTable))
