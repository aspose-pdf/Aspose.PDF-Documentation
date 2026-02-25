---
title: Trabajando con gráficos vectoriales usando Python
linktitle: Trabajando con gráficos vectoriales
type: docs
weight: 100
url: /es/python-net/working-with-vector-graphics/
description: Este artículo describe las características de trabajar con la herramienta GraphicsAbsorber usando Python.
lastmod: "2025-05-17"
TechArticle: true
AlternativeHeadline: Utiliza la herramienta GraphicsAbsorber en PDF con Python
Abstract: La documentación de Aspose.PDF para Python mediante .NET sobre el artículo Trabajando con gráficos vectoriales ofrece una guía completa para desarrolladores que buscan manipular gráficos vectoriales dentro de documentos PDF utilizando la clase GraphicsAbsorber. Esta clase facilita la extracción, movimiento, eliminación y duplicación de elementos gráficos vectoriales a lo largo de las páginas PDF.
---

En este capítulo, exploraremos cómo usar la poderosa clase `GraphicsAbsorber` para interactuar con gráficos vectoriales dentro de documentos PDF. Ya sea que necesites mover, eliminar o añadir gráficos, esta guía te mostrará cómo realizar estas tareas de manera efectiva.

## Introducción

Los gráficos vectoriales son un componente crucial de muchos documentos PDF, utilizados para representar imágenes, formas y otros elementos gráficos. Aspose.PDF proporciona la clase `GraphicsAbsorber`, que permite a los desarrolladores acceder y manipular estos gráficos de forma programática. Al usar el método `Visit` de `GraphicsAbsorber`, puedes extraer gráficos vectoriales de una página especificada y realizar diversas operaciones, como mover, eliminar o copiar a otras páginas.

## Extrayendo gráficos

El primer paso para trabajar con gráficos vectoriales es extraerlos de un documento PDF. Así es como puedes hacerlo usando la clase `GraphicsAbsorber`:

1. Abre el documento PDF.
1. Inicializa el GraphicsAbsorber.
1. Selecciona la página objetivo.
1. Extrae los gráficos de la página.
1. Itera y muestra los elementos extraídos.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Use the `Visit` method to extract graphics from the page
            graphics_absorber.visit(page)
            # Display information about the extracted elements
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

La clase GraphicsAbsorber es parte del espacio de nombres aspose.pdf.vector y está diseñada específicamente para interactuar con gráficos vectoriales dentro de documentos PDF.

## Moviendo gráficos

Una vez que hayas extraído los gráficos, puedes moverlos a una posición diferente en la misma página. Así es como puedes lograrlo:

1. Abre el documento PDF.
1. Inicializa el GraphicsAbsorber.
1. Selecciona la página objetivo.
1. Extrayendo elementos gráficos.
1. Suspendiendo actualizaciones para mejorar el rendimiento.
1. Modificando las posiciones de los elementos gráficos.
1. Reanudando actualizaciones y aplicando los cambios.
1. Guardando el documento actualizado.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create a GraphicsAbsorber instance
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Temporarily suspend updates to improve performance
            graphics_absorber.suppress_update()
            # Loop through each extracted graphic element and shift its position
            for element in graphics_absorber.elements:
                position = element.position
                # Move graphics by shifting its X and Y coordinates
                element.position = ap.Point(position.x + 150, position.y - 10)
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## Eliminando gráficos

Existen escenarios en los que podrías querer eliminar gráficos específicos de una página. Aspose.PDF para Python ofrece dos métodos para lograrlo:

### Método 1: Usando límite rectangular

El siguiente ejemplo muestra cómo eliminar elementos gráficos vectoriales ubicados dentro de un área rectangular específica en la primera página de un documento PDF usando la biblioteca Aspose.PDF para Python mediante .NET. Este proceso implica identificar los elementos gráficos dentro del rectángulo definido y eliminarlos para limpiar o modificar el contenido del PDF.

