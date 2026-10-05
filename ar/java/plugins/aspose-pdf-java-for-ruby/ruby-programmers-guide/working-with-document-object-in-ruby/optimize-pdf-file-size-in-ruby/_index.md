---
title: تحسين حجم ملف PDF في Ruby
linktitle: تحسين حجم ملف PDF في Ruby
type: docs
weight: 80
url: /ar/java/optimize-pdf-file-size-in-ruby/
description: تعلم كيفية تقليل حجم ملفات PDF دون التضحية بالجودة باستخدام Aspose.PDF for Ruby.
lastmod: "2026-10-05"
---
## Aspose.PDF - تحسين حجم ملف PDF

لتحسين حجم ملف PDF باستخدام **Aspose.PDF Java for Ruby**، استدعِ طريقة **optimize_filesize** من الوحدة **Optimize**.

كود Ruby

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

## تنزيل التعليمات البرمجية قيد التشغيل

تنزيل **Optimize PDF File Size (Aspose.PDF)** من أي من المواقع الاجتماعية للبرمجة المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
