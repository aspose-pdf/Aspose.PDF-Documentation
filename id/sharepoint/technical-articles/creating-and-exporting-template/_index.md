---
title: Membuat dan Mengekspor Template
linktitle: Membuat dan Mengekspor Template
type: docs
weight: 10
url: /id/sharepoint/creating-and-exporting-template/
lastmod: "2026-06-18"
description: Anda dapat membuat dan mengekspor template ke PDF di SharePoint menggunakan PDF SharePoint API.
---

{{% alert color="primary" %}}

Artikel ini menunjukkan cara membuat dan mengekspor template menggunakan Aspose.PDF for SharePoint.

Mulai dari Aspose.PDF for SharePoint 1.9.2, dukungan template PDF juga mencakup subsite SharePoint.

{{% /alert %}}

## **Membuat dan Mengekspor Template**
{{% alert color="primary" %}}

Untuk menggunakan fitur ekspor Aspose.PDF for SharePoint, pertama buat daftar yang menggunakan “PDF Templates”.

Membuat daftar yang menggunakan Template PDF:

![todo:image_alt_text](creating-and-exporting-template_1.png)

Dua template dokumen, Template Form Tugas dan Template Daftar Tugas telah dibuat:

![todo:image_alt_text](creating-and-exporting-template_2.png)



Form template memungkinkan Anda memasukkan informasi berikut:

- **Name**: nama file template.
- **Title**: judul template. (Secara default, sama dengan nama file.)
- **Description**: deskripsi template. Deskripsi yang baik membuat template lebih mudah digunakan.
- **Assigned List Types**: daftar ID yang dipisahkan koma (berkaitan dengan templat. Field ini juga dapat berisi nilai **AllListTypes**. Field ini hanya berlaku ketika field **Type** diatur ke **List**).
- **Assigned Content Types**: ID jenis konten yang dipisahkan koma (berkaitan dengan templat. Field ini dapat diatur ke **AllListTypes**. Field ini hanya berlaku ketika field **Type** diatur ke **Item**).
- **Type**: baik templat daftar atau templat item.
- **Status**: pilihannya adalah aktif, tidak aktif (tidak terlihat oleh siapa pun), dan debugging (hanya terlihat oleh admin).

**Formulir Template Daftar Tugas:**

![todo:image_alt_text](creating-and-exporting-template_3.png)




**Formulir Template Formulir Tugas:**

![todo:image_alt_text](creating-and-exporting-template_4.png)




Setelah disimpan, templat baru muncul di daftar templat, siap untuk digunakan:

**Dua templat daftar tugas:**

![todo:image_alt_text](creating-and-exporting-template_5.png)



**Satu templat formulir tugas:**

![todo:image_alt_text](creating-and-exporting-template_6.png)



#### **Mengembangkan Templat**
Sebuah templat adalah file XML yang berbasis pada Aspose XML PDF. Untuk membuat templat untuk sebuah daftar, letakkan penanda khusus yang terkait dengan nama internal bidang tipe konten target SharePoint ke dalam file XML PDF.
##### **Penanda**
- **SPListItemsCount** – digantikan dengan jumlah item daftar.
- **SPListTitle** – digantikan dengan judul daftar.
- **SPTableIterator** – diletakkan pada sel tabel pertama dan menandai tabel untuk iterasi penuh.
- **SPRowIterator** – diletakkan pada sel tabel pertama dan menandai tabel untuk iterasi baris.
- **SPField** – digantikan dengan nilai bidang item.

Sebagai referensi, silakan unduh [file XML templat](attachments/8421394/8618082.zip).
#### **Ekspor ke PDF**
Ketika sebuah templat telah sepenuhnya dikonfigurasi, Anda siap untuk mengekspor daftar atau item ke file PDF.

**Mengekspor daftar ke PDF menggunakan templat daftar tugas:**

![todo:image_alt_text](creating-and-exporting-template_7.png)

{{% /alert %}}
