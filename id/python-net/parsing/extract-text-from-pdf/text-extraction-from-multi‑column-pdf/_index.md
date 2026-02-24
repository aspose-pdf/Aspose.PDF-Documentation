---
title: Meningkatkan Ekstraksi Teks dari PDF Multi‑Kolom
linktitle: Ekstraksi Teks dari PDF Multi‑Kolom
type: docs
weight: 30
url: /id/python-net/text-extraction-from-multi‑column-pdf/
description: Bagian ini berisi artikel tentang pemformatan teks dan penskalaan menggunakan Aspose.PDF di Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

## Kurangi ukuran font secara manual dan kemudian ekstrak

Akurasi ekstraksi pada PDF multi-kolom dicapai dengan terlebih dahulu mengurangi ukuran font semua fragmen teks sebelum ekstraksi. Proses ini membantu mencegah masalah teks yang tumpang tindih yang dapat terjadi pada tata letak yang rapat atau multi-kolom.
Ini membantu dalam mengekstrak teks dari tata letak kompleks—seperti majalah, makalah akademik, atau brosur—di mana mengubah ukuran teks meningkatkan kejelasan tata letak dan hasil ekstraksi.

1. Muat PDF.
1. Kurangi ukuran font fragmen teks yang ada, simpan, dan buka kembali dokumen.
1. Gunakan 'TextAbsorber' untuk mengekstrak teks dari halaman.
1. Tulis teks yang telah diekstrak.

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
    try:
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
    finally:
        doc.close()
```

## Ekstrak teks dengan faktor skala

Ekstrak teks dari PDF dengan tata letak multi-kolom dengan menerapkan faktor skala pada dokumen. Menyesuaikan faktor skala memastikan fragmen teks ditafsirkan dengan benar, mengurangi tumpang tindih atau kesalahan penempatan selama ekstraksi.
Ini berguna untuk PDF dengan kolom, tabel, atau tata letak padat, di mana penskalaan membantu mempertahankan urutan bacaan dan struktur yang tepat dalam teks yang diekstrak.

1. Muat PDF.
1. Konfigurasikan 'TextExtractionOptions.ScaleFactor'.
1. Gunakan 'TextAbsorber' untuk mengekstrak teks dari halaman.
1. Tulis teks yang telah diekstrak.

```python

import aspose.pdf as ap

def extract_text_with_scale_factor(infile, outfile, scale_factor=0.5):
    """
    Extract text from a PDF with multi-column layout using scale factor.
    Args:
        infile (str): Input PDF path.
        outfile (str): Output text file path.
        scale_factor (float): Scale factor between 0.1 and 1.0 or 0 for auto-scaling.
    """
    doc = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        ext_opts = ap.text.TextExtractionOptions(ap.text.TextExtractionOptions.TextFormattingMode.PURE)
        ext_opts.scale_factor = scale_factor
        text_absorber.extraction_options = ext_opts
        doc.pages.accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        doc.close()
```
