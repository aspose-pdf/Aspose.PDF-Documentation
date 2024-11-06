---
title: 获取 PDF 页数的 Ruby
type: docs
weight: 40
url: zh/java/get-page-count-of-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 获取页数

要使用 **Aspose.PDF Java for Ruby** 获取 PDF 文档的页数，只需调用 **GetNumberOfPages** 模块。

Ruby 代码

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 创建 PDF 文档

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "页数:" + page_count.to_s
```

## 下载运行代码

从以下任一社交编程网站下载 **获取页数 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)