---
title: Dividir arquivos PDF em Java
linktitle: Dividir arquivos PDF
type: docs
weight: 60
url: /java/split-pdf-document/
description: Aprenda como dividir páginas PDF em arquivos PDF separados em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Divida documentos PDF por páginas, intervalos, grupos e padrões de nome de arquivo usando Java
Abstract: Este artigo explica como dividir documentos PDF usando Aspose.PDF para Java. Abrange a divisão em páginas únicas, duas ou três partes, páginas pares e ímpares, pedaços de tamanho fixo, intervalos personalizados, primeira ou última página mais o resto, grupos de páginas personalizados e geração de nome de arquivo estável.
---
Aspose.PDF para Java suporta vários padrões de divisão além da saída de uma página por arquivo.

## Divida um PDF em arquivos de uma única página

Use esta abordagem quando cada página de origem precisar se tornar um documento de saída separado.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um novo [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) PDF para cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) que deseja exportar.
1. Adicione a [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) selecionada ao novo documento.
1. Salve cada PDF de saída [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void splitDocuments(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            try (Document newDocument = new Document()) {
                newDocument.getPages().add(document.getPages().get_Item(pageNumber));
                newDocument.save(outputDir.resolve("Page_" + pageNumber + ".pdf").toString());
            }
        }
    }
}
```

## Divida um PDF em duas partes

Este exemplo divide o documento de origem em dois arquivos de saída sequenciais com base no ponto médio.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Calcule o ponto médio da coleção [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) disponível.
1. Copie a primeira metade das páginas em um documento de saída e as páginas restantes em outro.
1. Salve ambos os documentos de resultados.

```java
public static void splitDocumentsIntoTwoParts(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        int midPoint = totalPages / 2;

        try (Document firstDocument = new Document()) {
            for (int pageNumber = 1; pageNumber <= midPoint; pageNumber++) {
                firstDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            firstDocument.save(outputDir.resolve("Part_1.pdf").toString());
        }

        try (Document secondDocument = new Document()) {
            for (int pageNumber = midPoint + 1; pageNumber <= totalPages; pageNumber++) {
                secondDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            secondDocument.save(outputDir.resolve("Part_2.pdf").toString());
        }
    }
}
```

## Divida um PDF em grupos de páginas de tamanho fixo

Use este padrão quando cada arquivo de saída deve conter o mesmo número de páginas, exceto possivelmente a última parte.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Percorra a coleção [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) em grupos de `pagesPerPart`.
1. Crie um novo documento de saída para cada grupo e copie nele o intervalo de páginas calculado.
1. Salve cada parte com um nome de arquivo gerado.

```java
public static void splitDocumentsEveryNPages(Path inputFile, Path outputDir, int pagesPerPart) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        int partIndex = 1;

        for (int startPage = 1; startPage <= totalPages; startPage += pagesPerPart) {
            int endPage = Math.min(startPage + pagesPerPart - 1, totalPages);
            try (Document partDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= endPage; pageNumber++) {
                    partDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                partDocument.save(outputDir.resolve("Every_" + pagesPerPart + "_Part_" + partIndex + ".pdf").toString());
            }
            partIndex++;
        }
    }
}
```

## Divida um PDF por intervalos de páginas personalizados

Este exemplo permite definir páginas iniciais e finais explícitas para cada documento de saída.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Defina os intervalos [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) necessários em uma matriz ou outra coleção.
1. Valide cada intervalo em relação à contagem de páginas de origem e copie as páginas correspondentes em um novo documento.
1. Salve cada arquivo de saída baseado em intervalo.

```java
public static void splitDocumentsByPageRanges(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        Integer[][] ranges = {{1, 3}, {4, 6}, {7, null}};

        for (int index = 0; index < ranges.length; index++) {
            int startPage = ranges[index][0];
            Integer endPage = ranges[index][1];
            if (startPage > totalPages) {
                continue;
            }

            int effectiveEnd = endPage == null ? totalPages : Math.min(endPage, totalPages);
            if (startPage > effectiveEnd) {
                continue;
            }

            try (Document rangeDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= effectiveEnd; pageNumber++) {
                    rangeDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                rangeDocument.save(outputDir.resolve(
                        "Range_" + (index + 1) + "_" + startPage + "_to_" + effectiveEnd + ".pdf").toString());
            }
        }
    }
}
```

## Divida a primeira página e as páginas restantes

Use esta abordagem quando a página de rosto precisar ser exportada separadamente do restante do documento.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e confirme se ele contém páginas.
1. Crie um documento de saída para a primeira [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Crie outro documento para o intervalo de páginas restante quando mais de uma página estiver disponível.
1. Salve ambos os resultados.

```java
public static void splitDocumentsFirstPageAndRest(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        try (Document firstPageDocument = new Document()) {
            firstPageDocument.getPages().add(document.getPages().get_Item(1));
            firstPageDocument.save(outputDir.resolve("First_Page.pdf").toString());
        }

        if (totalPages == 1) {
            return;
        }

        try (Document remainingPagesDocument = new Document()) {
            for (int pageNumber = 2; pageNumber <= totalPages; pageNumber++) {
                remainingPagesDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            remainingPagesDocument.save(outputDir.resolve("Remaining_Pages.pdf").toString());
        }
    }
}
```

## Divida a última página e as páginas anteriores

Este exemplo separa a página final do resto do documento, o que é útil para extrair páginas de resumo ou assinatura.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e verifique se não está vazio.
1. Copie a última [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) em um novo documento de saída.
1. Remova essa página do documento original quando ainda restarem páginas anteriores.
1. Salve a última página e as páginas restantes como arquivos separados.

```java
public static void splitDocumentsLastPageAndRest(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        try (Document lastPageDocument = new Document()) {
            lastPageDocument.getPages().add(document.getPages().get_Item(totalPages));
            lastPageDocument.save(outputDir.resolve("Last_Page.pdf").toString());
        }

        if (totalPages == 1) {
            return;
        }

        document.getPages().delete(totalPages);
        document.save(outputDir.resolve("Previous_Pages.pdf").toString());
    }
}
```

## Divida um PDF em três partes

Use esse padrão quando o documento precisar ser dividido em três seções consecutivas de tamanho aproximadamente igual.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e determine o número total de páginas.
1. Calcule o tamanho aproximado de cada parte de saída.
1. Crie até três documentos e copie os intervalos [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) correspondentes.
1. Salve cada parte gerada.

```java
public static void splitDocumentsIntoThreeParts(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        int partSize = Math.max(1, (totalPages + 2) / 3);
        for (int partIndex = 0; partIndex < 3; partIndex++) {
            int startPage = partIndex * partSize + 1;
            int endPage = Math.min((partIndex + 1) * partSize, totalPages);
            if (startPage > totalPages) {
                break;
            }

            try (Document partDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= endPage; pageNumber++) {
                    partDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                partDocument.save(outputDir.resolve("Three_Parts_" + (partIndex + 1) + ".pdf").toString());
            }
        }
    }
}
```

## Divida um PDF em grupos de páginas personalizados

Este exemplo mostra como criar arquivos de saída a partir de conjuntos de páginas não sequenciais em vez de intervalos contínuos.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Defina grupos personalizados de números de [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Crie um novo documento de saída para cada grupo e adicione apenas as páginas válidas desse grupo.
1. Salve cada documento de grupo não vazio.

```java
public static void splitDocumentsCustomPageGroups(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        List<List<Integer>> groups = List.of(
                List.of(1, 2, 5),
                List.of(3, 4, 6, 7));

        int groupIndex = 1;
        for (List<Integer> group : groups) {
            try (Document groupDocument = new Document()) {
                for (Integer pageNumber : group) {
                    if (pageNumber >= 1 && pageNumber <= totalPages) {
                        groupDocument.getPages().add(document.getPages().get_Item(pageNumber));
                    }
                }
                if (groupDocument.getPages().size() > 0) {
                    groupDocument.save(outputDir.resolve("Custom_Group_" + groupIndex + ".pdf").toString());
                }
            }
            groupIndex++;
        }
    }
}
```

## Divida um PDF em páginas únicas com nomes de arquivo estáveis

Use esta versão quando os nomes de saída devem permanecer classificáveis ​​lexicamente, por exemplo, em pipelines automatizados.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um documento de saída para cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Salve cada arquivo com um número de página preenchido com zeros.

```java
public static void splitDocumentsWithStableFilenames(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            try (Document newDocument = new Document()) {
                newDocument.getPages().add(document.getPages().get_Item(pageNumber));
                newDocument.save(outputDir.resolve(String.format("Page_%03d.pdf", pageNumber)).toString());
            }
        }
    }
}
```

## Divida um PDF em páginas pares e ímpares

Este exemplo cria duas saídas separando as páginas de acordo com a paridade do número da página.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um documento de saída para números ímpares de [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e outro para números pares de páginas.
1. Itere pelas páginas de origem com o incremento necessário para cada documento de saída.
1. Salve os resultados das páginas pares e ímpares separadamente.

```java
public static void splitDocumentsOddEvenPages(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();

        try (Document oddDocument = new Document()) {
            for (int pageNumber = 1; pageNumber <= totalPages; pageNumber += 2) {
                oddDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            oddDocument.save(outputDir.resolve("Odd_Pages.pdf").toString());
        }

        try (Document evenDocument = new Document()) {
            for (int pageNumber = 2; pageNumber <= totalPages; pageNumber += 2) {
                evenDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            evenDocument.save(outputDir.resolve("Even_Pages.pdf").toString());
        }
    }
}
```
