---
title: Konversi PDF ke Buku Kerja Excel dalam Ruby
type: docs
weight: 40
url: /java/convert-pdf-to-excel-workbook-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Konversi PDF ke Buku Kerja Excel

Untuk mengkonversi dokumen PDF ke Buku Kerja Excel menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **PdfToExcel**.

Kode Ruby

```java

# Jalur ke direktori dokumen.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Buka dokumen target

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Instansiasi objek ExcelSave Option

excelsave = Rjb::import('com.aspose.pdf.ExcelSaveOptions').new

# Simpan keluaran ke format XLS

pdf.save(data_dir + "Converted_Excel.xls", excelsave)

puts "Dokumen telah berhasil dikonversi"
```

## Unduh Kode Berjalan

Unduh **Konversi PDF ke DOC atau DOCX (Aspose.PDF)** dari salah satu situs kode sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)