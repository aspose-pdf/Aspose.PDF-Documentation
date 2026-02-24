---
title: Trabajando con capas PDF usando Python
linktitle: Trabajando con capas PDF
type: docs
weight: 50
url: /es/python-net/work-with-pdf-layers/
description: Este artículo explica cómo bloquear una capa PDF, extraer elementos de capa PDF, aplanar un PDF con capas y combinar todas las capas dentro de un PDF en una sola.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo gestionar, bloquear, extraer, aplanar y combinar capas PDF en Python
Abstract: Este artículo explica cómo trabajar con capas PDF en Python usando Aspose.PDF para .NET, incluyendo el bloqueo de capas, la extracción de elementos de capa, el aplanado de PDFs con capas y la fusión de capas.
---

Las capas PDF permiten que un documento contenga varios conjuntos de contenido que pueden mostrarse u ocultarse de forma selectiva. Cada capa puede incluir texto, imágenes o gráficos, y los usuarios pueden activarlas o desactivarlas según sea necesario. Las capas son especialmente útiles en documentos complejos donde el contenido debe organizarse o separarse. Los ejemplos a continuación utilizan las APIs [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) y [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) y manipulan objetos [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) a través de la colección `layers` de la página.

## Bloquear una capa PDF

Con Aspose.PDF para Python a través de .NET puedes abrir un PDF (ver [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)), bloquear una [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) específica en la primera [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/), y guardar el documento con los cambios.

Métodos y propiedades disponibles en el objeto [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/):

- `layer.lock()` – Bloquea la capa. (ver [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.unlock()` – Desbloquea la capa. (ver [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.locked` – Devuelve el estado de bloqueo actual. (ver [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties))

1. Abre el documento PDF (ver [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Obtén la primera página usando la colección [`Pages`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) del documento (ver [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)).
1. Selecciona la [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) a bloquear desde `page.layers`.
1. Llama a `layer.lock()` para evitar que los usuarios cambien la visibilidad de la capa.
1. Guarda el documento actualizado usando [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import aspose.pdf as ap

def lock_layer(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        layer = page.layers[0]

        # Lock the layer
        layer.lock()

        # Save updated PDF
        document.save(path_outfile)
```

## Extraer elementos de capa PDF

Aspose.PDF te permite extraer cada [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) de una [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) y guardarla como un archivo PDF separado.

Para crear un nuevo PDF a partir de una capa, se puede usar el siguiente fragmento de código (la colección `layers` se accede a través de `Page.layers`):

```python

import aspose.pdf as ap

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF with a unique filename
        for i, layer in enumerate(layers):
            layer.save(f"{path_outfile}_layer_{i}.pdf")
```

También puedes guardar capas en un flujo:

```python

import aspose.pdf as ap
import io

def save_layers_to_stream(path_infile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        streams = []
        for layer in layers:
            layer_stream = io.BytesIO()
            layer.save(layer_stream)
            layer_stream.seek(0)
            streams.append(layer_stream)
        return streams
```

## Aplanar un PDF con capas

Aplanar hace que una [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) sea permanente en la página, eliminando su capacidad de alternar.

```python

import aspose.pdf as ap

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

El parámetro `cleanup_content_stream` controla si se eliminan los marcadores de grupo de contenido opcional (marcadores OCG). Establecerlo en `False` acelera el aplanado. Consulta el método [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) para más detalles.

## Combinar todas las capas dentro del PDF en una sola

Puedes combinar todas las capas (o algunas específicas) en una nueva [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) única (la API de combinación está en el objeto [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)).

Métodos del objeto [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/):

- `page.merge_layers(new_layer_name)` — combina todas las capas en un nuevo nombre de capa (ver [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).
- `page.merge_layers(new_layer_name, new_optional_content_group_id)` — combina usando un ID de grupo de contenido opcional personalizado (ver [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).

```python

import aspose.pdf as ap

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
