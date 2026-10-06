---
title: Extrair links de PDF em Java
linktitle: Extrair links
type: docs
weight: 30
url: /pt/java/extract-links/
description: Aprenda como extrair anotações de link e hiperlinks de documentos PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair anotações de link e destinos URI de arquivos PDF com Java
Abstract: Este artigo explica como extrair anotações de link de documentos PDF usando Aspose.PDF for Java. Ele mostra como enumerar anotações de link em uma página, ler seu índice de página e retângulo, e extrair destinos URI de instâncias de GoToURIAction.
---
Você pode inspecionar links de PDF iterando sobre as anotações da página e filtrando por `AnnotationType.Link`.

## Extrair anotações de link

Use este exemplo quando precisar da localização e das informações de página para anotações de link em uma página.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere através das anotações da página e filtre as anotações de link.
1. Leia o índice da página e o retângulo para cada link correspondente.

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

## Extrair destinos de hiperlink

Use este exemplo quando precisar ler os URIs de destino de anotações de link da web.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Encontrar objetos [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) cuja ação é um [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. Imprima o índice da página e o destino URI para cada hyperlink.

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
