---
title: Extraire le contenu balisé d'un PDF
linktitle: Extraire le contenu balisé
type: docs
weight: 20
url: /fr/python-net/extract-tagged-content-from-tagged-pdfs/
description: Cet article explique comment extraire le contenu balisé d'un document PDF à l'aide d'Aspose.PDF pour Python via .NET
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

Dans cet article, vous apprendrez comment extraire le contenu balisé d'un document PDF en utilisant Python.

## Obtention du contenu PDF balisé

Afin d'obtenir le contenu d'un document PDF avec du texte balisé, Aspose.PDF propose la propriété [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) de la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Le code suivant montre comment obtenir le contenu d'un document PDF avec du texte balisé :

```python

    import aspose.pdf as ap

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Work with Tagged PDF content
        # Set Title and Language for Document
        tagged_content.set_title("Simple Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Save Tagged PDF Document
        document.save(path_outfile)
```

## Obtention de la structure racine

Afin d'obtenir la structure racine d'un document PDF balisé, Aspose.PDF propose la propriété [struct_tree_root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties) de l'interface [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) ainsi que [root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties).

Le code suivant montre comment obtenir la structure racine d'un document PDF balisé :

```python

    import aspose.pdf as ap

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
```

## Accès aux éléments enfants

Afin d'accéder aux éléments enfants d'un document PDF balisé, Aspose.PDF propose la classe [ElementList](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/elementlist/). Le code suivant montre comment accéder aux éléments enfants d'un document PDF balisé :

```python

    import aspose.pdf as ap
    from aspose.pycore import *

    # Open PDF Document
    with ap.Document(path_infile) as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Access to root element(s)
        element_list = tagged_content.struct_tree_root_element.child_elements

        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = cast(ap.logical_structure.StructureElement, element)

                # Get properties
                title = structure_element.title
                language = structure_element.language
                actual_text = structure_element.actual_text
                expansion_text = structure_element.expansion_text
                alternative_text = structure_element.alternative_text

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
        document.save(path_outfile)
```
