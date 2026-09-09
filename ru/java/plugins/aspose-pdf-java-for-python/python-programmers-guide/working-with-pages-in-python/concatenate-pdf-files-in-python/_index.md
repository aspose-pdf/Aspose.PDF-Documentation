---
title: Конкатенировать PDF файлы в Python
linktitle: Конкатенировать PDF файлы в Python
type: docs
weight: 10
url: /ru/java/concatenate-pdf-files-in-python/
description: Узнайте, как конкатенировать несколько PDF-файлов в один PDF-документ на Python с использованием Aspose.PDF, упрощая управление документами.
lastmod: "2026-08-19"
---
Чтобы конкатенировать PDF-файлы с помощью **Aspose.PDF Java for Python**, просто вызовите класс **ConcatenatePdfFiles**.

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

**Загрузить исполняемый код**

СкачатьВ **Concatenate PDF Files (Aspose.PDF)**В fromВ любой из указанных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)


