---
title: Menambahkan header dan footer pada PDF dengan Python
linktitle: Menambahkan header dan footer
type: docs
weight: 70
url: /id/python-net/artifacts-header-footer/
description: Tambahkan artefak header dan footer bergaya ke halaman PDF di Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menambahkan header dan footer pada PDF dengan Python
Abstract: Tambahkan artefak header dan footer bergaya ke halaman PDF di Python.
---

Gunakan `HeaderArtifact` dan `FooterArtifact` untuk menambahkan teks berjalan ke halaman PDF. Contoh-contoh ini menambahkan artefak ke halaman pertama.

## Membuat artefak teks berformat

Definisikan fungsi pembantu ini sebelum menjalankan salah satu contoh penambahan. Fungsi ini menggunakan fon, ukuran, warna, dan perataan yang sama untuk header dan footer.

```python
import aspose.pdf as ap

def _create_text_artifact(artifact_class, text):
    """Create a text artifact (header/footer) with common styling."""
    artifact = artifact_class()
    artifact.text = text
    artifact.text_state.font_size = 14
    artifact.text_state.font = ap.text.FontRepository.find_font("Arial")
    artifact.text_state.foreground_color = ap.Color.navy
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    return artifact
```

## Menambahkan header ke PDF

Teruskan `HeaderArtifact` ke fungsi pembantu, lalu tambahkan artefak yang dihasilkan ke halaman.

```python
import aspose.pdf as ap

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## Menambahkan footer ke PDF

Teruskan `FooterArtifact` ke fungsi pembantu, lalu tambahkan artefak yang dihasilkan ke halaman.

```python
import aspose.pdf as ap

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## Topik terkait

- [Menghapus header dan footer](/pdf/id/python-net/remove-headers-footers/)
- [Artefak PDF](/pdf/id/python-net/artifacts/)
