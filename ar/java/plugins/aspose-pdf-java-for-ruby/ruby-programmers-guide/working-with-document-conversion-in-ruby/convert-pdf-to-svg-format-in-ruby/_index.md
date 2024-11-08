---
title: تحويل PDF إلى صيغة SVG في روبي
type: docs
weight: 50
url: /ar/java/convert-pdf-to-svg-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - تحويل PDF إلى SVG

لتحويل PDF إلى صيغة SVG باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء وحدة **PdfToSvg**.

كود روبي

```java

# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح المستند الهدف

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# إنشاء كائن من SvgSaveOptions

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# لا تقم بضغط صورة SVG إلى أرشيف Zip

save_options.CompressOutputToZipArchive = false

# احفظ الناتج بصيغة XLS

pdf.save(data_dir + "Output.svg", save_options)

puts "تم تحويل المستند بنجاح"
```

## تحميل الكود الجاري

قم بتحميل **تحويل PDF إلى صيغة SVG (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)