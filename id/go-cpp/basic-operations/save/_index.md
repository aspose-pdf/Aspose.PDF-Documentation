---
title: Simpan dokumen PDF secara programatik
linktitle: Simpan PDF
type: docs
weight: 30
url: /id/go-cpp/save-pdf-document/
description: Pelajari cara menyimpan file PDF dengan Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Simpan dokumen PDF dengan Aspose.PDF for Go via C++
Abstract: Aspose.PDF for Go via C++ menawarkan fungsionalitas komprehensif untuk menyimpan dokumen PDF dalam berbagai format dan lokasi dengan efisiensi dan fleksibilitas tinggi. Perpustakaan ini memungkinkan pengembang menyimpan PDF ke sistem file, dan stream memori, atau mengeluarkannya dalam format alternatif seperti DOCX, XLSX, dan gambar. Ia menyediakan opsi untuk menyesuaikan parameter penyimpanan, mengoptimalkan ukuran file, dan memastikan integritas data. Dokumentasi mencakup instruksi terperinci serta contoh kode untuk membantu pengembang secara efisien mengimplementasikan kemampuan penyimpanan PDF dalam aplikasi mereka.
SoftwareApplication: go-cpp
---

## Simpan dokumen PDF ke sistem file

Contoh tersebut memperlihatkan [Baru](https://reference.aspose.com/pdf/go-cpp/core/new/) metode untuk membuat dokumen PDF baru, yang merupakan fitur dasar untuk menghasilkan dokumen secara dinamis, seperti laporan atau faktur.

Kode ini sederhana dan dapat berfungsi sebagai templat untuk fitur yang lebih canggih seperti menambahkan teks, gambar, atau anotasi ke PDF.

Contoh ini memperlihatkan penggunaan langsung dari pustaka Aspose.PDF Go, menampilkan potensinya untuk membuat, memodifikasi, dan menyimpan dokumen.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // New creates a new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_New_SaveAs.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
