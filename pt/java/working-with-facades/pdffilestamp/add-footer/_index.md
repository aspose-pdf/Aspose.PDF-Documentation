---
title: Adicionar rodapé ao PDF
linktitle: Adicionar rodapé ao PDF
type: docs
weight: 10
url: /pt/java/add-footer/
description: Saiba como adicionar rodapés de texto e imagem às páginas PDF em Java com a fachada PdfFileStamp.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar rodapés de texto e imagem ao PDF em Java
Abstract: Saiba como adicionar conteúdo de rodapé a documentos PDF com Aspose.PDF for Java usando a fachada PdfFileStamp. Os exemplos em Java cobrem rodapés de texto simples, rodapés de imagem carregados a partir de um fluxo e rodapés de texto com margens explícitas à esquerda, à direita e inferior.
---
## Adicionar rodapé ao PDF

Use `PdfFileStamp` quando precisar de conteúdo de rodapé repetido em todas as páginas de um documento.

### Etapas

1. Crie uma instância de `PdfFileStamp` e vincule o PDF de origem.
2. Construa o conteúdo do rodapé como `FormattedText` ou um fluxo de imagem.
3. Chame o apropriado `addFooter` sobrecarga.
4. Salve o arquivo atualizado e feche o objeto facade.

### Exemplos em Java

```java
public static void addTextFooter(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Footer");
        pdfStamper.addFooter(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageFooter(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addFooter(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addFooterWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("This footer has margins on all sides.");
        pdfStamper.addFooter(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
