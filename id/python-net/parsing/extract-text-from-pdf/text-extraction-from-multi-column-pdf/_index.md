---
title: Meningkatkan Ekstraksi Teks dari PDF Multi‑Kolom
linktitle: Ekstraksi Teks dari PDF Multi‑Kolom
type: docs
weight: 30
url: /id/python-net/text-extraction-from-multi-column-pdf/
description: Pelajari teknik untuk meningkatkan ekstraksi teks dari tata letak PDF multi‑kolom dengan Aspose.PDF for Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Kurangi ukuran font secara manual lalu ekstrak

Pada beberapa tata letak multi‑kolom, mengurangi ukuran font fragmen teks sebelum ekstraksi dapat meningkatkan urutan bacaan dan mengurangi masalah tumpang tindih. Teknik ini dapat membantu dokumen yang diformat rapat seperti majalah, makalah penelitian, brosur, atau laporan dengan kolom teks yang padat.

1. Muat PDF.
1. Gunakan [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) untuk mengumpulkan fragmen teks.
1. Kurangi ukuran font setiap fragmen, lalu simpan dan buka kembali dokumen.
1. Gunakan [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) untuk mengekstrak teks.
1. Tuliskan teks yang diekstrak ke file output.

```python
import io
import aspose.pdf as ap


def extract_text_reduce_font(infile, outfile, reduce_ratio=0.7):
    """
    Extract text from a multi-column PDF by first reducing font size of all text fragments.
    Args:
        infile (str): Path to input PDF.
        outfile (str): Output text file.
        reduce_ratio (float): Ratio to reduce font size (e.g., 0.7 = 70%).
    """
    doc = ap.Document(infile)

    frag_absorber = ap.text.TextFragmentAbsorber()
    doc.pages.accept(frag_absorber)
    for frag in frag_absorber.text_fragments:
        frag.text_state.font_size = frag.text_state.font_size * reduce_ratio
    # Save to memory stream and reopen (to apply changes)
    ms = io.BytesIO()
    doc.save(ms)
    ms.seek(0)
    doc2 = ap.Document(ms)
    text_absorber = ap.text.TextAbsorber()
    doc2.pages.accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```

## Ekstrak teks dengan faktor skala

Opsi lain untuk ekstraksi multi-kolom adalah mengonfigurasi [TextExtractionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textextractionoptions/) dengan faktor skala. Menyesuaikan faktor skala dapat meningkatkan interpretasi fragmen yang sangat rapat dan membantu menjaga urutan baca yang lebih akurat dalam tata letak padat, tabel, atau dokumen berbasis kolom.

1. Muat PDF.
1. Buat sebuah [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/).
1. Konfigurasikan `TextExtractionOptions.scale_factor`.
1. Tetapkan opsi ekstraksi ke absorber.
1. Ekstrak teks halaman dan tulis hasilnya ke file output.

```python
import aspose.pdf as ap


def extract_text_scale_factor(infile, outfile, scale_factor=0.5):
    """
    Extract text from a PDF with multi-column layout using scale factor.
    Args:
        infile (str): Input PDF path.
        outfile (str): Output text file path.
        scale_factor (float): Scale factor between 0.1 and 1.0 or 0 for auto-scaling.
    """
    doc = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    ext_opts = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    ext_opts.scale_factor = scale_factor
    text_absorber.extraction_options = ext_opts
    doc.pages.accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```
