---
title: 在 Ruby 中将 PDF 转换为 DOC 或 DOCX 格式
linktitle: 在 Ruby 中将 PDF 转换为 DOC 或 DOCX 格式
type: docs
weight: 30
url: /java/convert-pdf-to-doc-or-docx-format-in-ruby/
description: 了解如何在 Ruby 中使用 Aspose.PDF 将 PDF 文档转换为 DOC 或 DOCX 格式，从而更轻松地进行编辑和处理。
lastmod: "2026-06-09"
---
## Aspose.PDF - 将 PDF 转换为 DOC 或 DOCX

要使用 **Aspose.PDF Java for Ruby** 将 PDF 文档转换为 DOC 或 DOCX 格式，只需调用 **PdfToDoc** 模块即可。

红宝石代码

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Save the concatenated output file (the target document)

pdf.save(data_dir + "output.doc")

puts "Document has been converted successfully"
```

## 下载运行代码

从以下任何社交编码网站下载**将 PDF 转换为 DOC 或 DOCX (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)
