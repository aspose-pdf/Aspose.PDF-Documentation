---
title: Membuat dan Mengekspor Template
type: docs
weight: 10
url: /id/sharepoint/creating-and-exporting-template/
lastmod: "2020-12-16"
description: Anda dapat membuat dan mengekspor template ke PDF di SharePoint menggunakan PDF SharePoint API.
---

{{% alert color="primary" %}}

Artikel ini menunjukkan cara membuat dan mengekspor template menggunakan Aspose.PDF untuk SharePoint.

Dari Aspose.PDF untuk SharePoint 1.9.2, dukungan template PDF juga mencakup subsitus SharePoint.

{{% /alert %}}

## **Membuat dan Mengekspor Template**
{{% alert color="primary" %}}

Untuk menggunakan fitur ekspor Aspose.PDF untuk SharePoint, pertama buat daftar yang menggunakan "PDF Templates".

Membuat daftar yang menggunakan PDF Templates:

![todo:image_alt_text](creating-and-exporting-template_1.png)

Dua template dokumen, Formulir Tugas dan Daftar Tugas dibuat:

![todo:image_alt_text](creating-and-exporting-template_2.png)

Formulir template memungkinkan Anda memasukkan informasi berikut:

- **Name**: nama file template.
- **Title**: judul template.
 (By default, sama dengan nama file.)
- **Deskripsi**: deskripsi dari template. Deskripsi yang baik membuat template lebih mudah digunakan.
- **Jenis Daftar yang Ditugaskan**: daftar ID yang dipisahkan koma (terkait dengan template. Bidang ini juga dapat berisi nilai **AllListTypes**. Bidang ini hanya berlaku ketika bidang **Type** diatur ke **List**).
- **Jenis Konten yang Ditugaskan**: ID jenis konten yang dipisahkan koma (terkait dengan template. Bidang ini dapat diatur ke **AllListTypes**. Bidang ini hanya berlaku ketika bidang **Type** diatur ke **Item**).
- **Type**: template daftar atau template item.
- **Status**: opsi yang tersedia adalah aktif, tidak aktif (tidak terlihat oleh semua), dan debugging (hanya terlihat oleh admin).

**Formulir Template Daftar Tugas:**

![todo:image_alt_text](creating-and-exporting-template_3.png)

**Formulir Template Formulir Tugas:**

![todo:image_alt_text](creating-and-exporting-template_4.png)

Ketika telah disimpan, template baru muncul dalam daftar template, siap untuk digunakan:

**Dua template daftar tugas:**
![todo:image_alt_text](creating-and-exporting-template_5.png)

**Template formulir tugas:**

![todo:image_alt_text](creating-and-exporting-template_6.png)

#### **Mengembangkan Template**
Template adalah file XML berdasarkan Aspose XML PDF. Untuk membuat template untuk daftar, letakkan penanda khusus terkait dengan nama internal bidang tipe konten target SharePoint ke dalam file XML PDF.
##### **Penanda**
- **SPListItemsCount** – digantikan oleh jumlah item dalam daftar.
- **SPListTitle** – digantikan oleh judul daftar.
- **SPTableIterator** – ditempatkan ke sel tabel pertama dan menandai tabel untuk iterasi penuh.
- **SPRowIterator** – ditempatkan ke sel tabel pertama dan menandai tabel untuk iterasi baris.
- **SPField** – digantikan oleh nilai dari bidang item.

Untuk referensi, silakan unduh [file XML template](attachments/8421394/8618082.zip).
#### **Ekspor ke PDF**
Ketika template sudah sepenuhnya dikonfigurasi, Anda siap untuk mengekspor daftar atau item ke file PDF.

**Mengekspor daftar ke PDF menggunakan template daftar tugas:**
![todo:teks_alt_gambar](creating-and-exporting-template_7.png)

{{% /alert %}}