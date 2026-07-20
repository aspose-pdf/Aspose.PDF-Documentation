---
title: Konfigurasi Runtime Aspose.PDF untuk Rust via C++
linktitle: Konfigurasi Runtime
type: docs
weight: 100
url: /id/rust-cpp/runtime-configuration/
description: Aplikasi Rust yang bergantung pada pustaka dinamis native—seperti Aspose.PDF—memerlukan konfigurasi jalur runtime yang benar agar berfungsi dengan baik pada sistem Linux dan macOS.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mengonfigurasi RPATH untuk Aspose.PDF Native untuk Rust
Abstract: Ketika bekerja dengan pustaka dinamis native di Rust, penautan runtime yang tepat sangat penting untuk memastikan aplikasi Anda dapat menemukan dependensi yang diperlukan. Pada Linux dan macOS, pemuat dinamis sistem tidak secara otomatis mencari direktori eksekutabel kecuali RPATH dikonfigurasi secara eksplisit. Artikel ini menjelaskan cara mengonfigurasi RPATH sehingga aplikasi Rust Anda dapat menemukan pustaka native Aspose.PDF dengan benar pada saat runtime. Ini mencakup konfigurasi tingkat proyek menggunakan Cargo, konfigurasi berbasis lingkungan dengan RUSTFLAGS, dan opsi instalasi seluruh sistem, beserta catatan tentang perilaku di Windows.
SoftwareApplication: rust-cpp
---

> Ini adalah persyaratan standar saat menggunakan pustaka dinamis native di Rust.

Di Linux dan macOS, pemuat dinamis sistem tidak secara otomatis mencari direktori executable kecuali RPATH dikonfigurasi. Untuk memastikan aplikasi Anda dapat menemukan pustaka native Aspose.PDF saat runtime, Anda perlu mengonfigurasi **RPATH** (Run-time Search Path).

Script build kami mengekstrak perpustakaan dan berusaha membuat tautan simbolik ke dalamnya di direktori output Anda (misalnya, `target/debug/`). Untuk memungkinkan executable menemukan itu, pilih salah satu opsi berikut:

## Opsi 1: Konfigurasi Tingkat Proyek (Disarankan)

Buat folder bernama `.cargo` di direktori root proyek Anda (jika belum ada) dan buat file bernama `config.toml` di dalamnya:

```toml
[target.'cfg(target_os = "linux")']
rustflags = ["-C", "link-arg=-Wl,-rpath,$ORIGIN"]

[target.'cfg(target_os = "macos")']
rustflags = ["-C", "link-arg=-Wl,-rpath,@loader_path"]
```

## Opsi 2: Variabel Lingkungan RUSTFLAGS

Bangun proyek Anda dengan flag berikut:

```bash
# Linux
RUSTFLAGS="-C link-arg=-Wl,-rpath,\$ORIGIN" cargo build

# macOS
RUSTFLAGS="-C link-arg=-Wl,-rpath,@loader_path" cargo build
```

## Opsi 3: Instalasi Seluruh Sistem (Tidak direkomendasikan untuk pengembangan)

Jika Anda lebih suka menginstal perpustakaan secara global:

* **Linux:** Salin `.so` file ke `/usr/local/lib` dan jalankan `sudo ldconfig`.
* **macOS:** Salin `.dylib` file ke `/usr/local/lib`.

> **Windows**
> Tidak ada tindakan yang biasanya diperlukan karena perpustakaan berada di folder yang sama dengan `.exe`. Alternatifnya, Anda dapat menambahkan direktori yang berisi `.dll` ke sistem Anda `PATH` variabel lingkungan.