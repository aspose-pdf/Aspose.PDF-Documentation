---
title: Extraer enlaces PDF en Java
linktitle: Extraer enlaces
type: docs
weight: 30
url: /es/java/extract-links/
description: Aprenda cómo extraer anotaciones de enlace e hipervínculos de documentos PDF en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer anotaciones de enlace y destinos URI de archivos PDF con Java
Abstract: Este artículo explica cómo extraer anotaciones de enlace de documentos PDF usando Aspose.PDF for Java. Muestra cómo enumerar anotaciones de enlace en una página, leer su índice de página y rectángulo, y extraer destinos URI de instancias de GoToURIAction.
---
Puede inspeccionar los enlaces PDF iterando sobre las anotaciones de página y filtrando por `AnnotationType.Link`.

## Extraer anotaciones de enlace

Utilice este ejemplo cuando necesite la ubicación e información de página para las anotaciones de enlace en una página.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar a través de las anotaciones de la página y filtrar las anotaciones de enlace.
1. Leer el índice de página y el rectángulo de cada enlace coincidente.

```java
public static void extractLinkAnnotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                System.out.println("Page: " + linkAnnotation.getPageIndex()
                        + ", location: " + linkAnnotation.getRect());
            }
        }
    }
}
```

## Extraer destinos de hipervínculos

Utilice este ejemplo cuando necesite leer los URI de destino de las anotaciones de enlaces web.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buscar [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) objetos cuya acción es una [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. Imprima el índice de página y el objetivo URI de cada hipervínculo.

```java
public static void extractHyperlinks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    System.out.println("Page " + linkAnnotation.getPageIndex() + ", URI:" + action.getURI());
                }
            }
        }
    }
}
```
