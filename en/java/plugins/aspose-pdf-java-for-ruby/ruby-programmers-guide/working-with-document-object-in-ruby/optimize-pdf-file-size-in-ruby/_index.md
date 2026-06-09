---
title: Optimize PDF File Size in Ruby
linktitle: Optimize PDF File Size in Ruby
type: docs
weight: 80
url: /java/optimize-pdf-file-size-in-ruby/
description: Learn to reduce the file size of PDFs without compromising quality using Aspose.PDF for Ruby.
lastmod: "2026-06-09"
---

## Aspose.PDF - Optimize PDF File Size

To optimize file Size of PDF document using **Aspose.PDF Java for Ruby**, call **optimize_filesize** method of **Optimize** module.

Ruby Code

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

## Download Running Code

DownloadВ **Optimize PDF File Size (Aspose.PDF)**В fromВ any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
