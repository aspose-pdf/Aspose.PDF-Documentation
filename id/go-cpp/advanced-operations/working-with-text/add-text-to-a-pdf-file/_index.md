---
title: Menambahkan Teks ke PDF menggunakan Go
linktitle: Menambahkan Teks ke PDF
type: docs
weight: 10
url: /id/go-cpp/add-text-to-pdf-file/
description: Pelajari cara menambahkan teks ke dokumen PDF dalam Go menggunakan Aspose.PDF untuk peningkatan konten dan pengeditan dokumen.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: Menambahkan Teks ke PDF menggunakan Aspose.PDF for Go
Abstract: Bagian Tambahkan Teks ke File PDF dalam dokumentasi Aspose.PDF untuk C++ dan Go menyediakan petunjuk langkah demi langkah tentang cara menyisipkan teks ke dalam dokumen PDF secara programatis. Bagian ini mencakup berbagai metode untuk menambahkan teks, termasuk penempatan, penyesuaian font, penyesuaian warna, dan opsi perataan teks. Panduan ini menunjukkan cara menambahkan teks ke halaman dan lokasi tertentu dalam PDF, memastikan penempatan konten yang tepat. Dengan contoh kode yang rinci dan penjelasan, pengembang dapat dengan mudah mengintegrasikan fitur penyisipan teks ke dalam aplikasi mereka untuk meningkatkan manajemen dokumen PDF.
SoftwareApplication: go-cpp
---

Untuk menambahkan teks ke file PDF yang ada:

1. Buka file PDF.
1. Tambahkan teks ke dokumen PDF dengan [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/) fungsi.
1. Menyimpan perubahan ke file yang sama.

## Menambahkan Teks

Potongan kode berikut menunjukkan cara menambahkan teks ke dalam file PDF yang sudah ada.

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
        // PageAddText(num int32, addText string) adds text on page
        err = pdf.PageAddText(1, "added text")
        if err != nil {
            log.Fatal(err)
        }
        // Save() saves previously opened PDF-document
        err = pdf.Save()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
