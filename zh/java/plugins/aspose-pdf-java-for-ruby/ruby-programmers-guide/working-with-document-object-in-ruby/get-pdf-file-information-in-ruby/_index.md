---
title: 在 Ruby 中获取 PDF 文件信息
linktitle: 在 Ruby 中获取 PDF 文件信息
type: docs
weight: 50
url: /zh/java/get-pdf-file-information-in-ruby/
description: 使用 Aspose.PDF 在 Ruby 中以编程方式提取 PDF 文件的元数据和详细信息。
lastmod: "2026-10-06"
---
## Aspose.PDF - 获取 PDF 文件信息

要使用 **Aspose.PDF Java for Ruby** 获取 PDF 文档的文件信息，只需调用 **GetPdfFileInfo** 模块。

Ruby 代码

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

下载 **获取 PDF 文件信息 (Aspose.PDF)** 从以下提及的社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)
