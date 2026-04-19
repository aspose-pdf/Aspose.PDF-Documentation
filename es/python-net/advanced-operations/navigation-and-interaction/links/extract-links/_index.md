---
title: Extraer enlaces PDF en Python
linktitle: Extraer enlaces
type: docs
weight: 30
url: /es/python-net/extract-links/
description: Aprenda cómo extraer anotaciones de enlaces e hipervínculos de documentos PDF en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Cómo extraer enlaces de PDF
Abstract: La guia de Aspose.PDF para Python a traves de .NET sobre la extraccion de enlaces explica como recuperar programaticamente anotaciones de hipervinculos de documentos PDF usando Python. La documentacion incluye ejemplos de codigo practicos y destaca como esta funcionalidad puede usarse para tareas como auditoria de enlaces, analisis de navegacion o creacion de funciones interactivas en documentos. Ya sea que trabaje con PDF de una sola pagina o procese grandes lotes, esta guia ofrece un enfoque claro y eficiente para la extraccion de hipervinculos.
---

## Extraer enlaces del archivo PDF

Este ejemplo muestra cómo iterar a través de todas las anotaciones de enlace en la primera página de un PDF usando Aspose.PDF for Python. Filtra las anotaciones para identificar aquellas de tipo LinkAnnotation, las convierte de forma segura y luego imprime su índice de página y su posición rectangular en la página.

Esto puede usarse para depuración, análisis o actualizaciones automáticas de anotaciones de enlace existentes en un PDF.

1. Cargue el documento PDF. Use ap.Document(path_infile) para abrir el archivo.
1. Acceda a las anotaciones de la primera página. Use document.pages[1].annotations para obtener todas las anotaciones.
1. Filtre solo los tipos LinkAnnotation. Verifique el annotation_type de cada anotación.
1. Convierta y procese las LinkAnnotations. Use is_assignable() y cast() para garantizar un acceso seguro a las propiedades de LinkAnnotation.
1. Imprima los detalles de la anotación. Salida el índice de página y el rectángulo (ubicación) de cada enlace.

```python

    import aspose.pdf as ap
    from os import path

    # Construct full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # (Optional) You can construct the output file path if needed later
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only LinkAnnotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Iterate over each link annotation
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (type-safe check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Safely cast the annotation to LinkAnnotation type
            annotation = cast(ap.annotations.LinkAnnotation, la)
            
            # Print annotation location and page index
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
            print(annotation.page_index)
```

## Extraer Hipervínculos del archivo PDF

Este código demuestra cómo extraer todos los objetos LinkAnnotation de la primera página de un documento PDF utilizando Aspose.PDF for Python, y luego identificar aquellos que contienen una GoToURIAction. Para cada enlace de este tipo, imprime el índice de página y el URI de destino.

Esto es útil para tareas como:

- Auditar enlaces externos en un PDF
- Extraer URLs de documentación o soporte
- Detectar hipervínculos rotos o desactualizados

1. Cargar el documento PDF. Abrir el archivo usando ap.Document.
1. Obtener todas las anotaciones de enlace de la primera página. Filtrar anotaciones para incluir solo aquellas con tipo AnnotationType.LINK.
1. Verificar el tipo y convertir a LinkAnnotation. Asegurarse de que cada anotación sea realmente una LinkAnnotation antes de acceder a sus propiedades.
1. Comprobar el tipo de acción del enlace. Filtrar los enlaces que utilizan un GoToURIAction (es decir, enlaces a una URL web).
1. Extraer e imprimir el URI y el índice de página. Usar .uri para obtener el enlace externo y .page_index para el contexto.

```python

    import aspose.pdf as ap
    from os import path

    # Construct the full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # Optional: construct output file path if needed
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only link annotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Iterate through filtered link annotations
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (safe type check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Cast the annotation to LinkAnnotation to access link-specific properties
            annotation = cast(ap.annotations.LinkAnnotation, la)

            # Check if the link's action is of type GoToURIAction (external web link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                # Cast the action to GoToURIAction to access the URI property
                action = cast(ap.annotations.GoToURIAction, annotation.action)

                # Print the page number and the link's URI
                print(f"Page {annotation.page_index}, URI: {action.uri}")
```

## Temas de enlace relacionados

- [Trabajar con enlaces PDF en Python](/pdf/es/python-net/links/)
- [Crear enlaces PDF en Python](/pdf/es/python-net/create-links/)
- [Actualizar enlaces en PDF usando Python](/pdf/es/python-net/update-links/)
