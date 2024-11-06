---
title: Menggunakan Generator Dokumen PDF OneClick
type: docs
weight: 10
url: id/net/using-oneclick-pdf-document-generator/
description: Pelajari cara menggunakan Generator Dokumen PDF OneClick Aspose.PDF di Microsoft Dynamics
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Membuat Template dan Menambahkannya dalam CRM

- Buka word dan buat sebuah template.
- Masukkan field MailMerge untuk data yang berasal dari CRM.

![Masukkan field MailMerge](using-oneclick-pdf-document-generator_1.png)

- Pastikan bahwa nama Field sesuai persis dengan field CRM.
- Template spesifik digunakan untuk entitas individu.

![Demo Template](using-oneclick-pdf-document-generator_2.png)

- Setelah Template dibuat, buka entitas Konfigurasi PDF OneClick di CRM dan Buat sebuah Rekaman Baru.
- Berikan nama template, pilih entitas yang didefinisikan untuk template dan lampirkan dokumen yang telah dibuat di lampiran.

![Pilih Template](using-oneclick-pdf-document-generator_3.png)

## Menghasilkan Dokumen dari Tombol Ribbon

- Buka Rekaman di mana Anda ingin menghasilkan dokumen.
- Buka Rekaman di mana Anda ingin menghasilkan dokumen.
- Klik tombol OneClick PDF dari pita.

![Klik OneClick PDF](using-oneclick-pdf-document-generator_4.png)

- Dari Popup: Pilih template, Nama File dan Aksi lalu Klik Hasilkan.
- Periksa file yang telah diunduh atau Catatan, berdasarkan pilihan.

## Konfigurasi Tombol OneClick dan gunakannya

- Untuk menggunakan Tombol OneClick langsung dari Formulir, Buka Kustomisasi Formulir.
- Masukkan WebResource di mana Anda ingin menambahkan Tombol OneClick.
- Pilih OpenButtonPage di Webresource dan beri nama.
- Konfigurasikan Tombol di kolom Data dengan contoh berikut.

![Properti WebResource](using-oneclick-pdf-document-generator_5.png)

- Gunakan baris terpisah untuk setiap tombol dan gunakan sintaks berikut:
  - Sintaks: Nama Template |<Aksi: Unduh/Catatan>|Nama File Keluaran
  - Contoh: Demo|Unduh|File Saya yang Diunduh
- Simpan dan publikasikan kustomisasi.
- Tombol tersedia di formulir.

![Tombol tersedia di formulir](using-oneclick-pdf-document-generator_6.png)
![Tombol tersedia pada formulir](using-oneclick-pdf-document-generator_6.png)
