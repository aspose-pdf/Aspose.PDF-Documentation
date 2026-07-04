---
title: Optimalkan Sumber Daya PDF menggunakan Go
linktitle: Optimalkan Sumber Daya PDF
type: docs
weight: 15
url: /id/go-cpp/optimize-pdf-resources/
description: Optimalkan Sumber Daya file PDF menggunakan alat Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimalkan Sumber Daya PDF menggunakan Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ menyediakan kemampuan lanjutan untuk mengoptimalkan sumber daya PDF, meningkatkan efisiensi dokumen dan mengurangi ukuran file. Perpustakaan ini memungkinkan pengembang mengoptimalkan Font, gambar, dan metadata dengan menghapus data berlebih serta mengompresi sumber daya tanpa mengorbankan kualitas dokumen. Teknik optimasi ini meningkatkan kinerja dokumen, menjadikan PDF lebih cocok untuk dibagikan dan disimpan. Dokumentasi menyediakan panduan detail dan contoh kode untuk membantu pengembang secara efektif menerapkan optimasi sumber daya dalam aplikasi mereka.
SoftwareApplication: go-cpp
---

## Optimalkan Sumber Daya PDF

Optimalkan sumber daya dalam dokumen:

  1. Sumber daya yang tidak digunakan pada halaman dokumen dihapus.
  1. Sumber daya yang sama digabungkan menjadi satu objek.
  1. Objek yang tidak digunakan dihapus.

Optimisasi dapat mencakup kompresi gambar, menghapus objek yang tidak digunakan, dan mengoptimalkan font untuk mengurangi ukuran file serta meningkatkan kinerja. Setiap kesalahan selama operasi ini dicatat dan menghentikan program.  
 
1. The [Buka](https://reference.aspose.com/pdf/go-cpp/core/open/) metode memuat file PDF yang ditentukan (sample.pdf) ke memori.
1. Mengoptimalkan sumber daya dalam PDF untuk efisiensi menggunakan [OptimizeResource](https://reference.aspose.com/pdf/go-cpp/organize/optimizeresource/) metode.
1. The [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) metode menyimpan PDF yang dioptimalkan ke file baru.

Potongan kode berikut menunjukkan cara mengoptimalkan dokumen PDF.

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
      // OptimizeResource() optimizes resources of PDF-document
      err = pdf.OptimizeResource()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_OptimizeResource.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```