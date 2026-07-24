---
title:  Enkripsi PDF menggunakan Rust
linktitle: Enkripsi File PDF
type: docs
weight: 10
url: /id/rust-cpp/encrypt-pdf/
description: Enkripsi File PDF dengan Aspose.PDF untuk Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Enkripsi File PDF menggunakan Password Pengguna atau Pemilik

Untuk dengan mudah dan aman mengenkripsi dokumen, Anda dapat menggunakan Aspose.PDF untuk Rust via C++.

- The **user_password**, jika disetel, adalah apa yang harus Anda berikan untuk membuka PDF. Acrobat/Reader akan meminta pengguna memasukkan password pengguna. Jika tidak benar, dokumen tidak akan terbuka.
- Password **owner_password**, jika diatur, mengontrol izin, seperti mencetak, mengedit, mengekstrak, memberi komentar, dll. Acrobat/Reader akan melarang hal‑hal ini berdasarkan pengaturan izin. Acrobat akan meminta password ini jika Anda ingin mengatur/mengubah izin.

PDF dilindungi dengan kata sandi pengguna dan pemilik, izin akses khusus, serta enkripsi AES‑128 yang sesuai dengan standar PDF 2.0. Setelah dienkripsi, dokumen disimpan ke disk, memastikan akses terkendali dan penanganan aman file PDF.

1. Buat dokumen PDF baru.
1. Enkripsi dokumen PDF dengan [enkripsi](https://reference.aspose.com/pdf/rust-cpp/security/encrypt/) metode.
1. Tentukan kata sandi pengguna untuk membatasi pembukaan dokumen.
1. Tentukan kata sandi pemilik untuk mengontrol izin.
1. Tentukan tindakan yang diizinkan menggunakan bitflag izin.
1. Pilih AES-128 sebagai algoritma enkripsi.
1. Aktifkan enkripsi PDF 2.0 untuk kepatuhan keamanan modern.
1. Simpan PDF yang dienkripsi menggunakan [simpan_sebagai](https://reference.aspose.com/pdf/rust-cpp/core/save_as/). 

```rs

  use asposepdf::{CryptoAlgorithm, Document, Permissions};

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Create a new PDF-document
      let pdf = Document::new()?;

      // Encrypt PDF-document
      pdf.encrypt(
          "userpass",  // User password
          "ownerpass", // Owner password
          Permissions::PRINT_DOCUMENT | Permissions::MODIFY_CONTENT | Permissions::FILL_FORM, // Permissions bitflag
          CryptoAlgorithm::AESx128, // Encryption algorithm
          true,                     // Use PDF 2.0 encryption
      )?;

      // Save the encrypted PDF-document
      pdf.save_as("sample_with_password.pdf")?;

      Ok(())
  }
```