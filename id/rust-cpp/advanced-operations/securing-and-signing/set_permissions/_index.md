---
title: Atur izin untuk dokumen PDF menggunakan Rust
linktitle: Atur izin
type: docs
weight: 80
url: /id/rust-cpp/set_permissions/
description: Atur izin untuk dokumen PDF dengan Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Atur izin akses untuk dokumen PDF

Sebuah dokumen PDF baru dibuat dan dilindungi dengan kata sandi pengguna dan pemilik, sementara tindakan spesifik—seperti mencetak, memodifikasi konten, dan mengisi formulir—diperbolehkan secara eksplisit. Dokumen kemudian disimpan dengan pembatasan izin yang telah ditentukan diterapkan.

1. Buat dokumen PDF baru.
1. Panggil [set_permissions](https://reference.aspose.com/pdf/rust-cpp/security/set_permissions/) untuk melindungi dokumen.
1. Tentukan kata sandi pengguna untuk membatasi akses.
1. Tentukan kata sandi pemilik untuk mengontrol pengaturan keamanan.
1. Tentukan operasi yang diizinkan menggunakan bitflag izin.
1. Simpan PDF dengan izin yang diterapkan menggunakan [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

```rs

    use asposepdf::{Document, Permissions};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Set permissions for PDF-document.
        pdf.set_permissions(
            "userpass",  // User password
            "ownerpass", // Owner password
            Permissions::PRINT_DOCUMENT | Permissions::MODIFY_CONTENT | Permissions::FILL_FORM, // Permissions bitflag
        )?;

        // Save the PDF-document with the updated permissions
        pdf.save_as("sample_with_permissions.pdf")?;

        Ok(())
    }
```