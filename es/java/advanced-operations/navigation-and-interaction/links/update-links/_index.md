---
title: Actualizar enlaces PDF en Java
linktitle: Actualizar enlaces
type: docs
weight: 20
url: /es/java/update-links/
description: Aprenda cómo actualizar la apariencia y los destinos de los enlaces PDF en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Actualice la apariencia de la anotación de enlace y los destinos web en archivos PDF con Java
Abstract: Este artículo muestra cómo actualizar anotaciones de vínculo existentes utilizando Aspose.PDF for Java. Los ejemplos demuestran cómo cambiar el color del texto cubierto por un vínculo, actualizar el color de la anotación de vínculo y reemplazar el URI de destino para enlaces web.
---
Los enlaces existentes pueden editarse encontrando la anotación de vínculo en una página y actualizando su apariencia o su acción.

## Actualizar color del texto vinculado

Utilice este ejemplo cuando el área de texto cubierta por una anotación de vínculo deba recolorarse.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Encuentre anotaciones de enlace y genere un rectángulo de búsqueda de texto a partir de cada área de anotación.
1. Recoloree los fragmentos de texto coincidentes y guarde el documento.

```java
public static void linkAnnotationUpdateTextColor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX() - 2);
                rect.setLLY(rect.getLLY() - 2);
                rect.setURX(rect.getURX() + 2);
                rect.setURY(rect.getURY() + 2);
                absorber.setTextSearchOptions(new TextSearchOptions(rect));
                absorber.visit(document.getPages().get_Item(1));
                for (TextFragment textFragment : absorber.getTextFragments()) {
                    textFragment.getTextState().setForegroundColor(Color.getRed());
                }
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Actualizar color del borde del enlace

Utilice este ejemplo cuando el color visible de las anotaciones de enlace existentes deba cambiarse.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de las anotaciones de la página y filtrar por [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) objetos.
1. Actualice el color de la anotación de enlace y guarde el documento.

```java
public static void linkAnnotationUpdateBorder(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                linkAnnotation.setColor(Color.getRed());
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Actualizar el destino de un enlace web

Utilice este ejemplo cuando un enlace web existente debe apuntar a una nueva URI.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buscar anotaciones de enlace cuya acción es una [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. Reemplazar el URI y guardar el documento actualizado.

```java
public static void linkAnnotationUpdateWebDestination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    action.setURI("https://www.aspose.com");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```
