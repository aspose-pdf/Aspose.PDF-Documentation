---
title: Добавьте строку HTML, используя DOM в Ruby
linktitle: Добавьте строку HTML, используя DOM в Ruby
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-ruby/
description: Узнайте, как добавить строку HTML в PDF-документ с помощью DOM API в Ruby с помощью Aspose.PDF для создания динамического контента.
lastmod: "2026-06-09"
---
## Aspose.PDF — Добавить HTML

Чтобы добавить строку HTML в документ PDF с помощью **Aspose.PDF Java for Ruby**, просто вызовите модуль **AddHtml**.

Рубиновый код

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

## Загрузите рабочий код

Загрузите **Добавьте HTML (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)
