---
title: 在 Ruby 中从 PDF 文件获取 XMP 元数据
linktitle: 在 Ruby 中从 PDF 文件获取 XMP 元数据
type: docs
weight: 60
url: /java/get-xmp-metadata-from-pdf-file-in-ruby/
description: 使用 Ruby 和 Aspose.PDF 访问和操作 PDF 文档中的 XMP 元数据。
lastmod: "2026-06-09"
---
## Aspose.PDF - 获取 XMP 元数据

要使用 **Aspose.PDF Java for Ruby** 从 Pdf 文档获取 XMP 元数据，只需调用 **GetXMPMetadata** 模块即可。

红宝石代码

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

从以下任何一个社交编码网站下载**获取 XMP 元数据 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)
