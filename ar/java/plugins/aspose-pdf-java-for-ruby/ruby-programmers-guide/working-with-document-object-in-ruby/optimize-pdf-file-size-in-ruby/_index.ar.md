---
title: تحسين حجم ملف PDF في روبي
type: docs
weight: 80
url: /java/optimize-pdf-file-size-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - تحسين حجم ملف PDF

لتحسين حجم ملف مستند PDF باستخدام **Aspose.PDF Java for Ruby**، قم باستدعاء طريقة **optimize_filesize** من وحدة **Optimize**.

كود روبي

```java

 def optimize_filesize()

    # المسار إلى دليل المستندات.

    data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

    # افتح مستند PDF.

    doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

    # تحسين حجم الملف بإزالة الكائنات غير المستخدمة

    opt = Rjb::import('aspose.document.OptimizationOptions').new

    opt.setRemoveUnusedObjects(true)

    opt.setRemoveUnusedStreams(true)

    opt.setLinkDuplcateStreams(true)

    doc.optimizeResources(opt)

    # حفظ المستند الناتج

    doc.save(data_dir + "Optimized_Filesize.pdf")

    puts "تم تحسين حجم ملف PDF، يرجى التحقق من الملف الناتج."

end 
```

## تحميل الكود التشغيلي

Download **تقليل حجم ملف PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/optimize.rb)