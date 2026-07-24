---
title: Dekripsi PDF menggunakan Rust
linktitle: Dekripsi File PDF
type: docs
weight: 40
url: /id/rust-cpp/decrypt-pdf/
description: Dekripsi File PDF dengan Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Dekripsi File PDF menggunakan Kata Sandi Pemilik

Anda dapat membuka, mendekripsi, dan menyimpan dokumen PDF yang dilindungi kata sandi menggunakan Aspose.PDF for Rust via C++.
PDF dibuka dengan kata sandi pemilik, didekripsi untuk menghapus semua pembatasan keamanan, dan kemudian disimpan sebagai PDF baru yang tidak dilindungi.

1. Gunakan [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) untuk memuat PDF yang dilindungi kata sandi dengan menyediakan jalur file dan kata sandi pemilik.
1. Panggil [decrypt](https://reference.aspose.com/pdf/rust-cpp/security/decrypt/) metode untuk menghapus perlindungan kata sandi dan semua pembatasan keamanan terkait dari dokumen.
1. Simpan PDF yang telah didekripsi menggunakan [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a password-protected PDF-document
      let pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

      // Decrypt PDF-document
      pdf.decrypt()?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_decrypt.pdf")?;

      Ok(())
  }
```