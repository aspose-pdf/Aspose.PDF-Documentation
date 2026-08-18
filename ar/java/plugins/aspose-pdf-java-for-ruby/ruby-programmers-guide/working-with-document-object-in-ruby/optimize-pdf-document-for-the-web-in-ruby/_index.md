---
title: تحسين مستند PDF للويب في روبي
linktitle: تحسين مستند PDF للويب في روبي
type: docs
weight: 70
url: /java/optimize-pdf-document-for-the-web-in-ruby/
description: قم بتبسيط ملفات PDF لتسليم الويب بشكل أسرع وتقليل حجم الملف باستخدام Aspose.PDF في Ruby.
lastmod: "2026-06-09"
---
## Aspose.PDF - تحسين PDF للويب

لتحسين مستند PDF للويب باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء طريقة **optimize_web** لوحدة **Optimize**.

كود روبي

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

## تحميل كود التشغيل

قم بتنزيل ** ** تحسين ملف PDF للويب (Aspose.PDF) ** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)
