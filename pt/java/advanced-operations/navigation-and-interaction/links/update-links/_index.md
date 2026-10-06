---
title: Atualizar links de PDF em Java
linktitle: Atualizar Links
type: docs
weight: 20
url: /pt/java/update-links/
description: Aprenda como atualizar a aparência e os destinos de links PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atualizar a aparência da anotação de link e destinos web em arquivos PDF com Java
Abstract: Este artigo mostra como atualizar anotações de link existentes usando Aspose.PDF for Java. Os exemplos demonstram a alteração da cor do texto coberto por um link, a atualização da cor da anotação de link e a substituição do URI de destino para links da web.
---
Links existentes podem ser editados encontrando a anotação de link em uma página e atualizando sua aparência ou sua ação.

## Atualizar cor do texto vinculado

Use este exemplo quando a área de texto coberta por uma anotação de link precisar ser recolorizada.

1. Abra o PDF fonte [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Encontre anotações de link e construa um retângulo de busca de texto a partir de cada área de anotação.
1. Recolore os fragmentos de texto correspondentes e salve o documento.

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

## Atualizar cor da borda do link

Use este exemplo quando a cor visível das anotações de link existentes deve ser alterada.

1. Abra o PDF fonte [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pelas anotações da página e filtre por [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) objetos.
1. Atualize a cor da anotação de link e salve o documento.

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

## Atualizar o destino de um link da web

Use este exemplo quando um link da web existente deve apontar para um novo URI.

1. Abra o PDF fonte [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Encontre anotações de link cuja ação é um [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. Substitua o URI e salve o documento atualizado.

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
