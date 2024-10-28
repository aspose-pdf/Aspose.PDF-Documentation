---
title: تحويل ملف SVG إلى تنسيق PDF في بايثون
type: docs
weight: 40
url: /java/convert-svg-file-to-pdf-format-in-python/
lastmod: "2021-06-05"
---

## كيفية تحويل ملف SVG إلى تنسيق PDF في بايثون

لتحويل ملف SVG إلى تنسيق PDF باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء وحدة **SvgToPdf**.

كود بايثون:

```python
options = self.SvgLoadOptions();
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'
احفظ الناتج بتنسيق XLS
doc.save(self.dataDir + "SVG1.pdf");
print "تم تحويل المستند بنجاح"
```

## تحميل الكود الجاري

حمل **تحويل SVG إلى PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/SvgToPdf/SvgToPdf.py)