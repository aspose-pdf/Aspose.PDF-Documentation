---
title: Adicionar rodapé ao PDF
linktitle: Adicionar rodapé ao PDF
type: docs
weight: 10
url: /java/add-footer/
description: Aprenda como adicionar rodapés de texto e imagem a páginas PDF em Java com a fachada PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicione rodapés de texto e imagem a PDF em Java
Abstract: Aprenda como adicionar conteúdo de rodapé a documentos PDF com Aspose.PDF para Java usando a fachada PdfFileStamp. Os exemplos Java abrangem rodapés de texto simples, rodapés de imagens carregados de um fluxo e rodapés de texto com margens esquerda, direita e inferior explícitas.
---
## Adicionar rodapé ao PDF

Use `PdfFileStamp` quando precisar repetir o conteúdo do rodapé em todas as páginas de um documento.

### Passos

1. Crie uma instância `PdfFileStamp` e vincule o PDF de origem.
2. Crie o conteúdo do rodapé como `FormattedText` ou como um fluxo de imagem.
3. Chame a sobrecarga `addFooter` apropriada.
4. Salve o arquivo atualizado e feche o objeto fachada.

### Exemplos Java

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
