---
title: Faire Pivoter les Pages PDF en Utilisant Python via C++
linktitle: Faire Pivoter les Pages PDF
type: docs
weight: 20
url: /fr/python-cpp/rotate-pages/
description: Ce sujet décrit comment faire pivoter l'orientation des pages dans un fichier PDF existant par programmation avec Python via C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Parfois, les pages PDF peuvent avoir une orientation incorrecte en raison de problèmes de numérisation ou de création. Faire pivoter les pages garantit qu'elles sont affichées dans la bonne orientation pour une lecture et une visualisation plus faciles. Faire pivoter les pages PDF aide à maintenir une expérience de visualisation cohérente sur différents appareils et plateformes.

Faire pivoter les pages PDF peut faciliter les tâches d'édition telles que l'ajout d'annotations, de commentaires ou de signatures. En faisant pivoter les pages à l'orientation désirée, vous pouvez rendre les processus d'édition et de révision plus efficaces.

De plus, lors de l'impression de documents PDF, il est important de s'assurer que les pages sont orientées correctement pour éviter les problèmes de désalignement ou de rognage.
 Faire pivoter les pages selon les besoins avant l'impression aide à optimiser le résultat de l'impression et garantit que le contenu est affiché comme prévu.  
Faire pivoter les pages PDF est une fonctionnalité utile qui aide à améliorer la lisibilité, la cohérence et la présentation des documents dans divers contextes et à diverses fins.

Ce sujet décrit comment mettre à jour ou modifier l'orientation des pages dans un fichier PDF existant de manière programmatique avec Python.

## Changer l'orientation de la page

Aspose.PDF pour Python via C++ prend en charge de grandes fonctionnalités comme le changement de l'orientation de la page

1. Créer un objet document à partir du fichier d'entrée
1. Obtenez la collection de pages du document en utilisant 'apCore.document_get_pages'
1. Obtenez la première page de la collection de pages avec 'apCore.page_collection_get_page'
1. Faire pivoter la page de 90 degrés dans le sens des aiguilles d'une montre en utilisant 'apCore.page_set_rotate'
1. Enregistrez le document modifié dans le fichier de sortie avec la méthode 'document.save'

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Création d'un chemin vers le répertoire contenant les fichiers d'exemple
    dataDir = os.path.join(os.getcwd(), "samples")

    # Création des chemins vers les fichiers d'entrée et de sortie
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "rotated_document.pdf")

    # Création d'un objet document en chargeant le fichier d'entrée
    doc = apCore.document_create_from_file(inputFile)

    # Obtention de la collection de pages dans le document
    pages = apCore.document_get_pages(doc)

    # Obtention de la première page de la collection
    page = apCore.page_collection_get_page(pages, 1)

    # Rotation de la page de 90 degrés dans le sens des aiguilles d'une montre
    apCore.page_set_rotate(page, apCore.Rotation(apCore.on90))

    # Enregistrement du document modifié dans le fichier de sortie
    apCore.document_save(doc, output_file)

    # Fermeture du gestionnaire de document pour libérer des ressources
    apCore.close_handle(doc)
```