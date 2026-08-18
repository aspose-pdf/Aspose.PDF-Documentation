---
title: Adicionar fundos de PDF em Java
linktitle: Adicionando planos de fundo
type: docs
weight: 20
url: /java/add-backgrounds/
description: Aprenda como adicionar uma imagem ou cor de fundo a páginas PDF em Java usando `BackgroundArtifact` com Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar plano de fundo ao PDF com Java
Abstract: Este artigo explica como adicionar ou remover planos de fundo de páginas PDF em Java usando Aspose.PDF. Abrange a adição de uma imagem de fundo, o ajuste da opacidade da imagem, a aplicação de uma cor de fundo e a remoção de artefatos de fundo de uma página.
---
Os artefatos de plano de fundo permitem colocar elementos visuais sem conteúdo atrás do conteúdo da página principal sem alterar o texto lógico do documento.

## Adicione uma imagem de fundo a um PDF

Use este exemplo quando a página precisar exibir uma imagem como artefato de plano de fundo.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e o fluxo de entrada da imagem.
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

## Adicione uma imagem de fundo com opacidade

Este exemplo coloca uma imagem de fundo semitransparente atrás do conteúdo da página.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e o fluxo de imagem.
1. Crie um [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/backgroundartifact/), atribua a imagem e defina a opacidade.
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

## Adicione uma cor de fundo a um PDF

Use este exemplo quando a página precisar usar uma cor de fundo sólida em vez de uma imagem.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

## Remover artefatos de fundo

Use esta abordagem quando os artefatos de segundo plano existentes precisarem ser excluídos da página.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pela coleção de artefatos da página na ordem inversa.
1. Exclua os artefatos cujo tipo seja paginação e o subtipo seja plano de fundo e salve o documento.

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
