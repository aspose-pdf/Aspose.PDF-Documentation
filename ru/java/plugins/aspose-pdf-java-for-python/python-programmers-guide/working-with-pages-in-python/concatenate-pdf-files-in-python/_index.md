---
title: Объединение PDF-файлов в Python
linktitle: Объединение PDF-файлов в Python
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-python/
description: Узнайте, как объединить несколько PDF-файлов в один PDF-документ на Python с помощью Aspose.PDF, что упрощает управление документами.
lastmod: "2026-06-09"
---
Чтобы объединить PDF-файлы с помощью **Aspose.PDF Java for Python**, просто вызовите класс **ConcatenatePdfFiles**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Open the source document
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# Add the pages of the source document to the target document
pdf1.getPages().add(pdf1.getPages())

# Save the concatenated output file (the target document)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "New document has been saved, please check the output file"
```

**Загрузить рабочий код**

Загрузите **Объединить PDF-файлы (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)
