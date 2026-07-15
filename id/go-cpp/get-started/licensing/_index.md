---
title: Lisensi Aspose PDF
linktitle: Lisensi dan batasan
type: docs
weight: 90
url: /id/go-cpp/licensing/
description: Aspose. PDF for Go mengundang pelanggannya untuk memperoleh Lisensi Klasik. Selain itu, dapat menggunakan lisensi terbatas untuk lebih mengeksplorasi produk.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lisensi Aspose.PDF untuk Go via C++
Abstract: Halaman Lisensi untuk Aspose.PDF untuk Go via C++ menjelaskan opsi lisensi yang tersedia untuk produk ini. Pelanggan dapat memilih antara Classic License, Metered License, atau lisensi terbatas untuk tujuan evaluasi. Halaman tersebut juga menyoroti manfaat memperoleh lisensi yang tepat, seperti membuka semua fungsi penuh dan menghilangkan batasan evaluasi.
SoftwareApplication: go-cpp
---


## Batasan versi evaluasi

Kami ingin pelanggan kami menguji komponen kami secara menyeluruh sebelum membeli sehingga versi evaluasi memungkinkan Anda menggunakannya seperti biasanya.

- **Dokumen dibuat dengan watermark evaluasi.** Versi evaluasi Aspose.PDF for Go menyediakan fungsionalitas produk lengkap, tetapi semua halaman dalam file yang dihasilkan memiliki watermark dengan teks "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." di bagian atas.

- **Batasi jumlah halaman yang dapat diproses.**
Dalam versi evaluasi, Anda hanya dapat memproses empat halaman pertama dari sebuah dokumen.

>Jika Anda ingin menguji Aspose.PDF for Go tanpa batasan versi evaluasi, Anda juga dapat meminta Lisensi Sementara selama 30 hari. Silakan merujuk ke [Bagaimana cara mendapatkan Lisensi Sementara?](https://purchase.aspose.com/temporary-license)

## Lisensi klasik

Menerapkan lisensi untuk mengaktifkan fungsi penuh dari pustaka Aspose.PDF menggunakan file lisensi (Aspose.PDF.GoViaCPP.lic).

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // Open(filename string) opens a PDF-document with filename
        pdf, err := asposepdf.Open("sample.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // SetLicense(filename string) licenses with filename
        err = pdf.SetLicense("Aspose.PDF.GoViaCPP.lic")
        if err != nil {
            log.Fatal(err)
        }
        // Working with PDF-document
        // ...
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
