---
title: 将 SVG 文件转换为 Ruby 中的 PDF 格式
linktitle: 将 SVG 文件转换为 Ruby 中的 PDF 格式
type: docs
weight: 60
url: /zh/java/convert-svg-file-to-pdf-format-in-ruby/
description: 了解如何在 Ruby 中使用 Aspose.PDF 将 SVG 文件转换为 PDF 格式，以实现准确且可伸缩的文档转换。
lastmod: "2026-10-06"
---
## Aspose.PDF - 将 SVG 转换为 PDF

要在 **Aspose.PDF Java for Ruby** 中将 SVG 文件转换为 PDF 格式，只需调用 **SvgToPdf** 模块。

Ruby 代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate LoadOption object using SVG load option

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# Create document object

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# Save the output to XLS format

pdf.save(data_dir + "SVG.pdf")

puts "Document has been converted successfully"
```

## 下载运行代码

下载В **将 SVG 转换为 PDF (Aspose.PDF)**В 来自В 以下提及的社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)
