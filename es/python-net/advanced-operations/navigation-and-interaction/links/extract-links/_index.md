---
title: Extraer enlaces PDF en Python
linktitle: Extraer enlaces
type: docs
weight: 30
url: /es/python-net/extract-links/
description: Aprende cómo extraer anotaciones de enlace e hipervínculos de documentos PDF en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer enlaces de PDF
Abstract: La guía de Aspose.PDF for Python via .NET sobre la extracción de enlaces explica cómo recuperar programáticamente anotaciones de hipervínculo de documentos PDF mediante Python. La documentación incluye ejemplos de código prácticos y destaca cómo esta funcionalidad puede usarse para tareas como auditoría de enlaces, análisis de navegación o creación de características interactivas en documentos. Ya sea que estés trabajando con PDFs de una sola página o procesando lotes grandes, esta guía ofrece un enfoque claro y eficiente para la extracción de hipervínculos.
---

## Extraer enlaces del archivo PDF

Este ejemplo muestra cómo iterar a través de todas las anotaciones de enlace en la primera página de un PDF usando Aspose.PDF for Python. Filtra las anotaciones para identificar aquellas de tipo LinkAnnotation, las convierte de forma segura y luego imprime su índice de página y su posición rectangular en la página.

Esto puede usarse para depuración, análisis o actualizaciones automáticas de anotaciones de enlace existentes en un PDF.

1. Cargue el documento PDF. Use ap.Document(path_infile) para abrir el archivo.
1. Acceda a las anotaciones de la primera página. Use document.pages[1].annotations para obtener todas las anotaciones.
1. Filtre solo los tipos LinkAnnotation. Verifique el annotation_type de cada anotación.
1. Convierta y procese las LinkAnnotations. Use is_assignable() y cast() para garantizar un acceso seguro a las propiedades de LinkAnnotation.
1. Imprimir detalles de anotaciones. Salida del índice de página y del rectángulo (ubicación) de cada enlace.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_link_annotation(infile):

    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
```

## Extraer hipervínculos del archivo PDF

Este código demuestra cómo extraer todos los objetos LinkAnnotation de la primera página de un documento PDF usando Aspose.PDF for Python, y luego identificar aquellos que contienen un GoToURIAction. Para cada uno de esos enlaces, imprime el índice de página y el URI de destino.

Esto es útil para tareas como:

- Auditar enlaces externos en un PDF
- Extraer URLs de documentación o soporte
- Detectar hipervínculos rotos o desactualizados

1. Cargar el documento PDF. Abrir el archivo usando ap.Document.
1. Obtenga todas las anotaciones de enlace de la primera página. Filtre las anotaciones para incluir solo aquellas con el tipo AnnotationType.LINK.
1. Verifique el tipo y convierta a LinkAnnotation. Asegúrese de que cada anotación sea realmente una LinkAnnotation antes de acceder a sus propiedades.
1. Compruebe el tipo de acción del enlace. Filtre los enlaces que utilizan un GoToURIAction (es decir, enlaces a una URL web).
1. Extraiga e imprima el URI y el índice de página. Utilice .uri para obtener el enlace externo y .page_index para el contexto.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_hyperlinks(infile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"Page {annotation.page_index}, URI:{action.uri}")
```

## Temas relacionados de enlaces

- [Trabajar con enlaces PDF en Python](/pdf/es/python-net/links/)
- [Crear enlaces PDF en Python](/pdf/es/python-net/create-links/)
- [Actualizar enlaces en el PDF usando Python](/pdf/es/python-net/update-links/)