---
title: Adicionar número de página ao PDF
linktitle: Adicionar número de página ao PDF
type: docs
weight: 30
url: /pt/java/page-number/
description: Saiba como adicionar números de página a documentos PDF em Java com a fachada PdfFileStamp.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar números de página ao PDF em Java
Abstract: Saiba como adicionar números de página a documentos PDF com Aspose.PDF for Java usando a fachada PdfFileStamp. Os exemplos em Java cobrem posicionamento padrão, coordenadas explícitas, posicionamento alinhado com margens e saída em numeração romana com um número inicial personalizado.
---
## Adicionar número de página ao PDF

Usar `PdfFileStamp` quando a numeração de páginas deve ser aplicada após o conteúdo do PDF já ter sido criado.

### Etapas

1. Criar um `PdfFileStamp` instancie e vincule o PDF de origem.
2. Escolha a estratégia de posicionamento de número de página que você precisar.
3. Opcionalmente, defina o estilo de numeração e o número inicial antes de aplicar o carimbo.
4. Chamar `addPageNumber` com a sobrecarga necessária.
5. Salve a saída e feche o objeto fachada.

### Exemplos Java

```java
public static void addPageNumbersDefault(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #");
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersAtCoordinates(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", 300, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithPositionAndMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_BOTTOM_RIGHT, 10, 10, 10, 10);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithRomanStyle(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pdfStamper.setStartingNumber(42);
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_UPPER_RIGHT);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
