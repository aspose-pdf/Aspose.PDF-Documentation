---
title: Adicionar marcas d'água ao PDF em Java
linktitle: Adicionar marcas d'água
type: docs
weight: 30
url: /pt/java/add-watermarks/
description: Adicionar artefatos de marca d'água de texto estilizado às páginas PDF em Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar marcas d'água em Java
Abstract: Adicionar artefatos de marca d'água de texto estilizado às páginas PDF em Java.
---
Os artefatos de marca d'água permitem que você coloque marcas visuais persistentes em uma página sem mesclá‑las ao conteúdo principal do documento.

## Adicionar um artefato de marca d'água

Use este exemplo quando a página deve exibir uma marca d'água de texto centralizada com rotação personalizada, opacidade e posicionamento de fundo.

1. Abra o PDF de origem com [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) e configure seu estado de texto e as configurações de posicionamento.
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

## Tópicos relacionados

- [Extrair detalhes da marca d'água](/pdf/pt/java/extract-watermarks/)
- [Remover marcas d'água](/pdf/pt/java/remove-watermarks/)
- [Trabalhar com artefatos PDF em Java](/pdf/pt/java/artifacts/)
