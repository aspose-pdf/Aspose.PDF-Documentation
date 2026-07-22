---
title: Dapatkan Izin menggunakan Rust
linktitle: Dapatkan Izin
type: docs
weight: 60
url: /id/rust-cpp/get-permissions/
description: Baca dan tampilkan izin akses dari dokumen PDF yang diproteksi kata sandi dengan Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Dapatkan izin dari dokumen PDF yang diproteksi kata sandi

Bagian ini menjelaskan cara membaca dan menampilkan izin akses dari dokumen PDF yang diproteksi kata sandi dalam Rust.
PDF dibuka dengan kata sandi pemilik, yang memberikan akses penuh ke pengaturan keamanan dokumen. Izin yang saat ini diberikan kemudian diambil dan dicetak ke konsol.

1. Buka dokumen PDF yang dilindungi.
1. Panggil [get_permissions](https://reference.aspose.com/pdf/rust-cpp/security/get_permissions/) untuk mendapatkan flag izin yang menentukan operasi mana yang diizinkan.
1. Cetak izin yang diambil ke konsol.

```rs

    use asposepdf::{Document, Permissions};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a password-protected PDF-document
        let pdf = Document::open_with_password("sample_with_permissions.pdf", "ownerpass")?;

        // Get current permissions of PDF-document
        let permissions: Permissions = pdf.get_permissions()?;

        // Print permissions
        println!("Permissions: {}", permissions);

        Ok(())
    }
```