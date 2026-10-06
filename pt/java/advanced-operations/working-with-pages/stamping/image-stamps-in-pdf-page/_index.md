---
title: Adicionar selos de imagem ao PDF em Java
linktitle: Selos de imagem em arquivo PDF
type: docs
weight: 10
url: /pt/java/image-stamps-in-pdf-page/
description: Aprenda como adicionar selos de imagem às páginas PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar selos de imagem e fundos de imagem às páginas PDF com Java
Abstract: Este artigo explica como adicionar carimbos de imagem a arquivos PDF usando Aspose.PDF for Java. Ele aborda carimbos de imagem com posicionamento, rotação, opacidade e controle de qualidade, e o uso de uma imagem como plano de fundo de uma caixa flutuante.
---
Aspose.PDF for Java suporta carimbos de imagem como sobreposições e elementos de layout com fundo de imagem.

## Adicionar um carimbo de imagem

Use este exemplo quando uma página deve exibir um carimbo de imagem com posicionamento e opacidade personalizados.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp/) e configure sua aparência.
1. Adicione o selo à página e salve o documento.

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

## Adicionar um carimbo de imagem com controle de qualidade

Use este exemplo quando precisar ajustar a qualidade de renderização do carimbo de imagem.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

## Usar uma imagem como fundo de uma caixa flutuante

Use este exemplo quando uma imagem deve servir como plano de fundo de um contêiner de layout estilizado.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e acesse a página de destino.
1. Crie um [FloatingBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/floatingbox/) com texto e configurações de borda.
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
