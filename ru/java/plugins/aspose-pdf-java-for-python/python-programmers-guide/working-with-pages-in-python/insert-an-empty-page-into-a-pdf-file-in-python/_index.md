---
title: Вставить пустую страницу в PDF‑файл с помощью Python
linktitle: Вставить пустую страницу в PDF‑файл с помощью Python
type: docs
weight: 70
url: /ru/java/insert-an-empty-page-into-a-pdf-file-in-python/
description: Узнайте, как вставить пустую страницу в любое положение в PDF‑файле, используя Python и Aspose.PDF для гибкой структуры документа.
lastmod: "2026-08-19"
---
Чтобы вставить пустую страницу в документ PDF, используя **Aspose.PDF Java for Python**, просто вызовите класс **InsertEmptyPage**.

```Python

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# insert a empty page in a PDF
pdf_document.getPages().insert(1)

# Save the concatenated output file (the target document)
pdf_document.save(self.dataDir + "output.pdf")

print "Empty page added successfully!"

```

**Скачать работающий код**

СкачатьВ **Вставить пустую страницу (Aspose.PDF)**В изВ любого из нижеупомянутых сайтов для совместного кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)

