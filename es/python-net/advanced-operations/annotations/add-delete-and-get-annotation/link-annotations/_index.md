---
title: Uso de anotaciones de enlace en PDF
linktitle: Anotaciones de enlace
type: docs
weight: 70
url: /es/python-net/link-annotations/
description: Aspose.PDF para Python a través de .NET le permite agregar, obtener y eliminar anotaciones de enlace de su documento PDF.
lastmod: "2025-07-28"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
---

## Añadir anotación de enlace a un archivo PDF existente

[Links](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) son anotaciones que abren URL o se desplazan a ciertas posiciones dentro del mismo documento o en un documento externo cuando se hace clic.

Una anotación de enlace es un área rectangular que se puede colocar en cualquier parte de la página. Cada enlace tiene una acción PDF correspondiente asociada. Esta acción se ejecuta cuando el usuario hace clic en el área de este enlace.

El siguiente fragmento de código muestra cómo agregar una anotación de enlace a un archivo PDF usando un ejemplo de número de teléfono:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create TextFragmentAbsorber object to find a phone number
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Accept the absorber for the 1st page only
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Create Link Annotation and set the action to call a phone number
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Add annotation to page
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```

### Obtener anotación de enlace

Por favor, intente usar el siguiente fragmento de código para obtener [LinkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) del documento PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### Eliminar anotación de enlace

El siguiente fragmento de código muestra cómo eliminar la anotación de enlace de un archivo PDF. Para ello, debemos encontrar y eliminar todas las anotaciones de enlace en la primera página. Después de esto guardaremos el documento con la anotación eliminada.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```
