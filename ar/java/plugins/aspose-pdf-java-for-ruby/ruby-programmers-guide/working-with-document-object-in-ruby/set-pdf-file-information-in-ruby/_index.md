---
title: تعيين معلومات ملف PDF في Ruby
linktitle: تعيين معلومات ملف PDF في Ruby
type: docs
weight: 120
url: /ar/java/set-pdf-file-information-in-ruby/
description: تعريف وتحديث بيانات تعريف PDF برمجياً مثل العنوان، المؤلف، والكلمات المفتاحية باستخدام Ruby.
lastmod: "2026-10-01"
---
## Aspose.PDF - تعيين معلومات ملف PDF

لتحديث معلومات مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء الوحدة **SetPdfFileInfo**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get document information

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF for java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("PDF Information")

doc_info.setTitle("Setting PDF Document Information")

# save update document with new information

doc.save(data_dir + "Updated_Information.pdf")

puts "Update document information, please check output file."
```

## تنزيل الكود الجاري

تحميلВ **تعيين معلومات ملف PDF (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)
