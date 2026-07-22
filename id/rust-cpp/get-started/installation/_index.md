---
title: Cara Menginstal Aspose.PDF untuk Rust via C++
linktitle: Instalasi
type: docs
weight: 20
url: /id/rust-cpp/installation/
description: Bagian ini menampilkan deskripsi produk dan petunjuk untuk menginstal Aspose.PDF untuk Rust secara mandiri.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Panduan instalasi Aspose.PDF untuk Rust
Abstract: Panduan Instalasi Aspose.PDF untuk Rust via C++ menyediakan instruksi langkah demi langkah untuk menginstal dan mengonfigurasi perpustakaan agar dapat digunakan dalam proyek Rust dengan integrasi C++. Panduan ini mencakup berbagai metode instalasi, termasuk penyiapan manual dan penggunaan pengelola paket seperti NuGet. Panduan juga menjabarkan persyaratan sistem, dependensi, dan langkah-langkah konfigurasi yang diperlukan untuk memastikan integrasi yang mulus ke dalam lingkungan pengembangan. Dokumentasi ini membantu pengembang memulai dengan membuat, membaca, dan memanipulasi dokumen PDF dalam Rust via C++ secara efektif.
SoftwareApplication: rust-cpp
---

## Instalasi

### Instalasi dari situs web Aspose

Paket ini menyertakan file besar yang disimpan sebagai arsip bzip2.

1. **Download** arsip **Aspose.PDF for Rust via C++** dari situs resmi Aspose.
   Versi terbaru (paling baru) terdaftar di bagian atas dan diunduh secara default ketika Anda mengklik tombol **Download**.
   Disarankan untuk menggunakan versi terbaru ini. Hanya unduh versi sebelumnya jika diperlukan.
   Contoh: `Aspose.PDF-for-Rust-via-CPP-25.6.zip`

   Format nama file arsip adalah: `Aspose.PDF-for-Rust-via-CPP-YY.M.zip`, di mana:
   - `YY` = dua digit terakhir tahun (misalnya, `25` untuk 2025)
   - `M` = nomor bulan dari `1` ke `12`

2. **Ekstrak** arsip ke direktori pilihan Anda `{path}` menggunakan alat yang sesuai:

   - Di Linux/macOS:

     ```bash
     unzip Aspose.PDF-for-Rust-via-CPP-YY.M.zip -d {path}
     ```

   - Di Windows, gunakan ekstraksi bawaan Explorer atau alat unzip apa saja (7-Zip, WinRAR).

3. **Add** perpustakaan sebagai dependensi dalam proyek Rust Anda. Anda dapat melakukan ini dengan dua cara:

   - **Menggunakan baris perintah:**

     ```bash
     cargo add asposepdf --path {path}/asposepdf
     ```

   - **Pengeditan manual** `Cargo.toml`:**
     Buka proyek Anda `Cargo.toml` dan tambahkan yang berikut di bawah `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = { path = "{path}/asposepdf" }
     ```

4. **Bangun proyek Anda** (`cargo build`). Pada build pertama, perpustakaan dinamis yang sesuai untuk platform Anda akan secara otomatis diekstrak dari `.bz2` arsipkan di dalam `lib` folder dan terhubung ke proyek Anda.

**Catatan**

