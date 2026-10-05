---
title: قسّم ملف PDF إلى صفحات فردية باستخدام Python
linktitle: قسّم ملف PDF إلى صفحات فردية باستخدام Python
type: docs
weight: 80
url: /ar/java/split-pdf-file-into-individual-pages-in-python/
description: استكشف كيفية تقسيم ملف PDF إلى صفحات فردية في Python باستخدام Aspose.PDF، مما يتيح استخراج وإدارة الصفحات بسهولة.
lastmod: "2026-10-05"
---
لتقسيم مستند PDF إلى صفحات فردية باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء الفئة **SplitAllPages**.

```python

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# loop through all the pages
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# create a new Document object
new_document = self.Document();

# get the page at particular index of Page Collection
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "Split process completed successfully!";
```

**تنزيل الشفرة القابلة للتشغيل**

تنزيل **Split Pages (Aspose.PDF)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)
