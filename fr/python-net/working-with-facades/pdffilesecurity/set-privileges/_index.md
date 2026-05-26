---
title: Définir les privilèges sur un fichier PDF existant
type: docs
weight: 40
url: /fr/python-net/set-privileges/
description: Définir et gérer les privilèges du document PDF pour contrôler les actions des utilisateurs telles que l'impression, la copie et la modification.
lastmod: "2026-05-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gérer les autorisations PDF et les contrôles d'accès
Abstract: Découvrez comment contrôler ce que les utilisateurs peuvent faire avec un PDF en définissant les privilèges du document à l'aide d'Aspose.PDF for Python via .NET. Ce guide couvre l'application des autorisations avec ou sans mots de passe pour restreindre des actions telles que l'impression, la copie ou la modification.
---

## Définir les privilèges PDF sans mots de passe

Vérifiez comment appliquer les privilèges du document à un PDF sans spécifier les mots de passe utilisateur ou propriétaire en utilisant Aspose.PDF for Python via .NET. Cet extrait de code montre comment contrôler les actions autorisées tout en gardant le document accessible.

1. Créer un objet 'PdfFileSecurity'.
1. Lier le PDF d'entrée.
1. Définir les privilèges du Document.
1. Appelez la méthode 'set_privilege()' sans fournir de mots de passe.
1. Enregistrer le PDF mis à jour.

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

## Définir les privilèges PDF avec les mots de passe utilisateur et propriétaire

Pour sécuriser complètement un document PDF, vous avez souvent besoin à la fois du contrôle d'accès (mots de passe) et des restrictions d'utilisation (permissions). En combinant ces deux éléments, vous pouvez vous assurer que seuls les utilisateurs autorisés peuvent ouvrir le document et réaliser des actions spécifiques.

En utilisant la méthode set_privilege avec des paramètres de mot de passe, vous pouvez :

- Protégez le document avec un mot de passe utilisateur
- Définissez un mot de passe propriétaire pour un contrôle complet
- Configurez les actions autorisées et restreintes
- Appliquez les politiques de sécurité au niveau du document

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

## Essayer de définir les privilèges du PDF sans exception

Cet extrait de code explique comment contrôler l'accès et restreindre des actions telles que la copie tout en permettant d'autres comme l'impression.

1. Créer un objet 'PdfFileSecurity'.
1. Chargez le PDF source en utilisant la méthode 'bind_pdf()'.
1. Définir les privilèges du Document.
1. Appliquer les privilèges avec des mots de passe.
1. Enregistrer le PDF mis à jour.

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
