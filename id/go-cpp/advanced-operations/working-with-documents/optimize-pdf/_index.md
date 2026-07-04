---
title: Optimalkan PDF menggunakan Aspose.PDF for Go via C++
linktitle: Optimalkan File PDF
type: docs
weight: 10
url: /id/go-cpp/optimize-pdf/
description: Optimalkan dan kompres file PDF menggunakan alat Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimalkan dan kompres file PDF menggunakan Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ menawarkan fitur optimasi yang kuat untuk mengurangi ukuran dan meningkatkan kinerja dokumen PDF. Perpustakaan ini menyediakan berbagai opsi optimasi, termasuk mengompres gambar, menghapus objek yang tidak digunakan, mengurangi ukuran font, dan mengoptimalkan alur konten. Fitur-fitur ini membantu meningkatkan efisiensi penyimpanan dokumen dan memastikan waktu pemrosesan serta pemuatan yang lebih cepat. Dokumentasi menyediakan instruksi langkah demi langkah dan contoh kode untuk membantu pengembang menerapkan optimasi PDF secara efektif dalam aplikasi mereka.
SoftwareApplication: go-cpp
---

## Optimalkan Dokumen PDF

Toolkit dengan Aspose.PDF for Go via C++ memungkinkan Anda mengoptimalkan dokumen PDF.

Cuplikan kode ini berguna untuk aplikasi di mana mengurangi ukuran atau meningkatkan efisiensi file PDF sangat penting, seperti untuk unggahan web, pengarsipan, atau berbagi melalui bandwidth terbatas.

1. The [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) metode memuat file PDF yang ditentukan (sample.pdf) ke dalam memori.
1. The [Metode Optimize](https://reference.aspose.com/pdf/go-cpp/organize/optimize/) mengurangi ukuran file dengan melakukan optimasi seperti menghapus objek yang tidak terpakai, mengompres gambar, meratakan anotasi, melepaskan font yang ter-embed, dan mengaktifkan penggunaan kembali konten. Langkah-langkah ini membantu mengurangi kebutuhan penyimpanan dan meningkatkan kecepatan pemrosesan dokumen PDF.
1. The [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) metode menyimpan PDF yang dioptimalkan ke file baru.

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
      // Optimize() optimizes PDF-document content
      err = pdf.Optimize()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_Optimize.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```