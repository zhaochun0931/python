import easyocr

reader = easyocr.Reader(['ch_sim','en'])

result = reader.readtext('example.jpg')




for i in result:
  word = i[1]
  print(word)
