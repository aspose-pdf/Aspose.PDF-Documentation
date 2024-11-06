---
title: الحصول على عدد صفحات PDF في بايثون
type: docs
weight: 40
url: ar/java/get-page-count-of-pdf-in-python/
lastmod: "2021-06-05"
---

للحصول على عدد صفحات مستند Pdf باستخدام **Aspose.PDF Java for Python**، ببساطة قم باستدعاء فئة **GetNumberOfPages**.

```Python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'
page_count = pdf.getPages().size()
print "عدد الصفحات:" . page_count

```

**تحميل الكود قيد التشغيل**

قم بتحميل **احصل على عدد الصفحات (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/GetNumberOfPages/GetNumberOfPages.py)