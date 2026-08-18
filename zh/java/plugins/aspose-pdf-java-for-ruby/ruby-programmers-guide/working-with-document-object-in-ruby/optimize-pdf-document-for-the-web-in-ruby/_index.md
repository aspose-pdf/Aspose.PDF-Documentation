---
title: 使用 Ruby 优化 Web PDF 文档
linktitle: 使用 Ruby 优化 Web PDF 文档
type: docs
weight: 70
url: /java/optimize-pdf-document-for-the-web-in-ruby/
description: 使用 Ruby 中的 Aspose.PDF 简化 PDF 以实现更快的网络交付并减小文件大小。
lastmod: "2026-06-09"
---
## Aspose.PDF - 优化 Web PDF

要使用 **Aspose.PDF Java for Ruby** 优化 Web PDF 文档，只需调用 **Optimize** 模块的 **optimize_web** 方法即可。

红宝石代码

```java

 def optimize_web()

В В В  # The path to the documents directory.

В В В  data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

В В В  # Open a pdf document.

В В В  doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

В В В  # Optimize for web

В В В  doc.optimize()

В В В  #Save output document

В В В  doc.save(data_dir + "Optimized_Web.pdf")

В В В  puts "Optimized PDF for the Web, please check output file."

end
```В 

## 下载运行代码

从以下任何一个社交编码网站下载**优化 Web PDF (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