- Skrip build berusaha membuat **tautan simbolik** ke perpustakaan di direktori output Anda (mis., `target/debug/`).
- Untuk **Linux dan macOS**, Anda juga harus mengikuti [Konfigurasi Runtime](#runtime-configuration) bagian di bawah untuk memastikan executable dapat menemukan library saat runtime.
- Semua `.bz2` arsip memiliki korespondensi `.sha256` file checksum. Jika checksum tidak ada atau tidak valid, proses build akan gagal.

### Instalasi dari GitHub

Paket ini mencakup pustaka native yang telah dikompilasi sebelumnya (`.dll`, `.so`, `.dylib`) yang disimpan dalam bentuk terkompresi `.bz2` arsip di dalam repositori GitHub.

1. **Add** perpustakaan sebagai dependensi dalam proyek Rust Anda. Anda dapat melakukan ini dengan dua cara:

   - **Menggunakan baris perintah:**

     ```bash
     cargo add asposepdf --git https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git
     ```

   - **Pengeditan manual** `Cargo.toml`:**

     Buka proyek Anda `Cargo.toml` dan tambahkan yang berikut di bawah `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = { git = "https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git" }
     ```

    > **Catatan:** Untuk menggunakan versi rilis tertentu, Anda dapat menentukan tag:
    >
    > ```toml
    > asposepdf = { git = "https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git", tag = "v1.26.1" }
    > ```

2. **Bangun proyek Anda** (`cargo build`). Pada build pertama, perpustakaan dinamis yang sesuai untuk platform Anda akan secara otomatis diekstrak dari `.bz2` arsipkan di dalam `lib` folder dan terhubung ke proyek Anda.

**Catatan**

- Anda tidak perlu mengunduh atau mengekstrak file secara manual - semuanya sudah termasuk dalam repositori GitHub.
- Skrip build berusaha membuat **tautan simbolik** ke perpustakaan di direktori output Anda (mis., `target/debug/`).
- Untuk **Linux dan macOS**, Anda juga harus mengikuti [Konfigurasi Runtime](#runtime-configuration) bagian di bawah untuk memastikan executable dapat menemukan library saat runtime.
- Semua `.bz2` arsip memiliki kecocokan `.sha256` file checksum. Checksum diverifikasi sebelum ekstraksi.
- Jika verifikasi checksum gagal atau arsip tidak ada, proses build akan gagal dengan kesalahan terperinci.

### Instalasi dari crates.io

Paket ini tersedia di [crates.io](https://crates.io/crates/asposepdf). 
Karena batasan ukuran, crate yang dipublikasikan tidak menyertakan pustaka biner native (`.dll`, `.so`, atau `.dylib`).
Anda dapat memperoleh pustaka native yang diperlukan baik dari arsip distribusi resmi (lihat [Instalasi dari situs web Aspose](#installation-from-aspose-website)) atau dari repositori GitHub (lihat [Instalasi dari GitHub](#installation-from-github)).
Skrip build akan menemukan, memverifikasi, dan mengekstrak pustaka native yang sesuai dari arsip .bz2 yang terkompresi selama proses build.

1. **Add** perpustakaan sebagai dependensi dalam proyek Rust Anda. Anda dapat melakukan ini dengan dua cara:

   - **Menggunakan baris perintah:**

     ```bash
     cargo add asposepdf
     ```

   - **Pengeditan manual** `Cargo.toml`:**

     Buka proyek Anda `Cargo.toml` dan tambahkan yang berikut di bawah `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = "1.26.1"
     ```

2. **Setel jalur** ke direktori yang berisi pustaka asli dan unduh file yang diperlukan:

   - **Setel variabel lingkungan `ASPOSE_PDF_LIB_DIR`** untuk menunjuk ke folder tempat Anda akan menempatkan native `.bz2` arsip, mereka `.sha256` file checksum, dan perpustakaan native yang diekstrak (`.dll`, `.so`, `.dylib`, dan untuk Windows juga `.lib`):

     - Di Linux/macOS:

       ```bash
       export ASPOSE_PDF_LIB_DIR=/path/to/lib
       ```

     - Pada Windows (Command Prompt):

       ```cmd
       set ASPOSE_PDF_LIB_DIR=C:\path\to\lib
       ```

     - Di Windows (PowerShell):
     
       ```powershell
       $env:ASPOSE_PDF_LIB_DIR = "C:\path\to\lib"
       ```

**Catatan tentang ASPOSE_PDF_LIB_DIR**

Itu `ASPOSE_PDF_LIB_DIR` variabel lingkungan mendefinisikan direktori kerja untuk skrip build. Ini digunakan **hanya selama kompilasi** untuk menemukan, memverifikasi, dan mengekstrak arsip pustaka native. Menetapkan variabel ini **tidak** secara otomatis menambahkan direktori ke jalur pencarian pustaka runtime sistem Anda (lihat [Konfigurasi Runtime](#runtime-configuration)).

  - **Unduh yang diperlukan** `.bz2` arsip** dan file checksum dari repositori GitHub [`lib/` folder](https://github.com/aspose-pdf/aspose-pdf-rust-cpp/tree/main/lib) dan **letakkan mereka** ke dalam folder yang ditetapkan di `ASPOSE_PDF_LIB_DIR`:

  - Untuk **Linux x64**, unduh:
    - `libAsposePDFforRust_linux_amd64.so.bz2`
    - `libAsposePDFforRust_linux_amd64.so.bz2.sha256`

  - Untuk **macOS x86_64**, unduh:
    - `libAsposePDFforRust_darwin_amd64.dylib.bz2`
    - `libAsposePDFforRust_darwin_amd64.dylib.bz2.sha256`

  - Untuk **macOS arm64**, unduh:
    - `libAsposePDFforRust_darwin_arm64.dylib.bz2`
    - `libAsposePDFforRust_darwin_arm64.dylib.bz2.sha256`

  - Untuk **Windows x64**, unduh:
    - `AsposePDFforRust_windows_amd64.dll.bz2`
    - `AsposePDFforRust_windows_amd64.dll.bz2.sha256`
    - `AsposePDFforRust_windows_amd64.lib` (pustaka impor asli, tidak terkompresi)

**Catatan:** Anda harus mengunduh file-file ini secara manual dari GitHub dan menaruhnya ke direktori yang ditunjuk oleh `ASPOSE_PDF_LIB_DIR`.  
Skrip build akan secara otomatis mengekstrak perpustakaan native dari `.bz2` arsip pada build pertama.

3. **Bangun** proyek Anda (`cargo build`). Pada build pertama, pustaka native yang cocok dengan platform Anda akan secara otomatis diekstrak dari `.bz2` arsipkan dan ditautkan ke proyek Anda.

**Penting:** Untuk **Linux dan macOS**, Anda juga harus mengikuti [Konfigurasi Runtime](#runtime-configuration) bagian di bawah untuk memastikan executable dapat menemukan library saat runtime.

**Catatan**

- Itu `ASPOSE_PDF_LIB_DIR` variabel digunakan **hanya selama proses build** untuk menemukan dan mengekstrak arsip.
- Skrip build berusaha membuat **tautan simbolik** ke perpustakaan yang diekstrak di direktori output Anda (misalnya, `target/debug/`).
- Anda harus menyediakan folder yang berisi `.bz2` dan `.sha256` file secara terpisah, karena arsip biner ini tidak didistribusikan melalui crates.io.
- Jika arsip yang diperlukan tidak ada atau checksum gagal, build akan gagal dengan kesalahan terperinci.
- Berkas biner yang sama yang digunakan untuk instalasi melalui GitHub atau situs web Aspose dapat digunakan kembali di sini.

## Panduan Cepat

Semua potongan kode berada di dalam [potongan](https://onedrive.live.com/examples).