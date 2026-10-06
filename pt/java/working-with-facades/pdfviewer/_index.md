---
title: Classe PdfViewer
linktitle: Classe PdfViewer
type: docs
weight: 135
url: /pt/java/pdfviewer-class/
description: Aprenda como usar a fachada PdfViewer em Java para decodificar páginas PDF e inspecionar configurações relacionadas ao visualizador.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Decodifique páginas PDF e inspecione dados do visualizador em Java com PdfViewer
Abstract: Esta seção explica como usar a fachada PdfViewer no Aspose.PDF for Java para tarefas de decodificação de páginas e inspeção relacionada ao visualizador. Os exemplos atuais em Java cobrem a renderização de todas as páginas em imagens, a decodificação de uma página específica e a inspeção da contagem de páginas, tipo de coordenada, resolução e configurações do visualizador vinculadas.
---
O Java `PdfViewerExamples` A classe demonstra os principais fluxos de trabalho do visualizador disponíveis através da API Facades.

## Decodificar todas as páginas do PDF

Use este fluxo de trabalho quando cada página do PDF de origem deve ser renderizada como uma imagem.

### Etapas

1. Criar e configurar um `PdfViewer` instância.
2. Vincular o PDF de origem com `bindPdf`.
3. Chamar `decodeAllPages()` para renderizar o documento em um `BufferedImage` matriz.
4. Salve cada página decodificada em um arquivo de imagem de saída.
5. Feche o arquivo PDF vinculado.

### Exemplo Java

```java
public static void decodeAllPages(Path inputFile, Path outputDir) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        BufferedImage[] pages = viewer.decodeAllPages();
        for (int index = 0; index < pages.length; index++) {
            ImageIO.write(pages[index], "png", outputDir.resolve("decode_all_pages_" + (index + 1) + ".png").toFile());
        }
    } finally {
        viewer.closePdfFile();
    }
}
```

## Decodificar uma página PDF específica

Use este fluxo de trabalho quando apenas uma página precisar ser renderizada para uma imagem.

### Etapas

1. Criar e configurar um `PdfViewer` instância.
2. Vincule o PDF de origem.
3. Chamar `decodePage()` para a página que você deseja renderizar.
4. Salve a página decodificada em um arquivo de imagem de saída.
5. Feche o visualizador.

### Exemplo Java

```java
public static void decodeSpecificPage(Path inputFile, Path outputFile) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        ImageIO.write(viewer.decodePage(1), "png", outputFile.toFile());
    } finally {
        viewer.close();
    }
}
```

## Inspecionar metadados PDF

Use este fluxo de trabalho quando precisar de informações do documento relacionadas ao visualizador antes da renderização ou impressão.

### Etapas

1. Criar e configurar um `PdfViewer` instância.
2. Vincule o PDF de origem.
3. Leia a contagem de páginas, o tipo de coordenada e a resolução de renderização.
4. Use ou imprima os valores recuperados.
5. Feche o arquivo PDF vinculado.

### Exemplo Java

```java
public static void inspectPdfMetadata(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Coordinate type: " + viewer.getCoordinateType());
        System.out.println("Resolution: " + viewer.getResolution());
    } finally {
        viewer.closePdfFile();
    }
}
```

## Inspecionar as configurações do visualizador vinculadas

Use este fluxo de trabalho quando precisar confirmar ou ajustar o comportamento do visualizador após vincular o PDF.

### Etapas

1. Criar e configurar um `PdfViewer` instância.
2. Vincule o PDF de origem.
3. Defina opções do visualizador, como redimensionamento automático, rotação automática e visibilidade da caixa de diálogo de impressão.
4. Leia as configurações do visualizador ativo e a contagem de páginas.
5. Feche o visualizador.

### Exemplo Java

```java
public static void inspectBoundViewerSettings(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        viewer.setAutoResize(true);
        viewer.setAutoRotate(true);
        viewer.setPrintPageDialog(false);
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Print as image: " + viewer.getPrintAsImage());
        System.out.println("Auto resize: " + viewer.getAutoResize());
        System.out.println("Auto rotate: " + viewer.getAutoRotate());
    } finally {
        viewer.close();
    }
}
```
