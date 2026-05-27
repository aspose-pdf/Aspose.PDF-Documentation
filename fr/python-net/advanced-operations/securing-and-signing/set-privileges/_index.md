---
title: Chiffrer et déchiffrer des fichiers PDF en Python
linktitle: Chiffrer et déchiffrer un fichier PDF
type: docs
weight: 70
url: /fr/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Apprenez à définir les privilèges PDF, chiffrer les fichiers, déchiffrer les PDF protégés et modifier les mots de passe en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Définissez les autorisations PDF et gérez le chiffrement en Python
Abstract: Cette page de documentation explique comment définir les privilèges d'un document, appliquer le chiffrement et déchiffrer des fichiers PDF à l'aide d'Aspose.PDF for Python. Elle guide les développeurs dans la configuration des mots de passe utilisateur et propriétaire, ainsi que dans la définition des restrictions d'accès (comme l'impression, la copie ou la modification). Des exemples de code illustrent comment protéger le contenu sensible et gérer la sécurité des PDF efficacement au sein des applications Python, garantissant un accès contrôlé et la confidentialité des données.
---

La gestion de la sécurité des documents est essentielle lorsqu'on travaille avec du contenu sensible ou crucial pour l'entreprise. Aspose.PDF for Python via .NET fournit une API robuste pour appliquer programmatiquement le chiffrement, contrôler l'accès via les autorisations et déchiffrer les fichiers PDF protégés.

Cet article guide les développeurs Python à travers des exemples pratiques pour définir les privilèges, appliquer et supprimer le chiffrement, modifier les mots de passe et détecter les états de protection — le tout dans le cadre d’un flux de travail PDF.

Aspose.PDF for Python via .NET donne aux développeurs un contrôle total sur la sécurité des PDF:

**Définir les privilèges** - Contrôle d'accès granulaire à l'aide des autorisations.
**Chiffrer le fichier** - Appliquer le chiffrement AES ou RC4 avec des mots de passe personnalisés.
**Déchiffrer le fichier** - Supprimer la sécurité à l'aide du mot de passe propriétaire.
**Changer les mots de passe** - Faire pivoter ou mettre à jour les informations d\u00e9\u00a0identification sans alt\u00e9rer le contenu.
**Inspecter la sécurité** - Détecter l'état du chiffrement ou les types de mot de passe requis.

Utilisez cette page lorsque vous devez protéger des documents PDF avec des mots de passe, restreindre l'impression ou la copie, faire pivoter les informations d'identification, ou vérifier si un document est chiffré.

## Définir les privilèges sur un fichier PDF existant

Vous pouvez restreindre ou autoriser des opérations spécifiques (par exemple, l'impression, la copie, le remplissage de formulaires) en attribuant des mots de passe utilisateur et propriétaire ainsi que des privilèges d'accès.

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

## Chiffrer le fichier PDF en utilisant différents types de chiffrement et algorithmes

Le chiffrement d'un PDF garantit que seuls les utilisateurs disposant d'identifiants valides peuvent ouvrir ou modifier le fichier.

>Termes clés :

- Mot de passe utilisateur. Requis pour ouvrir le document.

- Mot de passe propriétaire. Nécessaire pour modifier les autorisations ou supprimer le chiffrement.

- KeySize. Utilisez AE_SX128 pour une sécurité maximale dans les flux de travail modernes.

Le fragment de code suivant vous montre comment chiffrer des fichiers PDF.

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

## Décrypter le fichier PDF en utilisant le mot de passe propriétaire

Pour supprimer la protection par mot de passe et rétablir l'accès complet :

1. Charge le PDF chiffré en utilisant le mot de passe correct ('password' est le mot de passe utilisateur ou propriétaire).
1. Supprime toutes les protections par mot de passe et les paramètres de chiffrement du document.
1. Enregistre le PDF désormais non protégé dans le fichier de sortie spécifié.

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

## Chiffrer et déchiffrer un PDF avec des certificats à clé publique

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

## Modifier le mot de passe d’un fichier PDF

Mettre à jour les informations d'identification de sécurité (mot de passe utilisateur et propriétaire) d'un document PDF tout en préservant son contenu et sa structure.

1. Ouvre le PDF en utilisant le mot de passe propriétaire existant ('owner'), ce qui donne un accès complet, y compris la permission de modifier les paramètres de sécurité.
1. Remplace les anciens mots de passe par un nouveau mot de passe utilisateur ('newuser') et un nouveau mot de passe propriétaire ('newowner').
1. Enregistre le PDF avec les paramètres de mot de passe mis à jour.

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

## Comment - déterminer si le PDF source est protégé par mot de passe

### Déterminez le mot de passe correct à partir du tableau

Dans certains scénarios, vous pourriez devoir identifier le mot de passe correct parmi une liste de candidats potentiels afin d'accéder à un PDF sécurisé. Le fragment de code ci‑dessous montre comment vérifier si un fichier PDF est protégé par mot de passe, puis tenter de le débloquer en parcourant une liste prédéfinie de mots de passe à l'aide d'Aspose.PDF for Python via .NET.

Le processus comprend :

1. Utilisation de PdfFileInfo pour détecter si le PDF est chiffré.
1. Essaye d'ouvrir le PDF avec chaque mot de passe en utilisant ap.Document().
1. Si l'opération réussit, il affiche le nombre de pages.
1. Sinon, il intercepte l'exception et signale le mot de passe incorrect.

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

## Sujets de sécurité associés

- [Sécurisez et signez les fichiers PDF en Python](/pdf/fr/python-net/securing-and-signing/)
- [Signer numériquement des fichiers PDF en Python](/pdf/fr/python-net/digitally-sign-pdf-file/)
- [Extraire les informations de signature du PDF en Python](/pdf/fr/python-net/extract-image-and-signature-information/)
- [Signer des documents PDF à partir d'une carte à puce en Python](/pdf/fr/python-net/sign-pdf-document-from-smart-card/)

