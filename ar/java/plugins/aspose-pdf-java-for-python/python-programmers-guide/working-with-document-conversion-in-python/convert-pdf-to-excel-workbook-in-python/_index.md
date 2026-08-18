---
title: تحويل PDF إلى Excel Workbook في بايثون
linktitle: تحويل PDF إلى Excel Workbook في بايثون
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-python/
description: تعرف على كيفية تحويل مستندات PDF إلى مصنفات Excel في Python باستخدام Aspose.PDF لاستخراج البيانات المنظمة.
lastmod: "2026-06-09"
---
لتحويل مستند PDF إلى Excel Workbook باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء وحدة **PdfToExcel**.

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

** تنزيل كود التشغيل **

تنزيل ** تحويل PDF إلى Excel Workbook (Aspose.PDF) ** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)
