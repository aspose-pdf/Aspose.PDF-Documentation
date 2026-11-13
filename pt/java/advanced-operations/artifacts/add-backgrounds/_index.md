---
title: Adicionar fundos de PDF em Java
linktitle: Adicionar fundos
type: docs
weight: 20
url: /pt/java/add-backgrounds/
description: Adicionar imagens e fundos de cor sólida às páginas PDF em Java e ajustar a opacidade da imagem.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar fundos em Java
Abstract: Adicionar imagens e fundos de cor sólida às páginas PDF em Java e ajustar a opacidade da imagem.
---
Os artefatos de fundo permitem que você coloque elementos visuais que não são conteúdo atrás do conteúdo principal da página sem alterar o texto lógico do documento.

## Adicionar uma imagem de fundo a um PDF

Use este exemplo quando a página deve exibir uma imagem como artefato de fundo.

1. Abra o PDF de origem com [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e abra o fluxo de imagem.
1. Crie um [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) e atribua o fluxo de imagem.
1. Adicione o artefato à página de destino e salve o PDF de saída.

```java
public static void addBackgroundImageToPdf(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Adicionar uma imagem de fundo com opacidade

Este exemplo coloca uma imagem de fundo semitransparente atrás do conteúdo da página.

1. Abra o PDF de origem com [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e abra o fluxo de imagem.
1. Crie um [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/), atribua a imagem, e defina a opacidade.
1. Adicione o artefato à página e salve o documento.

```java
public static void addBackgroundImageWithOpacityToPdf(Path inputFile, Path imageFile, Path outputFile)
        throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundImage(imageStream);
        artifact.setOpacity(0.5);
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Adicionar uma cor de fundo a um PDF

Use este exemplo quando a página deve usar uma cor de fundo sólida em vez de uma imagem.

1. Abra o PDF de origem com [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/) e atribua a cor de fundo.
1. Adicione o artefato à página e salve o arquivo de saída.

```java
public static void addBackgroundColorToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        BackgroundArtifact artifact = new BackgroundArtifact();
        artifact.setBackgroundColor(Color.getDarkKhaki().toRgb());
        document.getPages().get_Item(1).getArtifacts().add(artifact);
        document.save(outputFile.toString());
    }
}
```

## Tópicos relacionados

- [Remover fundos](/pdf/pt/java/remove-backgrounds/)
- [Trabalhar com artefatos PDF em Java](/pdf/pt/java/artifacts/)
