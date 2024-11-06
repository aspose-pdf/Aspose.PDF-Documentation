---
title: Ajouter des Pages dans un PDF avec Python via C++
linktitle: Ajouter des Pages
type: docs
weight: 10
url: fr/python-cpp/add-pages/
description: Cet article explique comment insérer (ajouter) une page à l'emplacement souhaité dans un fichier PDF en Python en utilisant C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Insérer une Page Vide dans un Fichier PDF à l'Emplacement Souhaité

Le fragment de code ouvre un document PDF, y ajoute une page vide et enregistre le document modifié en tant que nouveau fichier PDF.

Pour insérer une page vide dans un fichier PDF :

1. Ouvrez le document PDF
1. Ajoutez une nouvelle page vierge au document
1. Enregistrez le document modifié dans le fichier de sortie avec la méthode 'document.save'

Le fragment de code suivant vous montre comment insérer une page dans un fichier PDF :

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Définir le chemin du répertoire où se trouvent les fichiers PDF d'exemple
    dataDir = os.path.join(os.getcwd(), "samples")

    # Définir le chemin du fichier d'entrée
    input_file = os.path.join(dataDir, "sample0.pdf")

    # Définir le chemin du fichier de sortie
    output_file = os.path.join(dataDir, "results", "blank_pdf_document.pdf")

    # Ouvrir le document PDF
    document = apw.Document(input_file)

    # Ajouter une nouvelle page vierge au document
    document.pages.add()

    # Enregistrer le document modifié dans le fichier de sortie
    document.save(output_file)
```