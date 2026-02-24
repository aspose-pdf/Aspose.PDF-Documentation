---
title: Trabajar con capas PDF usando Python
linktitle: Trabajar con capas PDF
type: docs
weight: 50
url: /es/python-net/working-with-pdf-layers/
description: La siguiente tarea explica cómo bloquear una capa PDF, extraer elementos de capas PDF, aplanar un PDF con capas y combinar todas las capas dentro del PDF en una sola.
lastmod: "2025-11-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manipular las capas PDF
Abstract: Esta guía ofrece una visión completa de cómo gestionar y manipular capas PDF usando la biblioteca Aspose.PDF para Python a través de .NET. Las capas PDF —también conocidas como Grupos de Contenido Opcional (OCG, por sus siglas en inglés)— permiten organizar el contenido en componentes visuales independientes que pueden activarse o desactivarse.
---

Las capas PDF son una forma poderosa de organizar y presentar contenido de manera flexible dentro de un único archivo PDF, permitiendo a los usuarios mostrar u ocultar diferentes partes según sus necesidades.

Con **Aspose.PDF para Python a través de .NET**, puedes:

- Bloquear/Desbloquear capas para controlar la visibilidad.
- Extraer capas en archivos o flujos separados.
- Aplanar capas para hacerlas permanentes.
- Combinar capas en una única capa unificada.

## Añadir capas a PDF

Este ejemplo muestra cómo crear y añadir múltiples capas a un documento PDF usando Aspose.PDF para Python a través de .NET. Cada capa contiene contenido gráfico separado, como líneas de colores, que pueden activarse o desactivarse en visores PDF que soportan capas.

1. Crear un nuevo documento PDF y añadir una página.
1. Crear y añadir la capa roja.
1. Crear y añadir la capa verde.
1. Crear y añadir la capa azul.
1. Guardar el documento PDF.

El PDF resultante contendrá tres capas separadas: una línea roja, una línea verde y una línea azul. Cada una puede activarse o desactivarse en lectores PDF que soportan contenido en capas.

```python

import aspose.pdf as ap
from os import path

def add_colored_layers(outfile: str, data_dir: str) -> None:
    """
    Creates a PDF with three layers (Red, Green, Blue lines).
    
    Args:
        outfile (str): Name of the output PDF file.
        data_dir (str): Directory path to save the file.
    """
    path_outfile = path.join(data_dir, outfile)

    try:
        # Create a new PDF document and add a blank page
        document = ap.Document()
        page = document.pages.add()

        # Helper function to add a colored line layer
        def add_layer(layer_id: str, layer_name: str, color: tuple, y_position: int):
            layer = ap.Layer(layer_id, layer_name)
            layer.contents.append(ap.operators.SetRGBColorStroke(*color))
            layer.contents.append(ap.operators.MoveTo(500, y_position))
            layer.contents.append(ap.operators.LineTo(400, y_position))
            layer.contents.append(ap.operators.Stroke())
            page.layers.append(layer)

        # Add Red, Green, and Blue layers
        add_layer("oc1", "Red Line", (1, 0, 0), 700)
        add_layer("oc2", "Green Line", (0, 1, 0), 750)
        add_layer("oc3", "Blue Line", (0, 0, 1), 800)

        # Save the document
        document.save(path_outfile)
        print(f"\nLayers added successfully.\nFile saved at: {path_outfile}")

    except Exception as e:
        print(f"Error adding layers: {e}")
```

## Bloquear una capa PDF

Con Aspose.PDF para Python a través de .NET puedes abrir un PDF, bloquear una capa específica en la primera página y guardar el documento con los cambios.

Este ejemplo muestra cómo bloquear una capa (Grupo de Contenido Opcional, OCG) en un documento PDF usando Aspose.PDF para Python a través de .NET. Bloquear impide que los usuarios cambien la visibilidad de la capa en un visor PDF, asegurando que el contenido permanezca siempre visible (o oculto) según lo definido por el documento.

Métodos y propiedades disponibles:

- layer.lock() – Bloquea la capa.
- layer.unlock() – Desbloquea la capa.
- layer.locked – Devuelve el estado de bloqueo actual.

1. Abrir el documento PDF.
1. Acceder a la primera página del PDF.
1. Verificar si la página tiene capas.
1. Obtener la primera capa y bloquearla.
1. Guardar el PDF actualizado.

Si el PDF contiene capas, la primera capa se bloqueará, garantizando que su estado de visibilidad no pueda ser modificado por el usuario. Si no se encuentran capas, se imprimirá un mensaje.

```python

import aspose.pdf as ap
from os import path

def lock_layer(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        layer = page.layers[0]

        # Lock the layer
        layer.lock()

        # Save updated PDF
        document.save(path_outfile)
```

## Extraer elementos de capas PDF

Este ejemplo utiliza la biblioteca Aspose.PDF para Python a través de .NET para extraer capas individuales de la primera página de un documento PDF y guardar cada capa como un archivo PDF separado.

Para crear un nuevo PDF a partir de una capa, se puede usar el siguiente fragmento de código:

1. Cargar el documento PDF. El PDF de entrada se carga en un objeto Aspose.PDF.Document.
1. Acceder a las capas en la página 1. El script recupera todas las capas de la primera página usando document.pages[1].layers.
1. Verificar la existencia de capas. Si no se encuentran capas, se imprime un mensaje y la función termina.
1. Iterar y guardar cada capa.

```python

import aspose.pdf as ap
from os import path

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF
        for layer in layers:
            layer.save(path_outfile)
```

Es posible extraer elementos de capas PDF y guardarlos en un nuevo flujo de archivo PDF:

```python

import aspose.pdf as ap
from os import path

def save_layers_to_stream(path_infile, output_stream):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        for layer in layers:
            layer.save(output_stream)
```

## Aplanar un PDF con capas

Este script usa Aspose.PDF para Python a través de .NET para aplanar todas las capas de la primera página de un documento PDF. El aplanado combina el contenido visual de cada capa en una única capa unificada, facilitando la impresión, el intercambio o el archivado sin perder fidelidad visual ni datos específicos de las capas.

1. Cargar el documento PDF. El PDF de entrada se carga en un objeto Aspose.PDF.Document.
1. Acceder a las capas en la página 1. El script recupera todas las capas de la primera página usando document.pages[1].layers.
1. Verificar la presencia de capas. Si no se encuentran capas, se imprime un mensaje y la función termina.
1. Aplanar cada capa. Cada capa se aplana usando layer.flatten(True), lo que fusiona su contenido en la página.
1. Guardar el documento modificado.

```python

import aspose.pdf as ap
from os import path

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if not page.layers:
            print("No layers found in the document.")
            return
        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

## Fusionar todas las capas dentro del PDF en una sola

Este fragmento de código usa Aspose.PDF para combinar todas las capas de la primera página de un PDF en una capa unificada con un nombre personalizado.

1. Cargar el documento PDF. El PDF se carga en un objeto Aspose.PDF.Document.
1. Acceder a la página y sus capas. Se selecciona la primera página y se recuperan sus capas.
1. Verificar la existencia de capas. Si no existen capas, se imprime un mensaje y el proceso termina.
1. Definir el nuevo nombre de capa. Se especifica un nuevo nombre de capa ("LayerNew") para el resultado combinado.
1. Combinar capas. Si se proporciona un ID de grupo de contenido opcional, se usa en la combinación. De lo contrario, las capas se combinan usando solo el nuevo nombre.
1. Guardar el documento

```python

import aspose.pdf as ap
from os import path

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
