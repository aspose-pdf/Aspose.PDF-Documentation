---
title: Ekstrak Data dari AcroForm menggunakan Rust
linktitle: Ekstrak Data dari AcroForm
type: docs
weight: 50
url: /id/rust-cpp/extract-data-from-acroform/
description: Aspose.PDF memudahkan mengekstrak data bidang formulir dari file PDF. Pelajari cara mengekstrak data dari AcroForm dan menyimpannya dalam format XML, FDF, atau XFDF.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mengekstrak Data dari AcroForm via Rust
Abstract: Artikel ini menjelaskan cara mengekstrak data AcroForm dari file PDF menggunakan Aspose.PDF untuk Rust via C++ dan mengekspornya ke format pertukaran data yang banyak digunakan - XML, FDF, dan XFDF. Artikel ini menunjukkan cara membuka dokumen PDF yang berisi bidang formulir interaktif dan secara programatik mengekspor nama bidang formulir serta nilai-nilainya untuk digunakan kembali di luar PDF asli. Dengan menyediakan contoh Rust yang praktis untuk setiap format ekspor, artikel ini menyoroti alur kerja umum, termasuk pemrosesan data, pengiriman formulir, integrasi sistem, dan penyimpanan data jangka panjang, membantu pengembang mengelola dan menggunakan kembali data formulir PDF secara efisien dalam aplikasi mereka.
---

## Ekspor Data ke XML dari File PDF

Cuplikan kode ini menunjukkan cara mengekspor data AcroForm dari dokumen PDF ke file XML menggunakan Aspose.PDF untuk Rust.
Proses ini melibatkan membuka file PDF yang sudah ada dengan bidang formulir, kemudian mengekspor bidang-bidang tersebut beserta nilai-nilainya ke dokumen XML untuk pemrosesan lebih lanjut, penyimpanan, atau pertukaran data.

1. Buka dokumen PDF.
1. Panggil metode 'export_xml' untuk mengekstrak data bidang formulir dan menyimpannya sebagai file XML.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XML-document
        pdf.export_xml("sample.xml")?;

        Ok(())
    }
```

## Ekspor Data ke FDF dari File PDF

Aspose.PDF for Rust via C++ memungkinkan Anda mengekspor data AcroForm dari dokumen PDF ke file FDF. Format Data Formulir (FDF) menyimpan nama dan nilai bidang formulir secara terpisah dari PDF, sehingga berguna untuk pertukaran data, alur kerja pengiriman formulir, dan mengarsipkan data formulir tanpa menyematkannya dalam dokumen asli.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to FDF-document
        pdf.export_fdf("sample.fdf")?;

        Ok(())
    }
```

## Ekspor Data ke XFDF dari File PDF

XFDF (XML Forms Data Format) adalah format berbasis XML yang merepresentasikan data bidang formulir secara terpisah dari file PDF, menjadikannya ideal untuk pertukaran data, pengiriman formulir, dan integrasi dengan alur kerja berbasis web.
Aspose.PDF for Rust via C++ membantu mengekspor data AcroForm dari dokumen PDF ke file XFDF.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XFDF-document
        pdf.export_xfdf("sample.xfdf")?;

        Ok(())
    }
```
