---
title: Конвертировать PDF в рабочую книгу Excel в Python
linktitle: Конвертировать PDF в рабочую книгу Excel в Python
type: docs
weight: 20
url: /ru/java/convert-pdf-to-excel-workbook-in-python/
description: Узнайте, как конвертировать PDF‑документы в рабочие книги Excel в Python, используя Aspose.PDF для извлечения структурированных данных.
lastmod: "2026-08-19"
---
Чтобы конвертировать PDF‑документ в рабочую книгу Excel, используя **Aspose.PDF Java for Python**, просто вызовите модуль **PdfToExcel**.

```python

doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# Instantiate ExcelSave Option object
excelsave=self.ExcelSaveOptions();

# Save the output to XLS format
doc.save(self.dataDir + "Converted_Excel.xls", excelsave);
print "Document has been converted successfully"
```

**Скачать Рабочий Код**

СкачатьВ **Convert PDF to Excel Workbook (Aspose.PDF)**В изВ любого из нижеупомянутых сайтов для совместного программирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)


