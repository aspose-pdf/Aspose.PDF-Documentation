---
title: PDF-Dokument programmatisch öffnen
linktitle: PDF öffnen
type: docs
weight: 20
url: /de/python-net/open-pdf-document/
description: Erfahren Sie, wie Sie eine PDF-Datei in Python mit der Aspose.PDF for Python via .NET-Bibliothek öffnen. Sie können ein vorhandenes PDF, ein Dokument aus einem Stream und ein verschlüsseltes PDF-Dokument öffnen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Öffnen von PDF-Dokumenten mit der Aspose.PDF-Bibliothek in Python
Abstract: Dieser Artikel bietet eine Anleitung zum Öffnen vorhandener PDF-Dokumente mithilfe der Aspose.PDF-Bibliothek in Python. Er beschreibt drei Methoden, um dies zu erreichen – das Öffnen eines PDFs durch Angabe des Dateinamens, das Öffnen eines PDFs aus einem Stream und das Öffnen eines verschlüsselten PDFs durch Bereitstellung eines Passworts. Jede Methode enthält einen Codeausschnitt, der zeigt, wie die Aspose.PDF-Bibliothek verwendet wird, um auf das PDF zuzugreifen und die Anzahl der Seiten auszugeben. Diese Beispiele veranschaulichen die Flexibilität und Funktionalität von Aspose.PDF beim Umgang mit verschiedenen PDF-Zugriffsszenarien.
---

## Vorhandenes PDF-Dokument öffnen

Es gibt mehrere Möglichkeiten, ein Dokument zu öffnen. Die einfachste ist, einen Dateinamen anzugeben.

```python
import aspose.pdf as ap

def open_document_from_file(infile):

    # Open document
    document = ap.Document(infile)
    print("Pages: " + str(len(document.pages)))
```

## Open existing PDF document from stream

```python
import aspose.pdf as ap
import io

def open_document_from_stream(infile):
    with io.FileIO(infile, "r") as stream:
        # Open document
        document = ap.Document(stream)
        print("Pages: " + str(len(document.pages)))
```

## Verschlüsseltes PDF-Dokument öffnen

```python
import aspose.pdf as ap

def open_document_encrypted(infile):
    password = "P@ssw0rd"
    # Open document
    document = ap.Document(infile, password)
    print("Pages: " + str(len(document.pages)))
```
