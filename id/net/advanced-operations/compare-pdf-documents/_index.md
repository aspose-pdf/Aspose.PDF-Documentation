---
title: Membandingkan Dokumen PDF
linktitle: Membandingkan PDF
type: docs
weight: 180
url: /id/net/compare-pdf-documents/
description: Sejak rilis 24.7, sudah memungkinkan untuk membandingkan konten dokumen PDF dengan tanda anotasi dan output berdampingan
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Membandingkan Dokumen PDF dengan Aspose.PDF untuk .NET

Saat bekerja dengan dokumen PDF, ada kalanya Anda perlu membandingkan konten dari dua dokumen untuk mengidentifikasi perbedaan. Pustaka Aspose.PDF untuk .NET menyediakan seperangkat alat yang kuat untuk tujuan ini. Dalam artikel ini, kita akan menjelajahi cara membandingkan dokumen PDF menggunakan beberapa potongan kode sederhana.

Fungsionalitas perbandingan di Aspose.PDF memungkinkan Anda untuk membandingkan dua dokumen PDF halaman demi halaman. Anda dapat memilih untuk membandingkan halaman tertentu atau seluruh dokumen. Dokumen perbandingan yang dihasilkan menyoroti perbedaan, sehingga memudahkan untuk mengidentifikasi perubahan antara kedua file tersebut.

### Membandingkan Halaman Tertentu

Potongan kode pertama menunjukkan cara membandingkan halaman pertama dari dua dokumen PDF.
Langkah-langkah:

1. Inisialisasi Dokumen.
Kode dimulai dengan menginisialisasi dua dokumen PDF menggunakan jalur file masing-masing (documentPath1 dan documentPath2). Jalur tersebut ditentukan sebagai string kosong untuk saat ini, tetapi dalam praktiknya, Anda akan menggantinya dengan jalur file yang sebenarnya.
2. Proses Perbandingan.
- Seleksi Halaman - perbandingan dibatasi pada halaman pertama dari setiap dokumen ('Pages[1]').
- Opsi Perbandingan:

'AdditionalChangeMarks = true' - opsi ini memastikan bahwa penanda perubahan tambahan ditampilkan. Penanda ini menyoroti perbedaan yang mungkin ada di halaman lain, meskipun mereka tidak berada di halaman yang sedang dibandingkan.

'ComparisonMode = ComparisonMode.IgnoreSpaces' - mode ini menginstruksikan pembanding untuk mengabaikan spasi dalam teks, hanya fokus pada perubahan dalam kata.

3.
```cs
    string documentPath1 = "";
    string documentPath2= "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

### Membandingkan Seluruh Dokumen

Snippet kode kedua ini memperluas cakupan untuk membandingkan seluruh konten dari dua dokumen PDF.

Langkah:

1. Inisialisasi Dokumen.
Sama seperti contoh pertama, dua dokumen PDF diinisialisasi dengan jalur file mereka.
2. Proses Perbandingan.
- Perbandingan Dokumen Seluruhnya - tidak seperti snippet pertama, kode ini membandingkan seluruh konten dari kedua dokumen.
- Opsi Perbandingan - opsi-opsinya sama seperti di snippet pertama, memastikan bahwa spasi diabaikan, dan penanda perubahan tambahan ditampilkan.

3.
```cs
    string documentPath1 = "";
    string documentPath2 = "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1, document2, resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

Hasil perbandingan yang dihasilkan oleh potongan kode ini adalah dokumen PDF yang dapat Anda buka dalam penampil seperti Adobe Acrobat. Jika Anda menggunakan tampilan Dua Halaman di Adobe Acrobat, Anda akan melihat perubahan secara berdampingan:

- Penghapusan - ini dicatat di halaman kiri.
- Penyisipan - ini dicatat di halaman kanan.

Dengan mengatur 'AdditionalChangeMarks' menjadi 'true', Anda juga dapat melihat penanda untuk perubahan yang mungkin terjadi di halaman lain, meskipun perubahan tersebut tidak ada di halaman yang sedang dilihat.

**Aspose.PDF for .NET** menyediakan alat yang kuat untuk membandingkan dokumen PDF, apakah Anda perlu membandingkan halaman tertentu atau seluruh dokumen.
**Aspose.PDF untuk .NET** menyediakan alat yang kuat untuk membandingkan dokumen PDF, apakah Anda perlu membandingkan halaman tertentu atau seluruh dokumen.
