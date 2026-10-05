---
title: تحسين مستند PDF للويب باستخدام Python
linktitle: تحسين مستند PDF للويب باستخدام Python
type: docs
weight: 60
url: /ar/java/optimize-pdf-document-for-the-web-in-python/
description: تعرف على كيفية تحسين ملفات PDF لتحميل أسرع على الويب باستخدام Python مع Aspose.PDF، مما يحسن تجربة المستخدم والأداء.
lastmod: "2026-10-05"
---
لتحسين مستند PDF للويب باستخدام **Aspose.PDF Java for Python**، ببساطة استدعِ طريقة **optimize_web** من فئة  **Optimize**.

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

**تنزيل الشفرة القابلة للتشغيل**

تنزيل **تحسين PDF للويب (Aspose.PDF)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
