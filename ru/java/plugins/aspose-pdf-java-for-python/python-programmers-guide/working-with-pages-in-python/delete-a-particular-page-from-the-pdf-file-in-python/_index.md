---
title: Удалить конкретную страницу из PDF‑файла в Python
linktitle: Удалить конкретную страницу из PDF‑файла в Python
type: docs
weight: 20
url: /ru/java/delete-a-particular-page-from-the-pdf-file-in-python/
description: Узнайте, как удалить конкретную страницу из PDF‑документа в Python с использованием Aspose.PDF, обеспечивая эффективное редактирование документов.
lastmod: "2026-08-19"
---
Чтобы удалить конкретную страницу из PDF‑документа с помощью **Aspose.PDF Java for Python**, просто вызовите класс **DeletePage**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# delete a particular page
pdf.getPages().delete(2)

# save the newly generated PDF file
doc.save(self.dataDir + "output.pdf")

print "Page deleted successfully!"

```

**Скачать работающий код**

Скачать **Delete Page (Aspose.PDF)**В из любого из указанных ниже сайтов для совместного программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)


