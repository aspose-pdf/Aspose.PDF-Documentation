---
title: Создать PDF портфолио на Java
linktitle: Портфолио
type: docs
weight: 20
url: /ru/java/portfolio/
description: Узнайте, как создавать и управлять PDF портфолио на Java с помощью Aspose.PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создавайте и редактируйте PDF портфолио с вложенными файлами на Java
Abstract: В этой статье объясняется, как создавать и управлять PDF портфолио с помощью Aspose.PDF for Java. Узнайте, как включить коллекцию в документ, добавить несколько типов файлов в портфолио и удалить все элементы коллекции из существующего PDF портфолио.
---
PDF портфолио может объединять несколько файлов в один PDF-контейнер, при этом сохраняя каждый файл в его исходном формате.

## Создайте PDF-портфолио

Используйте этот пример, когда нужно упаковать несколько файлов в коллекцию PDF-портфолио.

1. Создайте новый PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и включить его [Collection](https://reference.aspose.com/pdf/java/com.aspose.pdf/collection/).
1. Создайте [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) объекты для каждого входного файла и задайте их описания.
1. Добавьте файлы в коллекцию портфеля и сохраните выходной документ.

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

## Удалите файлы из PDF‑портфеля

Используйте этот пример, когда необходимо очистить существующую коллекцию PDF‑портфеля.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Удалите элементы коллекции документов.
1. Сохраните очищенный конечный документ.

```java
public static void removeFilesFromPdfPortfolio(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getCollection().delete();
        document.save(outputFile.toString());
    }
}
```


