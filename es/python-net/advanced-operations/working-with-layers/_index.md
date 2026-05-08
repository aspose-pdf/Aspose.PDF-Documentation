---
title: Trabajar con capas PDF usando Python
linktitle: Trabajar con capas PDF
type: docs
weight: 50
url: /es/python-net/working-with-pdf-layers/
description: Aprenda cómo agregar, bloquear, extraer, aplanar y combinar capas PDF en Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Administre capas PDF con Python
Abstract: Este artículo explica cómo trabajar con capas PDF (Grupos de Contenido Opcional) usando Aspose.PDF for Python via .NET. Aprenda cómo agregar capas, bloquear la visibilidad de capas, extraer el contenido de la capa, aplanar el contenido de capas y combinar capas en una.
---

Las capas de PDF, también llamadas Grupos de Contenido Opcional (OCGs), le permiten organizar el contenido en grupos visuales separados que pueden mostrarse u ocultarse en visores de PDF compatibles. En Aspose.PDF, las operaciones de capa se construyen alrededor del [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) API.

Con Aspose.PDF for Python via .NET, puedes:

- Agregar varias capas a una página.
- Bloquee y desbloquee capas para controlar el comportamiento de visibilidad.
- Extraer capas en archivos o flujos separados.
- Aplanar contenido en capas en la página.
- Combinar varias capas en una capa.

## Agregar capas a un PDF

Este ejemplo crea un PDF con tres capas. Utiliza un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), agrega un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/), y añade [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) objetos a esa página.

1. Crear un nuevo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) y agregar un [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Crear y agregar la capa roja.
1. Crear y agregar la capa verde.
1. Crear y agregar la capa azul.
1. Guarde el documento PDF.

El PDF resultante contendrá tres capas separadas: una línea roja, una línea verde y una línea azul. Cada una puede activarse o desactivarse en los lectores de PDF que admiten contenido en capas.

```python
import aspose.pdf as ap

def add_layers(outfile: str) -> None:
    document = ap.Document()
    page = document.pages.add()

    # Red layer
    layer = ap.Layer("oc1", "Red Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(1, 0, 0))
    layer.contents.append(ap.operators.MoveTo(500, 700))
    layer.contents.append(ap.operators.LineTo(400, 700))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Green layer
    layer = ap.Layer("oc2", "Green Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 1, 0))
    layer.contents.append(ap.operators.MoveTo(500, 750))
    layer.contents.append(ap.operators.LineTo(400, 750))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Blue layer
    layer = ap.Layer("oc3", "Blue Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 0, 1))
    layer.contents.append(ap.operators.MoveTo(500, 800))
    layer.contents.append(ap.operators.LineTo(400, 800))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    document.save(outfile)
    print(f"Layers added successfully. File saved at {outfile}")
```

## Bloquear una capa PDF

Este ejemplo abre un PDF, bloquea una capa específica en la primera página y guarda el archivo actualizado.

Bloquear una capa evita que los usuarios cambien el estado de visibilidad de esa capa en los visores PDF compatibles. Las capas se acceden desde una página y se gestionan a través de la colección de capas de la página.

Métodos y propiedad disponibles:

- [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) bloquea la capa.
- [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) desbloquea la capa.
- [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties) devuelve el estado actual del bloqueo.

1. Abra el documento PDF.
1. Acceda a la primera página del PDF.
1. Verifique si la página tiene capas.
1. Obtén la primera capa y bloquéala.
1. Guarda el PDF actualizado.

Si el PDF contiene capas, la primera capa se bloqueará, garantizando que su estado de visibilidad no pueda ser cambiado por el usuario. Si no se encuentran capas, se imprimirá un mensaje en su lugar.

```python
import aspose.pdf as ap

def lock_layer(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) > 0:
        layer = page.layers[0]
        layer.lock()
        document.save(outfile)
        print(f"Layer locked successfully. File saved at {outfile}")
    else:
        print("No layers found in the document.")
```

## Extraer elementos de capa PDF

Este ejemplo usa la biblioteca Aspose.PDF for Python via .NET para extraer capas individuales de la primera página de un documento PDF y guardar cada capa como un archivo PDF separado mediante [`Layer.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

Para crear un nuevo PDF a partir de una capa, se puede usar el siguiente fragmento de código:

1. Cargar el PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Acceder a capas en la página 1 mediante [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Verifique si existen capas.
1. Iterar sobre las capas y guardar cada una.

```python
import aspose.pdf as ap

def extract_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    index = 1
    for layer in layers:
        output_file = outfile.replace(".pdf", f"{index}.pdf")
        layer.save(output_file)
        print(f"Layer {index} saved to {output_file}")
        index += 1
```

Es posible extraer los elementos de capa de PDF y guardarlos en una nueva secuencia de archivo PDF:

```python
from io import FileIO
import aspose.pdf as ap

def extract_layers_stream(infile: str, outfile: str) -> None:
    document = ap.Document(infile)

    if len(document.pages[1].layers) == 0:
        print("No layers found in the document.")
        return

    layer = document.pages[1].layers[0]

    with FileIO(outfile, "wb") as output_layer:
        layer.save(output_layer)
    print(f"Layer extracted to stream: {outfile}")
```

## Aplanar un PDF en capas

Este script usa Aspose.PDF for Python via .NET para aplanar todas las capas en la primera página de un documento PDF. El aplanado combina el contenido visual de cada capa en una capa unificada, facilitando la impresión, el intercambio o el archivado sin perder la fidelidad visual ni los datos específicos de la capa. La operación se realiza con [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

1. Cargue el documento PDF.
1. Acceder a las capas en la página 1.
1. Verifique si existen capas.
1. Aplana cada capa con `layer.flatten(True)`.
1. Guarda el documento modificado.

```python
import aspose.pdf as ap

def flatten_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    for layer in layers:
        layer.flatten(True)

    document.save(outfile)
    print(f"Layers flattened successfully. File saved at {outfile}")
```

## Fusionar todas las capas de un PDF en una

Este fragmento de código utiliza Aspose.PDF para combinar todas las capas de la primera página de un PDF en una única capa unificada con un nombre personalizado mediante [`Page.merge_layers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods).

1. Cargue el documento PDF.
1. Acceda a la página 1 y recupere sus capas.
1. Verifique si existen capas.
1. Definir un nuevo nombre de capa.
1. Fusiona las capas en una.
1. Guarde el documento.

```python
import aspose.pdf as ap

def merge_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) == 0:
        print("No layers found in the document.")
        return

    new_layer_name = "LayerNew"
    page.merge_layers(new_layer_name)
    document.save(outfile)
    print(f"Layers merged successfully. File saved at {outfile}")
```

## Temas de capa relacionados

- [Trabajar con páginas PDF en Python](/pdf/es/python-net/working-with-pages/)
- [Trabajar con tablas en PDF usando Python](/pdf/es/python-net/working-with-tables/)
- [Agregar páginas PDF en Python](/pdf/es/python-net/add-pages/)
