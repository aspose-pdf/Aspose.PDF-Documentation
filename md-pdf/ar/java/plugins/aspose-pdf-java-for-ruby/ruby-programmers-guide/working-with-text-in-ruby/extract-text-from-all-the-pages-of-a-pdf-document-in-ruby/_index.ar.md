---
title: استخراج النص من جميع صفحات مستند PDF باستخدام روبي
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - استخراج النص من جميع الصفحات

لاستخراج النص من جميع صفحات مستند PDF باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء وحدة **ExtractTextFromAllPages**.

كود روبي

```java
# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح المستند المستهدف

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# إنشاء كائن TextAbsorber لاستخراج النص

text_absorber = Rjb::import('com.aspose.pdf.TextAbsorber').new

# قبول المستخرج لجميع الصفحات

pdf.getPages().accept(text_absorber)

# من أجل استخراج النص من صفحة معينة في المستند، نحتاج إلى تحديد الصفحة المعينة باستخدام فهرسها مقابل طريقة accept(..).

# قبول المستخرج لصفحة PDF معينة

# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# الحصول على النص المستخرج

extracted_text = text_absorber.getText()

# إنشاء كاتب وفتح الملف

writer = Rjb::import('java.io.FileWriter').new(Rjb::import('java.io.File').new(data_dir + "extracted_text.out.txt"))

writer.write(extracted_text)

# كتابة سطر من النص إلى الملف

# tw.WriteLine(extractedText);

# إغلاق التدفق

writer.close()

puts "تم استخراج النص بنجاح. تحقق من ملف الإخراج."
```


## تحميل الكود الجاري

قم بتنزيل **استخراج النص من جميع الصفحات (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)