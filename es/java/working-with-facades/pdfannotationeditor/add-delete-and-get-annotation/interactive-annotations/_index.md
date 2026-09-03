---
title: Anotaciones interactivas con Java
linktitle: Anotaciones interactivas
type: docs
weight: 30
url: /es/java/pdfannotationeditor-class/interactive-annotations/
description: Aprenda cómo agregar, inspeccionar y eliminar anotaciones de enlace en documentos PDF usando Java.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Trabaje con anotaciones PDF interactivas en Java
Abstract: Este artículo explica cómo trabajar con anotaciones de enlace interactivas en archivos PDF usando Java. Cubre la localización de texto, la creación de una anotación de enlace sobre el área de texto coincidente, la lectura de anotaciones de enlace existentes y su eliminación.
---
## Agregar una anotación de enlace

1. Cargue el documento PDF de origen y busque el texto objetivo en la primera página.
2. Utilice el rectángulo de texto coincidente para crear un `LinkAnnotation` y asigna la URI de destino.
3. Añada la anotación a la página y guarde el PDF actualizado.

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
