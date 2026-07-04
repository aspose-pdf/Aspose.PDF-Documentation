---
title: Buka dokumen PDF secara programatik
linktitle: Buka PDF
type: docs
weight: 20
url: /id/go-cpp/open-pdf-document/
description: Pelajari cara membuka file PDF dengan Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buka dokumen PDF dengan Aspose.PDF for Go via C++
Abstract: Aspose.PDF for Go via C++ menyediakan fungsionalitas yang kuat untuk membuka dan memuat dokumen PDF secara programatik, memungkinkan pengembang mengakses dan memanipulasi konten PDF dengan mudah. Perpustakaan ini mendukung pembukaan file PDF dari berbagai sumber, seperti jalur file dan stream memori, sambil memastikan pemrosesan yang efisien dan manajemen sumber daya. Ia menawarkan fitur untuk memeriksa properti dokumen, mengekstrak teks dan gambar, serta melakukan operasi lain pada PDF yang dimuat. Dokumentasi mencakup petunjuk terperinci dan contoh kode untuk membantu pengembang mengintegrasikan kemampuan membuka PDF ke dalam aplikasi mereka secara mulus.
SoftwareApplication: go-cpp
---

## Buka dokumen PDF yang ada

Cuplikan kode menunjukkan operasi penting untuk bekerja dengan PDF menggunakan Aspose.PDF for Go. Ini meliputi membuka file, menyimpan perubahan, dan menutup sumber daya dengan benar. Hal ini menjadikannya contoh dasar bagi pengembang yang menangani dokumen PDF.

Contoh ini sederhana, sehingga mudah dipahami dan dimodifikasi. Ini ideal untuk pemula atau sebagai boilerplate untuk aplikasi yang lebih kompleks.

Kemampuan untuk membuka dan menyimpan dokumen PDF merupakan kebutuhan utama dalam banyak skenario, seperti menghasilkan laporan, memodifikasi dokumen, atau membuat alur kerja otomatis.

Contoh ini menampilkan kemudahan penggunaan API untuk manipulasi PDF sederhana, yang dapat diperluas untuk mencakup fitur lanjutan seperti ekstraksi teks, anotasi, atau pengisian formulir.

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
        // Save() saves previously opened PDF-document
        err = pdf.Save()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
