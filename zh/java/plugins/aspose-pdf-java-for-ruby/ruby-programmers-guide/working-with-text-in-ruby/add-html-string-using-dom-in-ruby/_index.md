---
title: 在 Ruby 中使用 DOM 添加 HTML 字符串
linktitle: 在 Ruby 中使用 DOM 添加 HTML 字符串
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-ruby/
description: 了解如何使用 Ruby 中的 DOM API 和 Aspose.PDF 将 HTML 字符串添加到 PDF 文档中，以生成动态内容。
lastmod: "2026-06-09"
---
## Aspose.PDF - 添加 HTML

要使用 **Aspose.PDF Java for Ruby** 在 Pdf 文档中添加 HTML 字符串，只需调用 **AddHtml** 模块即可。

红宝石代码

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

## 下载运行代码

从以下任何一个社交编码网站下载**添加 HTML (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)
