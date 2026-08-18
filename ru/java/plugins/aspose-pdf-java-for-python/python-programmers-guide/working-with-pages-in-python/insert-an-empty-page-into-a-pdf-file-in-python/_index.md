---
title: Вставьте пустую страницу в PDF-файл на Python
linktitle: Вставьте пустую страницу в PDF-файл на Python
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-python/
description: Узнайте, как вставить пустую страницу в любую позицию PDF-файла с помощью Python и Aspose.PDF для гибкого структурирования документа.
lastmod: "2026-06-09"
---
Чтобы вставить пустую страницу в документ PDF с помощью **Aspose.PDF Java for Python**, просто вызовите класс **InsertEmptyPage**.

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

**Загрузить рабочий код**

Загрузите **Вставьте пустую страницу (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)
