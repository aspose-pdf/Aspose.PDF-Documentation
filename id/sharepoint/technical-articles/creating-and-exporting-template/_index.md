---
title: Membuat dan Mengekspor Template
linktitle: Membuat dan Mengekspor Template
type: docs
weight: 10
url: /id/sharepoint/creating-and-exporting-template/
lastmod: "2026-08-07"
description: Anda dapat membuat dan mengekspor template ke PDF di SharePoint menggunakan PDF SharePoint API.
---

{{% alert color="primary" %}}

Artikel ini menunjukkan cara membuat dan mengekspor template menggunakan Aspose.PDF for SharePoint.

Mulai dari Aspose.PDF for SharePoint 1.9.2, dukungan template PDF juga mencakup subsite SharePoint.

{{% /alert %}}

## Membuat dan Mengekspor Template

{{% alert color="primary" %}}

Untuk menggunakan fitur ekspor Aspose.PDF for SharePoint, pertama buat daftar yang menggunakan “PDF Templates”.

Membuat daftar yang menggunakan PDF Templates:

![Buat Daftar Template PDF](creating-and-exporting-template_1.png)

Dua template dokumen, Task Form Templates dan Task List Templates dibuat:

![Template Dokumen](creating-and-exporting-template_2.png)

Formulir templat memungkinkan Anda memasukkan informasi berikut:

- **Name**: nama file templat.
- **Title**: judul templat. (Secara default, sama dengan nama file.)
- **Description**: deskripsi templat. Deskripsi yang baik membuat templat lebih mudah digunakan.
- **Assigned List Types**: ID daftar yang dipisahkan koma (terkait dengan templat. Kolom ini juga dapat berisi nilai
- **AllListTypes**. Kolom ini hanya berlaku ketika kolom **Type** disetel ke **List**).
- **Assigned Content Types**: ID tipe konten yang dipisahkan koma terkait dengan templat. Bidang ini dapat diatur menjadi **AllListTypes**. Bidang ini hanya berlaku ketika bidang **Type** diatur ke **Item**.
- **Type**: baik templat daftar maupun templat item.
- **Status**: opsi-opsinya adalah aktif, tidak aktif (tidak terlihat oleh siapa pun), dan debug (hanya terlihat oleh admin).

Form Templat Daftar Tugas:

![Templat Daftar Tugas](creating-and-exporting-template_3.png)

Form Templat Form Tugas:

![Template Form Tugas](creating-and-exporting-template_4.png)

Setelah disimpan, template baru muncul dalam daftar template, siap untuk digunakan:

Dua template daftar tugas:*

![Templat Daftar Tugas](creating-and-exporting-template_5.png)

Sebuah template formulir tugas:

![Template Form Tugas](creating-and-exporting-template_6.png)

### Mengembangkan Template

Template adalah file XML yang berbasis Aspose XML PDF. Untuk membuat template untuk sebuah daftar, tempatkan penanda khusus yang terkait dengan nama internal bidang tipe konten target SharePoint ke dalam file XML PDF.

### Penanda

- **SPListItemsCount** – diganti dengan jumlah item daftar.
- **SPListTitle** – diganti dengan judul daftar.
- **SPTableIterator** – ditempatkan pada sel tabel pertama dan menandai tabel untuk iterasi penuh.
- **SPRowIterator** – ditempatkan pada sel tabel pertama dan menandai tabel untuk iterasi baris.
- **SPField** – diganti dengan nilai field item.

Untuk referensi, silakan unduh [file XML templat](attachments/8421394/8618082.zip).

### Ekspor ke PDF

Ketika sebuah templat sudah sepenuhnya dikonfigurasi, Anda siap mengekspor daftar atau item ke file PDF.

Mengekspor daftar ke PDF menggunakan templat daftar tugas:

![Ekspor ke PDF](creating-and-exporting-template_7.png)

{{% /alert %}}
