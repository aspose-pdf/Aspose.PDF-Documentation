---
title: Comment Fusionner des PDF en utilisant Python via C++
linktitle: Fusionner des fichiers PDF
type: docs
weight: 10
url: /fr/python-cpp/merge-pdf-documents/
description: Cette page explique comment fusionner des documents PDF en un seul fichier PDF avec Python.
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Fusionner ou combiner plusieurs PDF en un seul PDF en Python via C++

En utilisant Python et une bibliothèque C++ par Aspose, vous pouvez fusionner efficacement plusieurs fichiers PDF en un seul PDF avec facilité.

Pour concaténer deux fichiers PDF :

1. Ouvrir le premier document
1. Puis ajouter les pages du second document au premier
1. Enregistrer le fichier de sortie concaténé avec la méthode 'document.save'.

Le code suivant montre comment concaténer des fichiers PDF.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample0.pdf")
    output_file = os.path.join(dataDir , "results", "concatenated-files.pdf")

    # Ouvrir le premier document
    document1 = apw.Document(inputFile)
    document2 = apw.Document(inputFile)

    # Ajouter les pages du second document au premier
    document1.pages.add(document2.pages)

    # Enregistrer le fichier de sortie concaténé
    document1.save(output_file)
```