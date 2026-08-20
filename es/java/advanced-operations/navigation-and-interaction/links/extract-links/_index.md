---
title: Extraer enlaces PDF en Java
linktitle: Extraer enlaces
type: docs
weight: 30
url: /java/extract-links/
description: Aprenda a extraer anotaciones de enlaces e hipervínculos de documentos PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraiga anotaciones de enlaces y destinos URI de archivos PDF con Java
Abstract: Este artículo explica cómo extraer anotaciones de enlaces de documentos PDF utilizando Aspose.PDF para Java. Muestra cómo enumerar anotaciones de enlaces en una página, leer el índice y el rectángulo de su página y extraer destinos URI de instancias de GoToURIAction.
---
Puede inspeccionar enlaces PDF iterando sobre las anotaciones de la página y filtrando por `AnnotationType.Link`.


## 
Extraer anotaciones de enlaces



Utilice este ejemplo cuando necesite la ubicación y la información de la página para las anotaciones de enlaces en una página.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Itere a través de las anotaciones de la página y filtre las anotaciones de enlaces.
1. Lea el índice de la página y el rectángulo de cada enlace coincidente.


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

## 
Extraer destinos de hipervínculos



Utilice este ejemplo cuando necesite leer los URI de destino de las anotaciones de enlaces web.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Busque objetos [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) cuya acción sea una [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. Imprima el índice de la página y el destino URI para cada hipervínculo.

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
