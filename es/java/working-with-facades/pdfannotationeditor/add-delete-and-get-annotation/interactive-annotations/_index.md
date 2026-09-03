---
title: Anotaciones interactivas usando Java
linktitle: Anotaciones interactivas
type: docs
weight: 30
url: /java/pdfannotationeditor-class/interactive-annotations/
description: Aprenda a agregar, inspeccionar y eliminar anotaciones de enlaces en documentos PDF utilizando Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Trabajar con anotaciones PDF interactivas en Java
Abstract: Este artículo explica cómo trabajar con anotaciones de enlaces interactivos en archivos PDF usando Java. Cubre la localización de texto, la creación de una anotación de enlace sobre el área de texto coincidente, la lectura de anotaciones de enlaces existentes y su eliminación.
---
## Agregar una anotación de enlace


1. Cargue el documento PDF de origen y busque en la primera página el texto de destino.

2. Utilice el rectángulo de texto coincidente para crear un `LinkAnnotation` y asignar el URI de destino.

3. Agregue la anotación a la página y guarde el PDF actualizado.

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1), phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```
