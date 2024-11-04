---
title: تحسين مستند PDF للويب في بايثون
type: docs
weight: 60
url: /python-java/optimize-pdf-document-for-the-web-in-python/
---

<ins>لتحسين مستند PDF للويب باستخدام **Aspose.PDF Java for Python**، قم ببساطة باستدعاء طريقة **optimize_web** من فئة **Optimize**.

**كود بايثون**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# تحسين للويب
doc.optimize();

# حفظ مستند الخرج
doc.save(self.dataDir + "Optimized_Web.pdf")

print "تم تحسين PDF للويب، يرجى التحقق من ملف الخرج."
```


**تنزيل الكود التنفيذي**

قم بتنزيل **تحسين PDF للويب (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/Optimize/Optimize.py)