---
title: Menambahkan JavaScript di Ruby
linktitle: Menambahkan JavaScript di Ruby
type: docs
weight: 10
url: /id/java/adding-javascript-in-ruby/
description: Aktifkan fungsionalitas JavaScript dalam PDF menggunakan Aspose.PDF di Ruby untuk interaktivitas dan otomatisasi.
lastmod: "2026-09-29"
---
## Aspose.PDF - Menambahkan JavaScript

Untuk menambahkan JavaScript dalam dokumen Pdf menggunakan **Aspose.PDF Java for Ruby**, cukup panggil modul **AddJavaScript**.

Kode Ruby

```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Adding JavaScript at Document Level

# Instantiate JavascriptAction with desried JavaScript statement

javaScript = Rjb::import('com.aspose.pdf.JavascriptAction').new("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Assign JavascriptAction object to desired action of Document

doc.setOpenAction(javaScript)

# Adding JavaScript at Page Level

doc.getPages().get_Item(2).getActions().setOnOpen(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is opened')"))

doc.getPages().get_Item(2).getActions().setOnClose(Rjb::import('com.aspose.pdf.JavascriptAction').new("app.alert('page 2 is closed')"))

# Save PDF Document

doc.save(data_dir + "JavaScript-Added.pdf")

puts "Added JavaScript Successfully, please check the output file."
```

## Unduh Kode yang Berjalan

DownloadВ **Menambahkan JavaScript (Aspose.PDF)**В dariВ salah satu situs coding sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addjavascript.rb)
