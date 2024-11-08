---
title: Извлечение текста со всех страниц PDF-документа на Python
type: docs
weight: 30
url: /ru/java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2021-06-05"
keywords: извлечение текста pdf python
description: Объясняет, как извлечь текст со страниц PDF в Python с использованием API формата файла PDF.
---

## Извлечение текста из PDF с помощью Python

Чтобы извлечь текст со всех страниц PDF-документа с использованием **Aspose.PDF Java for Python**, просто вызовите модуль **ExtractTextFromAllPages**.

```python

# Открыть целевой документ
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Текст успешно извлечен. Проверьте выходной файл."

```

**Скачать выполняемый код**

Скачайте **Извлечение текста со всех страниц (Aspose.PDF)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)