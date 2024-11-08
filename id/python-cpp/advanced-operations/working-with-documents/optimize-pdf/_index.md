---
title: Optimalkan, Kompres, atau Kurangi Ukuran PDF di Python
linktitle: Optimalkan PDF
type: docs
weight: 30
url: /id/python-cpp/optimize-pdf/
keywords: "optimalkan pdf Python"
description: Optimalkan file PDF, perkecil semua gambar, kurangi ukuran PDF, Lepaskan font, Hapus objek yang tidak digunakan dengan Python.
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Sebuah dokumen PDF kadang-kadang dapat berisi data tambahan. Mengurangi ukuran file PDF akan membantu Anda mengoptimalkan transfer jaringan dan penyimpanan. Ini sangat berguna untuk publikasi di halaman web, berbagi di jejaring sosial, mengirim melalui e-mail, atau mengarsipkan di penyimpanan. Kita dapat menggunakan beberapa teknik untuk mengoptimalkan PDF:

- Optimalkan konten halaman untuk penelusuran online
- Perkecil atau kompres semua gambar
- Aktifkan penggunaan ulang konten halaman
- Gabungkan aliran duplikat
- Lepaskan font yang terpasang
- Hapus objek yang tidak digunakan
- Hapus bidang formulir yang diratakan
- Hapus atau ratakan anotasi

{{% alert color="primary" %}}

Penjelasan terperinci tentang metode optimasi dapat ditemukan di halaman Ikhtisar Metode Optimasi.

{{% /alert %}}

## Optimalkan Dokumen PDF untuk Web

Optimasi, atau linearisasi untuk Web, mengacu pada proses membuat file PDF cocok untuk penjelajahan online menggunakan peramban web. Untuk mengoptimalkan file untuk tampilan web:

Cuplikan kode berikut menunjukkan cara mengoptimalkan dokumen PDF untuk web.

```python

    import AsposePDFPythonWrappers as ap

    # Jalur ke direktori dokumen.
    dataDir = "..."

    # Buka dokumen
    document = ap.Document(dataDir + "OptimizeDocument.pdf")

    # Optimalkan untuk web
    document.optimize()

    dataDir = dataDir + "OptimizeDocument_out.pdf"

    # Simpan dokumen keluaran
    document.Save(dataDir)
```