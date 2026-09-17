---
title: Конвертация PDF в рабочую книгу Excel в Python
linktitle: Конвертация PDF в рабочую книгу Excel в Python
type: docs
weight: 20
url: /ru/java/convert-pdf-to-excel-workbook-in-python/
description: Узнайте, как конвертировать PDF‑документы в рабочие книги Excel в Python, используя Aspose.PDF для извлечения структурированных данных.
lastmod: "2026-09-17"
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

Скачайте **Convert PDF to Excel Workbook (Aspose.PDF)** с любого из перечисленных ниже сайтов для совместной разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)


