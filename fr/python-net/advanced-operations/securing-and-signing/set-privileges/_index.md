---
title: Définir les privilèges, chiffrer et déchiffrer le PDF
linktitle: Chiffrer et déchiffrer le fichier PDF
type: docs
weight: 70
url: /fr/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Chiffrer un fichier PDF avec Python en utilisant différents types de chiffrement et algorithmes. Aussi, déchiffrer les fichiers PDF à l'aide du mot de passe propriétaire.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Chiffrer ou déchiffrer un fichier PDF avec Python
Abstract: Cette page de documentation explique comment définir les privilèges d'un document, appliquer le chiffrement et déchiffrer les fichiers PDF en utilisant Aspose.PDF pour Python. Elle guide les développeurs dans la configuration des mots de passe utilisateur et propriétaire, la définition des restrictions d'accès (telles que l'impression, la copie ou la modification). Les exemples de code illustrent comment protéger le contenu sensible et gérer la sécurité des PDF efficacement dans les applications Python, assurant un accès contrôlé et la confidentialité des données.
---

La gestion de la sécurité des documents est essentielle lorsqu'on travaille avec du contenu sensible ou critique pour l'entreprise. Aspose.PDF pour Python via .NET offre une API robuste permettant d'appliquer programmatiquement le chiffrement, de contrôler l'accès via des autorisations et de déchiffrer les fichiers PDF protégés.

Cet article guide les développeurs Python à travers des exemples pratiques pour définir les privilèges, appliquer et retirer le chiffrement, changer les mots de passe et détecter les états de protection — le tout dans un flux de travail PDF.

Aspose.PDF pour Python via .NET donne aux développeurs un contrôle complet sur la sécurité des PDF :

**Définir les privilèges** - Contrôle d'accès granulaire grâce aux autorisations.
**Chiffrer le fichier** - Appliquer le chiffrement AES ou RC4 avec des mots de passe personnalisés.
**Déchiffrer le fichier** - Supprimer la sécurité à l'aide du mot de passe propriétaire.
**Changer les mots de passe** - Faire pivoter ou mettre à jour les identifiants sans modifier le contenu.
**Inspecter la sécurité** - Détecter le statut de chiffrement ou les types de mots de passe requis.

## Définir les privilèges sur un fichier PDF existant

Vous pouvez restreindre ou autoriser des opérations spécifiques (par exemple, impression, copie, remplissage de formulaires) en attribuant des mots de passe utilisateur et propriétaire ainsi que des privilèges d'accès.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate Document Privileges object
        # Apply restrictions on all privileges
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        # Only allow screen reading
        document_privilege.allow_screen_readers = True
        # Encrypt the file with User and Owner password
        # Need to set the password, so that once the user views the file with user password
        # Only screen reading option is enabled
        document.encrypt("user", "owner", document_privilege, ap.CryptoAlgorithm.AE_SX128, False)
        # Save PDF document
        document.save(path_outfile)
```

## Chiffrer un fichier PDF en utilisant différents types de chiffrement et algorithmes

Le chiffrement d'un PDF garantit que seuls les utilisateurs disposant d'identifiants valides peuvent ouvrir ou modifier le fichier.

>Termes clés :

- Mot de passe utilisateur. Nécessaire pour ouvrir le document.

- Mot de passe propriétaire. Nécessaire pour modifier les autorisations ou supprimer le chiffrement.

- Taille de clé. Utilisez AE_SX128 pour une sécurité maximale dans les flux de travail modernes.

Le extrait de code suivant vous montre comment chiffrer des fichiers PDF.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Encrypt PDF
        document.encrypt("user", "owner", ap.Permissions.EXTRACT_CONTENT, ap.CryptoAlgorithm.AE_SX128)
        # Save PDF document
        document.save(path_outfile)
```

## Déchiffrer un fichier PDF avec le mot de passe propriétaire

Pour supprimer la protection par mot de passe et rétablir l'accès complet :

1. Charge le PDF chiffré en utilisant le mot de passe correct ('password' est le mot de passe utilisateur ou propriétaire).
1. Supprime toutes les protections par mot de passe et les paramètres de chiffrement du document.
1. Enregistre le PDF maintenant non protégé dans le fichier de sortie spécifié.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "password") as document:
        # Decrypt PDF
        document.decrypt()
        # Save PDF document
        document.save(path_outfile)
```

## Modifier le mot de passe d'un fichier PDF

Pour mettre à jour les identifiants de sécurité (mots de passe utilisateur et propriétaire) d'un document PDF tout en conservant son contenu et sa structure.

1. Ouvre le PDF en utilisant le mot de passe propriétaire existant ('owner'), ce qui donne un accès complet y compris la permission de modifier les paramètres de sécurité.
1. Remplace les anciens mots de passe par un nouveau mot de passe utilisateur ('newuser') et un nouveau mot de passe propriétaire ('newowner').
1. Enregistre le PDF avec les paramètres de mot de passe mis à jour.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "owner") as document:
        # Change password
        document.change_passwords("owner", "newuser", "newowner")
        # Save PDF document
        document.save(path_outfile)
```

## Comment - déterminer si le PDF source est protégé par un mot de passe

### Déterminer le mot de passe correct à partir d'un tableau

Dans certains scénarios, vous pouvez devoir identifier le mot de passe correct parmi une liste de candidats potentiels afin d'accéder à un PDF sécurisé. L'extrait de code ci-dessous montre comment vérifier si un fichier PDF est protégé par un mot de passe puis tenter de le déverrouiller en parcourant une liste prédéfinie de mots de passe à l'aide d'Aspose.PDF pour Python via .NET.

Le processus comprend :

1. Utiliser PdfFileInfo pour détecter si le PDF est chiffré.
1. Essaie d'ouvrir le PDF avec chaque mot de passe en utilisant ap.Document().
1. Si réussi, il affiche le nombre de pages.
1. Sinon, il intercepte l'exception et signale le mot de passe incorrect.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    with ap.facades.PdfFileInfo() as pdf_file_info:
        # Bind PDF document
        pdf_file_info.bind_pdf(path_infile)
        # Determine if the source PDF is encrypted
        print("File is password protected " + str(pdf_file_info.is_encrypted))

        passwords = ["test", "test1", "test2", "test3", "sample"]

        for password_index in range(len(passwords)):
            try:
                with ap.Document(path_infile, passwords[password_index]) as document:
                    if len(document.pages) > 0:
                        print("Number of Pages in document are = " + str(len(document.pages)))
                    password_index = password_index + 1
            except Exception as e:
                print("Password = " + passwords[password_index] + " is not correct")
                password_index = password_index + 1
```


