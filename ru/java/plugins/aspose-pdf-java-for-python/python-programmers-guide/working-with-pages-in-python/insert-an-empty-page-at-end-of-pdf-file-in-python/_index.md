---
title: Вставьте пустую страницу в конец PDF-файла в Python
linktitle: Вставьте пустую страницу в конец PDF-файла в Python
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-python/
description: Узнайте, как вставить пустую страницу в конец PDF-документа в Python с помощью Aspose.PDF для удобного расширения документа.
lastmod: "2026-06-09"
---
Чтобы вставить пустую страницу в конец PDF-документа с помощью **Aspose.PDF Java for Python**, просто вызовите класс **InsertEmptyPageAtEndOfFile**.

```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().add();

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```

**Загрузить рабочий код**

Загрузите **Вставьте пустую страницу в конец PDF-файла (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)
