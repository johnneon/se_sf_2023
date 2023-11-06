from transformers import pipeline

translator = pipeline("translation", "facebook/wmt19-ru-en")

result = translator("Я обожаю инженерию машинного обучения!")

if (result[0] and result[0]["translation_text"]):
  print(result[0]["translation_text"])
  exit()


print("Не получилось перевести текст :(")
