---
title: Extraer contenido etiquetado de PDFs en Python
linktitle: Extraer contenido etiquetado
type: docs
weight: 20
url: /es/python-net/extract-tagged-content-from-tagged-pdfs/
description: Aprenda a extraer contenido de PDF etiquetados en Python con Aspose.PDF para Python a través de .NET, incluido el acceso al contenido etiquetado, a la estructura raíz y a los elementos secundarios de estructura.
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

En este artículo, aprenderá cómo extraer contenido etiquetado de documentos PDF usando Python.

Utilice estos ejemplos cuando necesite inspeccionar un PDF etiquetado, leer el árbol de estructura lógica o validar que los elementos de estructura se hayan creado correctamente para flujos de trabajo de accesibilidad.

## Obtener contenido de PDF etiquetado

Para obtener el contenido de un documento PDF con texto etiquetado, Aspose.PDF ofrece [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) propiedad de [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase.

Cree un documento PDF avanzado y completamente etiquetado con una Tabla de Contenidos (TOC) estructurada y jerárquica:

1. Crea un nuevo objeto Document.
1. Accede a la propiedad tagged_content.
1. Establece el título del documento usando 'set_title()'.
1. Establece el idioma del documento usando 'set_language()'.
1. Guardar el documento.

```python
import aspose.pdf as ap


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

## Obteniendo la estructura raíz

Los PDF etiquetados contienen un árbol de estructura lógica que define la estructura semántica del documento. El StructTreeRoot representa la raíz de este árbol lógico, mientras que el RootElement proporciona una interfaz para interactuar con el elemento de estructura de nivel superior del documento.

El siguiente fragmento de código muestra cómo obtener la estructura raíz del documento Tagged PDF:

1. Cree un nuevo documento Tagged PDF.
1. Acceda al contenido etiquetado y establezca metadatos.
1. Acceda a StructTreeRoot y RootElement.
1. Guardar el PDF etiquetado.

```python
import aspose.pdf as ap
from aspose.pycore import cast


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

## Accediendo a elementos hijos

Los PDF etiquetados contienen un árbol de estructura lógica que define la jerarquía semántica del documento (títulos, párrafos, formularios, listas, etc.). Acceder y modificar estos elementos de estructura le permite:

- Inspeccionar los metadatos como el título, el idioma, actual_text y las propiedades relacionadas con la accesibilidad
- Actualizar propiedades para mejorar la accesibilidad o la localización
- Ajustar programáticamente la estructura lógica del documento para cumplir con PDF/UA

 El siguiente fragmento de código muestra cómo acceder a los elementos hijos de un documento Tagged PDF:

```python
import aspose.pdf as ap
from aspose.pycore import cast


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

## Temas relacionados de Tagged PDF

- [Crear Tagged PDF](/pdf/es/python-net/create-tagged-pdf/) para crear documentos etiquetados accesibles antes de inspeccionar su estructura.
- [Configurar propiedades de elementos de estructura](/pdf/es/python-net/setting-structure-elements-properties/) para actualizar propiedades semánticas después de extraer elementos de estructura.
- [Trabajar con tablas en PDF etiquetados](/pdf/es/python-net/working-with-table-in-tagged-pdfs/) para flujos de trabajo de accesibilidad con tablas etiquetadas.
