---
title: Putar Halaman PDF dengan Go
linktitle: Putar Halaman PDF
type: docs
weight: 50
url: /id/go-cpp/rotate-pages/
description: Topik ini menjelaskan cara memutar orientasi halaman dalam file PDF yang ada secara programatis dengan Go melalui C++
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Putar Halaman PDF dengan Aspose.PDF untuk Go
Abstract: Aspose.PDF untuk Go melalui C++ menyediakan fungsionalitas yang kuat untuk memutar halaman dalam dokumen PDF, memungkinkan pengembang mengubah orientasi halaman sesuai kebutuhan. Perpustakaan ini mendukung pemutaran halaman sebesar 90, 180, atau 270 derajat, memungkinkan penyesuaian cepat dan efisien pada tata letak dokumen. Fitur ini berguna untuk memperbaiki halaman yang salah orientasi atau mengubah presentasi dokumen. Dokumentasi mencakup petunjuk langkah demi langkah dan contoh kode untuk membantu pengembang mengintegrasikan kemampuan pemutaran halaman dengan mulus ke dalam aplikasi mereka.
SoftwareApplication: go-cpp
---

Bagian ini menjelaskan cara mengubah orientasi halaman dari lanskap ke potret dan sebaliknya dalam file PDF yang ada menggunakan Go.

Memutar halaman memastikan penyelarasan yang tepat untuk pencetakan atau penampilan PDF dalam lingkungan profesional

1. Buka Dokumen PDF.
1. Putar Halaman PDF. The [PageRotate](https://reference.aspose.com/pdf/go-cpp/organize/rotate/) fungsi menerapkan rotasi khusus (dalam hal ini, 180 derajat) ke halaman tertentu.
1. Simpan Perubahan ke File Baru. The [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) Fungsi membuat file PDF baru untuk mempertahankan yang asli sambil menyimpan versi yang diperbarui.

Dalam contoh ini, Anda memutar halaman tertentu dalam dokumen PDF:

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
    // PageRotate(num int32, rotation int32) rotates page
    err = pdf.PageRotate(1, asposepdf.RotationOn180)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_page1_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```

Anda juga memiliki opsi untuk memutar semua halaman PDF dalam dokumen Anda:

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
    // Rotate(rotation int32) rotates PDF-document
    err = pdf.Rotate(asposepdf.RotationOn270)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```