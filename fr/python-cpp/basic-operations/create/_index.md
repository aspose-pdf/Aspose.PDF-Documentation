---
title: Créer un document PDF
linktitle: Créer un PDF
type: docs
weight: 10
url: fr/python-cpp/create-document/
description: Cette page décrit comment créer un document PDF à partir de zéro avec la bibliothèque Aspose.PDF pour Python via C++.
---

Pour les développeurs, il existe de nombreux scénarios où il devient nécessaire de générer des fichiers PDF de manière programmatique. Vous pourriez avoir besoin de générer des rapports PDF et d'autres fichiers PDF dans votre logiciel. Il est plutôt long et inefficace d'écrire votre propre code et vos propres fonctions à partir de zéro. Pour créer un fichier PDF avec Python, il existe une meilleure solution - **Aspose.PDF pour Python via C++**.

## Créer un fichier PDF avec Python

Pour créer un fichier PDF avec Python, les étapes suivantes peuvent être utilisées.

* importez toutes les classes et méthodes de la bibliothèque Aspose.PDF pour Python via C++.
* Créez un nouvel objet Document qui représente un document PDF vide en utilisant [document_create](https://reference.aspose.com/pdf/python-cpp/core/document_create/)

* Obtenez l'objet [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/) qui contient toutes les pages du document.
 * Ajoute une nouvelle page à la fin de la collection de pages [page_collection_add_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_add_page/) et retourne l'objet Page qui représente la page ajoutée.
* Enregistre le document dans un fichier avec le nom spécifié dans le répertoire de travail actuel.
* Ferme le handle du document et libère toutes les ressources associées.

```python

    from AsposePDFPython import *

    doc = document_create()
    pages = document_get_pages(doc)
    page = page_collection_add_page(pages)
    document_save(doc, "blank_pdf_document.pdf")
    close_handle(doc)
```


## Créer un fichier PDF basé sur le DOM

```python

    from AsposePDFPythonWrappers import *

    doc = Document()
    page = doc.pages.add()
    doc.save("blank_pdf_document1.pdf")
```