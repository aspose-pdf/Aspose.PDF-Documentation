---
title: Ekstrak gambar dan ubah posisi cap
type: docs
weight: 30
url: id/net/extract-image-and-change-position-of-a-stamp/
description: Bagian ini menjelaskan cara mengekstrak Gambar dan Mengubah Posisi Cap dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Ekstrak Gambar dari Cap Gambar

Kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) memungkinkan Anda mengekstrak gambar dari cap dalam file PDF. First, you need to create an object of [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, panggil metode [GetStamps](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getstamps) untuk mendapatkan array objek StampInfo dari halaman tertentu file PDF. Kemudian Anda bisa mendapatkan gambar dari StampInfo menggunakan properti StampInfo.Image. Setelah Anda mendapatkan gambar tersebut, Anda bisa menyimpan gambar atau bekerja dengan berbagai properti dari gambar tersebut. Cuplikan kode berikut menunjukkan kepada Anda bagaimana mengekstrak gambar dari cap gambar.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ExtractImageImageStamp-ExtractImageImageStamp.cs" >}}

## Ubah Posisi Cap dalam File PDF

Kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) memungkinkan Anda untuk mengubah posisi cap dalam file PDF. Pertama, Anda perlu membuat objek dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) dan mengikat file PDF input menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Setelah itu, panggil metode [MoveStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestamp) dengan indeks stempel dan posisi baru pada halaman tertentu dari file PDF. Kemudian, Anda dapat menyimpan file yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Cuplikan kode berikut menunjukkan cara memindahkan stempel di halaman tertentu.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPosition.cs" >}}

Selain itu, Anda dapat menggunakan metode [MoveStampById](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid) untuk memindahkan stempel tertentu dengan menggunakan StampId.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPositionByID.cs" >}}