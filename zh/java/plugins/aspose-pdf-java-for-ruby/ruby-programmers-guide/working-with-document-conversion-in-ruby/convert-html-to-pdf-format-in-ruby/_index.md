---
title: 在 Ruby 中将 HTML 转换为 PDF 格式
linktitle: 在 Ruby 中将 HTML 转换为 PDF 格式
type: docs
weight: 10
url: /java/convert-html-to-pdf-format-in-ruby/
description: 了解如何在 Ruby 中使用 Aspose.PDF 将 HTML 内容转换为 PDF 格式，以生成可靠且准确的文档。
lastmod: "2026-06-09"
---
## Aspose.PDF - 将 HTML 转换为 PDF 格式

要使用 **Aspose.PDF Java for Ruby** 将 HTML 转换为 PDF 格式，只需调用 **HtmlToPdf** 模块即可。

红宝石代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# Load HTML file

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# Save the concatenated output file (the target document)

pdf.save(data_dir + "html.pdf")

puts "Document has been converted successfully"
```

## 下载运行代码

从以下任何社交编码网站下载**将 HTML 转换为 PDF 格式 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)
