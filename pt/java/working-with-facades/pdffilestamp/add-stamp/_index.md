---
title: Adicionar carimbo ao PDF
linktitle: Adicionar carimbo ao PDF
type: docs
weight: 40
url: /pt/java/add-stamp/
description: Aprenda como adicionar um carimbo de imagem às páginas PDF em Java com a fachada PdfFileStamp.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar carimbos de imagem ao PDF em Java
Abstract: Aprenda como adicionar conteúdo de carimbo a documentos PDF com Aspose.PDF for Java usando a fachada PdfFileStamp. O conjunto atual de exemplos em Java demonstra como criar um `Stamp`, vinculá-lo a um arquivo de imagem, adicioná-lo ao documento e salvar o PDF carimbado.
---
## Adicionar carimbo ao PDF

Use este fluxo de trabalho quando um carimbo baseado em imagem deve ser aplicado ao PDF.

### Etapas

1. Criar um `PdfFileStamp` instância e vincule o PDF de origem.
2. Criar um `Stamp` objeto.
3. Vincular o carimbo a um arquivo de imagem com `bindImage`.
4. Adicionar o selo ao documento com `addStamp`.
5. Salve o resultado e feche o objeto fachada.

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

O atual `PdfFileStampExamples.java` a classe não inclui um exemplo Java separado para selos apenas de texto, rotação ou configuração de opacidade.
