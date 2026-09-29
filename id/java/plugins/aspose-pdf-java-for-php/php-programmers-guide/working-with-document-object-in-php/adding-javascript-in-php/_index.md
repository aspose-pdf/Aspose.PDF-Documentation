---
title: Menambahkan JavaScript di PHP
linktitle: Menambahkan JavaScript di PHP
type: docs
weight: 10
url: /id/java/adding-javascript-in-php/
description: Pelajari cara menambahkan JavaScript ke file PDF menggunakan PHP dan Aspose.PDF untuk meningkatkan interaktivitas dokumen.
lastmod: "2026-09-29"
---
## Aspose.PDF - Menambahkan JavaScript

Untuk menambahkan JavaScript dalam dokumen Pdf menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **AddJavaScript**.

Kode PHP

```php
# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Adding JavaScript at Document Level
# Instantiate JavascriptAction with desried JavaScript statement
$javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Assign JavascriptAction object to desired action of Document
$doc->setOpenAction($javaScript);

# Adding JavaScript at Page Level
$doc->getPages()->get_Item(2)->getActions()->setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));
$doc->getPages()->get_Item(2)->getActions()->setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

# Save PDF Document
$doc->save($dataDir . "JavaScript-Added.pdf");

print "Added JavaScript Successfully, please check the output file.";
```

**Unduh Kode yang Berjalan**

Unduh\u0412\u00A0**Adding JavaScript (Aspose.PDF)**\u0412\u00A0dari\u0412\u00A0salah satu situs pengkodean sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)
