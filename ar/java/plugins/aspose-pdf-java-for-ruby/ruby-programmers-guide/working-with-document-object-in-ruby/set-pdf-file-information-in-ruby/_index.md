---
title: تعيين معلومات ملف PDF في روبي
type: docs
weight: 120
url: /ar/java/set-pdf-file-information-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - تعيين معلومات ملف PDF

لتحديث معلومات مستند Pdf باستخدام **Aspose.PDF Java for Ruby**، ببساطة استدعِ وحدة **SetPdfFileInfo**.

كود روبي

```java

# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# فتح مستند pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# الحصول على معلومات المستند

doc_info = doc.getInfo()

doc_info.setAuthor("Aspose.PDF for java")

doc_info.setCreationDate(Rjb::import('java.util.Date').new)

doc_info.setKeywords("Aspose.PDF, DOM, API")

doc_info.setModDate(Rjb::import('java.util.Date').new)

doc_info.setSubject("PDF Information")

doc_info.setTitle("Setting PDF Document Information")

# حفظ المستند المحدث بالمعلومات الجديدة

doc.save(data_dir + "Updated_Information.pdf")

puts "تم تحديث معلومات المستند، يرجى التحقق من ملف الإخراج."
```


## تحميل الكود التشغيلي

قم بتنزيل **تعيين معلومات ملف PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setpdffileinfo.rb)