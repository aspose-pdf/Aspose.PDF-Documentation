---

title: Définir la Taille du PDF en utilisant Python via C++
linktitle: Définir la Taille du PDF
type: docs
weight: 30
url: /python-cpp/get-and-set-page-properties/
description: Cette section montre comment obtenir ou définir les propriétés de page du PDF telles que la taille du document en utilisant Python via C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Définir la Taille du fichier PDF

Aspose.PDF pour Python via C++ vous permet de lire et de définir les propriétés des pages dans un fichier PDF dans vos applications Python.

Le prochain extrait de code ouvre un fichier PDF, redimensionne la première page en ajustant la **zone de rognage** (la zone de rognage est la taille de "page" à laquelle votre document PDF est affiché dans Adobe Acrobat), et enregistre le document modifié dans un nouveau fichier.

1. Créez un objet document à partir du fichier d'entrée
1. Obtenez la collection de pages du document en utilisant [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/)

1. Obtenez la première page de la collection de pages avec [page_collection_get_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_get_page/)
1. Obtenez le rectangle de la boîte de recadrage de la page en utilisant [page_get_rectangle](https://reference.aspose.com/pdf/python-cpp/core/page_get_rectangle/)
1. Calculez les nouvelles coordonnées pour la boîte de recadrage
1. Mettez à jour les coordonnées de la boîte de recadrage avec les nouvelles valeurs
1. Enregistrez le document modifié dans le fichier de sortie avec la méthode 'document.save'

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Obtenez le répertoire de travail actuel et créez le chemin vers le répertoire "samples"
    dataDir = os.path.join(os.getcwd(), "samples")

    # Créez les chemins des fichiers d'entrée et de sortie
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "resized_document.pdf")

    # Créez un objet document à partir du fichier d'entrée
    doc = apCore.document_create_from_file(inputFile)

    # Obtenez la collection de pages du document
    pages = apCore.document_get_pages(doc)

    # Obtenez la première page de la collection de pages
    page = apCore.page_collection_get_page(pages, 1)

    # Obtenez le rectangle de la boîte de recadrage de la page
    crop_box = apCore.page_get_rectangle(page)

    # Calculez les nouvelles coordonnées pour la boîte de recadrage
    LLX = apCore.rectangle_get_LLX(crop_box) + 10
    LLY = apCore.rectangle_get_LLY(crop_box) + 10
    URX = apCore.rectangle_get_URX(crop_box) - 10
    URY = apCore.rectangle_get_URY(crop_box) - 10

    # Mettez à jour les coordonnées de la boîte de recadrage avec les nouvelles valeurs
    apCore.rectangle_set_LLX(crop_box, LLX)
    apCore.rectangle_set_LLY(crop_box, LLY)
    apCore.rectangle_set_URX(crop_box, URX)
    apCore.rectangle_set_URY(crop_box, URY)

    # Enregistrez le document modifié dans le fichier de sortie
    apCore.document_save(doc, output_file)

    # Fermez le handle du document
    apCore.close_handle(doc)
```