---
title: إضافة سلسلة HTML باستخدام DOM في Ruby
linktitle: إضافة سلسلة HTML باستخدام DOM في Ruby
type: docs
weight: 10
url: /ar/java/add-html-string-using-dom-in-ruby/
description: اكتشف كيفية إضافة سلسلة HTML إلى مستند PDF باستخدام واجهة برمجة تطبيقات DOM في Ruby مع Aspose.PDF لتوليد المحتوى الديناميكي.
lastmod: "2026-10-01"
---
## Aspose.PDF - إضافة HTML

لإضافة سلسلة HTML في مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **AddHtml**.

كود Ruby

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

## تنزيل الكود الجاري

تنزيل **إضافة HTML (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)
