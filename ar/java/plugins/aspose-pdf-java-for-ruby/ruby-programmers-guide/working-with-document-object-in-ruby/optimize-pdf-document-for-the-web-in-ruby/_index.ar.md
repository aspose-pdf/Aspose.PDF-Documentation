---
title: تحسين مستند PDF للويب باستخدام روبي
type: docs
weight: 70
url: /java/optimize-pdf-document-for-the-web-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - تحسين PDF للويب

لتحسين مستند PDF للويب باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء طريقة **optimize_web** من وحدة **Optimize**.

كود روبي

```java

def optimize_web()

    # المسار إلى دليل المستندات.

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # افتح مستند pdf.

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # تحسين للويب

    doc.optimize()

    # حفظ المستند الناتج

    doc.save(data_dir + "Optimized_Web.pdf")

    puts "تم تحسين PDF للويب، يرجى التحقق من ملف الإخراج."

end
``` 

## تنزيل الكود الجاهز

قم بتنزيل **تحسين PDF للويب (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)