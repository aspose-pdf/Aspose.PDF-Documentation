---
title: 在 Ruby 中设置 PDF 文件信息
linktitle: 在 Ruby 中设置 PDF 文件信息
type: docs
weight: 120
url: /java/set-pdf-file-information-in-ruby/
description: 使用 Ruby 以编程方式定义和更新 PDF 元数据，例如标题、作者和关键字。
lastmod: "2026-06-09"
---
## Aspose.PDF - 设置 PDF 文件信息

要使用 **Aspose.PDF Java for Ruby** 更新 Pdf 文档信息，只需调用 **SetPdfFileInfo** 模块即可。

红宝石代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF for java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("PDF Information")

doc_info.setTitle("Setting PDF Document Information")

# save update document with new information

doc.save(data_dir + "Updated_Information.pdf")

puts "Update document information, please check output file."
```

## 下载运行代码

从以下任何一个社交编码网站下载**设置 PDF 文件信息 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)
