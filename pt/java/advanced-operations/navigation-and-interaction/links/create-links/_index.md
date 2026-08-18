---
title: Crie links de PDF em Java
linktitle: Criar links
type: docs
weight: 10
url: /java/create-links/
description: Aprenda como criar links de PDF internos, externos e remotos em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crie anotações de link em arquivos PDF com Java
Abstract: Este artigo mostra como criar anotações de link usando Aspose.PDF para Java. Ele cobre ações de inicialização, navegação remota em documentos, navegação em páginas de documentos e links da web baseados em URI, anexando ações a objetos LinkAnnotation.
---
Aspose.PDF para Java usa `LinkAnnotation` junto com um objeto de ação para definir o comportamento do link.

## Crie um link de ação de lançamento

Use este exemplo quando uma anotação de link deve iniciar um arquivo ou destino externo.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e selecione a página de destino.
1. Crie um [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) e configure sua borda e cor.
1. Atribua um [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/launchaction/) e salve o documento.

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

## Crie um link de acesso remoto

Use este exemplo quando o link abrir uma página em outro documento PDF.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) na página de destino.
1. Atribua um [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoremoteaction/) e salve o arquivo de saída.

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

## Crie um link interno de acesso

Use this example when the link should navigate to another page inside the same PDF document.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) e configure sua aparência.
1. Atribua um [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) à página de destino e salve o documento.

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

## Crie um link de URI

Use este exemplo quando o link abrir um recurso da web por meio de uma ação de URI.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie uma [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) na página.
1. Atribua um [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) e salve o arquivo de saída.

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
