---
title: Criar links PDF em Java
linktitle: Criar links
type: docs
weight: 10
url: /pt/java/create-links/
description: Aprenda como criar links PDF internos, externos e remotos em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar anotações de link em arquivos PDF com Java
Abstract: Este artigo mostra como criar anotações de link usando Aspose.PDF for Java. Ele cobre ações de lançamento, navegação de documento remoto, navegação de página dentro do documento e links da web baseados em URI, anexando ações a objetos LinkAnnotation.
---
Aspose.PDF for Java usa `LinkAnnotation` juntos com um objeto de ação para definir o comportamento do link.

## Criar um link de ação de lançamento

Use este exemplo quando uma anotação de link deve lançar um arquivo ou destino externo.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e selecione a página de destino.
1. Crie um [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) e configure sua borda e cor.
1. Atribuir um [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/launchaction/) e salvar o documento.

```java
public static void createLinkAnnotationLaunchAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, inputFile.toString()));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## Criar um link remoto de ir para

Use este exemplo quando o link deve abrir uma página em outro documento PDF.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) na página de destino.
1. Atribuir um [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoremoteaction/) e salve o arquivo de saída.

```java
public static void createLinkAnnotationGoToRemoteAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(inputFile.toString(), 1));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## Criar um link interno de navegação

Use este exemplo quando o link deve navegar para outra página dentro do mesmo documento PDF.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) e configure sua aparência.
1. Atribuir um [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) para a página de destino e salvar o documento.

```java
public static void createLinkAnnotationGoToAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        if (document.getPages().size() >= 4) {
            link.setAction(new GoToAction(document.getPages().get_Item(4)));
        } else {
            link.setAction(new GoToAction(document.getPages().get_Item(document.getPages().size())));
        }
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## Criar um link URI

Use este exemplo quando o link deve abrir um recurso da web através de uma ação URI.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) na página.
1. Atribuir um [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) e salve o arquivo de saída.

```java
public static void createLinkAnnotationGoToUriAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToURIAction("https://docs.aspose.com/pdf/python"));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```
