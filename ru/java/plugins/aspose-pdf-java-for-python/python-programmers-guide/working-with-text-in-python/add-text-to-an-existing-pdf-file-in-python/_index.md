---
title: Добавление текста в существующий PDF с использованием Python
type: docs
weight: 20
url: /ru/java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2021-06-05"
keywords: добавить текст pdf python, написать текст pdf python
description: Пример кода, как добавить или написать текст в документ PDF с использованием Python и библиотеки PDF.
---

## Написание или добавление текста в PDF с использованием Python

Чтобы добавить текстовую строку в документ Pdf, используя **Aspose.PDF Java for Python**, просто вызовите модуль **AddText**.

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("main text")
position=self.Position()
text_fragment.setPosition(position(100,600))

font_repository=self.FontRepository()
color=self.Color()

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))
text_fragment.getTextState().setFontSize(14)

text_builder=self.TextBuilder(pdf_page)
text_builder.appendText(text_fragment)

# Сохранить PDF файл
doc.save(self.dataDir + "Text_Added.pdf")
print "Текст добавлен успешно"
```


**Скачать Рабочий Код**

Скачать **Добавить Текст (Aspose.PDF)** с любого из нижеперечисленных сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)