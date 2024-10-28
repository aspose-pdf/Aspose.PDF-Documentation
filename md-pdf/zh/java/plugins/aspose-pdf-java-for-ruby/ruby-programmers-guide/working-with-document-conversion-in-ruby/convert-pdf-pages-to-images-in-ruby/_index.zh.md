---
title: 将 PDF 页面转换为 Ruby 中的图像
type: docs
weight: 20
url: /java/convert-pdf-pages-to-images-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 将 PDF 页面转换为图像

要使用 **Aspose.PDF Java for Ruby** 将 PDF 文档的所有页面转换为图像，只需调用 **ConvertPagesToImages** 模块。

Ruby 代码

```java

# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

    converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

    image_count +=1

end

puts "PDF 页面已成功转换为单独的图像！"
```

## 下载运行代码

从以下任一社交编码网站下载 **将 PDF 页面转换为图像 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)