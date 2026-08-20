---
title: Actualizar enlaces PDF en Java
linktitle: Enlaces de actualización
type: docs
weight: 20
url: /java/update-links/
description: Aprenda a actualizar la apariencia y los destinos de los enlaces PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Actualice la apariencia de las anotaciones de enlaces y los destinos web en archivos PDF con Java
Abstract: Este artículo muestra cómo actualizar las anotaciones de enlaces existentes utilizando Aspose.PDF para Java. Los ejemplos demuestran cómo cambiar el color del texto cubierto por un enlace, actualizar el color de la anotación del enlace y reemplazar el URI de destino para los enlaces web.
---
Los enlaces existentes se pueden editar buscando la anotación del enlace en una página y actualizando su apariencia o su acción.


## 
Actualizar el color del texto vinculado



Utilice este ejemplo cuando deba cambiar el color del área de texto cubierta por una anotación de enlace.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Busque anotaciones de enlaces y cree un rectángulo de búsqueda de texto a partir de cada área de anotación.
1. Vuelva a colorear los fragmentos de texto coincidentes y guarde el documento.


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

## 
Actualizar color del borde del enlace



Utilice este ejemplo cuando deba cambiar el color visible de las anotaciones de enlaces existentes.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Itere a través de las anotaciones de la página y filtre por objetos [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/).
1. Actualice el color de la anotación del enlace y guarde el documento.


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

## 
Actualizar un destino de enlace web



Utilice este ejemplo cuando un enlace web existente deba apuntar a un nuevo URI.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Busque anotaciones de enlaces cuya acción sea [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. Reemplace el URI y guarde el documento actualizado.

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
