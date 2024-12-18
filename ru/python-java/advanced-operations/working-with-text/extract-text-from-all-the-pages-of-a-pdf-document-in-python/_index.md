---
title: Извлечение текста со всех страниц PDF-документа на Python
type: docs
weight: 30
url: /ru/python-java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
---

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

**Скачать код для выполнения**

Скачайте **Извлечение текста со всех страниц (Aspose.PDF)** с любого из нижеупомянутых сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)