---
title: Ganti Gambar dalam File PDF yang Ada menggunakan Python
linktitle: Ganti Gambar
type: docs
weight: 70
url: /id/python-net/replace-image-in-existing-pdf-file/
description: Bagian ini menjelaskan tentang mengganti gambar dalam file PDF yang ada menggunakan perpustakaan Python.
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: Ganti Gambar dalam PDF
Abstract: Dokumentasi Aspose.PDF untuk Python via .NET menyediakan panduan komprehensif tentang cara mengganti gambar di dalam file PDF yang ada. Fungsionalitas ini penting untuk tugas seperti memperbarui logo, grafik, atau elemen visual lainnya dalam dokumen PDF tanpa mengubah konten teksnya.
---

## Ganti Gambar dalam PDF

Bagaimana cara mengganti gambar yang ada pada halaman PDF dengan gambar baru? Terapkan ini menggunakan Aspose.PDF untuk Python via .NET.

1. Impor modul yang diperlukan (aspose.pdf, os.path, FileIO).
1. Tentukan jalur untuk:
- PDF Input (infile)
- File gambar baru (image_file)
- PDF Output (outfile)
1. Muat dokumen PDF menggunakan 'apdf.Document(path_infile)'.
1. Buka file gambar baru dalam mode baca biner.
1. Ganti gambar pertama pada halaman pertama:
- 'document.pages[1].resources.images.replace(1, image_stream)'
1. Simpan PDF yang diperbarui ke 'path_outfile'.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    with FileIO(path_image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(path_outfile)
```

## Ganti Gambar Tertentu

Contoh ini menunjukkan cara mengganti gambar tertentu pada halaman PDF dengan menemukannya melalui deteksi penempatan gambar.

1. Muat PDF menggunakan 'apdf.Document()'.
1. Buat 'ImagePlacementAbsorber' untuk mengumpulkan semua penempatan gambar pada halaman.
1. Terima absorber pada halaman pertama ('document.pages[1].accept(absorber)').
1. Periksa apakah ada penempatan gambar pada halaman.
1. Pilih penempatan gambar pertama (absorber.image_placements[1]) dan ganti.
1. Simpan PDF yang telah diubah ke 'path_outfile'.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    # Create ImagePlacementAbsorber to find image placements
    absorber = apdf.ImagePlacementAbsorber()

    # Accept the absorber for the first page
    document.pages[1].accept(absorber)

    # Replace the first image placement found
    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(path_image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(path_outfile)
```
