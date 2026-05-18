---
title: Berechtigungen für eine vorhandene PDF-Datei festlegen
type: docs
weight: 40
url: /de/python-net/set-privileges/
description: PDF-Dokumentberechtigungen festlegen und verwalten, um Benutzeraktionen wie Drucken, Kopieren und Bearbeiten zu steuern.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Berechtigungen und Zugriffskontrollen verwalten
Abstract: Erfahren Sie, wie Sie steuern können, was Benutzer mit einem PDF tun können, indem Sie Dokumentberechtigungen mit Aspose.PDF for Python via .NET festlegen. Dieser Leitfaden behandelt das Anwenden von Berechtigungen mit oder ohne Passwörter, um Aktionen wie Drucken, Kopieren oder Bearbeiten einzuschränken.
---

## PDF-Berechtigungen ohne Passwörter festlegen

Überprüfen Sie, wie Sie Dokumentenrechte auf ein PDF anwenden können, ohne Benutzer‑ oder Eigentümerpasswörter anzugeben, wobei Aspose.PDF for Python via .NET verwendet wird. Dieser Codeausschnitt zeigt, wie Sie zulässige Aktionen steuern können, während das Dokument zugänglich bleibt.

1. Erstellen Sie ein 'PdfFileSecurity'-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Definieren Sie Dokumentenrechte.
1. Rufen Sie die 'set_privilege()'-Methode auf, ohne Passwörter zu übergeben.
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges Without Passwords
def set_pdf_privileges_without_passwords(infile, outfile):
    """Set PDF privileges without specifying user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Apply privileges (owner password will be generated automatically)
    file_security.set_privilege(privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## PDF-Berechtigungen mit Benutzer- und Eigentümerkennwort festlegen

Um ein PDF-Dokument vollständig zu sichern, benötigen Sie oft sowohl Zugriffskontrolle (Passwörter) als auch Nutzungsbeschränkungen (Berechtigungen). Durch die Kombination dieser Optionen können Sie sicherstellen, dass nur autorisierte Benutzer das Dokument öffnen und bestimmte Aktionen ausführen können.

Durch die Verwendung der set_privilege‑Methode mit Passwortparametern können Sie:

- Schützen Sie das Dokument mit einem Benutzerkennwort
- Definieren Sie ein Owner-Passwort für die volle Kontrolle
- Konfigurieren Sie erlaubte und eingeschränkte Aktionen
- Durchsetzen von sicherheitsrichtlinien auf Dokumentenebene

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges with User and Owner Passwords
def set_pdf_privileges_with_passwords(infile, outfile):
    """Set PDF privileges using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = False

    # Apply privileges with passwords
    file_security.set_privilege("user_password", "owner_password", privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## Versuchen Sie, PDF-Berechtigungen ohne Ausnahme festzulegen

Dieses Code‑Snippet erklärt, wie man den Zugriff kontrolliert und Aktionen wie Kopieren einschränkt, während andere wie Drucken erlaubt werden.

1. Erstelle ein 'PdfFileSecurity'-Objekt.
1. Laden Sie das Quell‑PDF mit der 'bind_pdf()'-Methode.
1. Definieren Sie Dokumentenrechte.
1. Berechtigungen mit Passwörtern anwenden.
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Set PDF Privileges Without Exception
def try_set_pdf_privileges_without_exception(infile, outfile):
    """Attempt to set PDF privileges without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Attempt to apply privileges
    result = file_security.try_set_privilege(
        "user_password", "owner_password", privilege
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Setting privileges failed. Check passwords or document state.")
```
