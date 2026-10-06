---
title: Adicionar fundos de PDF em Java
linktitle: Adicionar fundos
type: docs
weight: 20
url: /pt/java/add-backgrounds/
description: Aprenda como adicionar uma imagem de fundo ou cor de fundo às páginas PDF em Java usando `BackgroundArtifact` com Aspose.PDF.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar fundo a PDF com Java
Abstract: Este artigo explica como adicionar ou remover planos de fundo de páginas PDF em Java usando Aspose.PDF. Ele cobre a adição de uma imagem de fundo, o ajuste da opacidade da imagem, a aplicação de uma cor de fundo e a remoção de artefatos de fundo de uma página.
---
Artefatos de fundo permitem colocar elementos visuais não de conteúdo atrás do conteúdo principal da página sem alterar o texto lógico do documento.

## Adicionar uma imagem de fundo a um PDF

Use este exemplo quando a página deve exibir uma imagem como um artefato de fundo.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e o fluxo de entrada da imagem.
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

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e fluxo de imagem.
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

## Adicionar uma cor de fundo a um PDF

Use este exemplo quando a página deve usar uma cor de fundo sólida em vez de uma imagem.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

Use esta abordagem quando os artefatos de fundo existentes devem ser excluídos da página.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar pela coleção de artefatos da página em ordem inversa.
1. Excluir artefatos cujo tipo é paginação e cujo subtipo é fundo, então salvar o documento.

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
