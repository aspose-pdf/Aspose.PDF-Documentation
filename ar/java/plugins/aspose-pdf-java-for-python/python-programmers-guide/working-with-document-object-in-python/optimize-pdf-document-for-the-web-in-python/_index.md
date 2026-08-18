---
title: تحسين مستند PDF للويب في بايثون
linktitle: تحسين مستند PDF للويب في بايثون
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-python/
description: تعرف على كيفية تحسين ملفات PDF لتحميل الويب بشكل أسرع في Python باستخدام Aspose.PDF، مما يحسن تجربة المستخدم والأداء.
lastmod: "2026-06-09"
---
لتحسين مستند PDF للويب باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء طريقة **optimize_web** للفئة **Optimize**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Optimize for web
doc.optimize();

#Save output document
doc.save(self.dataDir + "Optimized_Web.pdf")

print "Optimized PDF for the Web, please check output file."
```

** تنزيل كود التشغيل **

قم بتنزيل ** ** تحسين ملف PDF للويب (Aspose.PDF) ** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
