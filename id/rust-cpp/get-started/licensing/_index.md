---
title: Lisensi Aspose PDF
linktitle: Lisensi dan batasan
type: docs
weight: 90
url: /id/rust-cpp/licensing/
description: Aspose. PDF for Rust mengundang pelanggannya untuk mendapatkan Classic License. Selain itu, gunakan lisensi terbatas untuk lebih menjelajahi produk.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lisensi Aspose.PDF for Rust via C++
Abstract: Halaman Lisensi untuk Aspose.PDF for Rust via C++ menjelaskan opsi lisensi yang tersedia untuk produk ini. Pelanggan dapat memilih antara Classic License, Metered License, atau lisensi terbatas untuk tujuan evaluasi. Halaman ini juga menyoroti manfaat memperoleh lisensi yang tepat, seperti membuka semua fungsi dan menghapus batasan evaluasi.
SoftwareApplication: rust-cpp
---

## Lisensi

- Kode sumber **Rust** dilisensikan di bawah Lisensi MIT.
- The **shared library** (AsposePDFforRust_windows_amd64.dll, libAsposePDFforRust_linux_amd64.so, libAsposePDFforRust_darwin_amd64.dylib, libAsposePDFforRust_darwin_arm64.dylib) bersifat proprietary dan memerlukan lisensi komersial. Untuk menggunakan semua fungsionalitas, Anda harus memperoleh lisensi.

## Versi evaluasi

Anda dapat menggunakan **Aspose.PDF for Rust via C++** secara gratis untuk evaluasi. Versi evaluasi menyediakan hampir semua fungsionalitas produk dengan beberapa batasan. Versi evaluasi yang sama menjadi berlisensi ketika Anda membeli lisensi dan menambahkan beberapa baris kode untuk menerapkan lisensi.

- Jika Anda ingin menguji Aspose.PDF for Rust tanpa batasan versi evaluasi, Anda juga dapat meminta Lisensi Sementara selama 30 hari. Silakan merujuk ke [Bagaimana cara mendapatkan Lisensi Sementara?](https://purchase.aspose.com/temporary-license)?

### Batasan versi evaluasi

Kami ingin pelanggan kami menguji komponen kami secara menyeluruh sebelum membeli, sehingga versi evaluasi memungkinkan Anda menggunakannya seperti biasa.

- **Dokumen yang dibuat dengan watermark evaluasi**. Versi evaluasi Aspose.PDF for Rust menyediakan semua fungsi produk, tetapi semua halaman dalam file yang dihasilkan diberi watermark dengan teks "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." di bagian atas.
- **Batasi jumlah halaman yang dapat diproses**. Pada versi evaluasi, Anda hanya dapat memproses empat halaman pertama dari sebuah dokumen.

### Gunakan dalam produksi

Kunci lisensi komersial diperlukan di lingkungan produksi. Silakan hubungi kami untuk membeli lisensi komersial.

### Terapkan lisensi

Menerapkan lisensi untuk mengaktifkan fungsionalitas penuh Aspose.PDF for Rust menggunakan file lisensi (Aspose.PDF.RustViaCPP.lic).

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set license with filename
        pdf.set_license("Aspose.PDF.RustViaCPP.lic")?;

        // Now you can work with the licensed PDF document
        // ...

        Ok(())
    }
```