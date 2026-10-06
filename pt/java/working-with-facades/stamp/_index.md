---
title: Classe Stamp
linktitle: Classe Stamp
type: docs
weight: 150
url: /pt/java/stamp-class/
description: Aprenda como trabalhar com a classe Stamp em Java para adicionar carimbos baseados em imagem, PDF e texto a documentos PDF.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar carimbos de imagem, PDF e texto a documentos PDF em Java
Abstract: Esta seção explica como usar a classe Stamp em conjunto com PdfFileStamp no Aspose.PDF for Java para adicionar conteúdo de carimbo reutilizável a documentos PDF. Os exemplos atuais em Java cobrem carimbos de imagem, carimbos de página PDF, carimbos de texto com um TextState personalizado, carimbos específicos de página e carimbos de imagem de fundo com configurações de opacidade, tamanho e rotação.
---
A classe Java `StampExamples` demonstra os principais fluxos de trabalho de criação de carimbos disponíveis através da API Facades.

## Adicionar um carimbo de imagem

Use este fluxo de trabalho quando um arquivo de imagem deve ser colocado no PDF como um carimbo.

### Etapas

1. Crie uma instância de `PdfFileStamp` e vincule o PDF de origem.
2. Crie um objeto `Stamp` e vincule-o ao arquivo de imagem.
3. Defina o identificador do selo e a origem da colocação.
4. Adicione o selo ao documento.
5. Salve o resultado e feche o objeto de fachada.

### Exemplo Java

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setStampId(1);
        stamp.setOrigin(36, 520);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Adicionar uma página PDF como carimbo

Use este fluxo de trabalho quando o conteúdo de outra página PDF deve ser reutilizado como conteúdo de stamp.

### Etapas

1. Crie um `PdfFileStamp` instanciar e vincule o PDF de destino.
2. Crie um objeto `Stamp`.
3. Vincule o stamp a uma página específica de outro arquivo PDF.
4. Defina o número da página de destino e a origem para a colocação.
5. Adicione o selo, salve a saída e feche o objeto fachada.

### Exemplo Java

```java
public static void addPdfPageAsStamp(Path inputFile, Path stampPdf, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindPdf(stampPdf.toString(), 1);
        stamp.setPageNumber(1);
        stamp.setOrigin(36, 250);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Adicionar um carimbo de texto com TextState

Use este fluxo de trabalho quando o carimbo deve conter texto formatado em vez de uma imagem.

### Etapas

1. Crie uma instância de `PdfFileStamp` e vincule o PDF de origem.
2. Crie um objeto `Stamp`.
3. Vincule um `FormattedText` logotipo e um personalizado `TextState` para o carimbo.
4. Defina a origem e a rotação do carimbo.
5. Adicione o selo, salve a saída e feche o objeto fachada.

### Exemplo Java

```java
public static void addTextStampWithTextState(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindLogo(createTextLogo("Approved by signing workflow"));
        stamp.bindTextState(createTextState());
        stamp.setOrigin(36, 700);
        stamp.setRotation(15.0f);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Adicionar um selo a páginas específicas

Use este workflow quando o stamp deve aparecer apenas nas páginas selecionadas em vez de em todo o documento.

### Etapas

1. Crie uma instância de `PdfFileStamp` e vincule o PDF de origem.
2. Crie um objeto `Stamp` e vincule-o a um arquivo de imagem.
3. Defina a lista de páginas alvo, a origem e o tamanho da imagem.
4. Adicione o selo ao documento.
5. Salve o resultado e feche o objeto de fachada.

### Exemplo Java

```java
public static void addStampToSpecificPages(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setPages(new int[] {1});
        stamp.setOrigin(400, 40);
        stamp.setImageSize(120, 60);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Adicionar um carimbo de imagem de fundo

Use este fluxo de trabalho quando o selo deve aparecer atrás do conteúdo da página com opacidade e rotação controladas.

### Etapas

1. Crie uma instância de `PdfFileStamp` e vincule o PDF de origem.
2. Crie um objeto `Stamp` e vincule-o ao arquivo de imagem.
3. Marque o selo como conteúdo de plano de fundo.
4. Configure opacidade, qualidade, rotação, tamanho e origem.
5. Adicione o selo, salve a saída e feche o objeto fachada.

### Exemplo Java

```java
public static void addBackgroundImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setBackground(true);
        stamp.setOpacity(0.35f);
        stamp.setQuality(90);
        stamp.setRotation(45.0f);
        stamp.setImageSize(160, 80);
        stamp.setOrigin(200, 300);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
