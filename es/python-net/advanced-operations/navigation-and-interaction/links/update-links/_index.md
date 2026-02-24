---
title: Actualizar enlaces en PDF usando Python
linktitle: Actualizar enlaces
type: docs
weight: 20
url: /es/python-net/update-links/
description: Actualizar enlaces en PDF de forma programática. Esta guía trata sobre cómo actualizar enlaces en PDF en el lenguaje Python.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo actualizar enlaces en PDF
Abstract: La guía Aspose.PDF para Python vía .NET sobre la actualización de enlaces lleva a los desarrolladores a través del proceso de modificar el comportamiento de los hipervínculos dentro de documentos PDF usando Python. Explica cómo cambiar los destinos de los enlaces para que apunten a páginas específicas, sitios web externos o incluso a otros archivos PDF. La documentación también cubre cómo ajustar la apariencia de las anotaciones de enlace, incluido el color del texto, y ofrece ejemplos de código prácticos para cada escenario. Ya sea que estés corrigiendo URL obsoletas o mejorando la navegación, este recurso ofrece un enfoque claro y eficiente para gestionar enlaces de forma programática.
---

## Actualizar color de texto de LinkAnnotation

Este ejemplo muestra cómo detectar todas las anotaciones de enlace en la primera página de un PDF usando Aspose.PDF para Python, y luego resaltar el texto cercano a cada enlace cambiando su color de fuente a rojo. Utiliza TextFragmentAbsorber con un área ligeramente expandida alrededor de cada rectángulo de enlace para encontrar y modificar el texto cercano.

Esto se puede usar para:

- Marcar visualmente los enlaces en un documento
- Mejorar la accesibilidad destacando el contenido enlazado
- Preprocesar archivos PDF antes de la revisión o exportación

Para cada una de estas anotaciones de enlace, el script recupera su límite rectangular y expande ligeramente esa zona para incluir texto cercano, lo que permite una identificación visual más amplia. Luego aplica un TextFragmentAbsorber sobre esta área ampliada para extraer cualquier fragmento de texto ubicado dentro de ella. Estos fragmentos capturados se modifican cambiando su color de fuente a rojo, marcando efectivamente el texto circundante para enfatizarlo y revisarlo. Después de aplicar todas estas actualizaciones, el documento modificado se guarda en la ruta de salida, preservando las anotaciones resaltadas y su texto asociado.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Filter all link annotations on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Loop through each link annotation found
    for la in link_annotations:
        # Create a text absorber for extracting text fragments
        ta = ap.text.TextFragmentAbsorber()

        # Get the rectangle area of the annotation
        rect = la.rect

        # Expand the rectangle slightly to catch text near the link
        rect.llx -= 2  # Lower-left x
        rect.lly -= 2  # Lower-left y
        rect.urx += 2  # Upper-right x
        rect.ury += 2  # Upper-right y

        # Restrict text search to the adjusted rectangle
        ta.text_search_options = ap.text.TextSearchOptions(rect)

        # Apply the absorber to the first page
        ta.visit(document.pages[1])

        # Iterate through found text fragments and change their color to red
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    # Save the updated PDF document to the output path
    document.save(path_outfile)
```

## Actualizar borde

El script se centra en la primera página del documento y filtra todas las anotaciones, seleccionando solo aquellas del tipo LINK —que típicamente representan elementos interactivos, como hipervínculos o disparadores de navegación. Para cada una de estas anotaciones de enlace, el código las convierte al tipo LinkAnnotation y actualiza su propiedad de color a rojo, resaltándolas visualmente para que se distingan del resto del contenido. Después de que todas las anotaciones de enlace hayan sido modificadas, el documento actualizado se guarda en la ubicación de salida definida, preservando el nuevo estilo.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Get all annotations of type LINK on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Loop through each link annotation and change its color to red
    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red  # Highlight the link in red

    # Save the modified PDF to the output path
    document.save(path_outfile)
```    

## Actualizar destino web

Una vez que las rutas están configuradas, el documento original se carga usando la biblioteca Aspose.PDF, haciendo su contenido accesible para su modificación. A continuación, el script se centra en la primera página del documento, filtrando todas las anotaciones y seleccionando solo aquellas que son del tipo enlace, que típicamente representan áreas clicables o hipervínculos. Para evitar errores de tipo y garantizar un manejo seguro, cada anotación se verifica con is_assignable y luego se convierte al tipo LinkAnnotation correspondiente. Si el enlace está asociado a una GoToURIAction, lo que significa que apunta a una dirección web, el script actualiza esa URI para redirigir a los usuarios a "https://www.google.com". Finalmente, después de aplicar todos los cambios deseados, el documento modificado se guarda en la ruta de salida especificada.

```python

    import aspose.pdf as ap
    from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the PDF document
document = ap.Document(path_infile)

# Find all LINK annotations on the first page
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]

# Loop through annotations and replace target URI
for la in link_annotations:
    # Ensure the annotation is a LinkAnnotation
    if is_assignable(la, ap.annotations.LinkAnnotation):
        annotation = cast(ap.annotations.LinkAnnotation, la)
        
        # Check if the action is of type GoToURIAction
        if is_assignable(annotation.action, ap.annotations.GoToURIAction):
            action = cast(ap.annotations.GoToURIAction, annotation.action)
            
            # Replace the existing URI with Google
            action.uri = "https://www.google.com"

# Save the modified document to output path
document.save(path_outfile)
```
