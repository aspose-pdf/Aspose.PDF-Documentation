---
title: PDF-Dateien in Python schützen
linktitle: PDF-Datei verschlüsseln und entschlüsseln
type: docs
weight: 70
url: /de/python-net/protect-pdf-file/
description: Erfahren Sie, wie Sie Dateien verschlüsseln, geschützte PDFs entschlüsseln und Passwörter in Python ändern.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Berechtigungen festlegen und Verschlüsselung in Python verwalten
Abstract: Diese Seite erklärt, wie man Dokumentprivilegien festlegt, Verschlüsselung anwendet, PDF-Dateien entschlüsselt und Passwörter ändert, wobei Aspose.PDF for Python via .NET verwendet wird. Sie behandelt die Konfiguration von Benutzer- und Eigentümerpasswörtern, die Definition von Zugriffsrestriktionen (wie Drucken, Kopieren und Bearbeiten) und die Verwaltung der PDF-Sicherheit in Python-Anwendungen.
---

## PDF mit Passwort und Berechtigungen verschlüsseln

Verwenden Sie Aspose.PDF for Python via .NET, um ein PDF-Dokument mit passwortbasierter Verschlüsselung und eingeschränkten Berechtigungen zu sichern.

1. Laden Sie das PDF-Dokument.
1. Erstelle ein `DocumentPrivilege` Berechtigungsobjekt.
1. Aktivieren Sie die erforderlichen Berechtigungen.
1. Legen Sie Benutzer- und Eigentümerkennwörter fest.
1. Wählen Sie den Verschlüsselungsalgorithmus aus.
1. Wenden Sie die Verschlüsselung auf das Dokument an.
1. Speichern Sie das verschlüsselte PDF.

```python
import aspose.pdf as ap

def encrypt_password(infile, outfile):
    """
    Encrypt PDF with password and permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_password("sample.pdf", "sample_protected.pdf")

    Note:
        Uses AES 128-bit encryption. Allows screen readers, forbids all other operations.
        User password: "userpassword", Owner password: "ownerpassword".
    """
    document = ap.Document(infile)
    document_privilege = ap.facades.DocumentPrivilege.forbid_all
    document_privilege.allow_screen_readers = True

    document.encrypt(
        "userpassword",
        "ownerpassword",
        document_privilege,
        ap.CryptoAlgorithm.AESx128,
        False,
    )
    document.save(outfile)
```

## PDF mit vollen Berechtigungen verschlüsseln

Verschlüsseln Sie ein PDF-Dokument, während Sie vollständige Zugriffsberechtigungen mit Aspose.PDF for Python via .NET zulassen. Dieses Beispiel verwendet RC4‑128‑Bit‑Verschlüsselung für die Kompatibilität mit älteren PDF‑Betrachtern.

1. Laden Sie das PDF-Dokument.
1. Definieren Sie Benutzer- und Eigentümerpasswörter.
1. Setzen Sie vollständige Zugriffsberechtigungen.
1. Wählen Sie den Verschlüsselungsalgorithmus aus.
1. Anruf `encrypt()` mit Passwörtern, Berechtigungen und Algorithmus.
1. Speichern Sie das verschlüsselte PDF.

```python
import aspose.pdf as ap

def encrypt_pdf_file(infile, outfile):
    """
    Encrypt PDF with full permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_pdf_file("sample.pdf", "sample_protected.pdf")

    Note:
        Uses RC4 128-bit encryption with allow_all privileges.
    """
    document = ap.Document(infile)
    document.encrypt(
        "userpassword",
        "ownerpassword",
        ap.facades.DocumentPrivilege.allow_all,
        ap.CryptoAlgorithm.RC4x128,
        False,
    )
    document.save(outfile)
```

## PDF-Datei mit Besitzerpasswort entschlüsseln

Um den Passwortschutz zu entfernen und den vollen Zugriff wiederherzustellen:

1. Laden Sie das verschlüsselte PDF mit dem richtigen Passwort (Benutzer- oder Eigentümerpasswort).
1. Entfernen Sie jeglichen Passwortschutz und Verschlüsselungseinstellungen aus dem Dokument.
1. Speichern Sie das nun ungeschützte PDF in die angegebene Ausgabedatei.

```python
import aspose.pdf as ap

def decrypt_pdf_file(infile, outfile):
    """
    Decrypt password-protected PDF.

    Args:
        infile (str): Input encrypted PDF filename
        outfile (str): Output decrypted PDF filename

    Returns:
        None

    Example:
        decrypt_pdf_file("sample_protected.pdf", "sample_unprotected.pdf")

    Note:
        Requires user password to open document.
    """
    document = ap.Document(infile, "userpassword")
    document.decrypt()
    document.save(outfile)
```

## Passwort einer PDF-Datei ändern

Aktualisieren Sie die Sicherheitsinformationen (Benutzer‑ und Eigentümerpasswörter) eines PDF‑Dokuments, während dessen Inhalt und Struktur erhalten bleiben.

1. Öffnen Sie das PDF mit dem vorhandenen Eigentümerpasswort, das vollen Zugriff auf die Sicherheitseinstellungen gewährt.
1. Ersetzen Sie die alten Passwörter durch ein neues Benutzerpasswort und ein neues Eigentümerpasswort.
1. Speichern Sie das PDF mit den aktualisierten Passworteinstellungen.

```python
import aspose.pdf as ap

def change_password(infile, outfile):
    """
    Change user and owner passwords.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        change_password("sample_protected.pdf", "sample_changepassword.pdf")

    Note:
        Changes from ownerpassword to newuser/newowner.
    """
    document = ap.Document(infile, "ownerpassword")
    document.change_passwords("ownerpassword", "newuser", "newowner")
    document.save(outfile)

```

## Bestimmen Sie das korrekte Passwort aus dem Array

In einigen Szenarien müssen Sie möglicherweise das korrekte Passwort aus einer Liste möglicher Kandidaten ermitteln, um auf ein gesichertes PDF zuzugreifen. Der nachstehende Code prüft, ob eine PDF-Datei verschlüsselt ist, und versucht anschließend, sie zu öffnen, indem er eine vordefinierte Liste von Passwörtern durchläuft.

Der Vorgang umfasst:

1. Verwenden `PdfFileInfo` um festzustellen, ob das PDF verschlüsselt ist.
1. Öffnen Sie das PDF mit jedem Passwort unter Verwendung von `ap.Document()`.
1. Wenn erfolgreich, wird die Seitenanzahl ausgegeben.
1. Falls nicht, fängt es die Ausnahme ab und meldet das fehlgeschlagene Passwort.

```python
import aspose.pdf as ap

def determine_correct_password_from_list(infile):
    """
    Test multiple passwords to find correct one.

    Args:
        infile (str): Input encrypted PDF filename

    Returns:
        None

    Example:
        determine_correct_password_from_list("sample_protected.pdf")

    Note:
        Tries passwords: test, test1, test2, test3, userpassword.
        Prints page count if password is correct.
    """
    info = ap.facades.PdfFileInfo(infile)
    print(f"File is password protected {info.is_encrypted}")

    passwords = "test", "test1", "test2", "test3", "userpassword"

    for password in passwords:
        try:
            document = ap.Document(infile, password)
            count = len(document.pages)
            if count > 0:
                print(f"Number of Page in document are = {count}")
        except RuntimeError as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
```
