---
title: Mesclar arquivos PDF em Java
linktitle: Mesclar arquivos PDF
type: docs
weight: 50
url: /pt/java/merge-pdf-documents/
description: Aprenda como mesclar vários arquivos PDF em um único documento em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combine documentos completos, intervalos selecionados e páginas alternadas com Java
Abstract: Este artigo explica como mesclar documentos PDF usando Aspose.PDF for Java. Ele cobre a combinação de dois arquivos, mesclando vários documentos, selecionando intervalos de páginas, inserindo um documento em outro em uma posição específica, alternando páginas e construindo a saída mesclada com marcadores de seção.
---
Aspose.PDF for Java suporta várias estratégias de mesclagem dependendo de como a saída deve ser montada.

## Mesclar dois documentos PDF

Use esta abordagem quando precisar do fluxo de mesclagem mais simples e quiser anexar um documento completo a outro.

1. Abra ambos os PDFs de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objetos.
1. Adicionar o [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) coleção do segundo documento para o primeiro documento.
1. Salvar o PDF atualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```

## Copiar um intervalo de páginas selecionado entre documentos

Este método auxiliar mantém a lógica de mesclagem de intervalo de páginas em um só lugar, para que outros exemplos possam reutilizar a mesma rotina de cópia validada.

1. Abrir ou receber o PDF de origem e destino [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objetos.
1. Normalize o intervalo de páginas solicitado para que permaneça dentro do disponível [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) coleção.
1. Adicione cada página do intervalo validado ao documento de destino.

```java
private static void appendPageRange(Document sourceDocument, Document destinationDocument, int startPage, int endPage) {
    int totalPages = sourceDocument.getPages().size();
    if (totalPages == 0) {
        return;
    }

    int start = Math.max(1, startPage);
    int end = Math.min(endPage, totalPages);
    if (start > end) {
        return;
    }

    for (int pageNumber = start; pageNumber <= end; pageNumber++) {
        destinationDocument.getPages().add(sourceDocument.getPages().get_Item(pageNumber));
    }
}
```

## Mesclar vários documentos PDF em um único arquivo

Use este padrão quando precisar combinar uma lista de arquivos de entrada em um único documento de saída em sequência.

1. Criar um PDF de saída vazio [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Abra cada arquivo de entrada um de cada vez e copie todo o seu conteúdo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) intervalo no documento de saída.
1. Salve o resultado mesclado depois que todos os arquivos de origem forem processados.

```java
public static void mergeMultipleDocuments(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                appendPageRange(sourceDocument, outputDocument, 1, sourceDocument.getPages().size());
            }
        }
        outputDocument.save(outputFile.toString());
    }
}
```

## Mesclar intervalos de páginas selecionados de dois documentos

Este exemplo cria um arquivo de saída personalizado ao selecionar apenas intervalos de páginas específicos de cada documento de origem.

1. Abra ambos os PDFs de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objetos e criar um novo documento de saída.
1. Adicione apenas o necessário [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) intervalos de cada documento de origem.
1. Salve o documento de saída montado.

```java
public static void mergeSelectedPageRanges(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        appendPageRange(document1, outputDocument, 1, 2);
        appendPageRange(document2, outputDocument, 2, 3);
        outputDocument.save(outputFile.toString());
    }
}
```

## Inserir um documento PDF em outro em uma posição específica

Use esta abordagem quando um documento deve aparecer dentro de outro, em vez de apenas antes ou depois dele.

1. Abra o PDF base e o PDF inserido [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objetos e criar um novo documento de saída.
1. Copie a primeira parte do documento base, depois adicione o documento inserido completo e, por fim, adicione o restante do documento base. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) intervalo.
1. Salve o resultado reordenado em um novo arquivo.

```java
public static void mergeInsertDocumentAtPosition(Path inputFile1, Path inputFile2, int insertAfterPage, Path outputFile) {
    try (Document baseDocument = new Document(inputFile1.toString());
         Document insertDocument = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int baseTotalPages = baseDocument.getPages().size();
        int insertIndex = Math.max(0, Math.min(insertAfterPage, baseTotalPages));

        appendPageRange(baseDocument, outputDocument, 1, insertIndex);
        appendPageRange(insertDocument, outputDocument, 1, insertDocument.getPages().size());
        appendPageRange(baseDocument, outputDocument, insertIndex + 1, baseTotalPages);

        outputDocument.save(outputFile.toString());
    }
}
```

## Mesclar dois documentos PDF alternando páginas

Este exemplo intercala páginas de dois documentos, o que é útil quando ambas as entradas devem contribuir página por página para a saída final.

1. Abra ambos os PDFs de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objetos e criar um novo documento de saída.
1. Percorra a contagem máxima de páginas disponíveis e adicione cada uma disponível [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) do primeiro e do segundo documentos, respectivamente.
1. Salvar o documento de saída intercalado.

```java
public static void mergeAlternatingPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int document1Pages = document1.getPages().size();
        int document2Pages = document2.getPages().size();
        int maxPages = Math.max(document1Pages, document2Pages);

        for (int pageNumber = 1; pageNumber <= maxPages; pageNumber++) {
            if (pageNumber <= document1Pages) {
                outputDocument.getPages().add(document1.getPages().get_Item(pageNumber));
            }
            if (pageNumber <= document2Pages) {
                outputDocument.getPages().add(document2.getPages().get_Item(pageNumber));
            }
        }

        outputDocument.save(outputFile.toString());
    }
}
```

## Mesclar documentos com páginas separadoras e marcadores

Use este padrão quando o arquivo mesclado precisar permanecer fácil de navegar e mostrar claramente onde cada documento de origem começa.

1. Criar um PDF de saída vazio [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e abra cada arquivo fonte por sua vez.
1. Adicionar um separador [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) com um título, então crie um [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) marcador para essa seção.
1. Anexe as páginas de origem, opcionalmente adicione um marcador que aponta para a primeira página de conteúdo e salve o documento final mesclado.

```java
public static void mergeWithSectionSeparatorsAndBookmarks(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        int sectionIndex = 1;
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                int sourcePageCount = sourceDocument.getPages().size();

                Page separatorPage = outputDocument.getPages().add();
                separatorPage.getParagraphs().add(new TextFragment(
                        "Section " + sectionIndex + ": " + inputFile.getFileName()));

                OutlineItemCollection sectionBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                sectionBookmark.setTitle("Section " + sectionIndex);
                sectionBookmark.setAction(new GoToAction(separatorPage));
                outputDocument.getOutlines().add(sectionBookmark);

                int firstContentPageNumber = outputDocument.getPages().size() + 1;
                appendPageRange(sourceDocument, outputDocument, 1, sourcePageCount);

                if (sourcePageCount > 0 && firstContentPageNumber <= outputDocument.getPages().size()) {
                    OutlineItemCollection contentBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                    contentBookmark.setTitle("Section " + sectionIndex + " Content");
                    contentBookmark.setAction(new GoToAction(outputDocument.getPages().get_Item(firstContentPageNumber)));
                    sectionBookmark.add(contentBookmark);
                }
            }
            sectionIndex++;
        }

        outputDocument.save(outputFile.toString());
    }
}
```
