---
title: Anhänge aus PDF extrahieren
linktitle: Anhänge extrahieren
type: docs
weight: 50
url: /de/python-net/extract-attachment/
description: Erfahren Sie, wie Sie mit PDF-Anhängen unter Verwendung von Python und Aspose.PDF arbeiten.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Umfassender Leitfaden zur Verwaltung von PDF-Anhängen in Python: Hinzufügen, Extrahieren und Verarbeiten eingebetteter Dateien"
Abstract: PDF-Anhänge werden häufig verwendet, um unterstützende Dokumente, Berichte, Bilder und andere Ressourcen direkt in einer PDF-Datei zu speichern. Dieser Artikel bietet einen umfassenden Überblick über die Verarbeitung von PDF-Anhängen mit Python unter Verwendung von Aspose.PDF. Er erklärt, wie externe Dateien in vorhandene PDFs eingebettet, bestimmte oder alle Anhänge extrahiert, Metadaten wie Dateigröße und Zeitstempel geprüft und Dateien, die als FileAttachment-Annotationen gespeichert sind, wiederhergestellt werden können. Jedes Beispiel demonstriert praktische Techniken zur Automatisierung von Anhangs-Workflows, zur Verbesserung der Dokumentportabilität und zur Vereinfachung der Dateiverwaltung. Egal, ob Sie Unternehmensdokumentsysteme oder benutzerdefinierte Automatisierungsskripte erstellen, Entwickler können diese Methoden verwenden, um eingebettete Dateien in PDF-Dokumenten effizient zu verwalten.
---

## Spezifischen Anhang aus PDF extrahieren

Extrahieren Sie eine einzelne eingebettete Datei aus einem PDF-Dokument mit Python und Aspose.PDF. Es sucht nach einem Anhang anhand des Namens, ruft dessen Inhalt ab und speichert ihn als separate Datei. Dies ist nützlich, um auf eingebettete Dokumente wie Berichte, Protokolle oder unterstützende Dateien, die im PDF gespeichert sind, zuzugreifen.

1. Definieren Sie die Funktion 'extract_single_attachment()'.
1. PDF-Dokument öffnen.
1. Nach Anhang suchen.
1. Anhanginhalt extrahieren.

```python
import aspose.pdf as ap

def extract_single_attachment(infile, attachment_name, outfile):
    with ap.Document(infile) as document:
        print(f"Extracting attachment: {attachment_name}")

        attachment_found = False
        for file_spec in document.embedded_files:
            if file_spec.name == attachment_name:
                with open(outfile, "wb") as f:
                    f.write(file_spec.contents.read())
                print("Attachment extracted successfully")
                attachment_found = True
                break

        if not attachment_found:
            raise ValueError(f"Attachment '{attachment_name}' not found in PDF")
```

## Metadaten der Dateianlage anzeigen

Diese Hilfsfunktion gibt Metadateninformationen eines Dateispezifikationsobjekts aus. Sie wird typischerweise verwendet, wenn man mit eingebetteten Dateianhängen in PDFs unter Verwendung von Aspose.PDF arbeitet und ermöglicht Entwicklern, Details wie Prüfsumme, Erstellungsdatum, Änderungsdatum und Dateigröße zu prüfen.

```python
def _print_file_params(params):
    """Helper to print file specification parameters."""
    if params:
        print(f"CheckSum: {params.check_sum}")
        print(f"Creation Date: {params.creation_date}")
        print(f"Modification Date: {params.mod_date}")
        print(f"Size: {params.size}")
```

## Alle PDF-Anhänge extrahieren und inspizieren

Dieses Code‑Snippet zeigt, wie man alle eingebetteten Dateien aus einem PDF‑Dokument mit Python und Aspose.PDF extrahiert. Es speichert jede Anlage nicht nur in einem angegebenen Ordner, sondern gibt auch detaillierte Metadaten wie Dateiname, Beschreibung, MIME‑Typ, Prüfsumme und Zeitstempel aus. Das ist nützlich für die Prüfung, den Export oder die Verarbeitung eingebetteter Inhalte in PDF‑Dateien.

```python
from os import path
import aspose.pdf as ap

def extract_attachments(infile, output_dir):
    with ap.Document(infile) as document:
        print(f"Total files: {len(document.embedded_files)}")

        for file_spec in document.embedded_files:
            print(f"Name: {file_spec.name}")
            print(f"Description: {file_spec.description}")
            print(f"Mime Type: {file_spec.mime_type}")
            _print_file_params(file_spec.params)

            output_path = path.join(output_dir, file_spec.name)
            with open(output_path, "wb") as f:
                f.write(file_spec.contents.read())
```

## Extrahieren von Dateien aus PDF-Anhang-Anmerkungen

Extrahieren einer eingebetteten Datei aus einer FileAttachment‑Anmerkung in einem PDF mithilfe von Python und Aspose.PDF. Es durchsucht die erste Seite nach der ersten Anhang‑Anmerkung, ruft die eingebettete Datei ab und speichert sie in einem ausgewählten Ausgabeverzeichnis. Das ist nützlich, wenn PDFs anklickbare Datei‑Anhang‑Symbole anstelle von Standard‑eingebetteten Dateisammlungen enthalten.

```python
from os import path
import aspose.pdf as ap
from aspose.pycore import cast

def extract_file_attachment_annotation(infile, output_dir):
    # Open PDF document
    with ap.Document(infile) as document:

        # Get first page
        page = document.pages[1]

        # Find first FileAttachment annotation
        file_attachment = next(
            (
                annot
                for annot in page.annotations
                if annot.annotation_type == ap.annotations.AnnotationType.FILE_ATTACHMENT
            ),
            None,
        )

        if file_attachment is None:
            print("No FileAttachment annotation found on the first page.")
            return

        # Cast to FileAttachmentAnnotation
        faa = cast(ap.annotations.FileAttachmentAnnotation, file_attachment)

        # Access embedded file
        file_spec = faa.file
        print(f"File name: {file_spec.name}")

        # Save embedded file to disk
        output_path = path.join(output_dir, f"extracted-{file_spec.name}")
        with open(output_path, "wb") as f:
            f.write(file_spec.contents.read())

        print(f"Extracted to: {output_path}")
```