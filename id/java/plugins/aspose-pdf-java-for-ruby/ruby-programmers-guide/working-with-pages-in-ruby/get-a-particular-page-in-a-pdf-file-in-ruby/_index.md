---
title: Dapatkan Halaman Tertentu dalam File PDF di Ruby
linktitle: Dapatkan Halaman Tertentu dalam File PDF di Ruby
type: docs
weight: 30
url: /id/java/get-a-particular-page-in-a-pdf-file-in-ruby/
description: Akses dan manipulasi halaman individual dalam dokumen PDF menggunakan Ruby dan Aspose.PDF.
lastmod: "2026-09-29"
---
## Aspose.PDF - Dapatkan Halaman

Untuk mendapatkan Halaman Tertentu dalam dokumen PDF menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **GetPage**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get the page at particular index of Page Collection

pdf_page = pdf.getPages().get_Item(1)

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# add page to pages collection of new document object

new_document.getPages().add(pdf_page)

# save the newly generated PDF file

new_document.save(data_dir + "output.pdf")

puts "Process completed successfully!"
```

## Unduh Kode yang Berjalan

Unduh **Get Page (Aspose.PDF)**В dariВ salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpage.rb)
