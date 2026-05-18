---
title: Revision und Berechtigungen
type: docs
weight: 40
url: /de/python-net/revision-permissions/
description: Erfahren Sie, wie Sie Signaturrevisionen, Dokumentrevisionen und Zertifizierungsberechtigungen in PDF-Dateien mithilfe von PdfFileSignature in Python untersuchen können.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Signaturrevision und Zugriffsberechtigungsdaten in Python lesen
Abstract: Dieser Artikel erklärt, wie man Versions- und Berechtigungsinformationen in signierten oder zertifizierten PDF-Dateien mit Aspose.PDF for Python via .NET überprüft. Er zeigt, wie man die Revisionsnummer einer Signatur erhält, die Gesamtzahl der Dokumentrevisionen zählt und Zugriffsberechtigungen aus einer zertifizierten PDF-Datei liest.
---

Aspose.PDF for Python via .NET stellt die [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) Fassade zum Arbeiten mit signierten und zertifizierten PDF-Dokumenten. Neben dem Hinzufügen von Signaturen können Sie auch Signaturmetadaten untersuchen, um zu verstehen, wie viele Revisionen ein Dokument enthält und welche Änderungen nach der Zertifizierung zulässig sind.

Dieses Beispiel demonstriert drei gängige Prüfaufgaben:

1. Ermitteln Sie die Revisionsnummer einer bestehenden Signatur.
1. Ermitteln Sie die Gesamtzahl der Revisionen in einem signierten Dokument.
1. Lese die Zugriffsberechtigungen aus einem zertifizierten PDF.

## Erhalte die Revisionsnummer für eine Signatur

Verwenden Sie diesen Ansatz, wenn ein PDF bereits eine oder mehrere Signaturen enthält und Sie die mit einer bestimmten Signatur verbundene Revision ermitteln müssen. Das Beispiel ermittelt den ersten verfügbaren Signaturnamen und ruft dann auf `get_revision()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_revision(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_revision = pdf_signature.get_revision(sign_name)
        print(f"Signature Revision for '{sign_name}': {signature_revision}")
    finally:
        pdf_signature.close()
```

## Erhalte die Gesamtzahl der Dokumentrevisionen

Verwenden `get_total_revision()` wenn Sie wissen müssen, wie viele Revisionen im signierten PDF gespeichert sind. Dies ist nützlich, um zu prüfen, ob das Dokument nach der Anwendung der ursprünglichen Signatur mehrere Updates durchlaufen hat.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_total_document_revisions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        total_revisions = pdf_signature.get_total_revision()
        print(f"Total Document Revisions: {total_revisions}")
    finally:
        pdf_signature.close()
```

## Zugriffsberechtigungen aus einem zertifizierten PDF abrufen

Zertifizierte Dokumente können festlegen, welche Änderungen nach der Zertifizierung zulässig sind. Verwenden `get_access_permissions()` um die Berechtigungsstufe zu überprüfen und zu bestimmen, ob das Dokument keine Änderungen, das Ausfüllen von Formularen oder andere kontrollierte Änderungen zulässt.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_access_permissions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        access_permissions = pdf_signature.get_access_permissions()
        print(f"Access Permissions: {access_permissions}")
    finally:
        pdf_signature.close()
```

