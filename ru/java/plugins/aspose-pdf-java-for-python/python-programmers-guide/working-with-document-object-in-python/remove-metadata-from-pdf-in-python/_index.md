---
title: Удаление метаданных из PDF в Python
linktitle: Удаление метаданных из PDF в Python
type: docs
weight: 70
url: /ru/java/remove-metadata-from-pdf-in-python/
description: Узнайте, как удалить метаданные из PDF‑документов в Python с помощью Aspose.PDF, обеспечивая конфиденциальность и безопасность данных.
lastmod: "2026-09-17"
---
Чтобы удалить метаданные из PDF‑документа с помощью **Aspose.PDF Java for Python**, просто вызовите класс **RemoveMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# save update document with new information
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Removed metadata successfully, please check output file."

```

**Скачать исполняющий код**

Скачайте **Remove Metadata (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)


