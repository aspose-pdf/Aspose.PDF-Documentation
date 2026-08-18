---
title: تحسين حجم ملف PDF في روبي
linktitle: تحسين حجم ملف PDF في روبي
type: docs
weight: 80
url: /java/optimize-pdf-file-size-in-ruby/
description: تعلم كيفية تقليل حجم ملفات PDF دون المساس بالجودة باستخدام Aspose.PDF لـ Ruby.
lastmod: "2026-06-09"
---
## Aspose.PDF - تحسين حجم ملف PDF

لتحسين حجم ملف مستند PDF باستخدام **Aspose.PDF Java for Ruby**، اتصل بطريقة **optimize_filesize** لوحدة **Optimize**.

كود روبي

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

## تحميل كود التشغيل

تنزيل ** تحسين حجم ملف PDF (Aspose.PDF) ** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
