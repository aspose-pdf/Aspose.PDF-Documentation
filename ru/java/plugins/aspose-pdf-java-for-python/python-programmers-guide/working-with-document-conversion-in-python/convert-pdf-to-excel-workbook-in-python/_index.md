---
title: Преобразование PDF в книгу Excel на Python
linktitle: Преобразование PDF в книгу Excel на Python
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-python/
description: Узнайте, как конвертировать PDF-документы в книги Excel на Python с помощью Aspose.PDF для извлечения структурированных данных.
lastmod: "2026-06-09"
---
Чтобы преобразовать PDF-документ в книгу Excel с помощью **Aspose.PDF Java for Python**, просто вызовите модуль **PdfToExcel**.

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

**Загрузить рабочий код**

Загрузите **Конвертировать PDF в книгу Excel (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)
