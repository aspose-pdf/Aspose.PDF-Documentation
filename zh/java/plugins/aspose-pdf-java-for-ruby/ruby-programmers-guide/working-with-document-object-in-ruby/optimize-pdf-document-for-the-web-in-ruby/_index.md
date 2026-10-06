---
title: 在 Ruby 中优化 PDF 文档以用于网络
linktitle: 在 Ruby 中优化 PDF 文档以用于网络
type: docs
weight: 70
url: /zh/java/optimize-pdf-document-for-the-web-in-ruby/
description: 使用 Aspose.PDF 在 Ruby 中简化 PDF，以实现更快的网页传输并减小文件大小。
lastmod: "2026-10-06"
---
## Aspose.PDF - 为网络优化 PDF

要使用 **Aspose.PDF Java for Ruby** 优化 PDF 文档以供网页使用，只需调用 **optimize_web** 方法的В  **Optimize** 模块。

Ruby 代码

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
```

## 下载运行代码

下载В **Optimize PDF for Web (Aspose.PDF)**В 来自В 以下提到的任意社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
