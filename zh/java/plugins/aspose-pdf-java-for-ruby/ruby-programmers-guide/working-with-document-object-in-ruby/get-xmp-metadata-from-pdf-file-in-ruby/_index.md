---
title: 从 PDF 文件中获取 XMP 元数据在 Ruby 中
type: docs
weight: 60
url: zh/java/get-xmp-metadata-from-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 获取 XMP 元数据

要使用 **Aspose.PDF Java for Ruby** 从 Pdf 文档中获取 XMP 元数据，只需调用 **GetXMPMetadata** 模块。

Ruby 代码

```java
# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开 pdf 文档。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# 获取属性

puts "xmp:CreateDate: " + doc.getMetadata().get_Item("xmp:CreateDate").to_s

puts "xmp:Nickname: " + doc.getMetadata().get_Item("xmp:Nickname").to_s

puts "xmp:CustomProperty: " + doc.getMetadata().get_Item("xmp:CustomProperty").to_s
```

## 下载运行代码

从以下任何社交编码网站下载 **获取 XMP 元数据 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getxmpmetadata.rb)