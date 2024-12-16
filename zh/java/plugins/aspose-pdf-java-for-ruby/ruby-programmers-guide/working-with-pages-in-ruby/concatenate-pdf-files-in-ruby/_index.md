---
title: 连接 PDF 文件在 Ruby 中
type: docs
weight: 10
url: /zh/java/concatenate-pdf-files-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 连接 PDF 文件

要使用 **Aspose.PDF Java for Ruby** 连接 PDF 文件，只需调用 **ConcatenatePdfFiles** 模块。

Ruby 代码

```java
# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开目标文档

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 打开源文档

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# 将源文档的页面添加到目标文档

pdf1.getPages().add(pdf2.getPages())

# 保存连接后的输出文件（目标文档）

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "新文档已保存，请检查输出文件"
```

## 下载运行代码

从以下任意一个社交编码网站下载 **Concatenate PDF Files (Aspose.PDF)**:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)