---
title: Optimize PDF Document for the Web in Ruby
linktitle: Optimize PDF Document for the Web in Ruby
type: docs
weight: 70
url: /java/optimize-pdf-document-for-the-web-in-ruby/
description: Streamline PDFs for faster web delivery and reduced file size using Aspose.PDF in Ruby.
lastmod: "2026-06-09"
---

## Aspose.PDF - Optimize PDF for Web

To optimize PDF document for the web using **Aspose.PDF Java for Ruby**, simply invoke **optimize_web** method ofВ  **Optimize** module.

Ruby Code

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

## Download Running Code

DownloadВ **Optimize PDF for Web (Aspose.PDF)**В fromВ any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
