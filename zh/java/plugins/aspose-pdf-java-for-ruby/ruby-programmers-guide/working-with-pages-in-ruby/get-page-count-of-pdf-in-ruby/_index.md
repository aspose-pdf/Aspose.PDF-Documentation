---
title: 在 Ruby 中获取 PDF 的页数
linktitle: 在 Ruby 中获取 PDF 的页数
type: docs
weight: 40
url: /zh/java/get-page-count-of-pdf-in-ruby/
description: 使用 Ruby 和 Aspose.PDF 以编程方式检索 PDF 文档的总页数。
lastmod: "2026-10-06"
---
## Aspose.PDF - 获取页数

要使用 **Aspose.PDF Java for Ruby** 获取 PDF 文档的页数，只需调用 **GetNumberOfPages** 模块。

Ruby 代码

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Create PDF document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Page Count:" + page_count.to_s
```

## 下载运行代码

下载В **获取页面计数 (Aspose.PDF)**В 来自В 下面提到的任何社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)
