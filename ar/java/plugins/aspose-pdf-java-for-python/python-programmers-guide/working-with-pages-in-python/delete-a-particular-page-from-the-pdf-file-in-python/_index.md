---
title: حذف صفحة معينة من ملف PDF في بايثون
linktitle: حذف صفحة معينة من ملف PDF في بايثون
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-python/
description: تعرف على كيفية إزالة صفحة معينة من مستند PDF في Python باستخدام Aspose.PDF، مما يوفر تحريرًا فعالاً للمستندات.
lastmod: "2026-06-09"
---
لحذف صفحة معينة من مستند PDF باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء فئة **DeletePage**.

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

** تنزيل كود التشغيل **

قم بتنزيل **حذف الصفحة (Aspose.PDF)**В من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)
