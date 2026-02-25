---
title: Hapus Gambar dari File PDF menggunakan Python
linktitle: Hapus Gambar
type: docs
weight: 20
url: /id/python-net/delete-images-from-pdf-file/
description: Bagian ini menjelaskan cara menghapus Gambar dari File PDF menggunakan Aspose.PDF untuk Python via .NET.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Cara menghapus gambar dari PDF menggunakan Python
Abstract: Artikel ini membahas berbagai alasan untuk menghapus gambar dari file PDF, seperti melindungi privasi, mencegah akses tidak sah ke informasi sensitif, mengurangi ukuran file agar lebih mudah dibagikan dan disimpan, serta menyiapkan dokumen untuk kompresi atau ekstraksi teks. Artikel ini memperkenalkan **Aspose.PDF untuk Python via .NET** sebagai alat untuk menyelesaikan tugas ini. Artikel ini memberikan petunjuk langkah demi langkah dan cuplikan kode untuk menghapus gambar tertentu atau semua gambar dari file PDF menggunakan Aspose.PDF. Prosesnya meliputi membuka dokumen PDF yang ada, menghapus gambar secara individual atau massal, dan menyimpan file yang diperbarui. Kode Python yang disediakan menunjukkan cara menghapus gambar dengan mengakses sumber daya dokumen dan memodifikasi halaman yang diinginkan.
---

Ada banyak alasan untuk menghapus semua atau gambar tertentu dari PDF.
Kadang-kadang file PDF dapat berisi gambar penting yang perlu dihapus untuk melindungi privasi atau mencegah akses tidak sah ke informasi tertentu.

Menghapus gambar yang tidak diinginkan atau berlebih dapat membantu mengurangi ukuran file, sehingga lebih mudah untuk berbagi atau menyimpan PDF.
Jika diperlukan, Anda dapat mengurangi jumlah halaman dengan menghapus semua gambar dari dokumen.
Selain itu, menghapus gambar dari dokumen akan membantu menyiapkan PDF untuk kompresi atau ekstraksi informasi teks.

**Aspose.PDF untuk Python via .NET** akan membantu Anda dengan tugas ini.

## Hapus Gambar dari File PDF

Untuk menghapus sebuah gambar dari file PDF:

1. Buka Dokumen PDF yang ada.
1. Hapus gambar tertentu.
1. Simpan file PDF yang telah diperbarui.

Cuplikan kode berikut menunjukkan cara menghapus sebuah gambar dari file PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    document.pages[1].resources.images.delete(1)
    document.save(path_outfile)
```
