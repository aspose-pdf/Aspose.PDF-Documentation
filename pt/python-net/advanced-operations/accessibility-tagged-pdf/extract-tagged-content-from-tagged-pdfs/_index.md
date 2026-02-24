---
title: Extrair Conteúdo Etiquetado de PDF
linktitle: Extrair Conteúdo Etiquetado
type: docs
weight: 20
url: /pt/python-net/extract-tagged-content-from-tagged-pdfs/
description: Este artigo explica como extrair conteúdo etiquetado de documentos PDF usando Aspose.PDF para Python via .NET
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

Neste artigo, você aprenderá como extrair conteúdo etiquetado de documentos PDF usando Python.

## Obtendo Conteúdo PDF Etiquetado

Para obter o conteúdo de um Documento PDF com Texto Etiquetado, Aspose.PDF oferece a propriedade [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

O trecho de código a seguir mostra como obter o conteúdo de um documento PDF com Texto Etiquetado:

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

## Obtendo Estrutura Raiz

Para obter a estrutura raiz de um Documento PDF Etiquetado, Aspose.PDF oferece a propriedade [struct_tree_root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties) da interface [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) e [root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties).

O trecho de código a seguir mostra como obter a estrutura raiz de um Documento PDF Etiquetado:

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

## Acessando Elementos Filhos

Para acessar elementos filhos de um Documento PDF Etiquetado, Aspose.PDF oferece a classe [ElementList](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/elementlist/). O trecho de código a seguir mostra como acessar os elementos filhos de um Documento PDF Etiquetado:

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
