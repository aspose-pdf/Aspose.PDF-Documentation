---
title: أضف جدول المحتويات إلى ملف PDF الموجود في بايثون
linktitle: أضف جدول المحتويات إلى ملف PDF الموجود في بايثون
type: docs
weight: 20
url: /java/add-toc-to-existing-pdf-in-python/
description: تعرف على كيفية إضافة جدول محتويات (TOC) إلى مستند PDF موجود في Python باستخدام Aspose.PDF لسهولة التنقل.
lastmod: "2026-06-09"
---
لإضافة جدول محتويات إلى مستند Pdf باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء فئة **AddToc**.

```python

# Open a pdf document.
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get access to first page of PDF file
toc_page = doc.getPages().insert(1)

# Create object to represent TOC information
toc_info = self.TocInfo()
title = self.TextFragment("Table Of Contents")
title.getTextState().setFontSize(20)

# Set the title for TOC
toc_info.setTitle(title)
toc_page.setTocInfo(toc_info)

# Create string objects which will be used as TOC elements
titles = ["First page", "Second page"]

i = 0;
while (i < 2):

# Create Heading object
heading2 = self.Heading(1);

segment2 = self.TextSegment
heading2.setTocPage(toc_page)
heading2.getSegments().add(segment2)

# Specify the destination page for heading object
heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

# Destination page
heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

# Destination coordinate
segment2.setText(titles[i])

# Add heading to page containing TOC
toc_page.getParagraphs().add(heading2)

i +=1;

# Save PDF Document
doc.save(self.dataDir + "TOC.pdf")

print "Added TOC Successfully, please check the output file."
```

** تنزيل كود التشغيل **

تنزيلВ **إضافة TOC (Aspose.PDF)**В fromВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)
