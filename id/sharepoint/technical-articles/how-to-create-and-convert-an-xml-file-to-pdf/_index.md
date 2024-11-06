---
title: Cara Membuat dan Mengonversi File XML ke PDF
type: docs
weight: 30
url: id/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2020-12-16"
description: API PDF SharePoint mampu membuat dan mengonversi file XML ke format PDF.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint dibangun di atas komponen Aspose.PDF for .NET yang memenangkan penghargaan. Aspose.PDF for .NET menyediakan fitur luar biasa dari pembuatan dokumen PDF dari awal hingga manipulasi file PDF yang ada. Di antara fitur-fitur ini, konversi XML ke PDF adalah salah satu fitur hebat yang didukung oleh produk ini. Jadi kami percaya bahwa Aspose.PDF for SharePoint juga akan mampu mengonversi file XML ke format PDF.

{{% /alert %}}

## **Membuat File XML dan Mengonversinya ke PDF**

{{% alert color="primary" %}}

Langkah demi langkah, artikel ini memandu Anda melalui proses pembuatan file XML dan mengonversinya ke PDF:
1. [Buat file XML](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [Buat template PDF](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [Muat template XML](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [Tentukan jalur ke jalur sumber](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [Tentukan properti file](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [Ekspor file ke PDF](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [Simpan file PDF](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document).

#### **Langkah 1: Buat File XML**
Pertama buat file XML berdasarkan Aspose.PDF untuk .NET Document Object Model.

Menurut Aspose.PDF untuk .NET DOM, dokumen PDF berisi kumpulan objek Section, dan Section berisi satu atau lebih elemen Paragraph.
 Teks adalah objek tingkat Paragraf dan dapat berisi satu atau lebih segmen. Di bawah ini, sebuah string teks contoh ditambahkan ke objek Segmen dan ditambahkan ke objek Teks. Akhirnya, elemen Teks ditambahkan ke koleksi paragraf objek Section.

**XML**

{{< highlight csharp >}}



<?xml version="1.0" encoding="utf-8" ?>

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>Hello World</Segment>

    </Text>

   </Section>

  </Pdf>



{{< /highlight >}}
#### **Langkah 2: Buat Template PDF**
Sebelum melanjutkan, pastikan bahwa server SharePoint Foundation 2010 telah terpasang dan dikonfigurasi dengan benar pada sistem tempat konversi akan dilakukan.

1. Masuk ke situs SharePoint.
1. Pilih **Site Action** dan **All Items**.
1. Pilih opsi **Create** dan pilih **PDF Template** dari daftar.
1. Masukkan nama template.
1. Klik **Create**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_1.png)
#### **Langkah 3: Muat Template XML**

Setelah template dibuat, muat [file XML tersebut](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/):
1. Pada halaman template PDF, pilih **Tambah item baru**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_2.png)
#### **Langkah 4: Tentukan Jalur File Sumber**
Dalam dialog unggah dokumen:

1. Klik **Browse** dan temukan file XML di sistem Anda. Anda dapat mengaktifkan kotak centang untuk opsi menimpa file yang ada.
1. Tekan tombol **OK**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_3.png)
#### **Langkah 5: Tentukan Properti File**
Ketika file dimuat, tambahkan informasi ke dalam kolom wajib (ditandai dengan tanda bintang merah: *).

Untuk contoh ini, deskripsi sampel telah ditambahkan dan kolom berikut diselesaikan:

1. Deskripsi singkat dari dokumen.
1. Masukkan **AllListTypes** untuk kolom **Assigned List Types**.
1. Pilih **List** dari menu **Type**.
   Pastikan status tetap **Active**.
1. Klik **Save** untuk menyimpan properti.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_4.png)
#### **Langkah 6: Ekspor ke PDF**

Ketika file XML telah ditambahkan ke template PDF:
Either:

1. Klik kanan pada file test.xml.
1. Pilih **Ekspor ke PDF** dari menu.

Atau:

1. Pilih **Aspose Tools** dari **Library Tools**.
1. Klik **Ekspor**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_5.png)
#### **Langkah 7: Simpan Dokumen PDF**
1. Dalam dialog Ekspor ke PDF, pilih **Penyimpanan Template** (lokasi tempat file sumber disimpan).
1. Pilih file untuk diekspor dari menu **Nama Template**.
1. Klik **Ekspor ke PDF** untuk menyimpan dokumen PDF akhir.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_6.png)
#### **Buka PDF**
Dokumen PDF telah disimpan dan dapat dibuka. Pada gambar di bawah, perhatikan frasa "Hello World" yang ada dalam tag {segment] di XML. Juga perhatikan bahwa Produser PDF adalah Aspose.PDF untuk SharePoint.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}