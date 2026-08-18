---
title: 在 Ruby 中获取 PDF 文件信息
linktitle: 在 Ruby 中获取 PDF 文件信息
type: docs
weight: 50
url: /java/get-pdf-file-information-in-ruby/
description: 使用 Ruby 中的 Aspose.PDF 以编程方式从 PDF 文件中提取元数据和详细信息。
lastmod: "2026-06-09"
---
## Aspose.PDF - 获取 PDF 文件信息

要使用 **Aspose.PDF Java for Ruby** 获取 Pdf 文档的文件信息，只需调用 **GetPdfFileInfo** 模块即可。

红宝石代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

# Show document information

puts "Author:-" + doc_info.getAuthor().to_s

puts "Creation Date:-" + doc_info.getCreationDate().to_string

puts "Keywords:-" + doc_info.getKeywords().to_s

puts "Modify Date:-" + doc_info.getModDate().to_string

puts "Subject:-" + doc_info.getSubject().to_s

puts "Title:-" + doc_info.getTitle().to_s
```

## 下载运行代码

从以下任何一个社交编码网站下载**获取 PDF 文件信息 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)
