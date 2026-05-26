---
title: Extraire le contenu balisé des PDF en Python
linktitle: Extraire le contenu balisé
type: docs
weight: 20
url: /fr/python-net/extract-tagged-content-from-tagged-pdfs/
description: Découvrez comment extraire le contenu Tagged PDF en Python avec Aspose.PDF for Python via .NET, y compris l'accès au contenu balisé, à la structure racine et aux éléments de structure enfants.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Dans cet article, vous apprendrez comment extraire le contenu balisé des documents PDF en utilisant Python.

Utilisez ces exemples lorsque vous devez inspecter un PDF balisé, lire l'arbre de structure logique ou valider que les éléments de structure ont été créés correctement pour les flux de travail d'accessibilité.

## Obtenir le contenu du PDF balisé

Afin d'obtenir le contenu d'un Document PDF avec du texte balisé, Aspose.PDF propose [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) propriété de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.

Créez un document PDF avancé, entièrement balisé, avec une table des matières structurée et hiérarchique (TOC):

1. Créez un nouvel objet Document.
1. Accédez à la propriété tagged_content.
1. Définissez le titre du document en utilisant 'set_title()'.
1. Définissez la langue du document en utilisant 'set_language()'.
1. Enregistrez le document.

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

# region Extract Tagged Content from PDF
def get_tagged_content(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Work with Tagged PDF content
        # Set Title and Language for Document
        tagged_content.set_title("Simple Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Save Tagged PDF Document
        document.save(outfile)
```

## Obtention de la structure racine

Les Tagged PDFs contiennent un arbre de structure logique qui définit la structure sémantique du document. Le StructTreeRoot représente la racine de cet arbre logique, tandis que le RootElement fournit une interface pour interagir avec l'élément de structure de niveau supérieur du document.

Le fragment de code suivant montre comment obtenir la structure racine d'un Tagged PDF Document :

1. Créez un nouveau document PDF balisé.
1. Accédez au contenu balisé et définissez les métadonnées.
1. Accédez à StructTreeRoot et RootElement.
1. Enregistrez le PDF balisé.

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

def get_root_structure(outfile):

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Properties StructTreeRootElement and RootElement are used for access to
        # StructTreeRoot object of pdf document and to root structure element (Document structure element).
        struct_tree_root_element = tagged_content.struct_tree_root_element
        root_element = tagged_content.root_element

        print(f"StructTreeRootElement: {struct_tree_root_element}")
        print(f"RootElement: {root_element}")

        # Save Tagged PDF Document
        document.save(outfile)
```

## Accéder aux éléments enfants

Les PDFs balisés contiennent un arbre de structure logique qui définit la hiérarchie sémantique du document (titres, paragraphes, formulaires, listes, etc.). Accéder à ces éléments de structure et les modifier vous permet de :

- Inspecter les métadonnées telles que le titre, la langue, actual_text et les propriétés liées à l'accessibilité
- Mettre à jour les propriétés pour améliorer l'accessibilité ou la localisation
- Ajuster programmatiquement la structure logique du document pour la conformité PDF/UA

 Le fragment de code suivant montre comment accéder aux éléments enfants d'un Tagged PDF Document:

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

def access_child_elements(infile, outfile):

    # Open PDF Document
    with ap.Document(infile) as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Access to root element(s)
        element_list = tagged_content.struct_tree_root_element.child_elements

        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = cast(ap.logicalstructure.StructureElement, element)
                # Get properties
                print(
                    "StructureElement properties - "
                    f"title: {structure_element.title}, "
                    f"language: {structure_element.language}, "
                    f"actual_text: {structure_element.actual_text}, "
                    f"expansion_text: {structure_element.expansion_text}, "
                    f"alternative_text: {structure_element.alternative_text}"
                )

        # Access to child elements of first element in root element
        element_list = tagged_content.root_element.child_elements[1].child_elements
        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = element

                # Set properties
                structure_element.title = "title"
                structure_element.language = "fr-FR"
                structure_element.actual_text = "actual text"
                structure_element.expansion_text = "exp"
                structure_element.alternative_text = "alt"

        # Save Tagged PDF Document
        document.save(outfile)
```

## Sujets liés aux PDF balisés

- [Créer Tagged PDF](/pdf/fr/python-net/create-tagged-pdf/) pour créer des documents balisés accessibles avant d'inspecter leur structure.
- [Définir les propriétés des éléments de structure](/pdf/fr/python-net/setting-structure-elements-properties/) mettre à jour les propriétés sémantiques après l'extraction des éléments de structure.
- [Travailler avec la Table dans Tagged PDFs](/pdf/fr/python-net/working-with-table-in-tagged-pdfs/) pour les flux de travail d'accessibilité des tables balisées.