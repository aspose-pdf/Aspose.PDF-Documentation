---
title: Criar Portfólios PDF em Java
linktitle: Portfólio
type: docs
weight: 20
url: /pt/java/portfolio/
description: Aprenda como criar e gerenciar portfólios PDF em Java usando Aspose.PDF.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crie e edite portfólios PDF com arquivos incorporados em Java
Abstract: Este artigo explica como criar e gerenciar portfólios PDF usando Aspose.PDF for Java. Aprenda como habilitar uma coleção em um documento, adicionar vários tipos de arquivos ao portfólio e remover todos os itens da coleção de um portfólio PDF existente.
---
Um portfólio PDF pode agrupar vários arquivos dentro de um único contêiner PDF, preservando cada arquivo em seu formato original.

## Criar um portfólio PDF

Use este exemplo quando precisar agrupar vários arquivos em uma coleção de portfólio PDF.

1. Crie um novo documento PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e habilite o seu [Collection](https://reference.aspose.com/pdf/java/com.aspose.pdf/collection/).
1. Crie objetos [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) para cada arquivo de entrada e defina suas descrições.
1. Adicione os arquivos à coleção de portfólio e salve o documento de saída.

```java
public static void createPdfPortfolio(Path[] inputFiles, Path outputFile) {
    try (Document document = new Document()) {
        document.setCollection(new Collection());

        FileSpecification excel = new FileSpecification(inputFiles[0].toString());
        FileSpecification word = new FileSpecification(inputFiles[1].toString());
        FileSpecification image = new FileSpecification(inputFiles[2].toString());

        excel.setDescription("Excel File");
        word.setDescription("Word File");
        image.setDescription("Image File");

        document.getCollection().add(excel);
        document.getCollection().add(word);
        document.getCollection().add(image);

        document.save(outputFile.toString());
    }
}
```

## Remover arquivos de um portfólio PDF

Use este exemplo quando uma coleção de portfólio PDF existente deve ser limpa.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Exclua as entradas da coleção de documentos.
1. Salve o documento de saída limpo.

```java
public static void removeFilesFromPdfPortfolio(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getCollection().delete();
        document.save(outputFile.toString());
    }
}
```
