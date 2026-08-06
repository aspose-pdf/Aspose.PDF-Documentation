---
title: Membuat dan Mengekspor Templat
linktitle: Creating and Exporting Template
type: docs
weight: 10
url: /id/sharepoint/creating-and-exporting-template/
lastmod: "2020-12-16"
description: You can create and export templates to PDF in SharePoint using PDF SharePoint API.
---

{{% alert color="primary" %}}

Artikel ini memperlihatkan cara membuat dan mengekspor templat menggunakan Aspose.PDF untuk SharePoint.

Dari Aspose.PDF untuk SharePoint 1.9.2, dukungan templat PDF juga mencakup subsitus SharePoint.

{{% /alert %}}

## Membuat dan Mengekspor Template

{{% alert color="primary" %}}

To use the Aspose.PDF for SharePoint export feature, first create a list that uses “PDF Templates”.

Membuat daftar yang menggunakan Templat PDF:

![Create PDF Template List](creating-and-exporting-template_1.png)

Two document templates, Task Form Templates and Task List Templates are created:

![Document Templates](creating-and-exporting-template_2.png)

The template form lets you enter the following information:

- **Name**: the template's file name.
- **Title**: the template's title. (By default, the same as the file name.)
- **Deskripsi**: deskripsi template. Deskripsi yang baik membuat template lebih mudah digunakan.
- **Assigned List Types**: comma separated list IDs (related to the template. This field may also contain the value
- **AllListTypes**. This field is only applicable when the **Type** field is set to **List**).
- **Tipe Konten yang Ditugaskan**: ID tipe konten yang dipisahkan koma terkait dengan templat. Bidang ini mungkin berisi yang disetel ke **AllListTypes**. Bidang ini hanya berlaku bila bidang **Jenis** diatur ke **Item**.
- **Jenis**: templat daftar atau templat item.
- **Status**: opsinya aktif, tidak aktif (tidak terlihat oleh semua), dan debugging (hanya terlihat oleh admin).

The Task List Templates form:

![Task List Templates](creating-and-exporting-template_3.png)

The Task Form Templates form:

![Task Form Templates](creating-and-exporting-template_4.png)

When they have been saved, the new templates show up in the template list, ready to be used:

Two task list templates:*

![Task List Templates](creating-and-exporting-template_5.png)

Templat formulir tugas:

![Task Form Templates](creating-and-exporting-template_6.png)

### Developing Templates

A template is an XML file based on Aspose XML PDF. To make a template for a list, place special markers related to the SharePoint target content type field's internal name into the XML PDF file.

### Penanda

- **SPListItemsCount** – replaced by count of list items.
- **SPListTitle** – replaced by list title.
- **SPTableIterator** – placed to first table cell and mark table for full iteration.
- **SProwIterator** – ditempatkan ke sel tabel pertama dan menandai tabel untuk iterasi baris.
- **SPField** – diganti dengan nilai bidang item.

For reference, please download [template XML files](attachments/8421394/8618082.zip).

### Ekspor ke PDF

Ketika templat telah dikonfigurasi sepenuhnya, Anda siap mengekspor daftar atau item ke file PDF.

Exporting a list to PDF using a task list template:

![Export to PDF](creating-and-exporting-template_7.png)

{{% /alert %}}

