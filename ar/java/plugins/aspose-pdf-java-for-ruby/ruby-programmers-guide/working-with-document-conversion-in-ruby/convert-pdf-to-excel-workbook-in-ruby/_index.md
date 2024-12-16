---
title: تحويل PDF إلى مصنف Excel في روبي
type: docs
weight: 40
url: /ar/java/convert-pdf-to-excel-workbook-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - تحويل PDF إلى مصنف Excel

لتحويل مستند PDF إلى مصنف Excel باستخدام **Aspose.PDF Java for Ruby**، قم ببساطة باستدعاء وحدة **PdfToExcel**.

كود روبي

```java

# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح المستند الهدف

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# إنشاء كائن خيار ExcelSave

excelsave = Rjb::import('com.aspose.pdf.ExcelSaveOptions').new

# احفظ النتيجة بتنسيق XLS

pdf.save(data_dir + "Converted_Excel.xls", excelsave)

puts "تم تحويل المستند بنجاح"
```

## تنزيل الكود الجاري

قم بتنزيل **تحويل PDF إلى DOC أو DOCX (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)