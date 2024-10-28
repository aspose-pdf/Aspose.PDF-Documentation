---
title: Bekerja dengan Formulir XFA dalam PDF 
linktitle: Formulir XFA
type: docs
weight: 20
url: /java/xfa-forms/
description: Dengan Aspose.PDF untuk Java Anda dapat membuat formulir dari awal, mengisi bidang formulir dalam dokumen PDF, mengekstrak data dari formulir, menambah atau menghapus bidang dalam formulir yang ada.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XFA adalah singkatan dari XML Forms Architecture. Ini adalah serangkaian spesifikasi XML kepemilikan yang awalnya dibangun untuk digunakan dengan formulir web pada tahun 1999, dan sejak itu menjadi tersedia untuk PDF.

## Mengonversi Formulir XFA Dinamis ke AcroForm Standar

Formulir dinamis didasarkan pada spesifikasi XML yang dikenal sebagai XFA, “XML Forms Architecture”. Ini juga dapat mengonversi formulir XFA dinamis ke Acroform standar. Informasi tentang formulir (sejauh menyangkut PDF) sangat samar – ini menentukan bahwa bidang ada, dengan properti, dan acara JavaScript, tetapi tidak menentukan rendering apa pun. Objek dari formulir XFA digambar saat memuat dokumen.

Saat ini PDF mendukung dua metode berbeda untuk mengintegrasikan data dan formulir PDF:

- AcroForms (juga dikenal sebagai formulir Acrobat), diperkenalkan dan disertakan dalam spesifikasi format PDF 1.2.

- Adobe XML Forms Architecture (XFA) forms, diperkenalkan dalam spesifikasi format PDF 1.5 sebagai fitur opsional. (Spesifikasi XFA tidak termasuk dalam spesifikasi PDF, hanya dirujuk.)

Tidak mungkin untuk mengekstrak atau memanipulasi halaman Formulir XFA, karena konten formulir dihasilkan saat runtime (selama penayangan formulir XFA) dalam aplikasi yang mencoba menampilkan atau merender formulir XFA. Aspose.PDF memiliki fitur yang memungkinkan pengembang untuk mengkonversi formulir XFA ke AcroForms standar.

```java
// Muat formulir XFA dinamis
Document document = new Document("XFAform.pdf");
// Atur jenis bidang formulir sebagai AcroForm standar
document.getForm().setType(FormType.Standard);
// Simpan PDF hasil
document.save("Standard_AcroForm.pdf");
```