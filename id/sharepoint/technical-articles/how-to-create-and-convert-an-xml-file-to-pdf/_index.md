---
title: Cara Membuat dan Mengonversi File XML ke PDF
linktitle: Cara Membuat dan Mengonversi File XML ke PDF
type: docs
weight: 30
url: /id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2020-12-16"
description: PDF SharePoint API mampu membuat dan mengonversi file XML ke format PDF.
---

{{% alert color="primary" %}}

Aspose.PDF untuk SharePoint dibangun di atas komponen Aspose.PDF untuk .NET pemenang penghargaan kami. Aspose.PDF untuk .NET menyediakan fitur luar biasa mulai dari pembuatan dokumen PDF dari awal hingga manipulasi file PDF yang ada. Di antara fitur-fitur tersebut, konversi XML ke PDF adalah salah satu fitur hebat yang didukung produk ini. Jadi kami yakin Aspose.PDF untuk SharePoint juga akan mampu mengonversi file XML ke format PDF.

{{% /alert %}}

## Membuat dan File XML dan Mengonversinya ke PDF

{{% alert color="primary" %}}

Langkah demi langkah, artikel ini memandu Anda melalui proses pembuatan dan file XML serta mengonversinya menjadi PDF:

1. [Buat file XML](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [Buat templat PDF](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [Muat templat XML](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [Tentukan jalur ke jalur sumber](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [Tentukan properti file](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [Ekspor file ke PDF](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [Simpan file PDFnya](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document)

### Langkah 1: Buat File XML

Pertama buat file XML berdasarkan Aspose.PDF untuk Model Objek Dokumen .NET.

Menurut Aspose.PDF untuk .NET DOM, dokumen PDF berisi kumpulan objek Bagian, dan Bagian berisi satu atau lebih elemen Paragraf. Teks adalah objek tingkat Paragraf dan mungkin berisi satu atau lebih segmen. Di bawah ini, contoh string teks ditambahkan ke objek Segmen dan ditambahkan ke objek Teks. Terakhir, elemen Teks ditambahkan ke kumpulan paragraf objek Bagian.

```xml

<?xml version="1.0" encoding="utf-8" ?>

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>Hello World</Segment>

    </Text>

   </Section>

  </Pdf>

```

### Langkah 2: Buat Templat PDF

Sebelum melanjutkan, pastikan server SharePoint Foundation 2010 telah diinstal dan dikonfigurasi dengan benar pada sistem tempat konversi akan dilakukan.

1. Masuk ke situs SharePoint.
1. Pilih **Tindakan Situs** dan **Semua Item**.
1. Pilih opsi **Buat** dan pilih **Templat PDF** dari daftar.
1. Masukkan nama templat.
1. Klik **Buat**.

![Buat Templat PDF](how-to-create-and-convert-an-xml-file-to-pdf_1.png)

### Langkah 3: Muat Templat XML

Setelah template dibuat, muat [file XMLnya](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/)

1. Pada halaman templat PDF, pilih **Tambahkan item baru**.

![Muat Templat XML](how-to-create-and-convert-an-xml-file-to-pdf_2.png)

### Langkah 4: Tentukan Jalur File Sumber

Dalam dialog unggah dokumen:

1. Klik **Jelajahi** dan temukan file XML di sistem Anda. Anda dapat mengaktifkan kotak centang untuk menimpa opsi file yang ada.
1. Tekan tombol **OK**.

![Tentukan Jalur File Sumber](how-to-create-and-convert-an-xml-file-to-pdf_3.png)

### Langkah 5: Tentukan Properti File

Saat file dimuat, tambahkan informasi ke kolom wajib (ditandai dengan tanda bintang merah: *).

Untuk contoh ini, deskripsi sampel telah ditambahkan dan kolom berikut diisi:

1. Deskripsi singkat tentang dokumen tersebut.
1. Masukkan **AllListTypes** untuk bidang **Jenis Daftar yang Ditugaskan**.
1. Pilih **Daftar** dari menu **Jenis**.
   Pastikan statusnya tetap **Aktif**.
1. Klik **Simpan** untuk menyimpan properti.

![Tentukan Properti File](how-to-create-and-convert-an-xml-file-to-pdf_4.png)

### Langkah 6: Ekspor ke PDF

Ketika file XML telah ditambahkan ke template PDF:
Salah satu:

1. Klik kanan file test.xml.
1. Pilih **Ekspor ke PDF** dari menu.

Atau:

1. Pilih **Apose Tools** dari **Alat Perpustakaan**.
1. Klik **Ekspor**.

![Ekspor ke PDF](how-to-create-and-convert-an-xml-file-to-pdf_5.png)

### Langkah 7: Simpan Dokumen PDF

1. Dalam dialog Ekspor ke PDF, pilih **Penyimpanan template** (lokasi penyimpanan file sumber).
1. Pilih file yang akan diekspor dari menu **Nama template**.
1. Klik **Ekspor ke PDF** untuk menyimpan dokumen PDF akhir.

![Simpan Dokumen PDF](how-to-create-and-convert-an-xml-file-to-pdf_6.png)

## Buka PDFnya

Dokumen PDF telah disimpan dan dapat dibuka. Pada gambar di bawah, perhatikan frasa "Halo Dunia" yang ada di tag segmen di XML. Perhatikan juga bahwa Produser PDF adalah Aspose.PDF untuk SharePoint.

![Buka PDFnya](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}

