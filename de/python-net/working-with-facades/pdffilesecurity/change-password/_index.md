---
title: Passwort der PDF-Datei ändern
type: docs
weight: 10
url: /de/python-net/change-password/
description: Ändern Sie die Benutzer- und Eigentümerpasswörter eines gesicherten PDF-Dokuments mit Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Passwörter aktualisieren
Abstract: Erfahren Sie, wie Sie sowohl das Benutzer- als auch das Eigentümerpasswort in einer gesicherten PDF-Datei mit Aspose.PDF for Python via .NET ändern. Dieses Beispiel zeigt, wie Sie Zugangsberechtigungen sicher aktualisieren können, während die vorhandene Verschlüsselung und die Berechtigungen unverändert bleiben.
---

## Benutzer- und Eigentümerpasswort ändern

In vielen Fällen müssen Sie möglicherweise die Passwörter eines geschützten PDFs aktualisieren, ohne die bestehende Sicherheitseinstellung zu ändern. Dies kann nützlich sein, wenn Anmeldeinformationen rotiert, das Eigentum übertragen oder die Dokumentensicherheit verbessert wird.

Die Methode 'change_password' von [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) Klasse lässt Sie:

- Aktualisieren Sie das Benutzerpasswort (erforderlich, um das Dokument zu öffnen)
- Aktualisieren Sie das Eigentümerpasswort (verwendet, um Berechtigungen zu steuern)
- Behalten Sie die aktuellen Verschlüsselungs- und Berechtigungseinstellungen bei

1. Erstelle ein 'PdfFileSecurity'-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Passwörter mit der Methode 'change_password()' ändern.
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Change User and Owner Password
def change_user_and_owner_password(infile, outfile):
    """Change user and owner passwords while keeping existing security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Change passwords
    file_security.change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save updated PDF
    file_security.save(outfile)
```

## Passwort ändern und Sicherheit zurücksetzen

Beim Arbeiten mit gesicherten PDF-Dokumenten reicht das bloße Ändern von Passwörtern möglicherweise nicht aus. Möglicherweise müssen Sie auch Berechtigungen anpassen, wie z. B. Druck-, Kopier- oder Bearbeitungsrechte.

Erfahren Sie, wie Sie Benutzer- und Eigentümer-Passwörter aktualisieren und gleichzeitig die PDF-Sicherheitseinstellungen zurücksetzen können mit Aspose.PDF for Python via .NET. Dieses Beispiel zeigt, wie Dokumentberechtigungen und Verschlüsselungsstärke zusammen mit neuen Zugangskennungen neu definiert werden.

1. Erstelle ein 'PdfFileSecurity'-Objekt.
1. Binden Sie das Eingabe-PDF.
1. Erstellen Sie ein 'DocumentPrivilege'-Objekt und konfigurieren Sie die zulässigen Aktionen.
1. Passwörter ändern und Sicherheit zurücksetzen.
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Change Password and Reset Security
def change_password_and_reset_security(infile, outfile):
    """Change passwords and reset document security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define new privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Change passwords and reset security
    file_security.change_password(
        "owner_password",
        "new_user_password",
        "new_owner_password",
        privilege,
        pdf_facades.KeySize.X128,
    )

    # Save updated PDF
    file_security.save(outfile)
```

## Versuchen Sie, das Passwort ohne Ausnahme zu ändern

In einigen Workflows, insbesondere bei der Stapelverarbeitung oder in automatisierten Systemen, ist es wichtig, Ausnahmen zu vermeiden, die die Ausführung unterbrechen könnten. Anstatt Fehler zu werfen, bevorzugen Sie möglicherweise einen sicheren Vorgang, der Erfolg oder Misserfolg meldet.

Die 'try_change_password'-Methode der [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) Klasse stellt diese Funktionalität bereit durch:

1. Erstelle ein 'PdfFileSecurity'-Objekt.
1. Laden Sie das PDF-Dokument mit der 'bind_pdf()'-Methode.
1. Versuchen, Passwörter zu ändern.
1. Ergebnis prüfen.
1. Speichere das aktualisierte PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Change Password Without Exception
def try_change_password_without_exception(infile, outfile):
    """Attempt to change passwords without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to change passwords
    result = file_security.try_change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Password change failed. Check owner password or document security.")
```
