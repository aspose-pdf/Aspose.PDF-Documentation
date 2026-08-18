---
title: احصل على صفحة معينة في ملف PDF في بايثون
linktitle: احصل على صفحة معينة في ملف PDF في بايثون
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-python/
description: اكتشف كيفية استخراج صفحة معينة من ملف PDF في Python باستخدام Aspose.PDF لمعالجة المستندات بشكل تفصيلي.
lastmod: "2026-06-09"
---
للحصول على صفحة معينة في مستند PDF باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء فئة **GetPage**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# get the page at particular index of Page Collection
pdf_page = pdf.getPages().get_Item(1)

# create a new Document object
new_document = self.Document()

# add page to pages collection of new document object
new_document.getPages().add(pdf_page)

# save the newly generated PDF file
new_document.save(self.dataDir + "output.pdf")

print "Process completed successfully!

```

 ** تنزيل كود التشغيل **

قم بتنزيل **الحصول على الصفحة (Aspose.PDF)**В من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)
