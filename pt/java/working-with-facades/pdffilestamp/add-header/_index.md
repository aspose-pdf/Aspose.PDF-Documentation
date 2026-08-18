---
title: Adicionar cabeçalho ao PDF
linktitle: Adicionar cabeçalho ao PDF
type: docs
weight: 20
url: /java/add-header/
description: Aprenda como adicionar cabeçalhos de texto e imagem a páginas PDF em Java com a fachada PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicione cabeçalhos de texto e imagem ao PDF em Java
Abstract: Aprenda como adicionar conteúdo de cabeçalho a documentos PDF com Aspose.PDF para Java usando a fachada PdfFileStamp. Os exemplos Java abrangem cabeçalhos de texto simples, cabeçalhos de imagem carregados de um fluxo e cabeçalhos estilizados com valores de margem explícitos.
---
## Adicionar cabeçalho ao PDF

Use `PdfFileStamp` quando precisar repetir o conteúdo do cabeçalho em cada página.

### Passos

1. Crie uma instância `PdfFileStamp` e vincule o PDF de origem.
2. Crie o conteúdo do cabeçalho como `FormattedText` ou carregue-o de um fluxo de imagem.
3. Chame a sobrecarga `addHeader` apropriada.
4. Salve a saída e feche o objeto fachada.

### Exemplos Java

```java
public static void addTextHeader(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Header");
        pdfStamper.addHeader(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageHeader(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addHeader(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addHeaderWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText(
                "Sample Header",
                Color.BLUE,
                FontStyle.Helvetica,
                EncodingType.Winansi,
                true,
                12.0f);
        pdfStamper.addHeader(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
