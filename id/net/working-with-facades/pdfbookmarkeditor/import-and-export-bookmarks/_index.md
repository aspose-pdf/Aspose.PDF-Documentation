---
title: Impor dan Ekspor Penanda Buku
type: docs
weight: 20
url: id/net/import-and-export-bookmarks/
description: Bagian ini menjelaskan cara mengimpor dan mengekspor Penanda Buku dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Impor Penanda Buku dari XML ke File PDF yang Ada

[ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) metode memungkinkan Anda untuk mengimpor penanda buku ke dalam file PDF dari file XML. Untuk mengimpor penanda buku, Anda perlu membuat objek [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) dan mengikat file PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Setelah itu, Anda perlu memanggil metode [ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1). Terakhir, simpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Cuplikan kode berikut menunjukkan cara mengimpor penanda buku dari file XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ImportFromXML-ImportFromXML.cs" >}}

## Ekspor Penanda Buku ke XML dari File PDF yang Ada

Metode ExportBookmarksToXml memungkinkan Anda mengekspor penanda buku dari file PDF ke file XML.

Untuk mengekspor penanda buku:

1. Create a PdfBookmarkEditor object dan ikat file PDF menggunakan metode BindPdf.
1. Panggil metode ExportBookmarksToXml.
1. Simpan file PDF yang diperbarui menggunakan metode Save.

Cuplikan kode berikut menunjukkan cara mengekspor bookmark ke file XML.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExportToXML-ExportToXML.cs" >}}