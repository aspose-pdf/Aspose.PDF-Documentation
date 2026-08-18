---
title: 在 Ruby 中将 PDF 转换为 SVG 格式
linktitle: 在 Ruby 中将 PDF 转换为 SVG 格式
type: docs
weight: 50
url: /java/convert-pdf-to-svg-format-in-ruby/
description: 了解如何使用 Ruby 和 Aspose.PDF 将 PDF 文件转换为 SVG 格式，从而实现可扩展和可编辑的矢量图形。
lastmod: "2026-06-09"
---
## Aspose.PDF - 将 PDF 转换为 SVG

要使用 **Aspose.PDF Java for Ruby** 将 PDF 转换为 SVG 格式，只需调用 **PdfToSvg** 模块即可。

红宝石代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# instantiate an object of SvgSaveOptions

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# do not compress SVG image to Zip archive

save_options.CompressOutputToZipArchive = false

# Save the output to XLS format

pdf.save(data_dir + "Output.svg", save_options)

puts "Document has been converted successfully"
```

## 下载运行代码

从以下任何社交编码网站下载**将 PDF 转换为 SVG 格式 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)
