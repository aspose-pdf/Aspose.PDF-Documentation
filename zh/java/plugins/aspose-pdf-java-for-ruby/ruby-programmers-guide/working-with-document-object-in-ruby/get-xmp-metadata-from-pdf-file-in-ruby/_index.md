---
title: 在 Ruby 中获取 PDF 文件的 XMP 元数据
linktitle: 在 Ruby 中获取 PDF 文件的 XMP 元数据
type: docs
weight: 60
url: /zh/java/get-xmp-metadata-from-pdf-file-in-ruby/
description: 使用 Ruby 和 Aspose.PDF 访问并操作 PDF 文档中的 XMP 元数据。
lastmod: "2026-10-06"
---
## Aspose.PDF - 获取 XMP 元数据

要使用 **Aspose.PDF Java for Ruby** 从 PDF 文档获取 XMP 元数据，只需调用 **GetXMPMetadata** 模块。

Ruby 代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get properties

puts "xmp:CreateDate: " + doc.getMetadata().get_Item("xmp:CreateDate").to_s

puts "xmp:Nickname: " + doc.getMetadata().get_Item("xmp:Nickname").to_s

puts "xmp:CustomProperty: " + doc.getMetadata().get_Item("xmp:CustomProperty").to_s
```

## 下载运行代码

下载 **Get XMP Metadata (Aspose.PDF)** 来自以下提到的社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)
