---
title: تحسين مستند PDF للويب في Ruby
linktitle: تحسين مستند PDF للويب في Ruby
type: docs
weight: 70
url: /ar/java/optimize-pdf-document-for-the-web-in-ruby/
description: تبسيط ملفات PDF لتسليم أسرع على الويب وتقليل حجم الملف باستخدام Aspose.PDF في Ruby.
lastmod: "2026-10-01"
---
## Aspose.PDF - تحسين PDF للويب

لتحسين مستند PDF للويب باستخدام **Aspose.PDF Java for Ruby**، ببساطة استدعِ طريقة **optimize_web** منВ  **Optimize** module.

كود Ruby

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

## تنزيل الكود الجاري

DownloadВ **Optimize PDF for Web (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
