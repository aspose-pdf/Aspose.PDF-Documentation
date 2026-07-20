---
title: Dapatkan dan Atur Properti Halaman
linktitle: Dapatkan dan Atur Properti Halaman
type: docs
url: /id/rust-cpp/get-and-set-page-properties/
description: Pelajari cara mendapatkan dan mengatur properti halaman untuk dokumen PDF menggunakan Aspose.PDF for Rust, memungkinkan format dokumen yang disesuaikan.
lastmod: "2026-07-20"
TechArticle: true
AlternativeHeadline: Dapatkan dan Atur Properti Halaman dengan Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ menyediakan fitur komprehensif untuk mendapatkan dan mengatur properti halaman dalam dokumen PDF, memungkinkan pengembang mengakses dan memodifikasi berbagai atribut halaman seperti ukuran, rotasi, margin, dan metadata. Kemampuan ini memungkinkan kontrol yang tepat atas tata letak dan tampilan dokumen untuk memenuhi kebutuhan aplikasi tertentu. Perpustakaan ini memastikan kustomisasi dan optimisasi halaman PDF yang mulus. Dokumentasi menyediakan panduan terperinci dan contoh kode untuk membantu pengembang secara efisien mengambil dan memperbarui properti halaman dalam aplikasi mereka.
SoftwareApplication: rust-cpp
---


Aspose.PDF for Rust memungkinkan Anda membaca dan mengatur properti halaman dalam file PDF. Bagian ini menunjukkan cara mendapatkan jumlah halaman dalam file PDF, mendapatkan informasi tentang properti halaman PDF seperti warna, dan mengatur properti halaman.

## Dapatkan Jumlah Halaman dalam File PDF

Saat bekerja dengan dokumen, Anda sering ingin tahu berapa banyak halaman yang mereka miliki. Dengan Aspose.PDF ini tidak lebih dari dua baris kode.

**Aspose.PDF for Rust via C++** memungkinkan Anda menghitung Halaman dengan [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) fungsi.

Potongan kode berikut dirancang untuk membuka dokumen PDF, mengambil jumlah halamannya, dan kemudian mencetak hasilnya.

The [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) metode dipanggil untuk mendapatkan total jumlah halaman dalam dokumen PDF. Ini berguna untuk tugas yang perlu mengetahui panjang dokumen, seperti saat mengekstrak halaman tertentu atau melakukan operasi pada semua halaman. Metode ini adalah cara sederhana untuk menanyakan struktur dokumen.

Untuk mendapatkan jumlah halaman dalam file PDF:

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Return page count in PDF-document
      let count = pdf.page_count()?;

      // Print the page count
      println!("Count: {}", count);

      Ok(())
  }
```

## Atur Ukuran Halaman

Dalam contoh ini, metode pdf.PageSetSize() mengubah ukuran halaman pertama dari dokumen PDF. Konstanta PageSizeA1 memastikan bahwa halaman pertama diatur ke ukuran kertas A1. Ini berguna saat mengkonversi dokumen ke format standar atau memastikan bahwa konten tertentu cocok dengan benar pada halaman.

1. Membuka Dokumen PDF dengan [buka](https://reference.aspose.com/pdf/rust-cpp/core/open/) metode.
1. Mengatur Ukuran Halaman dengan [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/) fungsi.
1. Menyimpan Document menggunakan [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) metode.

```rs

    use asposepdf::{Document, PageSize};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set the size of a page in the PDF-document
        pdf.page_set_size(1, PageSize::A1)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_page1_set_size_A1.pdf")?;

        Ok(())
    }
```