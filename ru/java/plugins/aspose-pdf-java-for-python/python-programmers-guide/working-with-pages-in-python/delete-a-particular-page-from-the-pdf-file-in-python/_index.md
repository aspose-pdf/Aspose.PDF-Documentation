---
title: Удалить определенную страницу из PDF-файла в Python
linktitle: Удалить определенную страницу из PDF-файла в Python
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-python/
description: Узнайте, как удалить определенную страницу из PDF-документа в Python с помощью Aspose.PDF, обеспечивая эффективное редактирование документа.
lastmod: "2026-06-09"
---
Чтобы удалить определенную страницу из PDF-документа с помощью **Aspose.PDF Java for Python**, просто вызовите класс **DeletePage**.

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

**Загрузить рабочий код**

Загрузите **Удалить страницу (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)
