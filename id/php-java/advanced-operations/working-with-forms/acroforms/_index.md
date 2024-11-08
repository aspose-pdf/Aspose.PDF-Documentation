---
title: Bekerja dengan AcroForms dalam PDF 
linktitle: AcroForms
type: docs
weight: 10
url: /id/php-java/acroforms/
description: Dengan Aspose.PDF untuk PHP melalui Java, Anda dapat membuat formulir dari awal, mengisi bidang formulir dalam dokumen PDF, mengekstrak data dari formulir, menambah atau menghapus bidang dalam formulir yang ada.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Dasar-dasar AcroForms

**AcroForms** adalah teknologi formulir PDF asli. AcroForms adalah formulir berorientasi halaman. Mereka pertama kali diperkenalkan pada tahun 1998. Mereka menerima input dalam Format Data Formulir atau FDF dan Format Data Formulir XML atau xFDF. Vendor pihak ketiga mendukung AcroForms. Ketika Adobe memperkenalkan AcroForms, mereka merujuknya sebagai "formulir PDF yang dibuat dengan Adobe Acrobat Pro/Standard dan bukan jenis khusus formulir XFA statis atau dinamis. Acroforms dapat dibawa dan bekerja di semua platform.

Anda dapat menggunakan AcroForms untuk menambahkan halaman tambahan ke dokumen formulir PDF.
 Berkat konsep Template, Anda dapat menggunakan AcroForms untuk mendukung pengisian formulir dengan beberapa catatan database.

PDF 1.7 mendukung dua metode berbeda untuk mengintegrasikan data dan formulir PDF.

*AcroForms (juga dikenal sebagai formulir Acrobat)*, diperkenalkan dan disertakan dalam spesifikasi format PDF 1.2.

*Formulir Arsitektur Adobe XML (XFA)*, diperkenalkan dalam spesifikasi format PDF 1.5 sebagai fitur opsional. Spesifikasi XFA tidak disertakan dalam spesifikasi PDF, hanya dirujuk.

Untuk memahami **Acroforms** vs **XFA** forms, kita perlu memahami dasar-dasarnya terlebih dahulu. Sebagai permulaan, keduanya adalah formulir PDF yang dapat Anda gunakan. Acroforms adalah yang lebih tua, dibuat pada tahun 1998, dan masih disebut sebagai formulir PDF klasik. Formulir XFA adalah halaman web yang dapat Anda simpan sebagai PDF, dan muncul pada tahun 2003. Butuh beberapa waktu sebelum PDF mulai menerima formulir XFA.

AcroForms memiliki kemampuan yang tidak ditemukan di XFA dan sebaliknya XFA memiliki beberapa kemampuan yang tidak ditemukan di AcroForms. Misalnya:

- AcroForms mendukung konsep "Template", memungkinkan halaman tambahan untuk ditambahkan ke dokumen formulir PDF guna mendukung pengisian formulir dengan beberapa catatan database.- XFA mendukung konsep aliran ulang dokumen yang memungkinkan sebuah bidang untuk mengubah ukuran jika diperlukan untuk menampung data.

Jadi, PDF adalah format file terbaik untuk formulir karena dapat didistribusikan secara elektronik dan memiliki informasi yang diisi dalam dokumen serta dikirim kembali ke pengirim tanpa perlu mencetak atau mengirim melalui pos tradisional.

Untuk studi lebih mendalam tentang kemungkinan bekerja dengan formulir, pelajari artikel berikut di bagian ini:

-[Buat AcroForm](/pdf/id/php-java/create-form/) - buat formulir dari awal, tambahkan RadioButtonField, TextBoxField, Caption Field menggunakan PHP.

-[Isi AcroForm](/pdf/id/php-java/fill-form/) - untuk mengisi bidang formulir, dapatkan bidang dari koleksi Form objek Dokumen.

-[Ekstrak Data AcroForm](/pdf/id/php-java/extract-form/) - dapatkan nilai dari semua dan setiap bidang, dll.

-[Modifikasi AcroForm](/pdf/id/php-java/modifing-form/) - dapatkan/atur FieldLimit, hapus bidang dalam formulir yang ada, atur font bidang formulir selain dari 14 Font Inti PDF dengan PHP.