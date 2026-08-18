---
title: أضف سلسلة HTML باستخدام DOM في روبي
linktitle: أضف سلسلة HTML باستخدام DOM في روبي
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-ruby/
description: اكتشف كيفية إضافة سلسلة HTML إلى مستند PDF باستخدام DOM API في Ruby باستخدام Aspose.PDF لإنشاء محتوى ديناميكي.
lastmod: "2026-06-09"
---
## Aspose.PDF - إضافة HTML

لإضافة سلسلة HTML في مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **AddHtml**.

كود روبي

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate Document object

doc = Rjb::import('com.aspose.pdf.Document').new

# Add a page to pages collection of PDF file

page = doc.getPages().add()

# Instantiate HtmlFragment with HTML contents

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Table</i></b></fontsize>")

# set MarginInfo for margin details

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# Set margin information

title.setMargin(margin)

# Add HTML Fragment to paragraphs collection of page

page.getParagraphs().add(title)

# Save PDF file

doc.save(data_dir + "html.output.pdf")

puts "HTML added successfully"
```

## تحميل كود التشغيل

تنزيلВ **إضافة HTML (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)
