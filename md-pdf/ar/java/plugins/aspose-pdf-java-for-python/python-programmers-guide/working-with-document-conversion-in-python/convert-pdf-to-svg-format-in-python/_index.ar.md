---
title: تحويل PDF إلى تنسيق SVG في بايثون
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-python/
lastmod: "2021-06-05"
---

لتحويل PDF إلى تنسيق SVG باستخدام **Aspose.PDF Java لبايثون**، ببساطة قم باستدعاء وحدة **PdfToSvg**.

```python

# افتح المستند المستهدف
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# إنشاء كائن من SvgSaveOptions
save_options = self.SvgSaveOptions()

# لا تقم بضغط صورة SVG إلى أرشيف Zip
save_options.CompressOutputToZipArchive = False;

# احفظ الناتج بتنسيق XLS
doc.save(self.dataDir + "Output1.svg", save_options)

print "تم تحويل المستند بنجاح"
```

**تحميل الكود الجاري**

قم بتحميل **تحويل PDF إلى تنسيق SVG (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)