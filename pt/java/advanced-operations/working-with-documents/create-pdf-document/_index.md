---
title: Criar arquivos PDF em Java
linktitle: Criar documento PDF
type: docs
weight: 10
url: /pt/java/create-pdf-document/
description: Aprenda a criar arquivos PDF e a gerar PDFs pesquisáveis em Java usando o Aspose.PDF.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crie arquivos PDF e documentos PDF pesquisáveis com Java
Abstract: Este artigo mostra como criar documentos PDF usando Aspose.PDF for Java. Ele cobre a criação de um novo PDF do zero e a conversão de um documento baseado em imagem em um PDF pesquisável, fornecendo a saída HOCR de um motor OCR externo.
---
Aspose.PDF for Java oferece suporte tanto à criação simples de documentos quanto a fluxos de trabalho de PDF pesquisáveis assistidos por OCR.

## Criar um novo documento PDF

Use esta abordagem quando precisar gerar um arquivo PDF simples do zero.

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicionar um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) para o documento.
1. Criar um [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) e adicione-o à página.
1. Salvar o PDF de saída [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## Criar um PDF pesquisável

O `createSearchablePdf` exemplos de uso `Document.convert(...)` com um `CallBackGetHocr` implementação. O callback grava a imagem de origem em um arquivo temporário, invoca o Tesseract com o `hocr` opção, lê a marcação HOCR gerada e a retorna ao Aspose.PDF.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Criar o `CallBackGetHocr` callback e converta o documento de origem em conteúdo PDF pesquisável.
1. Salvar o PDF atualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createSearchablePdf(Path inputFile, Path outputFile) {
    Path tempDir = outputFile.getParent().resolve("ocr-temp");
    CallBackGetHocr cbgh = new CallBackGetHocr() {
        @Override
        public String invoke(java.awt.image.BufferedImage img) {
            // save the image, run Tesseract with "hocr", and return the HOCR text
            return fileContents.toString();
        }
    };
    try (Document document = new Document(inputFile.toString())) {
        document.convert(cbgh);
        document.save(outputFile.toString());
    }
}
```

## Obter configurações da janela do documento

Use este exemplo para inspecionar as preferências de visualização atuais armazenadas em um documento PDF existente.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Leia as propriedades de janela e exibição necessárias do documento.
1. Exiba as configurações atuais para inspeção ou depuração.

```java
public static void getDocumentWindow(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("CenterWindow: " + document.isCenterWindow());
        System.out.println("Direction: " + document.getDirection());
        System.out.println("DisplayDocTitle: " + document.isDisplayDocTitle());
        System.out.println("FitWindow: " + document.isFitWindow());
        System.out.println("HideMenuBar: " + document.isHideMenubar());
        System.out.println("HideToolBar: " + document.isHideToolBar());
        System.out.println("HideWindowUI: " + document.isHideWindowUI());
        System.out.println("NonFullScreenPageMode: " + document.getNonFullScreenPageMode());
        System.out.println("PageLayout: " + document.getPageLayout());
        System.out.println("PageMode: " + document.getPageMode());
    }
}
```

## Definir preferências da janela do documento

Este exemplo atualiza como o PDF deve ser exibido quando aberto em um visualizador compatível.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Defina as preferências de janela, layout e modo de página necessárias.
1. Salvar o PDF atualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void setDocumentWindow(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setCenterWindow(true);
        document.setDirection(Direction.R2L);
        document.setDisplayDocTitle(true);
        document.setFitWindow(true);
        document.setHideMenubar(true);
        document.setHideToolBar(true);
        document.setHideWindowUI(true);
        document.setNonFullScreenPageMode(PageMode.UseOC);
        document.setPageLayout(PageLayout.TwoColumnLeft);
        document.setPageMode(PageMode.UseThumbs);
        document.save(outputFile.toString());
    }
}
```

## Incorporar fontes em um PDF existente

Use esta abordagem quando um documento deve conter as fontes necessárias para uma renderização mais confiável em outros sistemas.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Habilite a incorporação padrão de font e itere pelas fonts usadas por cada [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Marque qualquer não incorporado [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) objetos para incorporação.
1. Salvar o documento atualizado.

```java
public static void embeddedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setEmbedStandardFonts(true);
        for (Page page : document.getPages()) {
            for (Font pageFont : page.getResources().getFonts()) {
                if (!pageFont.isEmbedded()) {
                    pageFont.setEmbedded(true);
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Incorporar fontes ao criar um novo PDF

Este exemplo cria um novo PDF e atribui uma fonte incorporada ao conteúdo de texto desde o início.

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Crie o necessário [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/), e [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Resolva o alvo [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) do repositório e marcá-lo como incorporado.
1. Adicione o conteúdo de texto à página e salve o documento de saída.

```java
public static void embeddedFontsInNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            TextFragment fragment = new TextFragment("");
            TextSegment segment = new TextSegment(" This is a sample text using Custom font.");
            TextState textState = new TextState();
            Font font = FontRepository.findFont("Arial");
            font.setEmbedded(true);
            textState.setFont(font);
            segment.setTextState(textState);
            fragment.getSegments().add(segment);
            page.getParagraphs().add(fragment);
        }
        document.save(outputFile.toString());
    }
}
```

## Defina uma fonte padrão para saída PDF

Use este padrão quando o documento salvo deve voltar a uma fonte específica durante a geração da saída.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Criar [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) e definir o nome da fonte padrão.
1. Salve o documento com as opções de salvamento configuradas.

```java
public static void setDefaultFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfSaveOptions saveOptions = new PdfSaveOptions();
        saveOptions.setDefaultFontName("Arial");
        document.save(outputFile.toString(), saveOptions);
    }
}
```

## Obter todas as fontes usadas em um PDF

Este exemplo lista todas as fontes detectadas no documento para que você possa auditar o uso de fontes antes de exportar ou atualizar o arquivo.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enumerar as fontes retornadas pelas utilidades de fontes do documento.
1. Exiba o nome de cada detectado [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## Melhorar a incorporação de fontes por subdefinição de fontes

Use esta abordagem quando quiser reduzir a carga da fonte enquanto mantém os dados da fonte incorporada alinhados com o uso do documento.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Execute a subdefinição de fontes através dos utilitários de fontes do documento com o necessário [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) valores.
1. Salve o documento otimizado.

```java
public static void improveFontsEmbedding(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
        document.save(outputFile.toString());
    }
}
```

## Definir o fator de zoom ao abrir o documento

Este exemplo configura o nível de zoom inicial que deve ser aplicado quando o PDF for aberto.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Criar um [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) com um [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Atribua a ação como a ação de abertura do documento e salve o resultado.

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## Obtenha o fator de zoom ao abrir o documento

Use este exemplo para inspecionar se um PDF já define um nível de zoom explícito para sua ação de abertura.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Verifique se a ação de abertura é um [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) com um [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Exiba o valor de zoom configurado ou informe que nenhum zoom está definido.

```java
public static void getZoomFactor(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getOpenAction() instanceof GoToAction action
                && action.getDestination() instanceof XYZExplicitDestination destination) {
            System.out.println("Zoom: " + destination.getZoom());
        } else {
            System.out.println("Zoom: not set");
        }
    }
}
```
