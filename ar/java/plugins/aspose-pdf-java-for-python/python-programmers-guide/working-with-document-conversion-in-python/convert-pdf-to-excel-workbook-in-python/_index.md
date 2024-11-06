---
title: تحويل PDF إلى Excel Workbook في بايثون
type: docs
weight: 20
url: ar/java/convert-pdf-to-excel-workbook-in-python/
lastmod: "2021-06-05"
---

لتحويل مستند PDF إلى Excel Workbook باستخدام **Aspose.PDF Java for Python**، قم ببساطة باستدعاء وحدة **PdfToExcel**.

```python

doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# إنشاء كائن خيارات حفظ Excel
excelsave=self.ExcelSaveOptions();

# حفظ الناتج بتنسيق XLS
doc.save(self.dataDir + "Converted_Excel.xls", excelsave);
print "تم تحويل المستند بنجاح"
```

**تنزيل الكود الجاري**

قم بتنزيل **تحويل PDF إلى Excel Workbook (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)