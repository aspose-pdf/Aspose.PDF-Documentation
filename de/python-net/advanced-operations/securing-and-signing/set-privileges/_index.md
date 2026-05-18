---
title: PDF-Dateien in Python verschlüsseln und entschlüsseln
linktitle: PDF-Datei verschlüsseln und entschlüsseln
type: docs
weight: 70
url: /de/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Erfahren Sie, wie Sie PDF-Berechtigungen festlegen, Dateien verschlüsseln, geschützte PDFs entschlüsseln und Passwörter in Python ändern.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Legen Sie PDF-Berechtigungen fest und verwalten Sie die Verschlüsselung in Python.
Abstract: Diese Dokumentationsseite erklärt, wie man Dokumentenrechte festlegt, Verschlüsselung anwendet und PDF-Dateien mit Aspose.PDF für Python entschlüsselt. Sie führt Entwickler durch die Konfiguration von Benutzer- und Besitzerkennwörtern, die Definition von Zugriffsrestriktionen (wie Drucken, Kopieren oder Bearbeiten). Codebeispiele zeigen, wie sensible Inhalte geschützt und die PDF‑Sicherheit effektiv in Python‑Anwendungen verwaltet wird, wodurch kontrollierter Zugriff und Datenvertraulichkeit gewährleistet sind.
---

Die Verwaltung der Dokumentensicherheit ist unverzichtbar, wenn mit sensiblen oder geschäftskritischen Inhalten gearbeitet wird. Aspose.PDF for Python via .NET bietet eine robuste API zum programmgesteuerten Anwenden von Verschlüsselung, zur Steuerung des Zugriffs über Berechtigungen und zum Entschlüsseln geschützter PDF‑Dateien.

Dieser Artikel führt Python‑Entwickler durch praktische Beispiele zum Festlegen von Berechtigungen, Anwenden und Entfernen von Verschlüsselung, Ändern von Passwörtern und Erkennen von Schutzzuständen — alles innerhalb eines PDF‑Workflows.

Aspose.PDF for Python via .NET gibt Entwicklern die volle Kontrolle über die PDF‑Sicherheit:

**Privilegien festlegen** - Feinkörnige Zugriffskontrolle mittels Berechtigungen.
**Datei verschlüsseln** - Wenden Sie AES- oder RC4-Verschlüsselung mit benutzerdefinierten Passwörtern an.
**Datei entschlüsseln** - Entfernen Sie die Sicherheit mit dem Besitzerpasswort.
**Passwörter ändern** - Anmeldeinformationen rotieren oder aktualisieren, ohne den Inhalt zu ändern.
**Sicherheit prüfen** - Erkennen Sie den Verschlüsselungsstatus oder die erforderlichen Passworttypen.

Verwenden Sie diese Seite, wenn Sie PDF-Dokumente mit Passwörtern schützen, das Drucken oder Kopieren einschränken, Anmeldedaten rotieren oder prüfen möchten, ob ein Dokument verschlüsselt ist.

## Berechtigungen für eine vorhandene PDF-Datei festlegen

Sie können bestimmte Vorgänge (z. B. Drucken, Kopieren, Ausfüllen von Formularen) einschränken oder zulassen, indem Sie Benutzer‑ und Eigentümerkennwörter zusammen mit Zugriffsrechten zuweisen.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def set_privileges_on_existing_pdf_file(infile: str, outfile: str) -> None:
    """Set restricted privileges on an existing PDF document."""
    with ap.Document(infile) as document:
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        document_privilege.allow_screen_readers = True
        document.encrypt(
            "user",
            "owner",
            document_privilege,
            ap.CryptoAlgorithm.AESx128,
            False,
        )
        document.save(outfile)
```

## PDF-Datei mit verschiedenen Verschlüsselungstypen und -Algorithmen verschlüsseln

Das Verschlüsseln einer PDF-Datei stellt sicher, dass nur Benutzer mit gültigen Anmeldeinformationen die Datei öffnen oder ändern können.

>Schlüsselbegriffe:

- Benutzerkennwort. Erforderlich, um das Dokument zu öffnen.

- Besitzer-Passwort. Erforderlich, um Berechtigungen zu ändern oder die Verschlüsselung zu entfernen.

- KeySize. Verwenden Sie AE_SX128 für maximale Sicherheit in modernen Arbeitsabläufen.

Der folgende Codeabschnitt zeigt Ihnen, wie Sie PDF-Dateien verschlüsseln.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def encrypt_pdf_file(infile: str, outfile: str) -> None:
    """Encrypt a PDF document with user and owner passwords."""
    with ap.Document(infile) as document:
        document.encrypt(
            "user",
            "owner",
            ap.Permissions.EXTRACT_CONTENT,
            ap.CryptoAlgorithm.AESx128,
        )
        document.save(outfile)
```

## PDF-Datei mit Besitzer-Passwort entschlüsseln

Um den Passwortschutz zu entfernen und den vollen Zugriff wiederherzustellen:

