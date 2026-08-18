---
title: Adicione carimbos de imagem a PDF em Java
linktitle: Carimbos de imagem em arquivo PDF
type: docs
weight: 10
url: /java/image-stamps-in-pdf-page/
description: Aprenda como adicionar carimbos de imagem a páginas PDF em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicione carimbos e fundos de imagens a páginas PDF com Java
Abstract: Este artigo explica como adicionar carimbos de imagem a arquivos PDF usando Aspose.PDF para Java. Abrange carimbos de imagem com posicionamento, rotação, opacidade e controle de qualidade, além de usar uma imagem como fundo de uma caixa flutuante.
---
Aspose.PDF para Java oferece suporte a carimbos de imagem como sobreposições e elementos de layout baseados em imagem.

## Adicione um carimbo de imagem

Use este exemplo quando uma página exibir um carimbo de imagem com posicionamento e opacidade personalizados.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) e configure sua aparência.
1. Adicione o carimbo à página e salve o documento.

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(300);
        imageStamp.setWidth(300);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## Adicione um carimbo de imagem com controle de qualidade

Use este exemplo quando precisar ajustar a qualidade de renderização do carimbo de imagem.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) e defina o valor da qualidade.
1. Adicione o carimbo à página e salve o resultado.

```java
public static void addImageStampWithQualityControl(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImageStamp imageStamp = new ImageStamp(imageFile.toString());
        imageStamp.setQuality(10);
        document.getPages().get_Item(1).addStamp(imageStamp);
        document.save(outputFile.toString());
    }
}
```

## Use uma imagem como fundo de caixa flutuante

Use este exemplo quando uma imagem deve servir como plano de fundo de um contêiner de layout estilizado.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e acesse a página de destino.
1. Crie uma [FloatingBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/floatingbox/) com configurações de texto e borda.
1. Defina a imagem de fundo, adicione a caixa à página e salve o documento.

```java
public static void addImageAsBackgroundInFloatingBox(Path inputFile, Path imageFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        FloatingBox box = new FloatingBox(200.0f, 100.0f);
        box.setLeft(40);
        box.setTop(80);
        box.setHorizontalAlignment(HorizontalAlignment.Center);
        box.getParagraphs().add(new TextFragment("Text in Floating Box"));
        box.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Image image = new Image();
        image.setFile(imageFile.toString());
        box.setBackgroundImage(image);
        box.setBackgroundColor(Color.getYellow());
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```
