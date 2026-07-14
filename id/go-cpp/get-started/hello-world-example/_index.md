---
title: Contoh Hello World menggunakan bahasa Go
linktitle: Contoh Hello World
type: docs
weight: 40
url: /id/go-cpp/hello-world-example/
description: Contoh ini menunjukkan cara membuat dokumen PDF sederhana dengan teks Hello World menggunakan Aspose.PDF for Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hello World melalui Aspose.PDF for Go
Abstract: Panduan Memulai untuk Aspose.PDF for Go via C++ menyediakan pengantar untuk bekerja dengan pustaka ini, mencakup langkah-langkah dasar untuk membuat dan memanipulasi dokumen PDF. Panduan ini menyertakan contoh 'Hello World' yang menunjukkan cara menghasilkan file PDF sederhana dengan konten teks, membantu pengembang dengan cepat memahami fungsionalitas inti API.
SoftwareApplication: go-cpp
---

Contoh \"Hello World\" secara tradisional digunakan untuk memperkenalkan fitur-fitur bahasa pemrograman atau perangkat lunak dengan kasus penggunaan yang sederhana.

**Aspose.PDF for Go** adalah API PDF yang kaya fitur yang memungkinkan pengembang menyematkan pembuatan dokumen PDF, manipulasi, dan kemampuan konversi dengan Go. Ini mendukung banyak format file populer, termasuk PDF, TXT, XPS, EPUB, TEX, DOC, DOCX, PPTX, format gambar, dll. Dalam artikel ini, kami membuat dokumen PDF yang berisi teks "Hello World!" Setelah menginstal Aspose.PDF for Go di lingkungan Anda, Anda dapat menjalankan contoh kode untuk melihat cara kerja API Aspose.PDF.
Potongan kode di bawah ini mengikuti langkah-langkah berikut:

1. Buat instance dokumen PDF baru.
1. Tambahkan halaman baru ke dokumen PDF menggunakan [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) fungsi.
1. Atur ukuran halaman menggunakan [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/).
1. Tambahkan teks "Hello World!" ke halaman pertama menggunakan [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/).
1. Simpan dokumen PDF yang diperbaiki menggunakan [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) metode.
1. Tutup dokumen PDF dan lepaskan sumber daya yang telah dialokasikan.

Potongan kode berikut adalah program Hello World untuk menunjukkan cara kerja Aspose.PDF for Go API.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // Create new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
                log.Fatal(err)
        }
        // Add new page
        err = pdf.PageAdd()
        if err != nil {
                log.Fatal(err)
        }
        // Set page size A4
        err = pdf.PageSetSize(1, asposepdf.PageSizeA4)
        if err != nil {
                log.Fatal(err)
        }
        // Add text on first page
        err = pdf.PageAddText(1, "Hello World!")
        if err != nil {
                log.Fatal(err)
        }
        // Save PDF-document with "hello.pdf" name
        err = pdf.SaveAs("hello.pdf")
        if err != nil {
                log.Fatal(err)
        }
        // Release allocated resources
        defer pdf.Close()
    }
```
