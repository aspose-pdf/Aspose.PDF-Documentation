---
title: "Mengonversi file SVG ke format PDF dalam Ruby"
linktitle: "Mengonversi file SVG ke format PDF dalam Ruby"
type: docs
weight: 60
url: /id/java/convert-svg-file-to-pdf-format-in-ruby/
description: Pelajari cara mengonversi file SVG ke format PDF dalam Ruby menggunakan Aspose.PDF untuk transformasi dokumen yang akurat dan dapat diskalakan.
lastmod: "2026-09-30"
---
## Aspose.PDF - konversi SVG ke PDF

Untuk mengonversi file SVG ke format PDF menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **SvgToPdf**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate LoadOption object using SVG load option

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# Create document object

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# Save the output to XLS format

pdf.save(data_dir + "SVG.pdf")

puts "Document has been converted successfully"
```

## Mengunduh kode yang dapat dijalankan

Unduh **Convert SVG to PDF (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)
