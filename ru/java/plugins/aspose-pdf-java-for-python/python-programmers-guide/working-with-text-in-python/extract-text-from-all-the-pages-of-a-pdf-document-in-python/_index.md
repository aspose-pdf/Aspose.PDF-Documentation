---
title: Извлечь текст со всех страниц PDF‑документа в Python
linktitle: Извлечь текст со всех страниц PDF‑документа в Python
type: docs
weight: 30
url: /ru/java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2026-08-19"
description: Объясняет, как извлекать текст со страниц PDF в Python, используя API формата PDF‑файла.
---
## Извлеките текст из PDF с помощью Python

Чтобы извлечь TextrFrom всех страниц PDF‑документа с использованием **Aspose.PDF Java for Python**, просто вызовите модуль **ExtractTextFromAllPages**.

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

**Скачать исполняющий код**

СкачатьВ **Извлечь текст со всех страниц (Aspose.PDF)**В из В любого из указанных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)

