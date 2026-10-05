---
title: حذف صفحة معينة من ملف PDF في Ruby
linktitle: حذف صفحة معينة من ملف PDF في Ruby
type: docs
weight: 20
url: /ar/java/delete-a-particular-page-from-the-pdf-file-in-ruby/
description: إزالة صفحات محددة من ملفات PDF برمجيًا باستخدام Aspose.PDF for Ruby.
lastmod: "2026-10-05"
---
## Aspose.PDF - حذف الصفحة

لحذف صفحة معينة من مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **DeletePage**.

كود Ruby

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

## تنزيل الكود القائم

تنزيل **Delete Page (Aspose.PDF)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/deletepage.rb)
