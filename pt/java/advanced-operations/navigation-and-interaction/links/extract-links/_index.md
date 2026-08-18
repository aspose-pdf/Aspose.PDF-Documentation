---
title: Extraia links de PDF em Java
linktitle: Extrair links
type: docs
weight: 30
url: /java/extract-links/
description: Aprenda como extrair anotações de links e hiperlinks de documentos PDF em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraia anotações de links e alvos URI de arquivos PDF com Java
Abstract: Este artigo explica como extrair anotações de links de documentos PDF usando Aspose.PDF para Java. Ele mostra como enumerar anotações de link em uma página, ler o índice e o retângulo da página e extrair alvos de URI de instâncias GoToURIAction.
---
Você pode inspecionar links de PDF iterando anotações de página e filtrando `AnnotationType.Link`.

## Extrair anotações de link

Use este exemplo quando precisar de informações de localização e página para anotações de link em uma página.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pelas anotações da página e filtre as anotações do link.
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

## Extraia destinos de hiperlinks

Use este exemplo quando precisar ler os URIs de destino das anotações de link da web.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Encontre objetos [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) cuja ação seja [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. Print the page index and URI target for each hyperlink.

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
