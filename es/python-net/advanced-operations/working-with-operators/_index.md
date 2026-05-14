---
title: Trabajar con Operadores PDF en Python
linktitle: Trabajando con Operadores
type: docs
weight: 90
url: /es/python-net/working-with-operators/
description: Aprende cómo usar operadores PDF de bajo nivel en Python para una manipulación precisa del flujo de contenido y control gráfico.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Usa operadores PDF de bajo nivel para el control del flujo de contenido en Python
Abstract: Este artículo explica cómo trabajar con operadores PDF de bajo nivel en Aspose.PDF for Python via .NET. Aprenda cómo manipular flujos de contenido directamente, posicionar gráficos con precisión mediante clases de operadores y eliminar objetos dibujados de las páginas PDF en flujos de trabajo de Python.
---

## Introducción a los Operadores PDF y su Uso

Un operador es una palabra clave PDF que especifica alguna acción que debe ejecutarse, como pintar una forma gráfica en la página. Una palabra clave de operador se distingue de un objeto nombrado por la ausencia de un carácter de barra inicial (2Fh). Los operadores solo tienen significado dentro del flujo de contenido.

Un flujo de contenido es un objeto de flujo PDF cuyos datos consisten en instrucciones que describen los elementos gráficos que se deben pintar en una página. Se pueden encontrar más detalles sobre los operadores PDF en el [Especificación PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

Utilice esta página cuando necesite control directo sobre los flujos de contenido PDF en Python, como colocar gráficos en coordenadas exactas, envolver cambios del estado gráfico, o eliminar operadores de dibujo específicos de una página.

## Agregar imágenes con clases de operador

Utilice clases de operador de bajo nivel cuando necesite colocar contenido de imagen con gran precisión en el flujo de una página PDF sin depender de abstracciones de diseño de alto nivel.

Este método proporciona un control granular sobre la colocación de imágenes dentro de un PDF al manipular directamente el flujo de contenido con operadores gráficos de bajo nivel. Es particularmente útil cuando se requiere un posicionamiento y transformación precisos de las imágenes, como por ejemplo:

- agregar marcas de agua o logotipos en ubicaciones específicas.
- superponer imágenes sobre contenido existente con alineación exacta.
- implementar diseños personalizados que no son posibles con abstracciones de nivel superior.

Al usar operadores como GSave, ConcatenateMatrix, Do y GRestore, los desarrolladores pueden garantizar que las imágenes se rendericen con precisión y sin efectos secundarios no deseados en el contenido de otras páginas.

- El [GSave](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) el operador guarda el estado gráfico actual del PDF.
- El [ConcatenateMatrix](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/) El operador (concatenate matrix) se usa para definir cómo se debe colocar una imagen en la página PDF.
- El [Do](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) El operador dibuja la imagen en la página.
- El [GRestore](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) el operador restaura el estado gráfico.

Para agregar una imagen a un archivo PDF:

1. Abrir el documento PDF
1. Definir coordenadas de colocación de la imagen
1. Acceder a la página de destino
1. Cargar la imagen en un flujo
1. Guardar el estado gráfico actual
1. Crear un rectángulo y una matriz de transformación
1. Aplicar la Matriz de Transformación
1. Dibujar la Imagen
1. Restaurar el Estado Gráfico Anterior
1. Guardar el Documento PDF Modificado

El siguiente fragmento de código muestra cómo usar los operadores PDF:

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_using_pdf_operators(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        page = document.pages[1]

        with open(imagefile, "rb") as image_stream:
            page.resources.images.add(image_stream)

        page.contents.append(ap.operators.GSave())

        rectangle = ap.Rectangle(
            lower_left_x, lower_left_y, upper_right_x, upper_right_y, True
        )
        matrix = ap.Matrix(
            [
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            ]
        )

        page.contents.append(ap.operators.ConcatenateMatrix(matrix))

        x_image = page.resources.images[len(page.resources.images)]

        page.contents.append(ap.operators.Do(x_image.name))

        page.contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## Dibujar XForm en la página usando operadores

Este ejemplo utilizó el poder de XForms y los operadores gráficos para reutilizar eficientemente contenido gráfico dentro de un PDF. Al encapsular la imagen en un XForm, puede dibujarse múltiples veces sin duplicar los datos de la imagen, lo que conduce a tamaños de archivo más pequeños y un rendimiento mejorado. Este enfoque es particularmente beneficioso cuando:

- la misma imagen o gráfico necesita aparecer múltiples veces en un documento.

- se requiere un control preciso sobre la ubicación y transformación de los gráficos.

- optimizar el PDF para el rendimiento y el tamaño es una prioridad.

Al gestionar el estado gráfico con GSave y GRestore, y al utilizar matrices de transformación con ConcatenateMatrix, esta técnica garantiza que cada gráfico se renderice correctamente y de forma independiente.

```python
import sys
import aspose.pdf as ap
from os import path

def draw_xform_on_page(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        page_contents = document.pages[1].contents

        page_contents.insert(1, ap.operators.GSave())
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GSave())

        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.append(form)

        form.contents.append(ap.operators.GSave())
        form.contents.append(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        with open(imagefile, "rb") as image_stream:
            form.resources.images.add(image_stream)

        x_image = form.resources.images[len(form.resources.images)]
        form.contents.append(ap.operators.Do(x_image.name))
        form.contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 500)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 300)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## Eliminar objetos gráficos usando clases de operador

El siguiente fragmento de código muestra cómo eliminar gráficos. Tenga en cuenta que si el archivo PDF contiene etiquetas de texto para los gráficos, podrían permanecer en el archivo PDF al usar este enfoque. Por lo tanto, busque los operadores gráficos para un método alternativo que elimine dichas imágenes.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_graphics_objects(infile, outfile):
    with ap.Document(infile) as document:
        page = document.pages[1]
        # Collect operators to remove in single pass
        # Operator codes: S=Stroke, h=ClosePathStroke, f=Fill'
        graphics_operators = {"S", "h", "f"}
        operators_to_remove = [
            op for op in page.contents if str(op) in graphics_operators
        ]

        page.contents.delete(operators_to_remove)
        document.save(outfile)
```

## Temas relacionados

- [Operaciones avanzadas de PDF en Python](/pdf/es/python-net/advanced-operations/)
- [Trabajar con páginas PDF en Python](/pdf/es/python-net/working-with-pages/)
- [Trabajar con imágenes en PDF usando Python](/pdf/es/python-net/working-with-images/)
- [Trabajar con gráficos PDF en Python](/pdf/es/python-net/working-with-graphs/)
