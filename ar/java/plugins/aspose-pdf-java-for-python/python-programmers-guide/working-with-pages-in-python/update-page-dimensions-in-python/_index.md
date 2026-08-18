---
title: تحديث أبعاد الصفحة في بايثون
linktitle: تحديث أبعاد الصفحة في بايثون
type: docs
weight: 90
url: /java/update-page-dimensions-in-python/
description: افهم كيفية تحديث أبعاد الصفحة داخل مستند PDF في Python باستخدام Aspose.PDF للتحكم بشكل أفضل في تخطيط المستند.
lastmod: "2026-06-09"
---
لتحديث أبعاد الصفحة باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء فئة **UpdatePageDimensions**.

```python
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# get page collection
page_collection = pdf.getPages()

# get particular page
pdf_page = page_collection.get_Item(1)

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points
# so A4 dimensions in points will be (842.4, 597.6)
pdf_page.setPageSize(597.6,842.4)

# save the newly generated PDF file
pdf.save(self.dataDir + "output.pdf")

print "Dimensions updated successfully!"

```

** تنزيل كود التشغيل **

تنزيل В ** تحديث أبعاد الصفحة (Aspose.PDF) ** В من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)