1. Lädt das verschlüsselte PDF mit dem korrekten Passwort ('password' ist das Benutzer- oder Eigentümer-Passwort).
1. Entfernt alle Passwortschutz- und Verschlüsselungseinstellungen aus dem Document.
1. Speichert das jetzt ungeschützte PDF in die angegebene Ausgabedatei.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def decrypt_pdf_file(infile: str, outfile: str) -> None:
    """Decrypt a password-protected PDF document."""
    with ap.Document(infile, "password") as document:
        document.decrypt()
        document.save(outfile)
```

## Verschlüsseln und Entschlüsseln einer PDF-Datei mit öffentlichen Schlüsselzertifikaten

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def pub_sec_encryption(
    crypto_algorithm,
    pub_cert: str,
    in_pfx: str,
    outfile: str,
) -> None:
    """Demonstrate public-key encryption and decryption."""
    pfx_password = "12345"

    with ap.Document() as document:
        document.info.title = "TestTitle"
        document.info.author = "TestAuthor"
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("Hello World!"))

        with open(pub_cert, "rb") as file_stream:
            byte_content = file_stream.read()

        document.encrypt(
            ap.Permissions.PRINT_DOCUMENT,
            crypto_algorithm,
            [byte_content],
        )
        document.save(outfile)

    with ap.Document(
        outfile,
        ap.security.CertificateEncryptionOptions(pub_cert, in_pfx, pfx_password),
    ) as document:
        print(document.info.title)
        print(document.info.author)

        text_absorber = ap.text.TextAbsorber()
        document.pages[1].accept(text_absorber)
        print(text_absorber.text)

        document.decrypt()
        document.save(path.join(path.dirname(outfile), "pubsec_decrypted_out.pdf"))
```

## Passwort einer PDF-Datei ändern

Um die Sicherheitsanmeldeinformationen (Benutzer- und Besitzerpasswörter) eines PDF-Dokuments zu aktualisieren, wobei dessen Inhalt und Struktur erhalten bleiben.

1. Öffnet das PDF mit dem vorhandenen Owner‑Passwort ('owner'), das vollen Zugriff gewährt, einschließlich der Berechtigung, Sicherheitseinstellungen zu ändern.
1. Ersetzt die alten Passwörter durch ein neues Benutzerpasswort ('newuser') und ein neues Besitzer‑Passwort ('newowner').
1. Speichert das PDF mit den aktualisierten Passworteinstellungen.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def change_password(infile: str, outfile: str) -> None:
    """Change the passwords of a password-protected PDF document."""
    with ap.Document(infile, "owner") as document:
        document.change_passwords("owner", "newuser", "newowner")
        document.save(outfile)
```

## Wie man – bestimmt, ob das Quell-PDF passwortgeschützt ist

### Bestimmen Sie das korrekte Passwort aus dem Array

In einigen Szenarien müssen Sie möglicherweise das richtige Passwort aus einer Liste potenzieller Kandidaten ermitteln, um auf ein gesichertes PDF zuzugreifen. Das nachstehende Code‑Snippet zeigt, wie Sie prüfen können, ob eine PDF‑Datei passwortgeschützt ist, und dann versuchen, sie zu entsperren, indem Sie durch eine vordefinierte Liste von Passwörtern iterieren, wobei Aspose.PDF for Python via .NET verwendet wird.

Der Prozess beinhaltet:

1. Verwenden von PdfFileInfo, um zu erkennen, ob das PDF verschlüsselt ist.
1. Versucht, das PDF mit jedem Passwort mit ap.Document() zu öffnen.
1. Wenn erfolgreich, gibt es die Anzahl der Seiten aus.
1. Falls nicht, fängt es die Ausnahme ab und meldet das fehlgeschlagene Passwort.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def determine_correct_password_from_array(infile: str) -> None:
    """Try a list of passwords until the document opens successfully."""
    with ap.facades.PdfFileInfo() as pdf_file_info:
        pdf_file_info.bind_pdf(infile)
        print(f"File is password protected {pdf_file_info.is_encrypted}")

    passwords = ["test", "test1", "test2", "test3", "sample"]

    for password in passwords:
        try:
            with ap.Document(infile, password) as document:
                if len(document.pages) > 0:
                    print(f"Password = {password} is correct")
                    print(f"Number of pages in document = {len(document.pages)}")
                    break
        except Exception:
            print(f"Password = {password} is not correct")
```

## Verwandte Sicherheitsthemen

- [PDF-Dateien in Python sichern und signieren](/pdf/de/python-net/securing-and-signing/)
- [PDF-Dateien in Python digital signieren](/pdf/de/python-net/digitally-sign-pdf-file/)
- [Extrahiere Signaturinformationen aus PDF in Python](/pdf/de/python-net/extract-image-and-signature-information/)
- [PDF-Dokumente mit einer Smartcard in Python signieren](/pdf/de/python-net/sign-pdf-document-from-smart-card/)

