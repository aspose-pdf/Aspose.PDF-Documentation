---
title: Memisahkan Halaman PDF
type: docs
weight: 60
url: id/net/split-pdf-pages/
description: Bagian ini menjelaskan cara memisahkan halaman PDF dengan Aspose.PDF Facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Memisahkan Halaman PDF dari Pertama Menggunakan Jalur Berkas

Metode [SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) memungkinkan Anda untuk memisahkan berkas PDF mulai dari halaman pertama dan berakhir pada nomor halaman yang ditentukan. Jika Anda ingin memanipulasi berkas PDF dari disk, Anda dapat memberikan jalur berkas dari berkas PDF input dan output ke metode ini. Potongan kode berikut menunjukkan cara memisahkan halaman PDF dari pertama menggunakan jalur berkas.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingPaths-SplitPagesUsingPaths.cs" >}}

## Memisahkan Halaman PDF dari Pertama Menggunakan Aliran Berkas

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) memungkinkan Anda untuk membagi file PDF mulai dari halaman pertama dan berakhir pada nomor halaman yang ditentukan. Jika Anda ingin memanipulasi file PDF dari aliran, Anda dapat memasukkan aliran PDF input dan output ke metode ini. Cuplikan kode berikut menunjukkan cara membagi halaman PDF dari yang pertama menggunakan aliran file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingStreams-SplitPagesUsingStreams.cs" >}}

## Membagi Halaman PDF ke Dalam Jumlah Besar Menggunakan Jalur File

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittobulks/index) metode dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) memungkinkan Anda untuk membagi file PDF menjadi beberapa set halaman. Dalam contoh ini, kami memerlukan dua set halaman (1, 2) dan (5, 6). Jika Anda ingin mengakses file PDF dari disk, Anda perlu memasukkan PDF sebagai jalur file. Metode ini mengembalikan array MemoryStream. Anda dapat melakukan loop melalui array ini dan menyimpan set halaman individu sebagai file terpisah. Potongan kode berikut menunjukkan kepada Anda cara membagi halaman PDF secara massal menggunakan jalur file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingPaths-SplitPagesToBulkUsingPaths.cs" >}}

## Membagi Halaman PDF Secara Massal Menggunakan Streams

Metode [SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membagi file PDF menjadi beberapa set halaman. Dalam contoh ini, kami memerlukan dua set halaman (1, 2) dan (5, 6). Anda dapat mengoper aliran ke metode ini alih-alih mengakses file dari disk. Metode ini mengembalikan array dari MemoryStream. Anda dapat melakukan loop melalui array ini dan menyimpan set halaman individual sebagai file terpisah. Cuplikan kode berikut menunjukkan cara membagi halaman PDF secara massal menggunakan aliran.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingStreams-SplitPagesToBulkUsingStreams.cs" >}}

## Membagi Halaman PDF Hingga Akhir Menggunakan Jalur File

Metode [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda untuk membagi PDF dari nomor halaman yang ditentukan hingga akhir file PDF dan menyimpannya sebagai PDF baru. Untuk melakukan ini, menggunakan jalur file, Anda perlu memberikan jalur file input dan output serta nomor halaman dari mana pemisahan perlu dimulai. PDF output akan disimpan ke disk. Cuplikan kode berikut menunjukkan cara memisahkan halaman PDF hingga akhir menggunakan jalur file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingPaths-SplitPagesToEndUsingPaths.cs" >}}

## Memisahkan Halaman PDF Hingga Akhir Menggunakan Streams

Metode [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) memungkinkan Anda memisahkan PDF dari nomor halaman yang ditentukan hingga akhir file PDF dan menyimpannya sebagai PDF baru. Untuk melakukan ini, menggunakan streams, Anda perlu melewatkan input dan output streams serta nomor halaman dari mana pemisahan perlu dimulai. PDF output akan disimpan ke output stream. Cuplikan kode berikut menunjukkan cara membagi halaman PDF hingga akhir menggunakan streams.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingStreams-SplitPagesToEndUsingStreams.cs" >}}

## Membagi PDF Menjadi Halaman Individual Menggunakan Jalur File

{{% alert color="primary" %}}

Anda dapat mencoba membagi dokumen PDF dan melihat hasilnya secara online di tautan ini:

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

Untuk membagi file PDF menjadi halaman individual, Anda perlu melewatkan PDF sebagai jalur file ke metode [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Metode ini akan mengembalikan array MemoryStream yang berisi halaman-halaman individual dari file PDF. Anda dapat melakukan iterasi melalui array MemoryStream ini dan menyimpan halaman-halaman individual sebagai file PDF individual di disk. Cuplikan kode berikut menunjukkan kepada Anda cara membagi PDF menjadi halaman-halaman individual menggunakan jalur file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingPaths-SplitToIndividualPagesUsingPaths.cs" >}}

## Membagi PDF Menjadi Halaman-Halaman Individual Menggunakan Stream

Untuk membagi file PDF menjadi halaman-halaman individual, Anda perlu mengirimkan PDF sebagai stream ke metode [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Metode ini akan mengembalikan array MemoryStream yang berisi halaman individu dari file PDF. Anda dapat melakukan loop melalui array MemoryStream ini dan menyimpan halaman individu sebagai file PDF individu di disk, atau Anda dapat menyimpan halaman individu ini dalam memory stream untuk digunakan nanti dalam aplikasi Anda. Cuplikan kode berikut menunjukkan cara membagi PDF menjadi halaman individu menggunakan stream.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingStreams-SplitToIndividualPagesUsingStreams.cs" >}}