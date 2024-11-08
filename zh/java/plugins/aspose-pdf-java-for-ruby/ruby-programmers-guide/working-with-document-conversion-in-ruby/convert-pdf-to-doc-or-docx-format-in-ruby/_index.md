---
title: 将 PDF 转换为 DOC 或 DOCX 格式在 Ruby 中
type: docs
weight: 30
url: /zh/java/convert-pdf-to-doc-or-docx-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 将 PDF 转换为 DOC 或 DOCX

要使用 **Aspose.PDF Java for Ruby** 将 PDF 文档转换为 DOC 或 DOCX 格式，只需调用 **PdfToDoc** 模块。

Ruby 代码

```java

# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开目标文档

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 保存连接输出文件（目标文档）

pdf.save(data_dir + "output.doc")

puts "文档已成功转换"
```

## 下载运行代码

从以下任何一个社交编码网站下载 **Convert PDF to DOC or DOCX (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)