---
title: احصل على صفحة معينة في ملف PDF في Python
linktitle: احصل على صفحة معينة في ملف PDF في Python
type: docs
weight: 30
url: /ar/java/get-a-particular-page-in-a-pdf-file-in-python/
description: استكشف كيفية استخراج صفحة معينة من ملف PDF في Python باستخدام Aspose.PDF لمعالجة المستندات التفصيلية.
lastmod: "2026-10-05"
---
للحصول على صفحة معينة في مستند PDF باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء الفئة **GetPage**.

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

**تنزيل الشفرة القابلة للتشغيل**

تحميل **Get Page (Aspose.PDF)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)
