---
title: Erstellen eines PDF/A-3A-konformen PDFs und Anhängen einer ZUGFeRD-Rechnung in Python
linktitle: ZUGFeRD an PDF anhängen
type: docs
weight: 10
url: /de/python-net/attach-zugferd/
description: Erfahren Sie, wie Sie ein PDF-Dokument mit ZUGFeRD in Aspose.PDF for Python via .NET erstellen
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man ZUGFeRD an ein PDF-Dokument anhängt
Abstract: Der Artikel bietet eine schrittweise Anleitung, wie man ZUGFeRD (ein Format für elektronische Rechnungen) an ein PDF-Dokument mit der Aspose.PDF‑Bibliothek anhängt. Das Verfahren beginnt mit dem Import der notwendigen Bibliothek und dem Einrichten der Verzeichnis‑pfade für Eingabe‑ und Ausgabedateien. Es beinhaltet das Laden der Ziel‑PDF‑Datei in ein Document‑Objekt und das Erstellen eines FileSpecification‑Objekts für die XML‑Rechnungs‑Metadaten‑Datei. Wichtige Eigenschaften wie `mime_type` und `af_relationship` werden gesetzt, um eine korrekte Integration der Metadaten zu gewährleisten. Die XML‑Datei wird dann zur Sammlung eingebetteter Dateien des PDFs hinzugefügt, wodurch sie effektiv als Metadaten angehängt wird. Anschließend wird das PDF‑Dokument in das PDF/A‑3A‑Format konvertiert, das für die Archivierung elektronischer Dokumente geeignet ist, bevor das endgültige PDF mit dem eingebetteten ZUGFeRD gespeichert wird. Der Artikel schließt mit einem Python‑Code‑Snippet ab, das die Implementierung dieser Schritte demonstriert und die Integration von ZUGFeRD in ein PDF für ein verbessertes Dokumentenmanagement zeigt.
---

## ZUGFeRD an PDF anhängen

Wir empfehlen die folgenden Schritte, um ZUGFeRD an ein PDF anzuhängen:

1. Importieren Sie die Aspose.PDF-Bibliothek und geben Sie ihr aus Bequemlichkeitsgründen einen Alias von ap.
1. Definieren Sie den Pfad zu dem Verzeichnis, in dem sich die Eingabe- und Ausgabe-PDF-Dateien befinden.
1. Definieren Sie den Pfad zu der PDF-Datei, die verarbeitet werden soll.
1. Laden Sie die PDF-Datei aus der Pfadvariablen und erstellen Sie ein Document-Objekt.
1. Erstellen Sie ein FileSpecification-Objekt für die XML-Datei, die die Rechnungsmetadaten enthält. Verwenden Sie die Pfadvariable und einen Beschreibungsstring, um das FileSpecification-Objekt zu erstellen.
1. Setze das `mime_type` und die `af_relationship` Eigenschaften des FileSpecification-Objekts zu `text/xml` und `ALTERNATIVE`, jeweils.
1. Fügen Sie das fileSpecification-Objekt zur eingebetteten Dateien‑Sammlung des Dokument‑Objekts hinzu. Dadurch wird die XML-Datei dem PDF-Dokument als Rechnungs‑Metadaten‑Datei angehängt.
1. Konvertieren Sie das PDF-Dokument in das PDF/A-3A-Format. Verwenden Sie den Pfad zur Protokolldatei, die `PdfFormat.PDF_A_3A` Aufzählung, und das `ConvertErrorAction.DELETE` Aufzählung, um das Dokumentobjekt zu konvertieren.
1. Speichern Sie das PDF-Dokument mit dem angehängten ZUGFeRD.

```python
import sys
import os
import aspose.pdf as ap

def attach_invoice_zugferd_format(infile, invoice, outfile):
    document = ap.Document(infile)

    # Create a FileSpecification object for the XML file that contains the invoice metadata
    description = "Invoice metadata conforming to ZUGFeRD standard"
    file_specification = ap.FileSpecification(invoice, description)

    # Set the MIME type and the AFRelationship properties of the embedded file
    file_specification.mime_type = "text/xml"
    file_specification.af_relationship = ap.AFRelationship.ALTERNATIVE

    # Add the embedded file to the PDF document's embedded files collection
    document.embedded_files.add("factur", file_specification)

    # Convert the PDF document to the PDF/A-3A format
    log_path = outfile.replace(".pdf", "_log.xml")
    document.convert(log_path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
