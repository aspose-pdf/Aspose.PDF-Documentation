---
title: Manipulate Page Properties
type: docs
weight: 80
url: id/net/manipulate-page-properties/
description: Bagian ini menjelaskan cara memanipulasi Properti Halaman dengan Aspose.PDF Facades menggunakan Kelas PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---

## Dapatkan Properti Halaman PDF dari File PDF yang Ada

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) memungkinkan Anda bekerja dengan halaman individu dari file PDF. Itu membantu Anda mendapatkan properti halaman individu seperti ukuran kotak halaman yang berbeda, rotasi halaman, zoom halaman, dll. Untuk mendapatkan properti tersebut, Anda perlu membuat objek [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, Anda dapat menggunakan metode yang berbeda untuk mendapatkan properti halaman seperti [GetPageRotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation), [GetPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpages), [GetPageBoxSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize) dll.

Cuplikan kode berikut menunjukkan kepada Anda cara mendapatkan properti halaman PDF dari file PDF yang ada.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-GetPageProperties-GetPageProperties.cs" >}}
## Mengatur Properti Halaman PDF dalam File PDF yang Sudah Ada

Untuk mengatur properti halaman seperti rotasi halaman, zoom, atau titik asal, Anda perlu menggunakan kelas [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor). Kelas ini menyediakan berbagai metode dan properti untuk mengatur properti halaman ini. Pertama-tama, Anda perlu membuat objek dari kelas [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, Anda dapat menggunakan metode dan properti ini untuk mengatur properti halaman. Akhirnya, simpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

Cuplikan kode berikut menunjukkan kepada Anda cara mengatur properti halaman PDF dalam file PDF yang sudah ada.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-SetPageProperties-SetPageProperties.cs" >}}

## Ubah Ukuran Konten Halaman pada Halaman Tertentu dalam File PDF

Metode ResizeContents dari kelas [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) memungkinkan Anda untuk mengubah ukuran konten halaman dalam file PDF. Kelas [ContentsResizeParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) digunakan untuk menentukan parameter yang digunakan untuk mengubah ukuran halaman, misalnya margin dalam persentase atau satuan lainnya. Anda dapat mengubah ukuran semua halaman atau menentukan array halaman yang akan diubah ukurannya menggunakan metode ResizeContents.

Cuplikan kode berikut menunjukkan cara mengubah ukuran konten dari beberapa halaman tertentu dalam file PDF.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-ResizePageContents-ResizePageContents.cs" >}}