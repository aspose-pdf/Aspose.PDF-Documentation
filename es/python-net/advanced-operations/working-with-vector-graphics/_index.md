---
title: Trabajar con gráficos vectoriales en Python
linktitle: Trabajar con gráficos vectoriales
type: docs
weight: 100
url: /es/python-net/working-with-vector-graphics/
description: Aprenda cómo extraer, mover, eliminar y copiar gráficos vectoriales entre páginas PDF usando GraphicsAbsorber en Python.
lastmod: "2026-05-07"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Utilice GraphicsAbsorber para inspeccionar y manipular gráficos vectoriales PDF en Python.
Abstract: Este artículo explica cómo trabajar con gráficos vectoriales en Aspose.PDF for Python via .NET usando la clase GraphicsAbsorber. Aprende cómo extraer elementos vectoriales de páginas PDF, moverlos o eliminarlos, y copiar gráficos entre páginas con control de bajo nivel en flujos de trabajo de Python.
---

[Aspose.PDF for Python via .NET](/pdf/es/python-net/) proporciona el [Absorbedor de Gráficos](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) clase para acceder y manipular gráficos vectoriales ya presentes en una página PDF. Llama a su `visit` método en cualquier página para extraer rutas, formas y otros operadores gráficos, luego mover, eliminar o copiar esos elementos según sea necesario.

Utilice esta página cuando necesite inspeccionar o modificar elementos de dibujo vectorial incrustados en un PDF existente, en lugar de dibujar nuevas formas desde cero.

## Extrayendo Gráficos

La extracción es el punto de partida para todas las tareas de gráficos vectoriales. `GraphicsAbsorber` lee la secuencia de contenido de una página y expone cada elemento gráfico con su referencia de página, posición y operadores sin procesar.

1. Abra el documento PDF.
1. Crear un [Absorbedor de Gráficos](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) instancia.
1. Llamar `visit` en la página de destino para rellenar `elements`.
1. Iterar sobre `elements` para inspeccionar la posición y los recuentos de operadores.

```python
import aspose.pdf as ap
import sys
from os import path

def using_graphics_absorber(infile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

`GraphicsAbsorber` es parte del `aspose.pdf.vector` el espacio de nombres y está diseñado específicamente para interactuar con gráficos vectoriales en flujos de contenido PDF.

## Gráficos en movimiento

Después de la extracción, establezca un nuevo `position` en cada elemento para reubicarlo en la misma página. Envuelve las actualizaciones en `suppress_update` / `resume_update` llamadas para agrupar escrituras de flujo de contenido en una sola operación y evitar repintados redundantes.

1. Abra el documento PDF.
1. Crear un `GraphicsAbsorber` y llamar `visit` en la página de destino.
1. Llamar `suppress_update` pausar las escrituras del flujo de contenido.
1. Actualizar el `position` de cada elemento.
1. Llamar `resume_update` para confirmar todos los cambios de una vez.
1. Guarde el documento modificado.

```python
import aspose.pdf as ap
import sys
from os import path

def move_graphics(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                position = element.position
                element.position = ap.Point(position.x + 150, position.y - 10)
            graphics_absorber.resume_update()
        document.save(outfile)
```

## Eliminando gráficos

Para eliminar elementos vectoriales específicos de una página, filtra por posición o rectángulo delimitador y luego elimínalos. Aspose.PDF for Python ofrece dos enfoques dependiendo de si deseas eliminar los elementos en línea o recopilarlos primero.

### Método 1: Eliminar en línea usando límite rectangular

Este enfoque verifica la posición de cada elemento contra un rectángulo y llama `element.remove()` directamente dentro del bucle. Úsalo cuando quieras código conciso y no necesites inspeccionar el conjunto eliminado después.

1. Abra el documento PDF.
1. Crear un `GraphicsAbsorber` y llamar `visit` en la página de destino.
1. Definir el objetivo [Rectángulo](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
1. Llamar `suppress_update` pausar las escrituras del flujo de contenido.
1. Iterar `elements`, llamando `remove()` en cada elemento cuya posición caiga dentro del rectángulo.
1. Llamar `resume_update` confirmar las eliminaciones.
1. Guarde el documento modificado.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    element.remove()
            graphics_absorber.resume_update()
        document.save(outfile)
```

### Método 2: Recopilar elementos primero, luego eliminar

Este enfoque reúne los elementos coincidentes en un [ColecciónDeElementosGráficos](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicelementcollection/) y pasa la colección a `page.delete_graphics`. Úselo cuando necesite revisar o registrar lo que se eliminará antes de confirmar la eliminación.

1. Abra el documento PDF.
1. Crear un `GraphicsAbsorber` y llamar `visit` en la página de destino.
1. Definir el rectángulo objetivo.
1. Iterar `elements` y agregar elementos coincidentes a un `GraphicElementCollection`.
1. Llamar `page.contents.suppress_update` pausar las escrituras del flujo de contenido.
1. Llamar `page.delete_graphics` con la colección.
1. Llamar `page.contents.resume_update` confirmar las eliminaciones.
1. Guarde el documento modificado.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.visit(page)
            removed_elements_collection = ap.vector.GraphicElementCollection()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    removed_elements_collection.add(element)
            page.contents.suppress_update()
            page.delete_graphics(removed_elements_collection)
            page.contents.resume_update()
        document.save(outfile)
```

## Agregar gráficos a otra página

Los elementos vectoriales extraídos de una página pueden colocarse en cualquier otra página del mismo documento. Hay dos métodos disponibles: agregar los elementos uno por uno, o pasar toda la colección en una única llamada.

### Método 1: Añadir elementos individualmente

Utilice este método cuando necesite control por elemento, como filtrar o transformar elementos individuales antes de colocarlos en la página de destino.

1. Abra el documento PDF.
1. Crear un `GraphicsAbsorber` y llamar `visit` en la página de origen.
1. Agregar una nueva página de destino al documento.
1. Llamar `page_2.contents.suppress_update` pausar las escrituras del flujo de contenido.
1. Llamar `element.add_on_page(page_2)` para cada elemento.
1. Llamar `page_2.contents.resume_update` confirmar todas las adiciones.
1. Guarde el documento modificado.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            for element in graphics_absorber.elements:
                element.add_on_page(page_2)
            page_2.contents.resume_update()
        document.save(outfile)
```

### Método 2: Añadir toda la colección de una vez

Utilice este método cuando desee copiar todos los elementos extraídos a una página en una sola operación sin iterar manualmente.

1. Abra el documento PDF.
1. Crear un `GraphicsAbsorber` y llamar `visit` en la página de origen.
1. Agregar una nueva página de destino al documento.
1. Llamar `page_2.contents.suppress_update` pausar las escrituras del flujo de contenido.
1. Llamar `page_2.add_graphics` con el completo `elements` colección.
1. Llamar `page_2.contents.resume_update` confirmar todas las adiciones.
1. Guarde el documento modificado.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            page_2.add_graphics(graphics_absorber.elements, None)
            page_2.contents.resume_update()
        document.save(outfile)
```

## Temas relacionados

- [Operaciones avanzadas de PDF en Python](/pdf/es/python-net/advanced-operations/)
- [Trabaja con gráficos PDF en Python](/pdf/es/python-net/working-with-graphs/)
- [Trabajar con operadores PDF en Python](/pdf/es/python-net/working-with-operators/)
- [Trabajar con páginas PDF en Python](/pdf/es/python-net/working-with-pages/)
