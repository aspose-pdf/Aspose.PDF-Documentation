---
title: PDF-Datei verschlüsseln
type: docs
weight: 30
url: /de/python-net/encrypt-pdf-file/
description: Verschlüsseln Sie ein PDF-Dokument und konfigurieren Sie Berechtigungen, um zu steuern, was Benutzer mit der Datei tun können.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF verschlüsseln und Benutzeraktionen steuern
Abstract: Erfahren Sie, wie Sie ein PDF verschlüsseln und dabei bestimmte Benutzerberechtigungen mit Aspose.PDF for Python via .NET festlegen. Dieser Leitfaden zeigt, wie Sie Aktionen wie Drucken und Kopieren zulassen oder einschränken können, während das Dokument sicher bleibt.
---

## PDF mit Benutzer- und Eigentümerpasswort verschlüsseln

Das Sichern von PDF-Dokumenten ist unerlässlich, wenn vertrauliche oder eingeschränkte Inhalte geteilt werden. Verschlüsselung ermöglicht es, ein Dokument mit Passwörtern zu schützen und festzulegen, welche Aktionen den Benutzern erlaubt sind. Dieses Code‑Snippet zeigt, wie Benutzer‑ und Eigentümerpasswörter zusammen mit Zugriffsberechtigungen angewendet werden, um eine PDF‑Datei zu sichern.

1. Erstellen Sie ein PdfFileSecurity-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Definieren Sie Dokumentberechtigungen.
1. Verschlüsseln Sie das PDF.
1. Speichern Sie das verschlüsselte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with User and Owner Password
def encrypt_pdf_with_user_owner_password(infile, outfile):
    """Encrypt a PDF document using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define document privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## PDF mit Berechtigungen verschlüsseln

Der nächste Codeabschnitt erklärt, wie ausgewählte Aktionen wie Drucken und Kopieren erlaubt werden können, während andere eingeschränkt werden.

1. Initialisiere das [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) Klasse.
1. Binden Sie das Eingabe-PDF.
1. Konfigurieren Sie die Dokumentberechtigungen.
1. Rufen Sie die Methode 'encrypt_file()' auf.
1. Speichern Sie das verschlüsselte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Permissions
def encrypt_pdf_with_permissions(infile, outfile):
    """Encrypt a PDF document and configure specific permissions."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Configure privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## PDF mit Verschlüsselungsalgorithmus verschlüsseln

Die PDF-Verschlüsselung schützt Dokumente nicht nur mit Passwörtern, sondern ermöglicht es Ihnen auch, den Verschlüsselungsalgorithmus und die Stärke auszuwählen. Die Auswahl des geeigneten Algorithmus gewährleistet eine höhere Sicherheit für vertrauliche Dokumente.

1. Erstellen Sie ein PdfFileSecurity-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Definieren Sie Dokumentberechtigungen.
1. Verschlüsseln Sie das PDF mit Algorithmus.
1. Speichern Sie das verschlüsselte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Encryption Algorithm
def encrypt_pdf_with_encryption_algorithm(infile, outfile):
    """Encrypt a PDF document using a specific encryption algorithm."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF using AES algorithm
    file_security.encrypt_file(
        "user_password",
        "owner_password",
        privilege,
        pdf_facades.KeySize.X256,
        pdf_facades.Algorithm.AES,
    )

    # Save encrypted PDF
    file_security.save(outfile)
```
