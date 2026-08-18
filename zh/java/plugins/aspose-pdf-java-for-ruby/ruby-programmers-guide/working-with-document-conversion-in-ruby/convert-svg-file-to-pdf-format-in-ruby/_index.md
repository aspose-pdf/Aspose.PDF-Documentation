---
title: 在 Ruby 中将 SVG 文件转换为 PDF 格式
linktitle: 在 Ruby 中将 SVG 文件转换为 PDF 格式
type: docs
weight: 60
url: /java/convert-svg-file-to-pdf-format-in-ruby/
description: 了解如何在 Ruby 中使用 Aspose.PDF 将 SVG 文件转换为 PDF 格式，以实现准确且可扩展的文档转换。
lastmod: "2026-06-09"
---
## Aspose.PDF - 将 SVG 转换为 PDF

要使用 **Aspose.PDF Java for Ruby** 将 SVG 文件转换为 PDF 格式，只需调用 **SvgToPdf** 模块即可。

红宝石代码

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

从以下任何社交编码网站下载**将 SVG 转换为 PDF (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)
