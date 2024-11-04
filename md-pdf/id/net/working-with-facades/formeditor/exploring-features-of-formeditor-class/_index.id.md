---
title: Menjelajahi fitur kelas FormEditor
type: docs
weight: 10
url: /net/exploring-features-of-formeditor-class/
description: Anda dapat mempelajari detail menjelajahi fitur kelas FormEditor dengan pustaka Aspose. PDF untuk .NET
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Dokumen PDF kadang-kadang berisi formulir interaktif, yang dikenal sebagai AcroForm. Ini seperti formulir yang digunakan di halaman web. Formulir ini berisi berbagai jenis kontrol yaitu Kotak teks, Kotak centang, dan Tombol, dll. Seorang pengembang yang bekerja dengan file PDF kadang-kadang harus mengedit formulir ini. Dalam artikel ini, kita akan melihat secara detail bagaimana [ruang nama Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) memungkinkan kita untuk melakukannya.

{{% /alert %}}

## Detail implementasi

Pengembang dapat menggunakan [ruang nama Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) tidak hanya untuk menambahkan formulir baru dan bidang formulir dalam dokumen PDF, tetapi juga memungkinkan Anda untuk mengedit bidang yang ada. Lingkup artikel ini terbatas pada fitur-fitur [Aspose.PDF for .NET](/pdf/net/) yang berhubungan dengan pengeditan formulir.

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) adalah kelas yang berisi sebagian besar metode dan properti yang memungkinkan pengembang untuk mengedit bidang formulir. Anda tidak hanya dapat menambahkan bidang baru, tetapi juga menghapus bidang yang ada, memindahkan satu bidang ke posisi lain, mengubah nama bidang, atau atribut lainnya. Daftar fitur yang disediakan oleh kelas ini cukup komprehensif, dan sangat mudah untuk bekerja dengan bidang formulir menggunakan kelas ini.

Metode-metode ini dapat dibagi menjadi dua kategori utama, salah satunya digunakan untuk memanipulasi bidang, dan yang lainnya digunakan untuk mengatur atribut baru dari bidang-bidang tersebut. Metode-metode yang dapat kita kelompokkan di bawah kategori pertama meliputi AddField, AddListItem, RemoveListItem, CopyInnerField, CopyOuterField, DelListItem, MoveField, RemoveField, dan RenameField dll. Dalam kategori kedua dari metode SetFieldAlignment, SetFieldAppearance, SetFieldAttribute, SetFieldLimit, SetFieldScript dapat dimasukkan. Cuplikan kode berikut menunjukkan kepada Anda beberapa metode dari kelas FormEditor yang sedang bekerja:

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-FormEditorFeatures-FormEditorFeatures.cs" >}}