---
title: 在 Ruby 中将 HTML 转换为 PDF 格式
linktitle: 在 Ruby 中将 HTML 转换为 PDF 格式
type: docs
weight: 10
url: /zh/java/convert-html-to-pdf-format-in-ruby/
description: 了解如何使用 Aspose.PDF 在 Ruby 中将 HTML 内容转换为 PDF 格式，以实现可靠且准确的文档生成。
lastmod: "2026-10-06"
---
## Aspose.PDF - 将 HTML 转换为 PDF 格式

要使用 **Aspose.PDF Java for Ruby** 将 HTML 转换为 PDF 格式，只需调用 **HtmlToPdf** 模块。

Ruby 代码

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

下载 **Convert HTML to PDF Format (Aspose.PDF)** 来自以下列出的社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)
