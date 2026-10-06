---
title: Adicionar marcas d'água ao PDF em Java
linktitle: Adicionar Marca d'água
type: docs
weight: 30
url: /pt/java/add-watermarks/
description: Aprenda como adicionar, extrair e excluir artefatos de marca d'água em arquivos PDF usando Aspose.PDF for Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar marca d'água ao PDF com Java
Abstract: Este artigo explica como adicionar, inspecionar e remover artefatos de marca d'água em documentos PDF usando Aspose.PDF for Java. Ele aborda a criação de uma marca d'água de texto com alinhamento, rotação, opacidade e configurações de plano de fundo, a inspeção de artefatos de marca d'água em uma página e a sua exclusão.
---
Os artefatos de marca d'água permitem que você coloque marcas visuais persistentes em uma página sem misturá-las ao conteúdo principal do documento.

## Extrair artefatos de marca d'água de um PDF

Use este exemplo quando precisar inspecionar artefatos de marca d'água existentes e ler seu texto ou posição.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere sobre a coleção de artefatos da página de destino.
1. Filtre artefatos de paginação de marca d'água e imprima seu texto e retângulos.

```java
public static void extractWatermarkFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                System.out.println(artifact.getText() + " " + artifact.getRectangle());
            }
        }
    }
}
```

## Adicionar um artefato de marca d'água

Use este exemplo quando a página deve exibir uma marca d'água de texto centralizada com rotação personalizada, opacidade e posicionamento de fundo.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) e configure seu estado de texto e configurações de posicionamento.
1. Adicione a marca d'água à página e salve o arquivo de saída.

```java
public static void addWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextState textState = new TextState();
        textState.setFontSize(72);
        textState.setForegroundColor(Color.getBlueViolet());
        textState.setFontStyle(FontStyles.Bold);
        textState.setFont(FontRepository.findFont("Arial"));

        WatermarkArtifact watermark = new WatermarkArtifact();
        watermark.setTextAndState("WATERMARK", textState);
        watermark.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
        watermark.setArtifactVerticalAlignment(VerticalAlignment.Center);
        watermark.setRotation(60);
        watermark.setOpacity(0.2);
        watermark.setBackground(true);

        document.getPages().get_Item(1).getArtifacts().add(watermark);
        document.save(outputFile.toString());
    }
}
```

## Excluir artefatos de marca d'água

Use esta abordagem quando os artefatos de marca d'água existentes devem ser removidos da página.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere pela coleção de artefatos da página em ordem reversa.
1. Exclua artefatos de paginação cujo subtipo é marca d'água, então salve o documento.

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
