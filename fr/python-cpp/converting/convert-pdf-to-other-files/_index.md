---
title: Convertir PDF en Texte en Python
linktitle: Convertir PDF en d'autres formats 
type: docs
weight: 90
url: /fr/python-cpp/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: convertir, PDF, EPUB, LaTex, Texte, XPS, Python
description: Ce sujet vous montre comment convertir un fichier PDF en d'autres formats de fichiers comme le texte en utilisant Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF en Texte

**Aspose.PDF pour Python** prend en charge la conversion de l'ensemble du document PDF et d'une seule page en un fichier texte.

### Convertir un document PDF en fichier texte

Vous pouvez convertir un document PDF en fichier TXT en utilisant la classe 'TextDevice'.

1. Créer le chemin d'accès pour les fichiers d'entrée et de sortie
1. Créer une instance de la façade d'extraction PDF avec [extractor_create]
(https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)
1. Lier le fichier PDF à l'extracteur avec [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)

1. Extraction du texte du fichier PDF en utilisant [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)
1. Écriture du texte extrait dans le fichier de sortie
1. Enregistrer le PDF de sortie avec la méthode 'document.save'.

Le snippet de code suivant explique comment extraire les textes de toutes les pages.

```python

    from AsposePdfPython import *

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"

    extactor = extractor_create()
    extractor_bind_pdf(extactor,input_pdf)
    text = extractor_extract_text(extactor)

    with open(output_pdf, 'w') as f:
        f.write(text)
```