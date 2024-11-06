---
title: Преобразование PDF в рабочую книгу Excel на Python
type: docs
weight: 20
url: ru/java/convert-pdf-to-excel-workbook-in-python/
lastmod: "2021-06-05"
---

Для преобразования PDF документа в рабочую книгу Excel с использованием **Aspose.PDF Java for Python**, просто вызовите модуль **PdfToExcel**.

```python

doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# Создание объекта ExcelSaveOption
excelsave=self.ExcelSaveOptions();

# Сохраните результат в формате XLS
doc.save(self.dataDir + "Converted_Excel.xls", excelsave);
print "Документ был успешно преобразован"
```

**Скачать исполняемый код**

Скачайте **Преобразование PDF в рабочую книгу Excel (Aspose.PDF)** с любого из указанных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)