---
title: Converter formatos de imagem para PDF em Java
linktitle: Converter imagens para PDF
type: docs
weight: 60
url: /pt/java/convert-images-format-to-pdf/
lastmod: "2026-10-06"
description: Aprenda como converter BMP, CGM, DICOM, PNG, TIFF, EMF, SVG, CDR e outros formatos de imagem para PDF em Java com Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Converter imagens para PDF em Java
Abstract: Este artigo explica como converter vários formatos de imagem para PDF usando Aspose.PDF for Java. Ele cobre a inserção direta de imagens em uma nova página PDF, bem como opções de carregamento específicas para cada tipo de arquivo para entradas CGM, SVG e CDR.
---
Aspose.PDF for Java pode converter muitos formatos de imagem raster e vetoriais em documentos PDF.

## Converter BMP para PDF

Use este exemplo quando uma imagem BMP deve ser inserida em um documento PDF.

1. Crie um objeto [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio para armazenar o PDF de saída.
1. Adicione um [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e coloque o BMP com `page.addImage(...)`.
1. Defina o retângulo de imagem de destino com [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/); assim, o conteúdo raster preenche a área da página PDF.
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

## Converter CGM para PDF

Use este exemplo quando um arquivo gráfico CGM deve ser convertido em PDF.

1. Abra a origem CGM passando o caminho do arquivo e [`CgmLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) para o [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) construtor.
1. Permita que o Aspose.PDF interprete o fluxo de gráficos CGM durante o carregamento do documento.
1. Salve o PDF convertido no caminho de saída de destino.

```java
public static void convertCgmToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CgmLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter DICOM para PDF

Use este exemplo quando uma imagem DICOM médica deve ser incorporada em um documento PDF.

1. Crie um objeto [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio para a saída PDF.
1. Crie um objeto [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), defina o seu [`ImageFileType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/) para `Dicom`, e atribua o caminho do arquivo de origem.
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

## Converter EMF para PDF com carregamento direto de documento

Use este exemplo quando um arquivo EMF deve ser convertido em PDF através do caminho principal de carregamento de EMF.

1. Crie um objeto [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio e abra a fonte EMF como um fluxo binário.
1. Adicione um [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e limpe suas margens para que a arte EMF possa ocupar toda a área da página.
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

## Converter EMF para PDF com um fluxo de trabalho alternativo

Use este exemplo quando o conteúdo EMF deve ser convertido usando uma configuração alternativa ou fluxo de composição de página.

1. Carregue a fonte EMF com Aspose.Imaging e renderize-a em um fluxo PNG em memória antes da colocação no PDF.
1. Crie um objeto [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio e adicione um [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
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

## Converter GIF para PDF

Use este exemplo quando uma imagem GIF deve ser adicionada a uma página PDF.

1. Crie um objeto [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio para a saída PDF.
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

## Converter JPEG para PDF

Use este exemplo quando uma imagem JPEG deve ser convertida em um PDF de uma página.

1. Crie um objeto [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio para o PDF de saída.
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

## Converter PNG para PDF

Use este exemplo quando uma imagem PNG deve ser envolvida em um documento PDF.

1. Crie um objeto [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio para a saída da conversão.
1. Adicione um [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e coloque a imagem PNG nele com `page.addImage(...)`.
1. Use [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) dimensionar a imagem em relação à tela da página.
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

## Converter SVG para PDF

Use este exemplo quando a arte SVG deve ser renderizada dentro de um documento PDF.

1. Abra a fonte SVG passando o caminho do arquivo e [`SvgLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/) para o [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) construtor.
1. Deixe o Aspose.PDF analisar a marcação SVG e criar o modelo gráfico PDF correspondente durante o carregamento.
1. Salve a saída PDF no caminho de destino do arquivo.

```java
public static void convertSvgToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new SvgLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Converter TIFF para PDF

Use este exemplo quando uma imagem TIFF deve ser convertida em PDF.

1. Crie um objeto [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vazio para a saída PDF.
1. Adicione um [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e coloque a imagem TIFF com `page.addImage(...)`.
1. Defina a área de posicionamento com [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/); assim, o conteúdo TIFF é mapeado para as coordenadas da página.
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

## Converter CDR para PDF

Use este exemplo quando um arquivo CorelDRAW CDR deve ser convertido em PDF.

1. Abra a fonte CDR passando o caminho do arquivo e [`CdrLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cdrloadoptions/) para o [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) construtor.
1. Permita que o Aspose.PDF carregue o conteúdo do CorelDRAW no modelo de documento PDF.
1. Salve o arquivo PDF convertido no caminho de saída solicitado.

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
