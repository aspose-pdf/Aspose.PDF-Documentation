---
title: Perbarui Dimensi Halaman di Ruby
linktitle: Perbarui Dimensi Halaman di Ruby
type: docs
weight: 90
url: /id/java/update-page-dimensions-in-ruby/
description: Pelajari cara memperbarui dimensi halaman dokumen PDF menggunakan Ruby dengan Aspose.PDF untuk pemformatan halaman yang tepat.
lastmod: "2026-09-29"
---
## Aspose.PDF - Perbarui Dimensi Halaman

Untuk memperbarui Dimensi halaman menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **UpdatePageDimensions**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get page collection

page_collection = pdf.getPages()

# get particular page

pdf_page = page_collection.get_Item(1)

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points

# so A4 dimensions in points will be (842.4, 597.6)

pdf_page.setPageSize(597.6,842.4)

# save the newly generated PDF file

pdf.save(data_dir + "output.pdf")

puts "Dimensions updated successfully!"
```

## Unduh Kode yang Berjalan

UnduhВ **Perbarui Dimensi Halaman (Aspose.PDF)**В dariВ salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/updatepagedimensions.rb)
