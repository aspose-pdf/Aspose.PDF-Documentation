---
title: تحويل PDF إلى DOC أو DOCX في Ruby
type: docs
weight: 30
url: ar/java/convert-pdf-to-doc-or-docx-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - تحويل PDF إلى DOC أو DOCX

لتحويل مستند PDF إلى تنسيق DOC أو DOCX باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء وحدة **PdfToDoc**.

كود Ruby

```java

# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح المستند الهدف

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# احفظ الملف الناتج المدمج (المستند الهدف)

pdf.save(data_dir + "output.doc")

puts "تم تحويل المستند بنجاح"
```

## تحميل الشيفرة الجارية

قم بتحميل **تحويل PDF إلى DOC أو DOCX (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)