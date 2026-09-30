---
title: "Menambahkan string HTML menggunakan DOM di Ruby"
linktitle: "Menambahkan string HTML menggunakan DOM di Ruby"
type: docs
weight: 10
url: /id/java/add-html-string-using-dom-in-ruby/
description: Temukan cara menambahkan string HTML ke dokumen PDF menggunakan API DOM di Ruby dengan Aspose.PDF untuk pembuatan konten dinamis.
lastmod: "2026-09-30"
---
## Aspose.PDF - tambah HTML

Untuk menambahkan string HTML dalam dokumen PDF menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **AddHtml**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate Document object

doc = Rjb::import('com.aspose.pdf.Document').new

# Add a page to pages collection of PDF file

page = doc.getPages().add()

# Instantiate HtmlFragment with HTML contents

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Table</i></b></fontsize>")

# set MarginInfo for margin details

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# Set margin information

title.setMargin(margin)

# Add HTML Fragment to paragraphs collection of page

page.getParagraphs().add(title)

# Save PDF file

doc.save(data_dir + "html.output.pdf")

puts "HTML added successfully"
```

## Mengunduh kode yang dapat dijalankan

Unduh **Add HTML (Aspose.PDF)** dari salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)
