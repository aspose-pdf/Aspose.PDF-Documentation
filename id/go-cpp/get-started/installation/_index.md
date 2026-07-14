---
title: Cara Menginstal Aspose.PDF untuk Go via C++
linktitle: Instalasi
type: docs
weight: 20
url: /id/go-cpp/installation/
description: Bagian ini menampilkan deskripsi produk dan instruksi untuk menginstal Aspose.PDF untuk Go secara mandiri.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Panduan instalasi Aspose.PDF untuk Go
Abstract: Panduan Instalasi Aspose.PDF for Go via C++ menyediakan petunjuk langkah demi langkah untuk menginstal dan mengkonfigurasi perpustakaan untuk digunakan dalam proyek Go dengan integrasi C++. Panduan ini mencakup berbagai metode instalasi, termasuk penyiapan manual dan penggunaan manajer paket seperti NuGet. Panduan juga merinci persyaratan sistem, ketergantungan, dan langkah-langkah konfigurasi yang diperlukan untuk memastikan integrasi yang mulus ke dalam lingkungan pengembangan. Dokumentasi ini membantu pengembang memulai dengan membuat, membaca, dan memanipulasi dokumen PDF dalam Go via C++ secara efektif.
SoftwareApplication: go-cpp
---

## Instalasi

Paket ini mencakup file besar yang disimpan sebagai arsip bzip2.

1. Tambahkan paket asposepdf ke Proyek Anda:

```sh
go get github.com/aspose-pdf/aspose-pdf-go-cpp@latest
```

2. Buat file besar:

- **macOS dan linux**

1. Buka Terminal

2. Daftar folder dari github.com/aspose-pdf dalam cache modul Go:

```sh
ls $(go env GOMODCACHE)/github.com/aspose-pdf/
```

3. Ubah folder saat ini ke folder versi spesifik dari paket yang diperoleh pada langkah sebelumnya:

```sh
cd $(go env GOMODCACHE)/github.com/aspose-pdf/aspose-pdf-go-cpp@vx.x.x
```

Ganti `@vx.x.x` dengan versi paket yang sebenarnya.

4. Jalankan go generate dengan hak istimewa superuser:

```sh
sudo go generate
```

- **Windows**

1. Buka Command Prompt

2. Daftar folder dari github.com/aspose-pdf dalam cache modul Go:

```cmd
for /f "delims=" %G in ('go env GOMODCACHE') do for /d %a in ("%G\github.com\aspose-pdf\*") do echo %~fa
```

3. Ubah folder saat ini ke folder versi spesifik dari paket yang diperoleh pada langkah sebelumnya:

```cmd
cd <specific version folder of the package>
```

4. Jalankan go generate:

```cmd
go generate
```

5. Tambahkan folder versi spesifik dari paket ke variabel lingkungan %PATH%:

```cmd
setx PATH "%PATH%;<specific version folder of the package>\lib\"
```

Ganti `<specific version folder of the package>` dengan jalur aktual yang diperoleh dari langkah 2.

## Pengujian

Pengujian dijalankan dari folder paket root:

```sh
go test -v
```

## Mulai Cepat

Semua potongan kode berada di dalam [cuplikan](https://github.com/aspose-pdf/aspose-pdf-go-cpp).