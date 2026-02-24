---
title: Travailler avec les arrière-plans comme artefacts avec Python
linktitle: Ajout d'arrière-plans
type: docs
weight: 20
url: /fr/python-net/add-backgrounds/
description: Ajoutez une image d'arrière-plan à votre fichier PDF avec Python. Utilisez la classe BackgroundArtifact.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter un arrière-plan à un PDF avec Python
Abstract: Cet article traite de l'utilisation d'images d'arrière-plan dans les documents PDF à l'aide d'Aspose.PDF pour Python via .NET. Il met en avant la possibilité d'ajouter des filigranes ou des designs subtils aux documents en utilisant la classe `BackgroundArtifact`, qui permet l'incorporation d'images d'arrière-plan dans les objets de pages individuels. L'article fournit un exemple de code pratique montrant comment implémenter cette fonctionnalité. Le processus consiste à créer un nouveau document PDF, ajouter une page, créer un objet `BackgroundArtifact`, définir une image d'arrière-plan et ajouter l'artefact d'arrière-plan à la collection d'artefacts de la page. Enfin, le document modifié est enregistré en tant que fichier PDF. Cette technique permet d'améliorer la présentation visuelle des documents PDF.
---

Les images d'arrière-plan peuvent être utilisées pour ajouter un filigrane ou un autre design subtil aux documents. Dans Aspose.PDF pour Python via .NET, chaque document PDF est une collection de pages et chaque page contient une collection d'artefacts. La classe [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) peut être utilisée pour ajouter une image d'arrière-plan à un objet page.

Le fragment de code suivant montre comment ajouter une image d'arrière-plan aux pages PDF en utilisant l'objet BackgroundArtifact avec Python.

```python

import aspose.pdf as ap
import io

def add_background_image(input_image_file, output_pdf):
    # Create a new PDF document
    document = ap.Document()

    # Add a blank page to the document
    page = document.pages.add()

    # Create a BackgroundArtifact object
    background = ap.BackgroundArtifact()

    # Load the image as a binary stream
    with open(input_image_file, "rb") as image_stream:
        background.background_image = image_stream

        # Add the background artifact to the page
        page.artifacts.append(background)

    # Save the resulting PDF
    document.save(output_pdf)
```


