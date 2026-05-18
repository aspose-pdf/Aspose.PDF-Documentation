---
title: Seiten aus PDF löschen
type: docs
weight: 20
url: /de/python-net/delete-pages-from-pdf/
description: Ausgewählte Seiten aus einem PDF-Dokument mit Aspose.PDF for Python entfernen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Bestimmte Seiten aus einem PDF-Dokument in Python löschen
Abstract: Erfahren Sie, wie Sie ausgewählte Seiten aus einem PDF-Dokument mit Aspose.PDF for Python entfernen. Dieses Beispiel demonstriert, wie man bestimmte Seiten aus einer vorhandenen PDF-Datei programmgesteuert löscht und dabei ein neues Dokument ohne die entfernten Seiten erstellt.
---

Manchmal enthalten PDF-Dokumente unnötige oder vertrauliche Seiten, die entfernt werden müssen. Mit Aspose.PDF for Python können Entwickler programmgesteuert bestimmte Seiten aus einem PDF löschen, ohne die Datei manuell zu bearbeiten.

Unser Beispiel zeigt, wie die delete-Methode von [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) Klasse zum Entfernen von Seiten aus einem PDF-Dokument. Durch Angabe der zu löschenden Seitennummern können Sie ein neues PDF erstellen, das unerwünschte Seiten ausschließt. Diese Funktion ist nützlich, um Berichte zu bereinigen, vertrauliche Informationen zu entfernen oder benutzerdefinierte Dokumentauszüge vorzubereiten.

1. Erstelle ein PdfFileEditor-Objekt.
1. Seiten zum Löschen definieren.
1. Seiten löschen.

```python

    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    import sys
    from os import path

    sys.path.append(path.join(path.dirname(__file__), ".."))
    from config import set_license, initialize_data_dir


    # Delete Pages from PDF
    def delete_pages_from_pdf(infile, outfile):
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the page numbers to be deleted (1-based index)
        pages_to_delete = [2, 4]

        # Delete the specified pages from the PDF document
        pdf_editor.delete(infile, pages_to_delete, outfile)
```