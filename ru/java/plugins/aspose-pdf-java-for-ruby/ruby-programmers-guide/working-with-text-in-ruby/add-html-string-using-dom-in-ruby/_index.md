---
title: Добавить HTML‑строку с использованием DOM в Ruby
linktitle: Добавить HTML‑строку с использованием DOM в Ruby
type: docs
weight: 10
url: /ru/java/add-html-string-using-dom-in-ruby/
description: Узнайте, как добавить HTML‑строку в PDF‑документ с помощью API DOM в Ruby, используя Aspose.PDF для динамического создания контента.
lastmod: "2026-08-19"
---
## Aspose.PDF - Добавить HTML

Чтобы добавить HTML‑строку в PDF‑документ, используя **Aspose.PDF Java for Ruby**, просто вызовите модуль **AddHtml**.

Код Ruby

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

## Скачать работающий код

СкачатьВ **Add HTML (Aspose.PDF)**В изВ любой из перечисленных ниже сайтов для совместного кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)


