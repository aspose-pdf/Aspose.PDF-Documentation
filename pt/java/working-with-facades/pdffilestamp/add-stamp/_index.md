---
title: Adicionar carimbo ao PDF
linktitle: Adicionar carimbo ao PDF
type: docs
weight: 40
url: /java/add-stamp/
description: Aprenda como adicionar um carimbo de imagem a páginas PDF em Java com a fachada PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicione carimbos de imagem ao PDF em Java
Abstract: Aprenda como adicionar conteúdo de carimbo a documentos PDF com Aspose.PDF para Java usando a fachada PdfFileStamp. O conjunto de exemplos Java atual mostra como criar um `Stamp`, vinculá-lo a um arquivo de imagem, adicioná-lo ao documento e salvar o PDF carimbado.
---
## Adicionar carimbo ao PDF

Use este fluxo de trabalho quando um carimbo baseado em imagem precisar ser aplicado ao PDF.

### Passos

1. Crie uma instância `PdfFileStamp` e vincule o PDF de origem.
2. Crie um objeto `Stamp`.
3. Vincule o carimbo a um arquivo de imagem com `bindImage`.
4. Adicione o carimbo ao documento com `addStamp`.
5. Salve a saída e feche o objeto fachada.

### Exemplo Java

```java
public static void addStampToPdf(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

A classe `PdfFileStampExamples.java` atual não inclui uma amostra Java separada para carimbos somente texto, rotação ou configuração de opacidade.
