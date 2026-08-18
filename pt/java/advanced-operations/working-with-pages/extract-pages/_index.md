---
title: Extraia páginas PDF em Java
linktitle: Extraindo páginas PDF
type: docs
weight: 80
url: /java/extract-pages/
description: Aprenda como extrair uma ou várias páginas PDF em novos arquivos em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraia páginas PDF em novos documentos com Java
Abstract: Este artigo explica como extrair páginas de arquivos PDF usando Aspose.PDF para Java. Abrange a cópia de uma única página e a extração de várias páginas em um documento de destino separado usando indexação de página baseada em 1.
---
Aspose.PDF for Java permite copiar páginas selecionadas em um novo documento de destino.

## Extraia uma única página

Use este exemplo quando precisar salvar uma página do PDF de origem em um documento separado.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e crie um documento de destino.
1. Copie a página de destino na coleção de páginas de destino.
1. Salve o novo PDF.

```java
public static void extractPage(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        dstDocument.getPages().add(srcDocument.getPages().get_Item(2));
        dstDocument.save(outputFile.toString());
    }
}
```

## Extraia várias páginas

Use este exemplo quando precisar copiar várias páginas em um PDF separado.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e crie um documento de destino.
1. Itere pelos índices de páginas selecionados e adicione-os ao destino.
1. Salve o documento de páginas extraídas.

```java
public static void extractBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        Integer[] pages = {2, 3};
        for (Integer pageIndex : pages) {
            anotherDocument.getPages().add(document.getPages().get_Item(pageIndex));
        }
        anotherDocument.save(outputFile.toString());
    }
}
```
