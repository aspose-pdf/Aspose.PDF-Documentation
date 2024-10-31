---
title: Добавление текста в существующий PDF файл на Python
type: docs
weight: 20
url: /python-java/add-text-to-an-existing-pdf-file-in-python/
---

Для добавления текстовой строки в документ Pdf с использованием **Aspose.PDF Java для Python**, просто вызовите модуль **AddText**.

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("основной текст")
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

print "Текст успешно добавлен"

```

**Скачать выполняемый код**

Скачайте **Add Text (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)