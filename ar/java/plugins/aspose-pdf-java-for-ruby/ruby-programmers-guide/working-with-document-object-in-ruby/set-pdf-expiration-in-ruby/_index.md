---
title: تعيين انتهاء PDF في Ruby
linktitle: تعيين انتهاء PDF في Ruby
type: docs
weight: 110
url: /ar/java/set-pdf-expiration-in-ruby/
description: تنفيذ تواريخ انتهاء الصلاحية في ملفات PDF باستخدام Aspose.PDF for Ruby للوثائق الحساسة للوقت.
lastmod: "2026-10-05"
---
## Aspose.PDF - تعيين انتهاء PDF

لتعيين انتهاء مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ببساطة استدعِ وحدة **SetExpiration**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

В В В  "var year=2014;

В В В  var month=4;

В В В  today = new Date();

В В В  today = new Date(today.getFullYear(), today.getMonth());

В В В  expiry = new Date(year, month);

В В В  if (today.getTime() > expiry.getTime())

В В В  app.alert('The file is expired. You need a new one.');")

doc.setOpenAction(javascript)

# save update document with new information

doc.save(data_dir + "set_expiration.pdf")

puts "Update document information, please check output file."
```

## تنزيل الكود القائم

تحميل **Set PDF Expiration (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)
