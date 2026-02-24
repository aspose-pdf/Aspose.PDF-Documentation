---
title: Extraer contenido etiquetado de PDF
linktitle: Extraer contenido etiquetado
type: docs
weight: 20
url: /es/python-net/extract-tagged-content-from-tagged-pdfs/
description: Este artículo explica cómo extraer contenido etiquetado de un documento PDF usando Aspose.PDF para Python a través de .NET
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

En este artículo aprenderá cómo extraer contenido etiquetado de un documento PDF usando Python.

## Obtención de contenido PDF etiquetado

Para obtener el contenido de un documento PDF con texto etiquetado, Aspose.PDF ofrece la propiedad [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

El siguiente fragmento de código muestra cómo obtener el contenido de un documento PDF con texto etiquetado:

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

## Obtención de la estructura raíz

Para obtener la estructura raíz de un documento PDF etiquetado, Aspose.PDF ofrece la propiedad [struct_tree_root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties) de la interfaz [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) y la propiedad [root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties).

El siguiente fragmento de código muestra cómo obtener la estructura raíz de un documento PDF etiquetado:

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

## Accediendo a los elementos hijos

Para acceder a los elementos hijos de un documento PDF etiquetado, Aspose.PDF ofrece la clase [ElementList](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/elementlist/). El siguiente fragmento de código muestra cómo acceder a los elementos hijos de un documento PDF etiquetado:

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
