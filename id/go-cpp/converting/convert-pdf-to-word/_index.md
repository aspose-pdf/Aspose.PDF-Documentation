---
title: Konversi PDF ke dokumen Word dalam Go
linktitle: Konversi PDF ke Word
type: docs
weight: 10
url: /id/go-cpp/convert-pdf-to-doc/
lastmod: "2026-07-04"
description: Pelajari cara menulis kode Go untuk konversi PDF ke DOC (DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Alat untuk Mengonversi PDF ke Word dengan Aspose.PDF untuk Go
Abstract: Aspose.PDF untuk Go via C++ memungkinkan konversi mulus dokumen PDF ke format DOC sambil mempertahankan teks asli, gambar, tabel, dan struktur dokumen secara keseluruhan. Fitur ini memungkinkan pengembang mengubah PDF statis menjadi file Word yang dapat diedit untuk modifikasi dan pemrosesan lebih lanjut. Pustaka menyediakan berbagai opsi penyesuaian untuk mengontrol output konversi, memastikan kesetiaan dan akurasi tinggi. Dokumentasi mencakup petunjuk terperinci dan contoh kode untuk membantu pengembang secara efisien mengimplementasikan konversi PDF-ke-DOC dalam aplikasi mereka.
SoftwareApplication: go-cpp
---

Untuk mengedit konten file PDF di Microsoft Word atau pengolah kata lain yang mendukung format DOC dan DOCX. File PDF dapat diedit, tetapi file DOC dan DOCX lebih fleksibel dan dapat disesuaikan.

## Konversi PDF ke DOC

Potongan kode Go yang disediakan menunjukkan cara mengonversi dokumen PDF menjadi DOC menggunakan perpustakaan Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi file PDF ke DOC menggunakan [SaveDoc](https://reference.aspose.com/pdf/go-cpp/convert/savedoc/) fungsi.
1. Tutup dokumen PDF dan bebaskan sumber daya yang dialokasikan.

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
      // SaveDoc(filename string) saves previously opened PDF-document as Doc-document with filename
      err = pdf.SaveDoc("sample.doc")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke DOC secara daring**

Aspose.PDF for Go mempersembahkan Anda aplikasi gratis daring [“PDF ke DOC”](https://products.aspose.app/pdf/conversion/pdf-to-doc), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi PDF ke DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) 
{{% /alert %}}

## Konversi PDF ke DOCX

Aspose.PDF for Go API memungkinkan Anda membaca dan mengonversi dokumen PDF ke DOCX. DOCX adalah format yang dikenal luas untuk dokumen Microsoft Word yang strukturnya diubah dari biner sederhana menjadi kombinasi file XML dan biner. File Docx dapat dibuka dengan Word 2007 dan versi‑versi selanjutnya, tetapi tidak dengan versi‑versi lama MS Word yang mendukung ekstensi file DOC.

Potongan kode Go yang disediakan menunjukkan cara mengonversi dokumen PDF menjadi DOCX menggunakan pustaka Aspose.PDF:

1. Buka dokumen PDF.
1. Konversi file PDF ke DOCX menggunakan [SaveDocX](https://reference.aspose.com/pdf/go-cpp/convert/savedocx/) fungsi.
1. Tutup dokumen PDF dan bebaskan sumber daya yang dialokasikan.

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
      // SaveDocX(filename string) saves previously opened PDF-document as DocX-document with filename
      err = pdf.SaveDocX("sample.docx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke DOCX secara online**

Aspose.PDF for Go mempersembahkan Anda aplikasi gratis daring [“PDF ke Word”](https://products.aspose.app/pdf/conversion/pdf-to-docx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke Word Gratis](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}