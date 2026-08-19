---
title: Вставить пустую страницу в конец PDF-файла на Python
linktitle: Вставить пустую страницу в конец PDF-файла на Python
type: docs
weight: 60
url: /ru/java/insert-an-empty-page-at-end-of-pdf-file-in-python/
description: Узнайте, как вставить пустую страницу в конец PDF‑документа на Python с помощью Aspose.PDF для удобного расширения документа.
lastmod: "2026-08-19"
---
Чтобы вставить пустую страницу в конец PDF‑документа, используя **Aspose.PDF Java for Python**, просто вызовите класс **InsertEmptyPageAtEndOfFile**.

```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().add();

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```

**Скачать запущенный код**

Скачать **Insert an Empty Page at End of PDF File (Aspose.PDF)**В изВ любого из перечисленных ниже сайтов совместного программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)

