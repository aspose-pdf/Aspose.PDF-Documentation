---
title: Tambahkan watermark ke PDF menggunakan Rust
linktitle: Tambahkan watermark
type: docs
weight: 80
url: /id/rust-cpp/add-watermarks/
description: Contoh ini menunjukkan cara menambahkan watermark teks yang dapat disesuaikan ke dokumen PDF menggunakan Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Watermark Teks
Abstract: Aspose.PDF for Rust via C++ menyediakan cara fleksibel untuk menambahkan watermark teks ke dokumen PDF. Contoh ini menunjukkan cara menyisipkan watermark yang dapat disesuaikan dengan menentukan konten teks, font, ukuran, warna, posisi, sudut rotasi, perilaku lapisan, dan transparansi. Watermark biasanya digunakan untuk branding, label kerahasiaan, tanda draf, atau perlindungan dokumen.
SoftwareApplication: rust-cpp
---

The [add_watermark](https://reference.aspose.com/pdf/rust-cpp/organize/add_watermark/) metode memungkinkan pengembang untuk secara programatis menerapkan watermark teks ke dokumen PDF yang ada. Watermark dapat sepenuhnya disesuaikan, termasuk:

- Teks watermark
- Keluarga Font
- Ukuran Font
- Warna teks (format HEX)
- Koordinat posisi X dan Y
- Sudut rotasi
- Penempatan latar depan atau latar belakang
- Opasitas (tingkat transparansi)

Dalam contoh ini, aplikasi membuka file PDF yang ada, menerapkan watermark berputar semi-transparan, dan menyimpan dokumen yang telah dimodifikasi dengan nama file baru.

Fungsionalitas ini sangat berguna untuk menandai dokumen sebagai Draft, Confidential, Sample, atau untuk menambahkan elemen merek sebelum distribusi.

1. Buka dokumen PDF yang ada.
1. Panggil metode add_watermark dan konfigurasikan properti watermark.
1. Simpan dokumen yang telah diperbarui.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add watermark to PDF-document
        pdf.add_watermark(
            "WATERMARK",
            "Arial",
            16.0,
            "#010101",
            100,
            100,
            45,
            true,
            0.5,
        )?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_watermark.pdf")?;

        Ok(())
    }
```