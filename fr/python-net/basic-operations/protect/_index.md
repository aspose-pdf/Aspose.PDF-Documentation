---
title: Protéger les fichiers PDF en Python
linktitle: Crypter et décrypter le fichier PDF
type: docs
weight: 70
url: /fr/python-net/protect-pdf-file/
description: Apprenez comment crypter les fichiers, décrypter les PDF protégés et changer les mots de passe en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Définir les autorisations PDF et gérer le chiffrement en Python
Abstract: Cette page explique comment définir les privilèges du document, appliquer le chiffrement, déchiffrer les fichiers PDF et modifier les mots de passe en utilisant Aspose.PDF for Python via .NET. Elle couvre la configuration des mots de passe utilisateur et propriétaire, la définition des restrictions d'accès (telles que l'impression, la copie et la modification), et la gestion de la sécurité PDF dans les applications Python.
---

## Chiffrer le PDF avec un mot de passe et des autorisations

Utilisez Aspose.PDF for Python via .NET pour sécuriser un document PDF avec un chiffrement basé sur un mot de passe et des autorisations restreintes.

1. Chargez le document PDF.
1. Créer un `DocumentPrivilege` objet d'autorisations.
1. Activez les autorisations requises.
1. Définissez les mots de passe utilisateur et propriétaire.
1. Choisissez l'algorithme de chiffrement.
1. Appliquer le chiffrement au document.
1. Enregistrer le PDF chiffré.

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

## Chiffrer le PDF avec des autorisations complètes

Cryptez un document PDF tout en autorisant les permissions d'accès complet à l'aide d'Aspose.PDF for Python via .NET. Cet exemple utilise le chiffrement RC4 128 bits pour la compatibilité avec les visionneuses PDF plus anciennes.

1. Chargez le document PDF.
1. Définissez les mots de passe utilisateur et propriétaire.
1. Définissez les permissions d'accès complet.
1. Choisissez l'algorithme de chiffrement.
1. Appeler `encrypt()` avec des mots de passe, des autorisations et un algorithme.
1. Enregistrer le PDF chiffré.

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

## Déchiffrer le fichier PDF à l'aide du mot de passe propriétaire

Pour supprimer la protection par mot de passe et rétablir l'accès complet :

1. Chargez le PDF chiffré en utilisant le mot de passe correct (utilisateur ou propriétaire).
1. Supprimez toute protection par mot de passe et tous les paramètres de chiffrement du document.
1. Enregistrez le PDF désormais non protégé dans le fichier de sortie spécifié.

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

## Modifier le mot de passe d'un fichier PDF

Mettez à jour les informations d'identification de sécurité (mots de passe utilisateur et propriétaire) d'un document PDF tout en conservant son contenu et sa structure.

1. Ouvrez le PDF en utilisant le mot de passe propriétaire existant, qui offre un accès complet aux paramètres de sécurité.
1. Remplacez les anciens mots de passe par un nouveau mot de passe utilisateur et un nouveau mot de passe propriétaire.
1. Enregistrez le PDF avec les paramètres de mot de passe mis à jour.

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

## Déterminer le mot de passe correct à partir du tableau

Dans certains scénarios, vous pouvez avoir besoin d'identifier le mot de passe correct parmi une liste de candidats possibles pour accéder à un PDF sécurisé. L'extrait ci‑dessous vérifie si un fichier PDF est chiffré, puis tente de l'ouvrir en parcourant une liste prédéfinie de mots de passe.

Le processus comprend :

1. Utiliser `PdfFileInfo` pour détecter si le PDF est chiffré.
1. Ouvrez le PDF avec chaque mot de passe en utilisant `ap.Document()`.
1. Si réussi, il affiche le nombre de pages.
1. Sinon, il attrape l'exception et signale le mot de passe échoué.

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
