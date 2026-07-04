---
title: Atur warna latar belakang untuk PDF dengan Go
linktitle: Atur warna latar belakang
type: docs
weight: 80
url: /id/go-cpp/set-background-color/
description: Atur warna latar belakang untuk file PDF Anda dengan Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atur warna latar belakang untuk PDF dengan Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ menawarkan fungsionalitas untuk mengatur warna latar belakang halaman PDF, memungkinkan pengembang menyesuaikan tampilan dokumen. Fitur ini memungkinkan penerapan warna solid ke seluruh latar belakang halaman, meningkatkan presentasi visual dokumen. Pengembang dapat dengan mudah menentukan nilai warna menggunakan model warna standar seperti RGB atau CMYK. Dokumentasi menyediakan instruksi detail dan contoh kode untuk membantu pengembang mengimplementasikan kustomisasi warna latar belakang secara efektif dalam aplikasi C++ mereka.
SoftwareApplication: go-cpp
---

1. Potongan kode yang disediakan menampilkan cara mengatur warna latar belakang untuk file PDF menggunakan perpustakaan Aspose.PDF dalam Go.
1. The [Buka](https://reference.aspose.com/pdf/go-cpp/core/open/) method memuat file PDF yang ditentukan ke memori, memungkinkan manipulasi lebih lanjut, seperti memodifikasi tampilan atau kontennya.
1. The [SetBackground](https://reference.aspose.com/pdf/go-cpp/organize/setbackground/) method menerapkan warna latar belakang baru ke dokumen PDF. Nilai RGB memungkinkan pengguna menyesuaikan gaya visual dokumen.
1. The [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) metode menyimpan PDF yang diperbarui dengan nama baru.

Kode ini ideal untuk aplikasi yang perlu mengotomatisasi kustomisasi PDF, seperti membuat laporan bermerk, menambahkan watermark, atau meningkatkan konsistensi visual di antara banyak dokumen.

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
      // SetBackground(r, g, b int32) sets PDF-document background color
      err = pdf.SetBackground(200, 100, 101)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_SetBackground.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```