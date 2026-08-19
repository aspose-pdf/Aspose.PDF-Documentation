---
title: Получить конкретную страницу в PDF-файле на Python
linktitle: Получить конкретную страницу в PDF-файле на Python
type: docs
weight: 30
url: /ru/java/get-a-particular-page-in-a-pdf-file-in-python/
description: Исследуйте, как извлечь конкретную страницу из PDF‑файла на Python с использованием Aspose.PDF для подробной работы с документами.
lastmod: "2026-08-19"
---
Чтобы получить конкретную страницу в PDF‑документе, используя **Aspose.PDF Java for Python**, просто вызовите класс **GetPage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# get the page at particular index of Page Collection
pdf_page = pdf.getPages().get_Item(1)

# create a new Document object
new_document = self.Document()

# add page to pages collection of new document object
new_document.getPages().add(pdf_page)

# save the newly generated PDF file
new_document.save(self.dataDir + "output.pdf")

print "Process completed successfully!

```

 **Скачать исполняемый код**

Скачать **Get Page (Aspose.PDF)**В изВ любого из перечисленных ниже сайтов с открытым кодом:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)

