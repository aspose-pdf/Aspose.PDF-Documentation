---
title: تحويل PDF إلى دفتر عمل Excel بلغة Ruby
linktitle: تحويل PDF إلى دفتر عمل Excel بلغة Ruby
type: docs
weight: 40
url: /ar/java/convert-pdf-to-excel-workbook-in-ruby/
description: فهم كيفية تحويل بيانات PDF إلى دفاتر عمل Excel باستخدام Ruby مع Aspose.PDF، وتبسيط استخراج البيانات والتحليل.
lastmod: "2026-10-05"
---
## Aspose.PDF - تحويل PDF إلى دفتر عمل Excel

لتحويل مستند PDF إلى دفتر عمل Excel باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **PdfToExcel**.

كود Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Instantiate ExcelSave Option object

excelsave = Rjb::import('com.aspose.pdf.ExcelSaveOptions').new

# Save the output to XLS format

pdf.save(data_dir + "Converted_Excel.xls", excelsave)

puts "Document has been converted successfully"
```

## تحميل الكود الجاري

Download **تحويل PDF إلى DOC أو DOCX (Aspose.PDF)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)
