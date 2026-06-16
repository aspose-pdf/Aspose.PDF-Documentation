---
title: Ekstrak Data Vektor dari file PDF menggunakan Python
linktitle: Ekstrak Data Vektor dari PDF
type: docs
weight: 80
url: /id/python-net/extract-vector-data-from-pdf/
description: Aspose.PDF memudahkan mengekstrak data vektor dari file PDF. Anda dapat memperoleh data vektor (path, polygon, polyline), seperti posisi, warna, lebar garis, dll.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Akses Data Vektor dari Dokumen PDF

Gunakan [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) untuk memeriksa elemen grafik vektor pada sebuah halaman [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Setelah mengunjungi halaman target, iterasi melalui elemen yang diekstrak untuk memeriksa properti seperti batas persegi panjang, posisi, dan operator gambar.

1. Buka PDF sumber sebagai `Document`.
1. Buat sebuah `GraphicsAbsorber` instansi.
1. Panggil `gr_absorber.visit(page)` pada halaman target.
1. Baca item yang diekstrak dari `gr_absorber.elements`.
1. Iterasi melalui elemen dan tuliskan properti mereka ke file output.

```python
import aspose.pdf as ap


def extract_graphics_elements(infile, outfile):
    """
    Extract vector graphic elements from a specified page of a PDF and log basic element properties.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file for logging element info.
    """
    document = ap.Document(infile)
    try:
        gr_absorber = ap.vector.GraphicsAbsorber()
        # Visit page 2 (pages collection is 1-indexed; document.pages[1] is the second page)
        gr_absorber.visit(document.pages[1])

        elements = gr_absorber.elements
        with open(outfile, "w", encoding="utf-8") as f:
            for idx, elem in enumerate(elements, start=1):
                # Basic properties
                rect = elem.rectangle
                pos = elem.position
                ops_count = len(elem.operators)
                f.write(
                    f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n"
                )
    finally:
        document.close()
```

## Simpan Grafik Vektor dari Halaman ke File SVG

Ekspor grafik vektor dari halaman PDF ke SVG untuk mempertahankan jalur dan bentuk yang dapat diskalakan di luar PDF asli. Metode ini berguna untuk menggunakan kembali karya seni vektor dalam alur kerja web, desain, atau penerbitan.

1. Muat dokumen PDF.
1. Akses halaman target.
1. Panggil `page.try_save_vector_graphics()` untuk mengekspor jalur vektor halaman ke SVG.
1. Tutup dokumen.

```python
import aspose.pdf as ap


def save_vector_graphics_to_svg(infile, svg_outfile):
    """
    Save vector graphics from a specified page of a PDF document into an SVG file.
    Args:
        infile (str): Path to input PDF file.
        svg_outfile (str): Path to output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        # Try to save vector graphics into SVG
        page.try_save_vector_graphics(svg_outfile)
    finally:
        document.close()
```

### Ekstrak Setiap Sub-jalur ke SVG Terpisah

Ketika sebuah halaman berisi beberapa jalur vektor independen, gunakan [SvgExtractionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractionoptions/) dengan [SvgExtractor](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) untuk menulis setiap sub-path ke file SVG terpisah.

1. Muat PDF.
1. Buat `SvgExtractionOptions` dan atur `extract_every_subpath_to_svg`.
1. Akses halaman pertama dokumen.
1. Instansiasi `SvgExtractor` dengan opsi-opsi.
1. Panggil `extractor.extract()` menulis file SVG terpisah untuk setiap sub‑jalur vektor.
1. Tutup dokumen.

```python
import aspose.pdf as ap


def extract_subpaths_to_svgs(infile, output_dir):
    """
    Extract each vector sub-path on a PDF page into separate SVG files using extraction options.
    Args:
        infile (str): Input PDF file path.
        output_dir (str): Directory path where SVG files will be saved.
    """
    document = ap.Document(infile)
    try:
        options = ap.vector.SvgExtractionOptions()
        options.extract_every_subpath_to_svg = True

        page = document.pages[1]
        extractor = ap.vector.SvgExtractor(options)
        extractor.extract(page, output_dir)
    finally:
        document.close()
```

### Ekstrak Daftar Elemen menjadi Satu Gambar

Ekstrak beberapa elemen vektor dari halaman PDF dan simpan sebagai satu gambar SVG gabungan. Ini berguna ketika Anda ingin mempertahankan hubungan visual antara bentuk yang dikelompokkan, diagram, atau fragmen gambar.

1. Buka PDF menggunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Pilih sebuah halaman dan siapkan daftar elemen vektor.
1. Gunakan [SvgExtractor](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) untuk menggabungkan elemen-elemen tersebut menjadi satu SVG.
1. Simpan file keluaran.

```python
import aspose.pdf as ap


def extract_list_of_elements_to_single_image(infile, outfile):
    """
    Extracts multiple vector graphic elements from a PDF page and saves them as a single SVG image.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        svg_extractor = ap.vector.SvgExtractor()
        elements = []  # Fill this list with specific graphic elements as needed
        svg_extractor.extract(elements, page, outfile)
    finally:
        document.close()
```

### Ekstrak satu elemen

Ekstrak satu elemen vektor tertentu dari PDF dan simpan sebagai file SVG terpisah. Ini berguna untuk mengisolasi logo, ikon, atau bentuk mandiri dari halaman berbasis vektor yang lebih kompleks.

1. Buat sebuah [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) untuk menangkap data vektor.
1. Kunjungi halaman tertentu untuk mengumpulkan elemen vektornya.
1. Pilih elemen target, seperti sebuah [XFormPlacement](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/xformplacement/).
1. Simpan elemen tunggal itu ke file SVG.

```python
import aspose.pdf as ap


def extract_single_vector_element(infile, outfile):
    """
    Extracts a specific vector graphic element (e.g., an XFormPlacement) from a PDF page and saves it as an SVG file.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        graphics_absorber = ap.vector.GraphicsAbsorber()
        page = document.pages[1]
        graphics_absorber.visit(page)
        xform_placement = graphics_absorber.elements[1]
        if isinstance(xform_placement, ap.vector.XFormPlacement):
            xform_placement.elements[2].save_to_svg(outfile)
    finally:
        document.close()
```
