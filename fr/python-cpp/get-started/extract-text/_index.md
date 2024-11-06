---
title: Extraire du texte d'un PDF en utilisant Python
linktitle: Extraire du texte d'un PDF
type: docs
weight: 10
url: fr/python-cpp/extract-text/
description: Cette section décrit comment extraire du texte d'un document PDF en utilisant une bibliothèque Python.
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire du texte de toutes les pages du document PDF

Extraire du texte d'un PDF n'est pas facile. Peu de lecteurs PDF peuvent extraire du texte à partir d'images PDF ou de PDF scannés. Mais l'outil **Aspose.PDF pour Python via C++** vous permet d'extraire facilement du texte de tout fichier PDF.

Consultez l'extrait de code et suivez les étapes pour extraire du texte de votre PDF :

1. Importez la bibliothèque Aspose.PDF pour Python
2. Créez un nouvel objet extracteur, qui est utilisé pour extraire du texte et des images des documents PDF.
3. Liez l'objet extracteur à un fichier PDF, qui est la source de l'extraction.
4. Extrayez tout le texte du document PDF et mettez-le dans une variable.

1. Faites n'importe quoi, imprimez le texte extrait sur la console, recherchez certains fragments, etc.

```python
from AsposePdfPython import *

extactor = Extract()
extractor_bind_pdf(extactor,"blank_pdf_document.pdf")
text = extractor_extract_text(extactor)

print(text)
```