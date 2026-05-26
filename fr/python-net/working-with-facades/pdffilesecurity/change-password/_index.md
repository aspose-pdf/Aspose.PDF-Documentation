---
title: Modifier le mot de passe du fichier PDF
type: docs
weight: 10
url: /fr/python-net/change-password/
description: Modifier les mots de passe utilisateur et propriétaire d'un document PDF sécurisé à l'aide d'Aspose.PDF for Python via .NET.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mettre à jour les mots de passe du PDF
Abstract: Apprenez comment modifier à la fois les mots de passe utilisateur et propriétaire dans un fichier PDF sécurisé à l'aide d'Aspose.PDF for Python via .NET. Cet exemple montre comment mettre à jour en toute sécurité les informations d'accès tout en conservant le chiffrement et les autorisations existants.
---

## Modifier le mot de passe utilisateur et propriétaire

Dans de nombreux cas, vous pourriez avoir besoin de mettre à jour les mots de passe d'un PDF protégé sans modifier sa configuration de sécurité existante. Cela peut être utile lors de la rotation des informations d'identification, du transfert de propriété ou du renforcement de la sécurité du document.

La méthode 'change_password' du [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) la classe vous permet :

- Mettre à jour le mot de passe utilisateur (nécessaire pour ouvrir le document)
- Mettre à jour le mot de passe propriétaire (utilisé pour contrôler les autorisations)
- Conserver les paramètres de chiffrement et d'autorisation actuels

1. Créer un objet 'PdfFileSecurity'.
1. Lier le PDF d'entrée.
1. Modifier les mots de passe avec la méthode 'change_password()'.
1. Enregistrer le PDF mis à jour.

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

## Modifier le mot de passe et réinitialiser la sécurité

Lorsque vous travaillez avec des documents PDF sécurisés, changer simplement les mots de passe peut ne pas suffire. Vous devrez peut-être également ajuster les autorisations, telles que l'impression, la copie ou les droits de modification.

Découvrez comment mettre à jour les mots de passe utilisateur et propriétaire tout en réinitialisant les paramètres de sécurité PDF avec Aspose.PDF for Python via .NET. Cet exemple montre comment redéfinir les autorisations du document et la force de chiffrement ainsi que les nouvelles informations d'accès.

1. Créer un objet 'PdfFileSecurity'.
1. Lier le PDF d'entrée.
1. Créez un objet 'DocumentPrivilege' et configurez les actions autorisées.
1. Modifiez les mots de passe et réinitialisez la sécurité.
1. Enregistrer le PDF mis à jour.

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

## Essayer de changer le mot de passe sans exception

Dans certains flux de travail, en particulier dans le traitement par lots ou les systèmes automatisés, il est important d'éviter les exceptions qui peuvent interrompre l'exécution. Au lieu de lever des erreurs, vous pouvez préférer une opération sécurisée qui rapporte le succès ou l'échec.

La méthode 'try_change_password' de [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) classe fournit cette fonctionnalité par:

1. Créer un objet 'PdfFileSecurity'.
1. Chargez le document PDF en utilisant la méthode 'bind_pdf()'.
1. Tentative de changer les mots de passe.
1. Vérifiez le résultat.
1. Enregistrer le PDF mis à jour.

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
