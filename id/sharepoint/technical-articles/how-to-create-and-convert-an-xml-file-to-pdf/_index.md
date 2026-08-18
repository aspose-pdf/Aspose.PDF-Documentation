---
title: Cara Membuat dan Mengonversi File XML ke PDF
linktitle: Cara Membuat dan Mengonversi File XML ke PDF
type: docs
weight: 30
url: /id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2026-08-07"
description: API PDF SharePoint mampu membuat dan mengonversi file XML ke format PDF.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint dibangun di atas komponen Aspose.PDF for .NET kami yang telah memenangkan penghargaan. Aspose.PDF for .NET menyediakan fitur luar biasa mulai dari pembuatan dokumen PDF dari awal hingga manipulasi file PDF yang ada. Di antara fitur-fitur ini, konversi XML ke PDF adalah salah satu fitur hebat yang didukung oleh produk ini. Oleh karena itu, kami yakin bahwa Aspose.PDF for SharePoint juga akan mampu mengonversi file XML ke format PDF.

{{% /alert %}}

## Membuat File XML dan Mengonversinya ke PDF

{{% alert color="primary" %}}

Langkah demi langkah, artikel ini memandu Anda melalui proses membuat file XML dan mengonversinya menjadi PDF:

1. [Buat file XML](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [Buat templat PDF](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [Muat templat XML](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [Tentukan jalur ke jalur sumber](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [Tentukan properti file](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [Ekspor file ke PDF](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [Simpan file PDF](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document)

### Langkah 1: Buat File XML

Pertama buat file XML berdasarkan Document Object Model Aspose.PDF for .NET.

Menurut Aspose.PDF for .NET DOM, sebuah dokumen PDF berisi koleksi objek Section, dan sebuah Section berisi satu atau lebih elemen Paragraph. Text adalah objek tingkat Paragraph dan dapat berisi satu atau lebih segmen. Di bawah ini, sebuah string teks contoh ditambahkan ke objek Segment dan ditambahkan ke objek Text. Akhirnya, elemen Text ditambahkan ke koleksi paragraf objek Section.

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

### Langkah 2: Buat Template PDF

Sebelum melanjutkan, pastikan bahwa server SharePoint Foundation 2010 telah terpasang dan dikonfigurasi dengan benar pada sistem dimana konversi akan dilakukan.

1. Masuk ke situs SharePoint.
1. Pilih **Site Action** dan **All Items**.
1. Pilih opsi **Create** dan pilih **PDF Template** dari daftar.
1. Masukkan nama template.
1. Klik **Create**.

![Buat PDF Template](how-to-create-and-convert-an-xml-file-to-pdf_1.png)

### Langkah 3: Muat XML Template

Setelah template dibuat, muat [file XML](/pdf/id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/)

1. Pada halaman templat PDF, pilih **Add new item**.

![Muat Templat XML](how-to-create-and-convert-an-xml-file-to-pdf_2.png)

### Langkah 4: Tentukan Jalur File Sumber

Di dialog unggah dokumen:

1. Klik **Browse** dan temukan file XML di sistem Anda. Anda dapat mengaktifkan kotak centang untuk opsi menimpa file yang ada.
1. Tekan tombol **OK**.

![Tentukan Path File Sumber](how-to-create-and-convert-an-xml-file-to-pdf_3.png)

### Langkah 5: Tentukan Properti File

Setelah file dimuat, tambahkan informasi ke dalam bidang wajib (ditandai dengan tanda bintang merah: *).

Untuk contoh ini, sebuah deskripsi contoh telah ditambahkan dan bidang-bidang berikut telah diisi:

1. Deskripsi singkat dokumen.
1. Masukkan **AllListTypes** untuk bidang **Assigned List Types**.
1. Pilih **List** dari menu **Type**.
   Pastikan status tetap **Active**.
1. Klik **Save** untuk menyimpan properti.

![Tentukan Properti File](how-to-create-and-convert-an-xml-file-to-pdf_4.png)

### Langkah 6: Ekspor ke PDF

Ketika file XML telah ditambahkan ke templat PDF:
Atau:

1. Klik kanan file test.xml.
1. Pilih **Export to PDF** dari menu.

Atau:

1. Pilih **Aspose Tools** dari **Library Tools**.
1. Klik **Export**.

![Ekspor ke PDF](how-to-create-and-convert-an-xml-file-to-pdf_5.png)

### Langkah 7: Simpan Dokumen PDF

1. Di dialog Ekspor ke PDF, pilih **Template storage** (lokasi di mana file sumber disimpan).
1. Pilih file yang akan diekspor dari menu **Template name**.
1. Klik **Export to PDF** untuk menyimpan dokumen PDF akhir.

![Simpan Dokumen PDF](how-to-create-and-convert-an-xml-file-to-pdf_6.png)

## Buka PDF

Dokumen PDF telah disimpan dan dapat dibuka. Pada gambar di bawah, perhatikan frasa "Hello World" yang ada di tag segmen dalam XML. Juga perhatikan bahwa PDF Producer adalah Aspose.PDF for SharePoint.

![Buka PDF](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}
