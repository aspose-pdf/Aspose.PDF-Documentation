---
title: Добавить текст в существующий PDF-файл с помощью Python
linktitle: Добавить текст в существующий PDF-файл с помощью Python
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2026-06-09"
description: Пример кода, как добавить или записать текст в документ PDF с помощью Python с библиотекой PDF.
---
## Напишите или добавьте текст в PDF с помощью Python

Чтобы добавить текстовую строку в документ PDF с помощью **Aspose.PDF Java for Python**, просто вызовите модуль **AddText**.

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

# Save PDF file
doc.save(self.dataDir + "Text_Added.pdf")
print "Text added successfully"
```

**Загрузить рабочий код**

Загрузите **Добавить текст (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)
