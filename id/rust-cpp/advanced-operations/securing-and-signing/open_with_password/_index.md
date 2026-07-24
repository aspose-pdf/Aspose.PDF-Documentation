---
title: Buka PDF yang dilindungi kata sandi menggunakan Rust
linktitle: Buka PDF yang dilindungi kata sandi
type: docs
weight: 70
url: /id/rust-cpp/open-password-protected-pdf/
description: Buka File PDF yang dilindungi kata sandi dengan Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Buka dokumen PDF yang dilindungi kata sandi

Buka dokumen PDF yang dilindungi kata sandi dengan Aspose.PDF for Rust via C++. Dokumen dibuka dengan kata sandi pemilik, yang memberikan akses penuh dan memungkinkan operasi lebih lanjut seperti membaca metadata, memodifikasi konten, mengubah izin, atau menghapus enkripsi.

1. Buka dokumen PDF yang dilindungi dengan [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) dan berikan jalur file bersama dengan kata sandi pemilik untuk membuka kunci dokumen.
1. Bekerja dengan dokumen yang dibuka.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a password-protected PDF-document
        let _pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

        // working...

        Ok(())
    }
```