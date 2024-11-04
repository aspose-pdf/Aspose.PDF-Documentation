---
title: الحصول على عدد صفحات PDF في بايثون
type: docs
weight: 40
url: /python-java/get-page-count-of-pdf-in-python/
---

<ins>للحصول على عدد صفحات مستند Pdf باستخدام **Aspose.PDF Java for Python**، قم فقط باستدعاء فئة **GetNumberOfPages**.

**كود بايثون**
```
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'
page_count = pdf.getPages().size()
print "عدد الصفحات:" . page_count

```

**تحميل الكود الجاري**

قم بتحميل **Get Page Count (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/GetNumberOfPages/GetNumberOfPages.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/GetNumberOfPages/GetNumberOfPages.py)