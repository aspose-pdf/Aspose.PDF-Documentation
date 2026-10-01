---
title: حذف صفحة معينة من ملف PDF في بايثون
linktitle: حذف صفحة معينة من ملف PDF في بايثون
type: docs
weight: 20
url: /ar/java/delete-a-particular-page-from-the-pdf-file-in-python/
description: تعلم كيفية إزالة صفحة محددة من مستند PDF في بايثون باستخدام Aspose.PDF، مع توفير تحرير مستند فعال.
lastmod: "2026-10-01"
---
لحذف صفحة معينة من مستند PDF باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء الفئة **DeletePage**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# delete a particular page
pdf.getPages().delete(2)

# save the newly generated PDF file
doc.save(self.dataDir + "output.pdf")

print "Page deleted successfully!"

```

**تنزيل الكود التشغيلي**

تنزيل **حذف الصفحة (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)
