---
title: تعيين انتهاء صلاحية PDF في روبي
type: docs
weight: 110
url: /java/set-pdf-expiration-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - تعيين انتهاء صلاحية PDF

لتعيين انتهاء صلاحية مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء وحدة **SetExpiration**.

كود روبي

```java
# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح مستند pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

javascript = Rjb::import('com.aspose.pdf.JavascriptAction').new(

    "var year=2014;

    var month=4;

    today = new Date();

    today = new Date(today.getFullYear(), today.getMonth());

    expiry = new Date(year, month);

    if (today.getTime() > expiry.getTime())

    app.alert('The file is expired. You need a new one.');")

doc.setOpenAction(javascript)

# حفظ المستند المحدث بالمعلومات الجديدة

doc.save(data_dir + "set_expiration.pdf")

puts "تحديث معلومات المستند، يرجى التحقق من ملف الإخراج."
```


## تحميل الكود التشغيلي

قم بتنزيل **تعيين انتهاء صلاحية PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setexpiration.rb)