---
title: أضف سلسلة HTML باستخدام DOM في Python
linktitle: أضف سلسلة HTML باستخدام DOM في Python
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-python/
lastmod: "2026-06-09"
description: يشرح كيفية إضافة سلسلة HTML في DOM باستخدام Python مع مكتبة تنسيق الملفات PDF
---
## أضف سلسلة HTML إلى PDF DOM باستخدام Python

لإضافة سلسلة HTML في مستند Pdf باستخدام **Aspose.PDF Java for Python**، ما عليك سوى استدعاء وحدة **AddHtml**.

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

** تنزيل كود التشغيل **

تنزيلВ **إضافة HTML (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)
