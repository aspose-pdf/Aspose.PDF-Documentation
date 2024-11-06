---
title: تقسيم ملف PDF إلى صفحات فردية في بايثون
type: docs
weight: 80
url: ar/python-java/split-pdf-file-into-individual-pages-in-python/
---

<ins>لتقسيم مستند PDF إلى صفحات فردية باستخدام **Aspose.PDF Java for PHP**، ببساطة قم باستدعاء فئة **SplitAllPages**.

**كود بايثون**
```

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# التجول عبر جميع الصفحات
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# إنشاء كائن Document جديد
new_document = self.Document();

# الحصول على الصفحة في فهرس معين من مجموعة الصفحات
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# حفظ ملف PDF الذي تم إنشاؤه حديثًا
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "تم إكمال عملية التقسيم بنجاح!";
```


**تحميل الكود الجاري**

قم بتحميل **تقسيم الصفحات (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/SplitAllPages/SplitAllPages.py)