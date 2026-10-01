---
title: "Mengonversi PDF ke Format SVG dalam Ruby"
linktitle: "Mengonversi PDF ke Format SVG dalam Ruby"
type: docs
weight: 50
url: /id/java/convert-pdf-to-svg-format-in-ruby/
description: Temukan cara mengonversi file PDF ke format SVG menggunakan Ruby dan Aspose.PDF, memungkinkan grafik vektor yang dapat diskalakan dan dapat diedit.
lastmod: "2026-09-30"
---
## Aspose.PDF - konversi PDF ke SVG

Untuk mengonversi PDF ke format SVG menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **PdfToSvg**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# instantiate an object of SvgSaveOptions

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# do not compress SVG image to Zip archive

save_options.CompressOutputToZipArchive = false

# Save the output to XLS format

pdf.save(data_dir + "Output.svg", save_options)

puts "Document has been converted successfully"
```

## Mengunduh kode yang dapat dijalankan

Unduh **Convert PDF to SVG Format (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)
