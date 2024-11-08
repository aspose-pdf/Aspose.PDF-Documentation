---
title: تحسين مستند PDF للويب في بايثون
type: docs
weight: 60
url: /ar/java/optimize-pdf-document-for-the-web-in-python/
lastmod: "2021-06-05"
---

لتحسين مستند PDF للويب باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء طريقة **optimize_web** من فئة **Optimize**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# تحسين للويب
doc.optimize();

#حفظ مستند الإخراج
doc.save(self.dataDir + "Optimized_Web.pdf")

print "تم تحسين ملف PDF للويب، يرجى التحقق من ملف الإخراج."
```

**تنزيل الكود القابل للتشغيل**

قم بتنزيل **تحسين PDF للويب (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)