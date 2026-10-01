---
title: إضافة سلسلة HTML باستخدام DOM في بايثون
linktitle: إضافة سلسلة HTML باستخدام DOM في بايثون
type: docs
weight: 10
url: /ar/java/add-html-string-using-dom-in-python/
lastmod: "2026-10-01"
description: يوضح كيفية إضافة سلسلة HTML في DOM باستخدام بايثون مع مكتبة تنسيق ملفات PDF
---
## إضافة سلسلة HTML في DOM لملف PDF باستخدام بايثون

لإضافة سلسلة HTML في مستند Pdf باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء الوحدة **AddHtml**.

```python

# Instantiate Document object
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Set margin information
title.setMargin(margin)

# Add HTML Fragment to paragraphs collection of page
page.getParagraphs().add(title)

# Save PDF file
doc.save(self.dataDir + 'html.output.pdf')

print "HTML added successfully"
```

**تنزيل الكود الجاري**

تنزيلВ **إضافة HTML (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)
