---
title: Periksa Batas Bentuk dalam Grafik PDF dengan Python
linktitle: Periksa Batas Bentuk
type: docs
weight: 70
url: /id/python-net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: Pelajari cara memvalidasi batas bentuk dalam kumpulan grafik PDF menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validasi batas bentuk grafik dalam file PDF menggunakan Python
Abstract: Artikel ini menunjukkan cara memvalidasi batas bentuk dalam kumpulan Graph dengan Aspose.PDF for Python via .NET. Artikel ini mencakup konfigurasi BoundsCheckMode, mendeteksi bentuk di luar jangkauan, dan menangani pengecualian batas dengan aman.
---

## Periksa batas bentuk dalam Graph

Saat Anda menambahkan bentuk ke sebuah [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/), Anda dapat mengaktifkan validasi batas untuk memastikan setiap bentuk cocok dalam area grafik.

Gunakan [BoundsCheckMode](https://reference.aspose.com/pdf/python-net/aspose.pdf/boundscheckmode/) untuk mendefinisikan perilaku ketika sebuah bentuk berada di luar jangkauan. Dalam contoh ini, `THROW_EXCEPTION_IF_DOES_NOT_FIT` digunakan untuk menimbulkan sebuah pengecualian.

Ikuti langkah-langkah di bawah ini:

1. Buat PDF baru [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Tambahkan sebuah [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Buat sebuah [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) dan tambahkan ke halaman.
1. Buat sebuah [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/rectangle/) yang melampaui batas grafik.
1. Atur mode pemeriksaan batas ke `THROW_EXCEPTION_IF_DOES_NOT_FIT`.
1. Tambahkan persegi panjang dan tangani eksepsi.
1. Simpan dokumen.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing


def check_shape_bounds(outfile: str):
    document = ap.Document()
    page = document.pages.add()

    graph = drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato

    try:
        graph.shapes.update_bounds_check_mode(
            ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT
        )
        graph.shapes.add(rect)
    except Exception as e:
        print(e)

    document.save(outfile)
```

## Catatan

- Gunakan `THROW_EXCEPTION_IF_DOES_NOT_FIT` ketika validasi tata letak yang ketat diperlukan.
- Untuk perilaku permisif, pilih yang lain `BoundsCheckMode` opsi berdasarkan kebutuhan tata letak Anda.

## Topik Grafik Terkait

- [Bekerja dengan grafik PDF di Python](/pdf/id/python-net/working-with-graphs/)
- [Tambahkan bentuk persegi panjang ke PDF di Python](/pdf/id/python-net/add-rectangle/)
- [Tambahkan bentuk garis ke PDF di Python](/pdf/id/python-net/add-line/)
- [Tambahkan bentuk elips ke PDF di Python](/pdf/id/python-net/add-ellipse/)
