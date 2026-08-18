---
title: Converta formatos de imagem em PDF em Java
linktitle: Converter imagens em PDF
type: docs
weight: 60
url: /java/convert-images-format-to-pdf/
lastmod: "2026-06-16"
description: Aprenda como converter BMP, CGM, DICOM, PNG, TIFF, EMF, SVG, CDR e outros formatos de imagem para PDF em Java com Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Como converter imagens em PDF em Java
Abstract: Este artigo explica como converter vários formatos de imagem em PDF usando Aspose.PDF para Java. Ele cobre o posicionamento direto da imagem em uma nova página PDF, bem como opções de carregamento específicas do tipo de arquivo para entradas CGM, SVG e CDR.
---
Aspose.PDF para Java pode converter muitos formatos de imagem raster e vetorial em documentos PDF.

## Converter BMP em PDF

Use este exemplo quando uma imagem BMP precisar ser colocada em um documento PDF.

1. Crie um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio para armazenar o PDF de saída.
1. Adicione um [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e coloque o BMP com `page.addImage(...)`.
1. Defina o retângulo da imagem de destino com [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) para que o conteúdo raster preencha a área da página PDF.
1. Salve o arquivo PDF de saída.

```java
public static void convertBmpToPdf(Path inputFile, Path outputFile) {
        try (Document document = new Document()) {
            try (Page page = document.getPages().add()) {
                page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
            }
            document.save(outputFile.toString());
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## Converter CGM em PDF

Use este exemplo quando um arquivo gráfico CGM precisar ser convertido em PDF.

1. Abra a fonte CGM passando o caminho do arquivo e [`CgmLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) para o construtor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Deixe o Aspose.PDF interpretar o fluxo gráfico CGM durante o carregamento do documento.
1. Salve o PDF convertido no caminho de saída de destino.

```java
public static void convertCgmToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CgmLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter DICOM em PDF

Use este exemplo quando uma imagem DICOM médica precisar ser agrupada em um documento PDF.

1. Crie um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio para a saída do PDF.
1. Crie um objeto [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), defina seu [`ImageFileType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/) como `Dicom` e atribua o caminho do arquivo de origem.
1. Adicione um [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e anexe a imagem DICOM à coleção de parágrafos da página.
1. Salve o resultado como PDF.

```java
public static void convertDicomToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setFile(inputFile.toString());

        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta EMF em PDF com carregamento direto de documentos

Use este exemplo quando um arquivo EMF precisar ser convertido em PDF por meio do caminho de carregamento EMF primário.

1. Crie um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio e abra a fonte EMF como um fluxo binário.
1. Adicione um [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e limpe suas margens para que a arte do EMF possa ocupar toda a área da página.
1. Crie um [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), vincule o fluxo EMF a ele e adicione-o à coleção de parágrafos da página.
1. Salve o arquivo PDF de saída.

```java
public static void convertEmfToPdf01(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         FileInputStream imageStream = new FileInputStream(inputFile.toFile())) {
        try (Page page = document.getPages().add()) {
            page.getPageInfo().getMargin().setBottom(0);
            page.getPageInfo().getMargin().setTop(0);
            page.getPageInfo().getMargin().setLeft(0);
            page.getPageInfo().getMargin().setRight(0);

            Image image = new Image();
            image.setFileType(ImageFileType.Unknown);
            image.setImageStream(imageStream);
            page.getParagraphs().add(image);
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converta EMF em PDF com um fluxo de trabalho alternativo

Use este exemplo quando o conteúdo EMF precisar ser convertido usando uma configuração alternativa ou um fluxo de composição de página.

1. Carregue a fonte EMF com Aspose.Imaging e renderize-a em um fluxo PNG na memória antes de colocar o PDF.
1. Crie um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio e adicione um [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Crie um [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) do fluxo de bytes intermediário e adicione-o à página.
1. Salve o PDF convertido.

```java
public static void convertEmfToPdf02(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         com.aspose.imaging.Image emfImage = com.aspose.imaging.Image.load(inputFile.toString());
         ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream()) {
        emfImage.save(byteArrayOutputStream, new PngOptions());

        try (Page page = document.getPages().add()) {
            Image image = new Image();
            image.setImageStream(new ByteArrayInputStream(byteArrayOutputStream.toByteArray()));
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter GIF em PDF

Use este exemplo quando uma imagem GIF precisar ser adicionada a uma página PDF.

1. Crie um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio para a saída do PDF.
1. Adicione um [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e coloque o GIF com `page.addImage(...)`.
1. Defina os limites de posicionamento com [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) para que a imagem preencha a área da página.
1. Salve o PDF de saída.

```java
public static void convertGifToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter JPEG em PDF

Use este exemplo quando uma imagem JPEG precisar ser convertida em um PDF de uma página.

1. Crie um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio para o PDF de saída.
1. Adicione um [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e insira a imagem JPEG com `page.addImage(...)`.
1. Use [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) para controlar como a imagem raster é mapeada para as coordenadas da página.
1. Salve o arquivo PDF gerado.

```java
public static void convertJpegToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter PNG em PDF

Use este exemplo quando uma imagem PNG precisar ser agrupada em um documento PDF.

1. Crie um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio para a saída de conversão.
1. Adicione um [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e coloque a imagem PNG nele com `page.addImage(...)`.
1. Use [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) para dimensionar a imagem em relação à tela da página.
1. Salve o arquivo de saída.

```java
public static void convertPngToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter SVG em PDF

Use este exemplo quando a arte SVG precisar ser renderizada dentro de um documento PDF.

1. Abra a fonte SVG passando o caminho do arquivo e [`SvgLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/) para o construtor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Deixe o Aspose.PDF analisar a marcação SVG e criar o modelo gráfico PDF correspondente durante o carregamento.
1. Salve a saída do PDF no caminho do arquivo de destino.

```java
public static void convertSvgToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new SvgLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter TIFF em PDF

Use este exemplo quando uma imagem TIFF precisar ser convertida em PDF.

1. Crie um [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio para a saída do PDF.
1. Adicione um [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e coloque a imagem TIFF com `page.addImage(...)`.
1. Defina a área de posicionamento com [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) para que o conteúdo TIFF seja mapeado para as coordenadas da página.
1. Salve o resultado como PDF.

```java
public static void convertTiffToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter CDR em PDF

Use este exemplo quando um arquivo CDR do CorelDRAW precisar ser convertido em PDF.

1. Abra a fonte do CDR passando o caminho do arquivo e [`CdrLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cdrloadoptions/) para o construtor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Deixe o Aspose.PDF carregar o conteúdo do CorelDRAW no modelo de documento PDF.
1. Salve o arquivo PDF convertido no caminho de saída solicitado.

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
