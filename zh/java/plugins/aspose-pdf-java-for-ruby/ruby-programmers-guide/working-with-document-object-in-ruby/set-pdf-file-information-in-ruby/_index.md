---
title: 在 Ruby 中设置 PDF 文件信息
type: docs
weight: 120
url: /zh/java/set-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 设置 PDF 文件信息

要使用 **Aspose.PDF Java for Ruby** 更新 PDF 文档信息，只需调用 **SetPdfFileInfo** 模块。

Ruby 代码

```java

# 文档目录的路径。

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 打开一个 pdf 文档。

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# 获取文档信息

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF for java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("PDF 信息")

doc_info.setTitle("设置 PDF 文档信息")

# 保存更新的文档和新信息

doc.save(data_dir + "Updated_Information.pdf")

puts "更新文档信息，请检查输出文件。"
```


## 下载运行代码

从以下任意一个社交编码网站下载**设置 PDF 文件信息 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)