---
title: Ekstrak Teks Dari Semua Halaman Dokumen PDF dengan Ruby
linktitle: Ekstrak Teks Dari Semua Halaman Dokumen PDF dengan Ruby
type: docs
weight: 30
url: /id/java/extract-text-from-all-the-pages-of-a-pdf-document-in-ruby/
description: Pahami cara mengekstrak teks dari semua halaman dokumen PDF menggunakan Ruby dan Aspose.PDF, ideal untuk analisis konten.
lastmod: "2026-09-29"
---
## Aspose.PDF - Ekstrak Teks Dari Semua Halaman

Untuk mengekstrak TextrFrom Semua Halaman dokumen PDF menggunakan **Aspose.PDF Java untuk Ruby**, cukup panggil modul **ExtractTextFromAllPages**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# create TextAbsorber object to extract text

text_absorber = Rjb::import('com.aspose.pdf.TextAbsorber').new

# accept the absorber for all the pages

pdf.getPages().accept(text_absorber)

# In order to extract text from specific page of document, we need to specify the particular page using its index against accept(..) method.

# accept the absorber for particular PDF page

# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

#get the extracted text

extracted_text = text_absorber.getText()

# create a writer and open the file

writer = Rjb::import('java.io.FileWriter').new(Rjb::import('java.io.File').new(data_dir + "extracted_text.out.txt"))

writer.write(extracted_text)

# write a line of text to the file

# tw.WriteLine(extractedText);

# close the stream

writer.close()

puts "Text extracted successfully. Check output file."
```

## Unduh Kode yang Berjalan

Download\u0412\u00A0**Ekstrak Teks Dari Semua Halaman (Aspose.PDF)**\u0412\u00A0dari\u0412\u00A0setiap situs pengkodean sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/extracttextfromallpages.rb)
