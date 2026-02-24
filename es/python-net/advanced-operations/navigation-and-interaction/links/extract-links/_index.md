---
title: Extraer enlaces del archivo PDF usando Python
linktitle: Extraer enlaces
type: docs
weight: 30
url: /es/python-net/extract-links/
description: Descubra cómo extraer hipervínculos de documentos PDF en Python usando Aspose.PDF para la gestión de contenidos y el análisis de enlaces.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer enlaces de PDF
Abstract: La guía de Aspose.PDF para Python mediante .NET sobre la extracción de enlaces explica cómo recuperar programáticamente anotaciones de hipervínculos de documentos PDF usando Python. La documentación incluye ejemplos de código prácticos y destaca cómo esta funcionalidad puede utilizarse para tareas como auditoría de enlaces, análisis de navegación o creación de funcionalidades interactivas en documentos. Ya sea que trabaje con PDFs de una sola página o procesando grandes lotes, esta guía ofrece un enfoque claro y eficiente para la extracción de hipervínculos.
---

## Extraer enlaces del archivo PDF

Este ejemplo muestra cómo iterar a través de todas las anotaciones de enlaces en la primera página de un PDF usando Aspose.PDF para Python. Filtra las anotaciones para identificar las de tipo LinkAnnotation, las convierte de forma segura y luego imprime su índice de página y posición rectangular en la página.

Esto puede usarse para depuración, análisis o actualizaciones automáticas de anotaciones de enlace existentes en un PDF.

1. Cargue el documento PDF. Use ap.Document(path_infile) para abrir el archivo.
1. Acceda a las anotaciones de la primera página. Use document.pages[1].annotations para obtener todas las anotaciones.
1. Filtre solo los tipos LinkAnnotation. Verifique el annotation_type de cada anotación.
1. Convierta y procese LinkAnnotations. Use is_assignable() y cast() para garantizar un acceso seguro a las propiedades de LinkAnnotation.
1. Imprima los detalles de la anotación. Muestre el índice de página y el rectángulo (ubicación) de cada enlace.

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

## Extraer hipervínculos del archivo PDF

Este código demuestra cómo extraer todos los objetos LinkAnnotation de la primera página de un documento PDF usando Aspose.PDF para Python, y luego identificar los que contienen una GoToURIAction. Para cada enlace de este tipo, imprime el índice de página y el URI de destino.

Esto es útil para tareas como:

- Auditar enlaces externos en un PDF
- Extraer URLs de documentación o soporte
- Detectar hipervínculos rotos o desactualizados

1. Cargue el documento PDF. Abra el archivo usando ap.Document.
1. Obtenga todas las anotaciones de enlace de la primera página. Filtre las anotaciones para incluir solo aquellas con tipo AnnotationType.LINK.
1. Verifique el tipo y convierta a LinkAnnotation. Asegúrese de que cada anotación sea realmente una LinkAnnotation antes de acceder a sus propiedades.
1. Verifique el tipo de acción del enlace. Filtre los enlaces que utilizan una GoToURIAction (es decir, enlaces a una URL web).
1. Extraiga e imprima el URI y el índice de página. Use .uri para obtener el enlace externo y .page_index para el contexto.

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
