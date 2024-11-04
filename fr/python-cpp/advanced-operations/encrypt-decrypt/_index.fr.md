---
title: Chiffrer et Déchiffrer un PDF
linktitle: Chiffrer et Déchiffrer un Fichier PDF
type: docs
weight: 30
url: /python-cpp/set-privileges-encrypt-and-decrypt-pdf-file/
description: Chiffrer et Déchiffrer un Fichier PDF avec Python via une application C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Chiffrer un Fichier PDF en Utilisant Différents Types et Algorithmes de Chiffrement

Une manière efficace de protéger les fichiers PDF est par le biais du chiffrement. Dans cet article, nous allons explorer comment chiffrer des documents PDF en utilisant Python avec l'aide de la bibliothèque Aspose.PDF.

Le chiffrement PDF implique de brouiller le contenu d'un document PDF à l'aide d'algorithmes cryptographiques pour empêcher un accès non autorisé. Les fichiers PDF chiffrés nécessitent un mot de passe pour être ouverts et peuvent avoir des restrictions sur des actions comme l'impression, la copie et l'édition.

- Le **mot de passe utilisateur**, s'il est défini, est celui que vous devez fournir pour ouvrir un PDF. Acrobat/Reader demandera à l'utilisateur de saisir le mot de passe utilisateur. S'il n'est pas correct, le document ne s'ouvrira pas.
- Le **mot de passe propriétaire**, s'il est défini, contrôle les permissions, telles que l'impression, l'édition, l'extraction, les commentaires, etc.
 Acrobat/Reader désactivera ces choses en fonction des paramètres d'autorisation. Acrobat exigera ce mot de passe si vous souhaitez définir/modifier des autorisations.

Le fragment de code suivant vous montre comment chiffrer des fichiers PDF.

1. Créer le chemin d'accès au fichier d'entrée et de sortie
1. Charger le document PDF en utilisant AsposePDFPythonWrappers
1. Définir les autorisations pour le document chiffré
1. Définir l'algorithme de chiffrement à utiliser
1. Chiffrer le document avec les mots de passe utilisateur et propriétaire spécifiés, les autorisations et l'algorithme de chiffrement en utilisant la méthode 'document.encrypt'
1. Enregistrer le document chiffré dans le fichier de sortie spécifié avec la méthode 'document.save'.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Définir le chemin du répertoire pour les fichiers d'exemple
    dataDir = os.path.join(os.getcwd(), "samples")

    # Définir le chemin du fichier d'entrée
    input_file = os.path.join(dataDir, "sample.pdf")

    # Définir le chemin du fichier de sortie
    output_file = os.path.join(dataDir, "results", "sample-enc.pdf")

    # Charger le document PDF en utilisant AsposePDFPythonWrappers
    document = apw.Document(inputFile)

    # Définir les autorisations pour le document chiffré
    permission = apCore.Permissions(apCore.Permissions.ExtractContent | apCore.ModifyContent)

    # Définir l'algorithme de chiffrement à utiliser
    cryptoAlgorithm = apCore.CryptoAlgorithm.RC4x128

    # Chiffrer le document avec les mots de passe utilisateur et propriétaire spécifiés, les autorisations et l'algorithme de chiffrement
    document.encrypt("user", "owner", permission, cryptoAlgorithm)

    # Enregistrer le document chiffré dans le fichier de sortie spécifié
    document.save(output_file)
```

## Décrypter un fichier PDF en utilisant le mot de passe propriétaire

1. Créer le chemin du fichier d'entrée et de sortie
1. Créer une nouvelle instance de la classe Document à partir du module AsposePDFPythonWrappers
1. Décrypter le document en utilisant la méthode [document_decrypt](https://reference.aspose.com/pdf/python-cpp/core/document_decrypt/)
1. Enregistrer le document décrypté dans le chemin du fichier de sortie en utilisant la méthode save() avec la fonction [document_save](https://reference.aspose.com/pdf/python-cpp/core/document_save/).

```Python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Définir le chemin du répertoire pour les fichiers d'exemple
    dataDir = os.path.join(os.getcwd(), "samples")

    # Définir le chemin du fichier d'entrée
    input_file = os.path.join(dataDir, "sample_enc.pdf")

    # Définir le chemin du fichier de sortie
    output_file = os.path.join(dataDir, "results", "sample-dec.pdf")

    # Créer une nouvelle instance de la classe Document à partir du module AsposePDFPythonWrappers
    document = apw.Document(input_file, "owner")

    # Décrypter le document en utilisant la méthode decrypt()
    document.decrypt()

    # Enregistrer le document décrypté dans le chemin du fichier de sortie en utilisant la méthode save()
    document.save(output_file)
```