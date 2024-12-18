---
title: Sisipkan Halaman PDF
type: docs
weight: 50
url: /id/net/insert-pdf-pages/
description: Bagian ini menjelaskan cara menyisipkan halaman PDF dengan Aspose.PDF Facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Sisipkan Halaman PDF Antara Dua Nomor Menggunakan Jalur File

Rentang halaman tertentu dapat disisipkan dari satu PDF ke yang lain menggunakan metode [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor).
``` Untuk melakukan itu, Anda memerlukan file PDF input di mana Anda ingin menyisipkan halaman, file port dari mana halaman perlu diambil untuk penyisipan, lokasi di mana halaman akan disisipkan, dan rentang halaman dari file port yang harus disisipkan dalam file PDF input. Rentang ini ditentukan dengan parameter halaman awal dan halaman akhir. Akhirnya, file PDF output disimpan dengan rentang halaman yang ditentukan disisipkan dalam file input. Potongan kode berikut menunjukkan kepada Anda bagaimana menyisipkan halaman PDF antara dua angka menggunakan aliran file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesBetweenNumbers-InsertPagesBetweenNumbers.cs" >}}

## Sisipkan Array Halaman PDF Menggunakan Jalur File

Jika Anda ingin menyisipkan beberapa halaman tertentu ke dalam file PDF lain, maka Anda dapat menggunakan overload dari metode [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) yang membutuhkan array integer dari halaman. Dalam array ini, Anda dapat menentukan halaman tertentu yang ingin Anda masukkan ke dalam file PDF input. Untuk melakukannya, Anda memerlukan file PDF input di mana Anda ingin memasukkan halaman, file port dari mana halaman harus diambil untuk dimasukkan, lokasi di mana halaman akan dimasukkan, dan array integer dari halaman dari file port yang harus dimasukkan ke dalam file PDF input. Array ini berisi daftar halaman tertentu yang ingin Anda masukkan ke dalam file PDF input. Akhirnya, file PDF output disimpan dengan array halaman yang ditentukan dimasukkan ke dalam file input.

Potongan kode berikut menunjukkan kepada Anda cara memasukkan array halaman PDF menggunakan jalur file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertArrayOfPages-InsertArrayOfPages.cs" >}}

## Menyisipkan Halaman PDF antara Dua Angka Menggunakan Stream

Jika Anda ingin memasukkan rentang halaman menggunakan stream, Anda hanya perlu menggunakan overload yang sesuai dari metode [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) dari kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Untuk melakukan itu, Anda memerlukan aliran PDF masukan di mana Anda ingin menyisipkan halaman, aliran port dari mana halaman perlu diambil untuk penyisipan, lokasi di mana halaman akan disisipkan, dan rentang halaman dari aliran port yang harus disisipkan dalam aliran PDF masukan. Rentang ini ditentukan dengan parameter halaman awal dan halaman akhir. Akhirnya, aliran PDF keluaran disimpan dengan rentang halaman yang ditentukan disisipkan dalam aliran masukan. Cuplikan kode berikut menunjukkan cara menyisipkan halaman PDF antara dua angka menggunakan aliran.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesBetweenNumbersUsingStreams-InsertPagesBetweenNumbersUsingStreams.cs" >}}

## Menyisipkan Array Halaman PDF Menggunakan Aliran

Anda juga dapat menyisipkan array halaman ke dalam file PDF lain menggunakan aliran dengan bantuan overload metode Insert yang sesuai yang memerlukan array integer dari halaman. Dalam array ini, Anda dapat menentukan halaman tertentu yang ingin Anda masukkan ke dalam aliran PDF masukan. Untuk melakukan itu, Anda memerlukan aliran PDF masukan di mana Anda ingin memasukkan halaman, aliran port dari mana halaman harus diambil untuk dimasukkan, lokasi di mana halaman akan dimasukkan, dan array integer dari halaman dari aliran port yang harus dimasukkan ke dalam file PDF masukan. Array ini berisi daftar halaman tertentu yang Anda ingin masukkan ke dalam aliran PDF masukan. Akhirnya, aliran PDF keluaran disimpan dengan array halaman yang ditentukan dimasukkan ke dalam file masukan. Cuplikan kode berikut menunjukkan kepada Anda bagaimana cara memasukkan array halaman PDF menggunakan aliran.