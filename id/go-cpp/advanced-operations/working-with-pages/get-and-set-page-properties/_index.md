---
title: Dapatkan dan Atur Properti Halaman
linktitle: Dapatkan dan Atur Properti Halaman
type: docs
url: /id/go-cpp/get-and-set-page-properties/
description: Pelajari cara mendapatkan dan mengatur properti halaman untuk dokumen PDF menggunakan Aspose.PDF for Go, memungkinkan pemformatan dokumen yang disesuaikan.
lastmod: "2026-07-04"
TechArticle: true
AlternativeHeadline: Dapatkan dan Atur Properti Halaman dengan Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ menyediakan fitur lengkap untuk mendapatkan dan mengatur properti halaman dalam dokumen PDF, memungkinkan pengembang mengakses dan memodifikasi berbagai atribut halaman seperti ukuran, rotasi, margin, dan metadata. Kemampuan ini memungkinkan kontrol yang tepat atas tata letak dan tampilan dokumen untuk memenuhi kebutuhan aplikasi tertentu. Perpustakaan ini memastikan kustomisasi dan optimalisasi halaman PDF yang mulus. Dokumentasi menawarkan panduan terperinci dan contoh kode untuk membantu pengembang secara efisien mengambil dan memperbarui properti halaman dalam aplikasi mereka.
SoftwareApplication: go-cpp
---


Aspose.PDF for Go memungkinkan Anda membaca dan mengatur properti halaman dalam file PDF. Bagian ini menunjukkan cara mendapatkan jumlah halaman dalam file PDF, mendapatkan informasi tentang properti halaman PDF seperti warna, dan mengatur properti halaman.

## Dapatkan Jumlah Halaman dalam File PDF

Saat bekerja dengan dokumen, Anda sering ingin mengetahui berapa banyak halaman yang mereka miliki. Dengan Aspose.PDF ini tidak memerlukan lebih dari dua baris kode.

**Aspose.PDF for Go via C++** memungkinkan Anda menghitung Halaman dengan [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) fungsi.

Potongan kode berikut dirancang untuk membuka dokumen PDF, mengambil jumlah halamannya, dan kemudian mencetak hasilnya.

The [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) metode dipanggil untuk mendapatkan total jumlah halaman dalam dokumen PDF. Ini berguna untuk tugas yang perlu mengetahui panjang dokumen, seperti saat mengekstrak halaman tertentu atau melakukan operasi pada semua halaman. Metode ini adalah cara langsung untuk menanyakan struktur dokumen.

Untuk mendapatkan jumlah halaman dalam file PDF:

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"
    import "fmt"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)

      }
      // PageCount() returns page count in PDF-document
      count, err := pdf.PageCount()
      if err != nil {
        log.Fatal(err)
      }
      // Print
      fmt.Println("Count:", count)
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## Atur Ukuran Halaman

Dalam contoh ini, metode pdf.PageSetSize() mengubah ukuran halaman pertama dari dokumen PDF. Konstanta PageSizeA1 memastikan bahwa halaman pertama diatur ke ukuran kertas A1. Ini berguna saat mengonversi dokumen ke format standar atau memastikan bahwa konten tertentu cocok dengan benar pada halaman.

1. Membuka Dokumen PDF dengan [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) metode.
1. Mengatur Ukuran Halaman dengan [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/) fungsi.
1. Menyimpan Dokumen menggunakan [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) metode.

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
        // PageSetSize(num int32, pageSize int32) sets size of page
        err = pdf.PageSetSize(1, asposepdf.PageSizeA1)
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_page1_SetSize_A1.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```