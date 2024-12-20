---
title: Menggabungkan Dokumen PDF di C#
linktitle: Menggabungkan Dokumen PDF
type: docs
weight: 20
url: /id/net/concatenate-pdf-documents/
description: Bagian ini menjelaskan cara menggabungkan dokumen PDF dengan Aspose.PDF Facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
---

## **Ikhtisar**

Artikel ini menjelaskan cara menggabungkan, mengkombinasikan, atau menyatukan berbagai file PDF menjadi satu PDF menggunakan C#. Ini mencakup topik-topik seperti

- [C# Menggabungkan File PDF](#concatenate-pdf-files-using-file-paths)
- [C# Mengkombinasikan File PDF](#concatenate-pdf-files-using-file-paths)

- [C# Menggabungkan Beberapa File PDF menjadi satu PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Gabungkan Beberapa File PDF menjadi satu PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Gabungkan semua file PDF dalam satu folder](#concatenating-all-pdf-files-in-particular-folder)
- [C# Gabungkan semua file PDF dalam satu folder](#concatenating-all-pdf-files-in-particular-folder)
- [C# Gabungkan file PDF menggunakan jalur file](#concatenate-pdf-files-using-file-paths)
- [C# Gabungkan file PDF menggunakan stream](#concatenate-array-of-pdf-files-using-streams)
- [C# Gabungkan semua file PDF dalam folder](#concatenate-pdf-files-in-folder)

## Gabungkan file PDF menggunakan jalur file

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) adalah kelas dalam [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) yang memungkinkan Anda untuk menggabungkan beberapa file PDF. Anda tidak hanya dapat menggabungkan file menggunakan FileStreams tetapi juga menggunakan MemoryStreams. Dalam artikel ini, proses penggabungan file menggunakan MemoryStreams akan dijelaskan dan kemudian ditunjukkan menggunakan cuplikan kode.

Metode [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) dapat digunakan untuk menggabungkan dua file PDF. Metode [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) memungkinkan Anda untuk memasukkan tiga parameter: PDF input pertama, PDF input kedua, dan PDF output. PDF output akhir berisi kedua file PDF input.

Cuplikan kode C# berikut menunjukkan cara menggabungkan file PDF menggunakan jalur file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-ConcatenateUsingPath.cs" >}}

Dalam beberapa kasus, ketika ada banyak outline, pengguna dapat menonaktifkannya dengan mengatur CopyOutlines ke false dan meningkatkan kinerja penggabungan.
{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-CopyOutline.cs" >}}

## Menggabungkan beberapa file PDF menggunakan MemoryStreams

Metode [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) mengambil file PDF sumber dan file PDF tujuan sebagai parameter. Parameter ini dapat berupa jalur ke file PDF di disk atau mereka bisa berupa MemoryStreams. Sekarang, untuk contoh ini, kita akan terlebih dahulu membuat dua aliran file untuk membaca file PDF dari disk. Kemudian kita akan mengonversi file-file ini menjadi array byte. Array byte dari file PDF ini akan diubah menjadi MemoryStreams. Setelah kita mendapatkan MemoryStreams dari file PDF, kita akan dapat meneruskannya ke metode penggabungan dan menggabungkannya menjadi satu file keluaran.


Cuplikan kode C# berikut menunjukkan cara menggabungkan beberapa file PDF menggunakan MemoryStreams:

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenateMultiplePDFUsingMemoryStream-ConcatenateMultiplePDFUsingMemoryStream.cs" >}}

## Menggabungkan Array File PDF Menggunakan Jalur File

Jika Anda ingin menggabungkan beberapa file PDF, Anda dapat menggunakan overload dari metode [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index), yang memungkinkan Anda untuk memasukkan array file PDF. Output akhir disimpan sebagai file gabungan yang dibuat dari semua file dalam array. Potongan kode C# berikut menunjukkan cara menggabungkan array file PDF menggunakan jalur file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfFilesWithPath-ConcatenateArrayOfFilesWithPath.cs" >}}

## Menggabungkan Array File PDF Menggunakan Streams

Menggabungkan array file PDF tidak terbatas hanya pada file yang berada di disk. Anda juga dapat menggabungkan array file PDF dari aliran. Jika Anda ingin menggabungkan beberapa file PDF, Anda dapat menggunakan overload yang sesuai dari metode [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). Pertama, Anda perlu membuat array dari aliran input dan satu aliran untuk output PDF dan kemudian memanggil metode [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). Output akan disimpan dalam aliran output. Potongan kode C# berikut menunjukkan cara menggabungkan array file PDF menggunakan aliran.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfPdfUsingStreams-ConcatenateArrayOfPdfUsingStreams.cs" >}}

## Menggabungkan semua file Pdf dalam folder tertentu

Anda bahkan dapat membaca semua file Pdf dalam folder tertentu saat runtime dan menggabungkannya, tanpa perlu mengetahui nama file. Berikan jalur direktori, yang berisi dokumen PDF, yang ingin Anda gabungkan.

Silakan coba gunakan potongan kode C# berikut untuk mencapai fungsi ini.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatingAllPdfFiles-ConcatenatingAllPdfFiles.cs" >}}

## Menggabungkan Formulir PDF dan menjaga nama bidang tetap unik

Kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) dalam [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) menawarkan kemampuan untuk menggabungkan file PDF. Sekarang, jika file Pdf yang akan digabungkan memiliki bidang formulir dengan nama bidang yang serupa, Aspose.PDF menyediakan fitur untuk menjaga agar bidang dalam file Pdf hasil tetap unik dan Anda juga dapat menentukan akhiran untuk membuat nama bidang unik. Properti [KeepFieldsUnique](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) dari [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) sebagai true akan membuat nama bidang unik ketika formulir Pdf digabungkan. Juga, properti [UniqueSuffix](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) dari PdfFileEditor dapat digunakan untuk menentukan format akhiran yang ditentukan pengguna yang ditambahkan ke nama bidang untuk membuatnya unik ketika formulir digabungkan. String ini harus mengandung substring `%NUM%` yang akan diganti dengan angka dalam file hasil.

Silakan lihat cuplikan kode sederhana berikut untuk mencapai fungsionalitas ini.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePDFForms-ConcatenatePDFForms.cs" >}}
## Menggabungkan file PDF dan membuat Daftar Isi

## Menggabungkan file PDF

Silakan lihat potongan kode berikut untuk informasi tentang cara menggabungkan file PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-ConcatenatePdfFilesAndCreateTOC.cs" >}}

### Menyisipkan halaman kosong

Setelah file PDF digabungkan, kita dapat menyisipkan halaman kosong di awal dokumen di mana kita dapat membuat Daftar Isi. Untuk memenuhi persyaratan ini, kita dapat memuat file yang digabungkan ke dalam objek **Document** dan kita perlu memanggil metode Page.Insert(...) untuk menyisipkan halaman kosong.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-InsertBlankPage.cs" >}}

### Menambahkan Stempel Teks

Untuk membuat Daftar Isi, kita perlu menambahkan stempel teks pada halaman pertama menggunakan objek [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) dan [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp). Stamp class menyediakan metode `BindLogo(...)` untuk menambahkan [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) dan kita juga dapat menentukan lokasi untuk menambahkan stempel teks ini menggunakan metode `SetOrigin(..)`. Dalam artikel ini, kita menggabungkan dua file PDF, jadi kita perlu membuat dua objek stempel teks yang mengarah ke dokumen individual ini.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-AddTextStamps.cs" >}}

### Buat tautan lokal

Sekarang kita perlu menambahkan tautan ke halaman di dalam file yang digabungkan. Untuk memenuhi persyaratan ini, kita dapat menggunakan metode `CreateLocalLink(..)` dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Dalam cuplikan kode berikut, kami telah mengirimkan Transparent sebagai argumen ke-4 sehingga persegi panjang di sekitar tautan tidak terlihat.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CreateLocalLinks.cs" >}}
### Complete code

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CompletedCode.cs" >}}


## Menggabungkan file PDF dalam folder

Kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) dalam namespace Aspose.Pdf.Facades menawarkan kemampuan untuk menggabungkan file PDF. Anda bahkan dapat membaca semua file Pdf dalam folder tertentu pada waktu proses dan menggabungkannya, tanpa harus mengetahui nama file. Cukup berikan jalur direktori yang berisi dokumen PDF yang ingin Anda gabungkan.

Silakan coba gunakan potongan kode C# berikut untuk mencapai fungsi ini dari Aspose.PDF:

```csharp
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

// Ambil nama semua file Pdf dalam Direktori tertentu
string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

// Dapatkan tanggal Sistem saat ini dan atur formatnya
string date = DateTime.Now.ToString("MM-dd-yyyy");
// Dapatkan waktu Sistem saat ini dan atur formatnya
string hoursSeconds = DateTime.Now.ToString("hh-mm");
// Tetapkan nilai untuk dokumen Pdf Hasil Akhir
string masterFileName = date + "_" + hoursSeconds + "_out.pdf";

// Instansiasi objek PdfFileEditor
Aspose.Pdf.Facades.PdfFileEditor pdfEditor = new PdfFileEditor();

// Panggil metode Concatenate dari objek PdfFileEditor untuk menggabungkan semua file input
// Menjadi satu file output
pdfEditor.Concatenate(fileEntries, dataDir + masterFileName);
```