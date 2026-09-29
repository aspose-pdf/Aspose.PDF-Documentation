---
title: Konversi PDF ke Buku Kerja Excel dengan Ruby
linktitle: Konversi PDF ke Buku Kerja Excel dengan Ruby
type: docs
weight: 40
url: /id/java/convert-pdf-to-excel-workbook-in-ruby/
description: Pahami cara mengonversi data PDF menjadi buku kerja Excel menggunakan Ruby dengan Aspose.PDF, mempermudah ekstraksi dan analisis data.
lastmod: "2026-09-29"
---
## Aspose.PDF - Konversi PDF ke Buku Kerja Excel

Untuk mengonversi dokumen PDF ke Buku Kerja Excel menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **PdfToExcel**.

Kode Ruby

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

## Unduh Kode yang Berjalan

DownloadВ **Konversi PDF ke DOC atau DOCX (Aspose.PDF)**В dariВ semua situs sosial coding yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)
