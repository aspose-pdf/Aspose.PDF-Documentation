---
title: 在 Ruby 中获取 PDF 的页数
linktitle: 在 Ruby 中获取 PDF 的页数
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-ruby/
description: 使用 Ruby 和 Aspose.PDF 以编程方式检索 PDF 文档中的总页数。
lastmod: "2026-06-09"
---
## Aspose.PDF - 获取页数

要使用 **Aspose.PDF Java for Ruby** 获取 Pdf 文档的页数，只需调用 **GetNumberOfPages** 模块即可。

红宝石代码

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Create PDF document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Page Count:" + page_count.to_s
```

## 下载运行代码

从以下任何一个社交编码网站下载**获取页数 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)
