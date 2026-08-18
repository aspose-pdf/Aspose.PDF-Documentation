---
title: 在 Ruby 中将 PDF 页面转换为图像
linktitle: 在 Ruby 中将 PDF 页面转换为图像
type: docs
weight: 20
url: /java/convert-pdf-pages-to-images-in-ruby/
description: 了解如何使用 Ruby 和 Aspose.PDF 将 PDF 页面转换为图像，从而轻松从 PDF 中提取可视内容。
lastmod: "2026-06-09"
---
## Aspose.PDF - 将 PDF 页面转换为图像

要使用 **Aspose.PDF Java for Ruby** 将所有页面转换为 Pdf 文档的图像，只需调用 **ConvertPagesToImages** 模块即可。

红宝石代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

В В В  converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

В В В  image_count +=1

end

puts "PDF pages are converted to individual images successfully!"
```

## 下载运行代码

从以下任何社交编码网站下载**将 PDF 页面转换为图像 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)
