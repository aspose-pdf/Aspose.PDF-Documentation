---
title: 在 Ruby 中连接 PDF 文件
linktitle: 在 Ruby 中连接 PDF 文件
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-ruby/
description: 使用 Ruby 和 Aspose.PDF 有效地将多个 PDF 合并到一个文档中。
lastmod: "2026-06-09"
---
## Aspose.PDF - 连接 PDF 文件

要使用 **Aspose.PDF Java for Ruby** 连接 PDF 文件，只需调用 **ConcatenatePdfFiles** 模块即可。

红宝石代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Open the source document

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# Add the pages of the source document to the target document

pdf1.getPages().add(pdf2.getPages())

# Save the concatenated output file (the target document)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "New document has been saved, please check the output file"
```

## 下载运行代码

从以下任何社交编码网站下载**连接 PDF 文件 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)
