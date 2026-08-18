---
title: 在 Ruby 中优化 PDF 文件大小
linktitle: 在 Ruby 中优化 PDF 文件大小
type: docs
weight: 80
url: /java/optimize-pdf-file-size-in-ruby/
description: 了解使用 Aspose.PDF for Ruby 在不影响质量的情况下减小 PDF 文件大小。
lastmod: "2026-06-09"
---
## Aspose.PDF - 优化 PDF 文件大小

要使用 **Aspose.PDF Java for Ruby** 优化 PDF 文档的文件大小，请调用 **Optimize** 模块的 **optimize_filesize** 方法。

红宝石代码

```java
 def optimize_filesize()

В В В  # The path to the documents directory.

В В В  data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

В В В  # Open a pdf document.

В В В  doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

В В В  # Optimize the file size by removing unused objects

В В В  opt = Rjb::import('aspose.document.OptimizationOptions').new

В В В  opt.setRemoveUnusedObjects(true)

В В В  opt.setRemoveUnusedStreams(true)

В В В  opt.setLinkDuplcateStreams(true)

В В В  doc.optimizeResources(opt)

В В В  # Save output document

В В В  doc.save(data_dir + "Optimized_Filesize.pdf")

В В В  puts "Optimized PDF Filesize, please check output file."

endВ
```

## 下载运行代码

从以下任何社交编码网站下载**优化 PDF 文件大小 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
