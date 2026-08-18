---
title: Извлечь текст со всех страниц PDF-документа в Python
linktitle: Извлечь текст со всех страниц PDF-документа в Python
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2026-06-09"
description: Объясняет, как извлечь текст из страниц PDF в Python с помощью API формата файла PDF.
---
## Извлеките текст из PDF с помощью Python

Чтобы извлечь документ TextrFrom All the Pages Pdf с помощью **Aspose.PDF Java for Python**, просто вызовите модуль **ExtractTextFromAllPages**.

```python

# Open the target document
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Text extracted successfully. Check output file."

```

**Загрузить рабочий код**

Загрузите **Извлечение текста со всех страниц (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)
