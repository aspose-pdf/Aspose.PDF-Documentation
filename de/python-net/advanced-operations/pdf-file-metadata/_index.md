---
title: Arbeiten Sie mit PDF-Dateimetadaten in Python
linktitle: PDF-Dateimetadaten
type: docs
weight: 200
url: /de/python-net/pdf-file-metadata/
description: Erfahren Sie, wie Sie PDF-Dateimetadaten und XMP-Eigenschaften in Python mit Aspose.PDF extrahieren, aktualisieren und verwalten.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Abrufen und Festlegen von PDF-Dokumentinformationen und XMP-Metadaten in Python
Abstract: Dieser Artikel erklärt, wie man mit PDF-Metadaten in Aspose.PDF for Python via .NET arbeitet. Erfahren Sie, wie Sie Dokumentinformationen wie Autor, Titel und Schlüsselwörter lesen, Dateieigenschaften aktualisieren, XMP-Metadatenfelder setzen und benutzerdefinierte Metadaten‑Präfixe für PDF‑Dateien in Python registrieren.
---

Verwenden Sie diese Anleitung, wenn Sie Dokumenteigenschaften prüfen, PDF‑Dateiinformationen für die Suche oder Katalogisierung aktualisieren oder XMP‑Metadaten programmgesteuert in Python verwalten müssen.

## PDF‑Dateiinformationen abrufen

Dieses Codebeispiel zeigt, wie man Metadaten aus einem PDF-Dokument mit Aspose.PDF for Python via .NET extrahiert. Durch den Zugriff auf die info property des Document-Objekts werden wichtige Informationen wie Autor, Erstellungsdatum, Schlüsselwörter, Änderungsdatum, Betreff und Titel abgerufen. Diese Funktionalität ist für Anwendungen unerlässlich, die eine Dokumentenkatalogisierung, Suchoptimierung oder Validierung von Dokumenteneigenschaften erfordern.

1. Öffnen Sie die PDF-Datei mit der Document-Klasse
1. Rufen Sie die Metadaten des Dokuments über die info property ab
1. Metadaten anzeigen. Geben Sie die gewünschten Metadatenfelder aus.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def get_pdf_file_information(infile):
    # Open PDF document
    document = ap.Document(infile)

    # Get document information
    doc_info = document.info

    # Display document information
    print(f"Author: {doc_info.author}")
    print(f"Creation Date: {doc_info.creation_date}")
    print(f"Keywords: {doc_info.keywords}")
    print(f"Modify Date: {doc_info.mod_date}")
    print(f"Subject: {doc_info.subject}")
    print(f"Title: {doc_info.title}")
```

## PDF-Dateiinformationen festlegen

Aspose.PDF for Python via .NET ermöglicht es Ihnen, dateispezifische Informationen für ein PDF festzulegen, Informationen wie Autor, Erstellungsdatum, Betreff und Titel. Um diese Informationen festzulegen:

1. Öffnen Sie die PDF-Datei mit der Document-Klasse.
1. Erstelle ein [DocumentInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/documentinfo/) Objekt und setzen Sie die gewünschten Metadaten‑Eigenschaften.
1. Speichern Sie die Änderungen in einer neuen PDF-Datei mit der save-Methode.

Das folgende Code‑Snippet zeigt Ihnen, wie Sie PDF-Dateiinformationen festlegen.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_file_information(infile, outfile):

    # Open PDF document
    document = ap.Document(infile)

    # Specify document information
    doc_info = ap.DocumentInfo(document)
    doc_info.author = "Aspose"
    doc_info.creation_date = datetime.datetime.now()
    doc_info.keywords = "Aspose.Pdf, DOM, API"
    doc_info.mod_date = datetime.datetime.now()
    doc_info.subject = "PDF Information"
    doc_info.title = "Setting PDF Document Information"
    doc_info.producer = "Custom producer"
    doc_info.creator = "Custom creator"

    # Save PDF document
    document.save(outfile)
```

## XMP-Metadaten in einer PDF-Datei festlegen

Dieses Code‑Snippet demonstriert, wie man programmgesteuert XMP‑Metadaten in einem PDF‑Dokument mithilfe von Aspose.PDF for Python via .NET festlegt oder aktualisiert. Durch die Änderung von Eigenschaften wie xmp:CreateDate, xmp:Nickname und benutzerdefinierten Feldern können Sie standardisierte Metadaten in Ihre PDF‑Dateien einbetten. Dieser Ansatz ist besonders nützlich, um die Dokumentenorganisation zu verbessern, die Durchsuchbarkeit zu erleichtern und wesentliche Informationen direkt in die Datei einzubetten.

Aspose.PDF ermöglicht das Festlegen von Metadaten in einer PDF‑Datei. So setzen Sie Metadaten:

1. Öffnen Sie die PDF-Datei mit [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse.
1. Ändern Sie die XMP‑Metadaten, indem Sie bestimmten Schlüsseln Werte zuweisen.
1. Speichern Sie das aktualisierte PDF‑Dokument.

Der folgende Codeabschnitt zeigt Ihnen, wie Sie Metadaten in einer PDF‑Datei festlegen.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_xmp_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Set XMP metadata properties
    document.metadata.add("xmp:CreateDate", datetime.datetime.now().isoformat())
    document.metadata.add("xmp:Nickname", "Nickname")
    document.metadata.add("xmp:CustomProperty", "Custom Value")

    # Save the updated PDF document
    document.save(outfile)
```

## Insert Metadata with Prefix

Some developers need to create a new metadata namespace with a prefix. The following code snippet shows how to insert metadata with prefix.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_prefix_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Register a namespace URI for the 'xmp' prefix
    document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

    # Set the metadata property using the registered prefix
    document.metadata.add(
        "xmp:ModifyDate", datetime.datetime.now().isoformat()
    )  # ISO 8601 format

    # Save the updated PDF document
    document.save(outfile)
```

## Verwandte Themen

- [Erweiterte PDF-Operationen in Python](/pdf/de/python-net/advanced-operations/)
- [Arbeiten Sie mit PDF-Dokumenten in Python](/pdf/de/python-net/working-with-documents/)
- [Arbeiten mit PDF-Anhängen in Python](/pdf/de/python-net/attachments/)
- [PDF-Dokumente in Python vergleichen](/pdf/de/python-net/compare-pdf-documents/)
