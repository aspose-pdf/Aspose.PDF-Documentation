---
title: Chiffrer le fichier PDF
type: docs
weight: 30
url: /fr/python-net/encrypt-pdf-file/
description: Chiffrer un document PDF et configurer les autorisations pour contrôler ce que les utilisateurs peuvent faire avec le fichier.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Chiffrer le PDF et contrôler les actions des utilisateurs
Abstract: Apprenez à chiffrer un PDF tout en définissant des autorisations d'utilisateur spécifiques à l'aide d'Aspose.PDF for Python via .NET. Ce guide montre comment autoriser ou restreindre des actions telles que l'impression et la copie tout en maintenant le document sécurisé.
---

## Crypter le PDF avec un mot de passe utilisateur et propriétaire

Sécuriser les documents PDF est essentiel lors du partage de contenus sensibles ou restreints. Le chiffrement vous permet de protéger un document avec des mots de passe et de définir quelles actions les utilisateurs sont autorisés à effectuer. Cet extrait de code montre comment appliquer des mots de passe utilisateur et propriétaire ainsi que des autorisations d'accès pour sécuriser un fichier PDF.

1. Créer un objet PdfFileSecurity.
1. Lier le PDF d'entrée.
1. Définir les privilèges du document.
1. Chiffrer le PDF.
1. Enregistrer le PDF chiffré.

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

## Chiffrer le PDF avec des autorisations

Le fragment de code suivant explique comment autoriser certaines actions comme l'impression et la copie tout en en restreignant d'autres.

1. Initialiser le [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) classe.
1. Lier le PDF d'entrée.
1. Configurer les privilèges du Document.
1. Appeler la méthode 'encrypt_file()'.
1. Enregistrer le PDF chiffré.

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

## Crypter le PDF avec un algorithme de chiffrement

Le chiffrement PDF ne protège pas seulement les documents avec des mots de passe, mais il permet également de choisir l'algorithme de chiffrement et la force. Sélectionner l'algorithme approprié assure une sécurité plus forte pour les documents sensibles.

1. Créer un objet PdfFileSecurity.
1. Lier le PDF d'entrée.
1. Définir les privilèges du document.
1. Crypter le PDF avec l'algorithme.
1. Enregistrer le PDF chiffré.

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
