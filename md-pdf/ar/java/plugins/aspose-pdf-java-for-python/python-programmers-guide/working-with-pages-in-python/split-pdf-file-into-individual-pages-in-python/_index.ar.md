---
title: تقسيم ملف PDF إلى صفحات فردية في بايثون
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-python/
lastmod: "2021-06-05"
---

لتقسيم مستند PDF إلى صفحات فردية باستخدام **Aspose.PDF Java for PHP**، ببساطة استدعِ فئة **SplitAllPages**.

```python

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# حلقة عبر جميع الصفحات
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# إنشاء كائن مستند جديد
new_document = self.Document();

# احصل على الصفحة عند الفهرس المحدد في مجموعة الصفحات
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# حفظ ملف PDF الذي تم إنشاؤه حديثًا
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "تمت عملية التقسيم بنجاح!";
```

**تحميل الشيفرة الجارية**

قم بتحميل **تقسيم الصفحات (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)