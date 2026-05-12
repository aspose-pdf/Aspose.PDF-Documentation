---
title: Agregar páginas PDF en Python
linktitle: Agregar páginas
type: docs
weight: 10
url: /es/python-net/add-pages/
description: Aprenda cómo agregar o insertar páginas en documentos PDF con Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar o insertar páginas PDF con Python
Abstract: Este artículo explica cómo agregar páginas a archivos PDF usando Aspose.PDF for Python via .NET. Aprende cómo insertar páginas en blanco en posiciones específicas, agregar páginas al final de un documento y importar una página de otro PDF utilizando las APIs Document y PageCollection.
---

Aspose.PDF for Python via .NET proporciona operaciones flexibles a nivel de página para documentos PDF. Puedes gestionar páginas a través de [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) y agregar páginas a un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) en posiciones específicas o al final del archivo.

Utilice esta página cuando necesite insertar nuevas páginas en blanco en un PDF existente o agregar páginas al final de un documento durante los flujos de trabajo de generación.

## Agregar o Insertar páginas en un archivo PDF

Aspose.PDF for Python via .NET admite tanto la inserción de página en un índice específico como la adición de páginas al final de un PDF.

### Insertar una página en blanco en un archivo PDF

Para insertar una página en blanco en un archivo PDF:

1. Abrir un existente [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando métodos apropiados.
1. Inserte una nueva página vacía en un índice específico usando el [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `insert()` método.
1. Guarde lo modificado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) a la ruta de salida deseada.

Inserte una página en blanco en un archivo PDF existente en una posición especificada:

```python
import aspose.pdf as ap

def insert_empty_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### Agregar una página en blanco al final de un archivo PDF

A veces, desea asegurarse de que un documento termine en una página en blanco. Este tema explica cómo insertar una página en blanco al final del documento PDF.

Para insertar una página en blanco al final de un archivo PDF:

1. Abrir un existente [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando métodos apropiados.
1. Agregar una nueva página en blanco al final del documento usando el [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `add()` método.
1. Guardar lo actualizado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

El siguiente fragmento de código le muestra cómo insertar una página vacía al final de un archivo PDF.

```python
import aspose.pdf as ap

def add_empty_page_to_end(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.add()
    document.save(output_file_name)
```

### Agregar una página de otro documento PDF

Con Aspose.PDF for Python via .NET, puedes crear un nuevo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), agrega una página inicial y luego importa una página de otro PDF en ella.

1. Crear un nuevo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Añade un nuevo blanco [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) y escribe algo de texto en él usando [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. Abrir otro existente [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Copiar un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) desde ese documento.
1. Pegar la página copiada en su documento principal usando [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Guarda el archivo combinado.

```python
import aspose.pdf as ap

def add_page_from_another_document(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    document.save(output_file_name)
```

## Temas de página relacionados

- [Trabajar con páginas PDF en Python](/pdf/es/python-net/working-with-pages/)
- [Mover páginas PDF en Python](/pdf/es/python-net/move-pages/)
- [Eliminar páginas PDF en Python](/pdf/es/python-net/delete-pages/)
- [Extraer páginas PDF en Python](/pdf/es/python-net/extract-pages/)
