---
title: "Memisahkan file PDF menjadi halaman individu di Ruby"
linktitle: "Memisahkan file PDF menjadi halaman individu di Ruby"
type: docs
weight: 80
url: /id/java/split-pdf-file-into-individual-pages-in-ruby/
description: Pahami cara memisahkan file PDF menjadi halaman individu dengan Ruby dan Aspose.PDF, sehingga lebih mudah mengelola dan mengekstrak konten.
lastmod: "2026-09-30"
---
## Aspose.PDF - memisahkan halaman

Untuk memisahkan dokumen PDF menjadi halaman individu menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **SplitAllPages**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# loop through all the pages

pdf_page = 1

#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)

while pdf_page <= pdf.getPages().size()

# create a new Document object

new_document = Rjb::import('com.aspose.pdf.Document').new

# get the page at particular index of Page Collection

new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file

new_document.save(data_dir + "page_#{pdf_page}.pdf")

pdf_page +=1

end

puts "Split process completed successfully!"
```

## Mengunduh kode yang dapat dijalankan

Unduh **Split Pages (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/splitallpages.rb)
