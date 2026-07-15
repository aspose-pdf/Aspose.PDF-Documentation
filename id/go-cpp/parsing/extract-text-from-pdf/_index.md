---
title: Ekstrak Teks dari PDF menggunakan Go
linktitle: Ekstrak teks dari PDF
type: docs
weight: 30
url: /id/go-cpp/extract-text-from-pdf/
description: Artikel ini menjelaskan berbagai cara untuk mengekstrak teks dari dokumen PDF menggunakan Aspose.PDF for Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ekstrak Teks dengan Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ menyediakan cara yang kuat dan efisien untuk mengekstrak teks dari dokumen PDF. Perpustakaan ini mendukung berbagai teknik ekstraksi, memungkinkan pengguna mengambil teks dari seluruh dokumen, halaman tertentu, atau area yang telah ditentukan dalam PDF.
SoftwareApplication: go-cpp
---

## Ekstrak Teks dari Dokumen PDF

Mengekstrak teks dari dokumen PDF adalah tugas yang sangat umum dan berguna. PDF sering berisi informasi kritis yang perlu diakses, dianalisis, atau diproses untuk berbagai tujuan. Mengekstrak teks memungkinkan penggunaan kembali yang lebih mudah dalam basis data, laporan, atau dokumen lainnya.

Mengekstrak teks membuat konten PDF dapat dicari, memungkinkan pengguna menemukan informasi spesifik dengan cepat tanpa harus meninjau seluruh dokumen secara manual.

Jika Anda ingin mengekstrak teks dari dokumen PDF, Anda dapat menggunakan [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) fungsi.
Silakan periksa cuplikan kode berikut untuk mengekstrak teks dari file PDF menggunakan Go.

1. Buka dokumen PDF dengan nama file yang diberikan.
1. [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) mengekstrak konten teks dari dokumen PDF.
1. Cetak teks yang diekstrak ke konsol.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"
    import "fmt"

    func main() {
        // Open(filename string) opens a PDF-document with filename
        pdf, err := asposepdf.Open("sample.pdf")
        if err != nil {
            log.Fatal(err)

        }
        // ExtractText() returns PDF-document contents as plain text
        txt, err := pdf.ExtractText()
        if err != nil {
            log.Fatal(err)
        }
        // Print
        fmt.Println("Extracted text:\n", txt)
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```