---
title: تحويل PDF إلى تنسيق SVG في بايثون
linktitle: تحويل PDF إلى تنسيق SVG في بايثون
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-python/
description: تعرف على كيفية تحويل مستندات PDF إلى تنسيق SVG في Python باستخدام Aspose.PDF لمخرجات متجهة قابلة للتطوير.
lastmod: "2026-06-09"
---
لتحويل تنسيق PDF إلى SVG باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء وحدة **PdfToSvg**.

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

** تنزيل كود التشغيل **

تنزيل В ** تحويل PDF إلى تنسيق SVG (Aspose.PDF)** В fromВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)
