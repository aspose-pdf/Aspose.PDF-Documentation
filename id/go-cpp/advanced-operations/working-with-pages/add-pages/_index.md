---
title: Tambahkan Halaman ke Dokumen PDF
linktitle: Tambahkan Halaman
type: docs
weight: 10
url: /id/go-cpp/add-pages/
description: Jelajahi cara menambahkan halaman ke PDF yang sudah ada di Go dengan Aspose.PDF untuk meningkatkan dan memperluas dokumen Anda.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Halaman PDF dengan Aspose.PDF untuk Go
Abstract: Aspose.PDF untuk Go via C++ menyediakan fungsionalitas kuat untuk menambahkan halaman ke dokumen PDF, memungkinkan pengembang membuat halaman baru secara dinamis dan menyesuaikannya sesuai kebutuhan spesifik. Perpustakaan ini mendukung penyisipan halaman kosong atau penyalinan halaman dari dokumen yang ada sambil menawarkan opsi untuk menentukan ukuran halaman, orientasi, dan konten. Kemampuan ini memungkinkan ekspansi dan penyesuaian dokumen secara mulus. Dokumentasi mencakup petunjuk terperinci dan contoh kode untuk membantu pengembang mengimplementasikan fitur penambahan halaman secara efisien dalam aplikasi mereka.
SoftwareApplication: go-cpp
---

## Tambahkan Halaman dalam File PDF

Potongan kode Go yang disediakan menunjukkan cara melakukan operasi Add Page di akhir PDF menggunakan pustaka Aspose.PDF. 

1. The [Buka](https://reference.aspose.com/pdf/go-cpp/core/open/) fungsi memungkinkan program memuat file PDF yang ada (sample.pdf) untuk manipulasi. Ini penting untuk segala operasi terkait PDF, seperti mengedit, menambahkan konten, atau membaca data.
1. The [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) metode digunakan untuk menyisipkan halaman kosong baru ke dalam dokumen PDF yang ada. Ini berguna untuk memperluas dokumen atau menyiapkannya untuk konten tambahan.
1. The [Simpan](https://reference.aspose.com/pdf/go-cpp/core/save/) metode memastikan bahwa modifikasi pada PDF ditulis kembali ke file. Langkah ini penting untuk mempertahankan perubahan, seperti penambahan halaman baru.
1. The [Tutup](https://reference.aspose.com/pdf/go-cpp/core/close/) metode dipanggil menggunakan defer untuk melepaskan sumber daya apa pun yang dialokasikan selama operasi PDF. Hal ini penting untuk mencegah kebocoran memori dan memastikan penggunaan sumber daya yang efisien.

Potongan kode ini adalah contoh yang singkat dan efisien tentang cara menggunakan pustaka Aspose.PDF Go untuk tugas manipulasi PDF dasar.

Aspose.PDF for Go memungkinkan Anda menyisipkan halaman ke dokumen PDF di lokasi mana pun dalam file serta menambahkan halaman ke akhir file PDF.

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
        // PageAdd() adds new page in PDF-document
        err = pdf.PageAdd()
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

## Sisipkan Halaman dalam File PDF

The [PageInsert](https://reference.aspose.com/pdf/go-cpp/core/pageinsert/) Metode menyisipkan halaman baru pada posisi yang ditentukan. Fitur ini berguna ketika Anda perlu menyisipkan halaman tambahan ke dalam dokumen yang ada, misalnya, menambahkan bagian baru atau konten ke laporan atau presentasi.

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
        // PageInsert(num int32) inserts new page at the specified position in PDF-document
        err = pdf.PageInsert(1)
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