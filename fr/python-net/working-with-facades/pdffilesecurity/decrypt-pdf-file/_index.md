---
title: Décrypter le fichier PDF
type: docs
weight: 20
url: /fr/python-net/decrypt-pdf-file/
description: Ce guide explique comment supprimer les restrictions telles que l'impression, la copie et la modification afin d'obtenir un accès complet à votre document PDF.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer la protection par mot de passe d'un PDF
Abstract: Cet article montre comment décrypter un fichier PDF à l'aide d'un mot de passe propriétaire. Il couvre le processus de suppression des restrictions de sécurité qui limitent des actions telles que l'impression, la modification ou la copie de contenu. En appliquant le mot de passe propriétaire correct, les utilisateurs peuvent déverrouiller le document et retrouver le plein contrôle de ses fonctionnalités.
---

## Décrypter le PDF avec le mot de passe propriétaire

Décrypter un document PDF protégé par mot de passe en utilisant le mot de passe propriétaire avec Aspose.PDF for Python via .NET. Cette opération supprime le chiffrement et permet un accès illimité au document.

1. Créer un objet 'PdfFileSecurity'.
1. Chargez le PDF chiffré en utilisant la méthode 'bind_pdf()'.
1. Déchiffrez le Document.
1. Enregistrez le PDF déchiffré.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Decrypt PDF with Owner Password
def decrypt_pdf_with_owner_password(infile, outfile):
    """Decrypt a PDF document using the owner password."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Decrypt the PDF
    file_security.decrypt_file("owner_password")

    # Save decrypted PDF
    file_security.save(outfile)
```

## Essayer de déchiffrer le PDF sans exception

Les documents PDF sont souvent protégés par des mots de passe afin de restreindre l'accès et l'utilisation. Pour accéder pleinement ou modifier de tels documents, il peut être nécessaire de retirer le chiffrement. Déchiffrez un document PDF sécurisé en utilisant le mot de passe propriétaire pour supprimer le chiffrement et les restrictions d'accès avec Aspose.PDF for Python via .NET.

1. Créer un objet 'PdfFileSecurity'.
1. Lier le PDF d'entrée.
1. Déchiffrer le PDF.
1. Enregistrer le PDF de sortie.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Decrypt PDF Without Exception
def try_decrypt_pdf_without_exception(infile, outfile):
    """Attempt to decrypt a PDF without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to decrypt the PDF
    result = file_security.try_decrypt_file("owner_password")

    # Save only if decryption was successful
    if result:
        file_security.save(outfile)
    else:
        print("Decryption failed. Check password or document security.")
```
