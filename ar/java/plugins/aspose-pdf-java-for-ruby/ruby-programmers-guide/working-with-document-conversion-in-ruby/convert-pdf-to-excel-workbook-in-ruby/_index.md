---
title: تحويل PDF إلى مصنف Excel في روبي
linktitle: تحويل PDF إلى مصنف Excel في روبي
type: docs
weight: 40
url: /java/convert-pdf-to-excel-workbook-in-ruby/
description: افهم كيفية تحويل بيانات PDF إلى مصنفات Excel باستخدام Ruby مع Aspose.PDF، مما يبسط استخراج البيانات وتحليلها.
lastmod: "2026-06-09"
---
## Aspose.PDF - تحويل PDF إلى مصنف Excel

لتحويل مستند PDF إلى Excel Workbook باستخدام **Aspose.PDF Java for Ruby**، ما عليك سوى استدعاء وحدة **PdfToExcel**.

كود روبي

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

## تحميل كود التشغيل

تنزيل ** تحويل PDF إلى DOC أو DOCX (Aspose.PDF) **В من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)
