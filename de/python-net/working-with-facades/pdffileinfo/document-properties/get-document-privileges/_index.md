---
title: Dokumentberechtigungen abrufen
type: docs
weight: 10
url: /de/python-net/get-document-privileges/
description: Erfahren Sie, wie Sie die Berechtigungen eines PDF-Dokuments programmgesteuert mit Aspose.PDF for Python überprüfen können. Dieses Tutorial zeigt, wie die Klasse PdfFileInfo verwendet wird, um die Sicherheitseinstellungen des Dokuments zu lesen, wie etwa Druck-, Kopier- oder Änderungsberechtigungen.
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Dokumentberechtigungen mit Aspose.PDF for Python abrufen
Abstract: PDF-Dokumente können Sicherheitsbeschränkungen haben, die Aktionen wie Drucken, Kopieren, Ändern oder Ausfüllen von Formularen einschränken. Durch den programmgesteuerten Zugriff auf diese Berechtigungen können Entwickler feststellen, welche Vorgänge bei einem PDF erlaubt sind. Dieses Handbuch zeigt, wie die Klasse PdfFileInfo verwendet wird, um die Dokumentberechtigungen eines PDFs abzurufen und in Python anzuzeigen.
---

PDF-Berechtigungen bestimmen, was Benutzer mit einem Dokument tun können und was nicht. Häufige Berechtigungen umfassen:

- Drucken des Dokuments
- Kopieren von Inhalten
- Ändern von Anmerkungen oder Inhalten
- Ausfüllen von FormFields
- Verwendung von Bildschirmlesern
- Zusammenstellen oder Zusammenführen von Documents

Mit Aspose.PDF for Python können Sie diese Einstellungen programmgesteuert mithilfe der [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) Klasse. Das ist besonders nützlich beim Arbeiten mit mehreren PDFs in automatisierten Workflows, bei der Überprüfung der Konformität oder bei der Steuerung der Dokumentenverarbeitung in Anwendungen.

1. Lade eine PDF-Datei.
1. Rufe seine Dokumentberechtigungen ab.
1. Zeige an, welche Aktionen für das Dokument zulässig sind.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_document_privileges(input_file_name):
    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)

    privileges = pdf_metadata.get_document_privilege()

    print("Document Privileges:")
    print(f"  Can Print: {privileges.allow_print}")
    print(f"  Can Degraded Print: {privileges.allow_degraded_printing}")
    print(f"  Can Copy: {privileges.allow_copy}")
    print(f"  Can Modify Contents: {privileges.allow_modify_contents}")
    print(f"  Can Modify Annotations: {privileges.allow_modify_annotations}")
    print(f"  Can Fill In: {privileges.allow_fill_in}")
    print(f"  Can Screen Readers: {privileges.allow_screen_readers}")
    print(f"  Can Assembly: {privileges.allow_assembly}")
```
