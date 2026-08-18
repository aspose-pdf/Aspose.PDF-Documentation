---
title: قم بتعيين معلومات ملف PDF في روبي
linktitle: قم بتعيين معلومات ملف PDF في روبي
type: docs
weight: 120
url: /java/set-pdf-file-information-in-ruby/
description: قم بتحديد وتحديث بيانات تعريف PDF برمجيًا مثل العنوان والمؤلف والكلمات الرئيسية باستخدام Ruby.
lastmod: "2026-06-09"
---
## Aspose.PDF - ضبط معلومات ملف PDF

لتحديث معلومات مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **SetPdfFileInfo**.

كود روبي

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

## تحميل كود التشغيل

تنزيلВ **تعيين معلومات ملف PDF (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)
