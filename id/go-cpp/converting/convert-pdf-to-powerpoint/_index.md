---
title: Konversi PDF ke PPTX dengan Go
linktitle: Konversi PDF ke PowerPoint
type: docs
weight: 30
url: /id/go-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-04"
description: Aspose.PDF memungkinkan Anda mengonversi PDF ke format PPTX menggunakan Go.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Alat Golang untuk Mengonversi PDF ke PowerPoint
Abstract: Aspose.PDF for Go via C++ menyediakan solusi andal untuk mengonversi dokumen PDF ke format PowerPoint (PPTX) sambil mempertahankan tata letak, pemformatan, dan struktur konten asli. Fungsionalitas ini memungkinkan pengembang untuk secara mulus mengubah file PDF statis menjadi presentasi dinamis yang dapat diedit. Perpustakaan ini menawarkan opsi kustomisasi untuk mengontrol proses konversi, memastikan output berkualitas tinggi yang cocok untuk penggunaan bisnis dan profesional. Dokumentasi menyediakan panduan langkah demi langkah serta contoh kode untuk membantu pengembang mengintegrasikan konversi PDF-ke-PowerPoint ke dalam aplikasi mereka dengan efisien.
SoftwareApplication: go-cpp
---

## Konversi PDF ke PPTX

Cuplikan kode Go yang diberikan menunjukkan cara mengonversi dokumen PDF menjadi PPTX menggunakan perpustakaan Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi file PDF ke PPTX menggunakan [SavePptx](https://reference.aspose.com/pdf/go-cpp/convert/savepptx/) fungsi.
1. Tutup dokumen PDF dan lepaskan semua sumber daya yang dialokasikan.

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
      // SavePptX(filename string) saves previously opened PDF-document as PptX-document with filename
      err = pdf.SavePptX("sample.pptx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke PowerPoint secara online**

Aspose.PDF for Go mempersembahkan aplikasi gratis online untuk Anda [“PDF ke PPTX”](https://products.aspose.app/pdf/conversion/pdf-to-pptx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke PPTX dengan Aplikasi Gratis](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}