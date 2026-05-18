---
title: PDF-Metadaten abrufen
type: docs
weight: 20
url: /de/python-net/get-pdf-metadata/
description: Metadaten aus PDF-Dokumenten extrahieren und anzeigen mit Aspose.PDF für Python.
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Abrufen von PDF-Metadaten mit Aspose.PDF für Python.
Abstract: Dieses Handbuch zeigt, wie man Metadaten aus PDF-Dokumenten mit Aspose.PDF für Python extrahiert und anzeigt. Sie lernen, wie Sie auf standardmäßige PDF-Eigenschaften wie Titel, Autor, Schlüsselwörter, Erstellungs‑/Änderungsdaten sowie auf benutzerdefinierte Metadatenfelder zugreifen. Zusätzlich behandelt das Handbuch Prüfungen zur PDF‑Gültigkeit, Verschlüsselung und zum Portfolio‑Status.
---

PDF-Dokumente enthalten häufig wertvolle Metadaten, die den Dokumentinhalt, die Urheberschaft und Berechtigungen beschreiben. Aspose.PDF bietet eine praktische API zum Abrufen sowohl standardmäßiger als auch benutzerdefinierter Metadaten‑Eigenschaften. Dieses Code‑Snippet zeigt, wie man die [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) Klasse, um PDF-Dateien programmgesteuert zu untersuchen, einschließlich Schritt‑für‑Schritt‑Beispielen in Python.

1. Laden Sie die PDF-Datei.
1. Standardmetadaten abrufen.
1. PDF-Status und -Sicherheit prüfen.
1. Benutzerdefinierte Metadaten abrufen.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_metadata(infile):

    # Get and display PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)
    print(f"Subject: {pdf_info.subject}")
    print(f"Title: {pdf_info.title}")
    print(f"Keywords: {pdf_info.keywords}")
    print(f"Creator: {pdf_info.creator}")
    print(f"Creation Date: {pdf_info.creation_date}")
    print(f"Modification Date: {pdf_info.mod_date}")

    # Check PDF status
    print(f"Is Valid PDF: {pdf_info.is_pdf_file}")
    print(f"Is Encrypted: {pdf_info.is_encrypted}")
    print(f"Has Open Password: {pdf_info.has_open_password}")
    print(f"Has Edit Password: {pdf_info.has_edit_password}")
    print(f"Is Portfolio: {pdf_info.has_collection}")

    # Retrieve and display a specific custom attribute
    reviewer = pdf_info.get_meta_info("Reviewer")
    print(f"Reviewer: {reviewer if reviewer else 'No Reviewer metadata found.'}")
```
