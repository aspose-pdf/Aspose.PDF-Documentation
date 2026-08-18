---
title: إزالة البيانات الوصفية من PDF في روبي
linktitle: إزالة البيانات الوصفية من PDF في روبي
type: docs
weight: 90
url: /java/remove-metadata-from-pdf-in-ruby/
description: قم بمسح البيانات التعريفية الحساسة أو غير المرغوب فيها من ملفات PDF برمجيًا باستخدام Aspose.PDF لـ Ruby.
lastmod: "2026-06-09"
---
## Aspose.PDF - إزالة البيانات الوصفية

لإزالة البيانات الوصفية من مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **RemoveMetadata**.

كود روبي

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

if doc.getMetadata().contains("pdfaid:part")

В В В  doc.getMetadata().removeItem("pdfaid:part")

endВ В  В

if doc.getMetadata().contains("dc:format")

В В В  doc.getMetadata().removeItem("dc:format")

end

# save update document with new information

doc.save(data_dir + "Remove_Metadata.pdf")

puts "Removed metadata successfully, please check output file."
```

## تحميل كود التشغيل

تنزيلВ **إزالة البيانات الوصفية (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/removemetadata.rb)
