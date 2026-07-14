---
title: Hapus Halaman PDF dengan Go
linktitle: Hapus Halaman PDF
type: docs
weight: 30
url: /id/go-cpp/delete-pages/
description: Anda dapat menghapus halaman dari file PDF Anda menggunakan Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Halaman PDF dengan Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ menawarkan fungsionalitas yang efisien untuk menghapus halaman dari dokumen PDF, memungkinkan pengembang menghapus halaman yang tidak diinginkan atau tidak diperlukan dengan mudah. Perpustakaan ini memungkinkan penghapusan satu atau beberapa halaman dengan menentukan nomor halaman atau rentang, memastikan modifikasi dokumen yang tepat. Fitur ini membantu menyederhanakan file PDF dengan menghilangkan konten berlebih dan mengoptimalkan struktur dokumen. Dokumentasi menyediakan instruksi langkah demi langkah dan contoh kode untuk membantu pengembang mengimplementasikan fungsionalitas penghapusan halaman secara efektif dalam aplikasi mereka.
SoftwareApplication: go-cpp
---

Anda dapat menghapus halaman dari file PDF menggunakan **Aspose.PDF for Go via C++**. Potongan kode berikut menunjukkan cara memanipulasi dokumen PDF dengan menghapus halaman tertentu. Metode ini efisien untuk tugas manipulasi dokumen PDF, khususnya untuk menghapus halaman, menyimpan dokumen yang dimodifikasi, dan memastikan manajemen sumber daya yang tepat.

1. Membuka File PDF.
1. Menghapus Halaman Tertentu dengan [PageDelete](https://reference.aspose.com/pdf/go-cpp/core/pagedelete/) fungsi.
1. Menyimpan Dokumen menggunakan [Save](https://reference.aspose.com/pdf/go-cpp/core/save/) metode.

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
      // PageDelete(num int32) deletes specified page in PDF-document
      err = pdf.PageDelete(1)
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
