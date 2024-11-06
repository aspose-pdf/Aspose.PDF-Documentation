---
title: 获取 PDF 文件信息在 Ruby 中
type: docs
weight: 50
url: zh/java/get-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 获取 PDF 文件信息

要使用 **Aspose.PDF Java for Ruby** 获取 PDF 文档的文件信息，只需调用 **GetPdfFileInfo** 模块。

Ruby 代码

```java
# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开一个 pdf 文档。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# 获取文档信息

doc_info = doc.getInfo()

# 显示文档信息

puts "作者:-" + doc_info.getAuthor().to_s

puts "创建日期:-" + doc_info.getCreationDate().to_string

puts "关键词:-" + doc_info.getKeywords().to_s

puts "修改日期:-" + doc_info.getModDate().to_string

puts "主题:-" + doc_info.getSubject().to_s

puts "标题:-" + doc_info.getTitle().to_s
```

## 下载运行代码

从以下任何一个社交编码网站下载 **获取 PDF 文件信息 (Aspose.PDF)**:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getpdffileinfo.rb)