---
title: Adicionar Selos de Página ao PDF em Java
linktitle: Adicionar Selos de Página
type: docs
weight: 30
url: /pt/java/page-stamps-in-the-pdf-file/
description: Aprenda como adicionar selos de página PDF como sobreposições ou planos de fundo em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar selos baseados em página a arquivos PDF com Java
Abstract: Este artigo explica como adicionar um carimbo de página a um documento PDF usando Aspose.PDF for Java. O exemplo carrega outra página PDF como um carimbo, a configura como plano de fundo e a aplica a uma página de destino.
---
Aspose.PDF for Java pode aplicar uma página de outro PDF como um carimbo ou adicionar sobreposições de numeração de página.

## Adicionar um carimbo de página de outro PDF

Use este exemplo quando uma página de um PDF separado deve ser usada como um carimbo de plano de fundo.

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Criar um [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfpagestamp/) da página PDF externa.
1. Configure o selo e adicione‑o à página de destino, então salve o resultado.

```java
public static void addPageStamp(Path inputFile, Path pageStampFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfPageStamp pageStamp = new PdfPageStamp(pageStampFile.toString(), 1);
        pageStamp.setBackground(true);
        document.getPages().get_Item(1).addStamp(pageStamp);
        document.save(outputFile.toString());
    }
}
```

## Adicionar um carimbo de número de página padrão

Use este exemplo quando a página de destino deve mostrar o número atual com formatação de texto personalizada.

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Criar e configurar um [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/).
1. Adicione o selo à página e salve o documento.

```java
public static void addPageNumStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + document.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        document.getPages().get_Item(1).addStamp(pageNumberStamp);
        document.save(outputFile.toString());
    }
}
```

## Adicionar um carimbo de número de página em numeral romano

Use este exemplo quando a numeração de páginas deve começar a partir de um valor personalizado e usar numerais romanos maiúsculos.

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Criar um [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) e configure a numeração em numerais romanos.
1. Adicione o selo a todas as páginas e salve o PDF.

```java
public static void addPageNumStampRoman(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(42);
        pageNumberStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        for (Page page : document.getPages()) {
            page.addStamp(pageNumberStamp);
        }
        document.save(outputFile.toString());
    }
}
```
