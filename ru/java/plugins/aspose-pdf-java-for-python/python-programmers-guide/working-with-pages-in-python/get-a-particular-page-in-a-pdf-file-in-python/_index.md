---
title: Получить определенную страницу в PDF-файле на Python
linktitle: Получить определенную страницу в PDF-файле на Python
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-python/
description: Узнайте, как извлечь определенную страницу из PDF-файла на Python с помощью Aspose.PDF для детальной обработки документов.
lastmod: "2026-06-09"
---
Чтобы получить конкретную страницу в PDF-документе с помощью **Aspose.PDF Java for Python**, просто вызовите класс **GetPage**.

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

 **Загрузить рабочий код**

Загрузите **Get Page (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)
