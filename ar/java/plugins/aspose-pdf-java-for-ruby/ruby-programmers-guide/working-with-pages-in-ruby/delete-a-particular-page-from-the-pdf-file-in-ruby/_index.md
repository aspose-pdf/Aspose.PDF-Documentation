---
title: حذف صفحة معينة من ملف PDF في روبي
linktitle: حذف صفحة معينة من ملف PDF في روبي
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-ruby/
description: قم بإزالة صفحات معينة من ملفات PDF برمجيًا باستخدام Aspose.PDF لـ Ruby.
lastmod: "2026-06-09"
---
## Aspose.PDF - حذف الصفحة

لحذف صفحة معينة من مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **DeletePage**.

كود روبي

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# delete a particular page

pdf.getPages().delete(2)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Page deleted successfully!"
```

## تحميل كود التشغيل

قم بتنزيل **حذف الصفحة (Aspose.PDF)**В من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)
