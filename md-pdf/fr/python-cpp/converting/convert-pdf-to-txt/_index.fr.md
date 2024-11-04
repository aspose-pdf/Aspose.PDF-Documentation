---
title: Convertir PDF en TXT en Python
linktitle: Convertir PDF en TXT
type: docs
weight: 20
url: /python-cpp/convert-pdf-to-txt/
lastmod: "2024-04-23"
description: Aspose.PDF pour Python via la bibliothèque C++ vous permet de convertir un PDF en format TXT en utilisant Python.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Convertir PDF en TXT

Aspose.PDF pour Python via C++ prend en charge la conversion d'un document PDF en un fichier texte en suivant les étapes suivantes :

1. Créer le chemin des fichiers d'entrée et de sortie
1. Créer une instance de la façade d'extraction PDF avec [extractor_create](https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)
1. Lier le fichier PDF à l'extracteur avec [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)
1. Extraire le texte du fichier PDF en utilisant [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)
1. Écrire le texte extrait dans le fichier de sortie
1. Enregistrer le PDF de sortie avec la méthode 'document.save'.

Le snippet de code ci-dessous montre comment convertir une image JPG en PDF en utilisant Python via C++ :

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Création du chemin du répertoire de données
    dataDir = os.path.join(os.getcwd(), "samples")

    # Création du chemin du fichier d'entrée
    input_file = os.path.join(dataDir, "sample.pdf")

    # Création du chemin du fichier de sortie
    output_file = os.path.join(dataDir, "results", "pdf-to-txt.txt")

    # Création d'une instance de la façade d'extraction PDF
    extactor = apCore.facades_pdf_extractor_create()

    # Liaison du fichier PDF à l'extracteur
    apCore.facades_facade_bind_pdf(extactor, input_file)

    # Extraction du texte du fichier PDF
    text = apCore.facades_pdf_extractor_extract_text(extactor)

    # Écriture du texte extrait dans le fichier de sortie
    with open(output_file, 'w') as f:
        f.write(text)
```