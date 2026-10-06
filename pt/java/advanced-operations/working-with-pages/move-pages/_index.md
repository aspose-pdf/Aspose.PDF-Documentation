---
title: Mover páginas PDF em Java
linktitle: Movendo páginas PDF
type: docs
weight: 100
url: /pt/java/move-pages/
description: Aprenda como mover páginas PDF dentro de um documento ou entre documentos em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mover páginas PDF entre documentos em Java
Abstract: Este artigo explica como mover páginas em PDFs usando Aspose.PDF for Java. Ele aborda mover uma única página ou várias páginas para outro documento e reposicionar uma página dentro do mesmo PDF.
---
Aspose.PDF for Java permite mover páginas entre documentos ou reposicionar páginas dentro do mesmo PDF.

## Mover uma página para outro documento

Use este exemplo quando uma única página deve ser removida do PDF de origem e salva em um documento separado.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e crie um documento de destino.
1. Adicione a página alvo ao destino e exclua-a da origem.
1. Salve ambos os documentos.

```java
public static void movePageFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        anotherDocument.getPages().add(document.getPages().get_Item(2));
        document.getPages().delete(2);
        document.save(sourceOutputFile.toString());
        anotherDocument.save(outputFile.toString());
    }
}
```

## Mover várias páginas para outro documento

Use este exemplo quando várias páginas devem ser transferidas do PDF de origem para um novo documento.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e crie o documento de destino.
1. Copie as páginas selecionadas para o documento de destino.
1. Exclua as páginas movidas da origem e salve ambos os arquivos.

```java
public static void moveBunchPagesFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        Integer[] pages = {1, 2};
        for (Integer pageIndex : pages) {
            dstDocument.getPages().add(srcDocument.getPages().get_Item(pageIndex));
        }
        dstDocument.save(outputFile.toString());
        srcDocument.getPages().delete(pages);
        srcDocument.save(sourceOutputFile.toString());
    }
}
```

## Mover uma página dentro do mesmo documento

Use este exemplo quando uma página precisar ser reposicionada para um novo local no mesmo PDF.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Duplique a página de destino para a nova posição e remova a entrada da página original.
1. Salve o documento reordenado.

```java
public static void movePageInNewLocationInSameDocument(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString())) {
        srcDocument.getPages().add(srcDocument.getPages().get_Item(2));
        srcDocument.getPages().delete(2);
        srcDocument.save(outputFile.toString());
    }
}
```