1. Abre el documento PDF.
1. Inicializa el GraphicsAbsorber.
1. Selecciona la página objetivo.
1. Extrayendo elementos gráficos.
1. Definiendo el rectángulo objetivo.
1. Suspendiendo actualizaciones para mejorar el rendimiento.
1. Eliminando los elementos gráficos dentro del rectángulo.
1. Reanudando actualizaciones y aplicando los cambios.
1. Guardando el documento actualizado.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Temporarily suspend updates for better performance
            graphics_absorber.suppress_update()
            # Iterate through the extracted graphic elements and remove elements inside the rectangle
            for element in graphics_absorber.elements:
                # Check if the graphic's position falls within the rectangle
                if rectangle.contains(element.position, False):
                    # Remove the graphic element
                    element.remove()
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### Método 2: Usando una colección de elementos eliminados

El siguiente ejemplo muestra cómo eliminar elementos gráficos vectoriales ubicados dentro de un área rectangular específica en la primera página de un documento PDF usando la biblioteca Aspose.PDF para Python mediante .NET. Este proceso implica identificar los elementos gráficos dentro del rectángulo definido y eliminarlos para limpiar o modificar el contenido del PDF.

1. Abre el documento PDF.
1. Inicializa el GraphicsAbsorber.
1. Selecciona la página objetivo.
1. Definiendo el rectángulo objetivo.
1. Extrayendo elementos gráficos.
1. Creando una colección para eliminar.
1. Identificando elementos dentro del rectángulo.
1. Suspendiendo actualizaciones para mejorar el rendimiento.
1. Eliminando elementos gráficos.
1. Reanudando actualizaciones y aplicando cambios.
1. Guardando el documento actualizado.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Create a collection for the removed elements
            removed_elements_collection = ap.vector.GraphicElementCollection()
            # Add elements within the rectangle to the collection
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position,False):
                    removed_elements_collection.add(item)
            # Temporarily suppress updates for better performance
            page.contents.suppress_update()
            # Delete the selected graphic elements
            page.delete_graphics(removed_elements_collection)
            # Resume updates and apply changes
            page.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## Añadiendo gráficos a otra página

Los gráficos absorbidos de una página pueden añadirse a otra página dentro del mismo documento.
Aquí hay dos métodos para lograr esto:

### Método 1: Añadir gráficos individualmente

El siguiente ejemplo copia elementos gráficos vectoriales de la primera página de un documento PDF y los pega en la segunda página. Esta operación es facilitada por la clase GraphicsAbsorber, que permite la extracción y manipulación de gráficos vectoriales dentro de documentos PDF.

1. Abrir el documento PDF.
1. Inicializar el GraphicsAbsorber.
1. Seleccionar la página de destino.
1. Extrayendo elementos gráficos de la primera página.
1. Suspendiendo actualizaciones en la segunda página para mejorar el rendimiento.
1. Añadiendo los elementos gráficos extraídos a la segunda página.
1. Reanudando actualizaciones y aplicando cambios.
1. Guardando el documento actualizado.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add each graphic element from the first page to the second page
            for element in graphics_absorber.elements:
                element.add_on_page(page_2) # Add each graphic element to the second page.
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### Método 2: Añadir gráficos como una colección

El siguiente ejemplo duplica elementos gráficos vectoriales de la primera página de un documento PDF y los coloca en la segunda página. Esto se logra mediante el uso de la clase GraphicsAbsorber, que facilita la extracción y manipulación de gráficos vectoriales dentro de documentos PDF.

1. Abrir el documento PDF.
1. Inicializar el GraphicsAbsorber.
1. Seleccionar la página de destino.
1. Extrayendo elementos gráficos de la primera página.
1. Suspendiendo actualizaciones en la segunda página para mejorar el rendimiento.
1. Añadiendo los elementos gráficos extraídos a la segunda página.
1. Reanudando actualizaciones y aplicando cambios.
1. Guardando el documento actualizado.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add all graphics at once from the first page to the second page
            page_2.add_graphics(graphics_absorber.elements, None)
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```
