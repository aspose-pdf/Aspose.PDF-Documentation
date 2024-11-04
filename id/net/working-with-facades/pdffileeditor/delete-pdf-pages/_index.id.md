---
title: Hapus halaman PDF
type: docs
weight: 70
url: /net/delete-pdf-pages/
description: Bagian ini menjelaskan cara menghapus halaman PDF dengan Aspose.PDF Facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

Jika Anda ingin menghapus sejumlah halaman dari file PDF yang berada di disk, maka Anda dapat menggunakan overload dari metode [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) yang mengambil tiga parameter berikut: jalur file input, array nomor halaman yang akan dihapus, dan jalur file PDF output. Parameter kedua adalah array integer yang mewakili semua halaman yang perlu dihapus. Halaman yang ditentukan dihapus dari file input dan hasilnya disimpan sebagai file output. Cuplikan kode berikut menunjukkan cara menghapus halaman PDF menggunakan jalur file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingFilePath-DeletePagesUsingFilePath.cs" >}}


## Hapus Halaman PDF Menggunakan Streams

The [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) method dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) juga menyediakan overload yang memungkinkan Anda untuk menghapus halaman dari file PDF input, sementara file input dan output berada dalam aliran. Overload ini mengambil tiga parameter berikut: aliran input, array integer dari halaman PDF yang akan dihapus, dan aliran output. Cuplikan kode berikut menunjukkan cara menghapus halaman PDF menggunakan aliran.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingStream-DeletePagesUsingStream.cs" >}}