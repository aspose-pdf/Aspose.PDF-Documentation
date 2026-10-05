---
title: تحويل PDF إلى تنسيق SVG في Python
linktitle: تحويل PDF إلى تنسيق SVG في Python
type: docs
weight: 30
url: /ar/java/convert-pdf-to-svg-format-in-python/
description: تعلم كيفية تحويل مستندات PDF إلى تنسيق SVG في Python باستخدام Aspose.PDF للحصول على مخرجات متجهية قابلة للتكبير.
lastmod: "2026-10-05"
---
لتحويل PDF إلى تنسيق SVG باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء وحدة **PdfToSvg**.

```python

# Open the target document
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# instantiate an object of SvgSaveOptions
save_options = self.SvgSaveOptions()

# do not compress SVG image to Zip archive
save_options.CompressOutputToZipArchive = False;

# Save the output to XLS format
doc.save(self.dataDir + "Output1.svg", save_options)

print "Document has been converted successfully"
```

**تنزيل الشفرة القابلة للتشغيل**

Download\u0412\u00A0**تحويل PDF إلى تنسيق SVG (Aspose.PDF)**\u0412\u00A0من\u0412\u00A0أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)
