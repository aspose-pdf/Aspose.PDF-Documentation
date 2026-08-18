---
title: Создание PDF-портфолио на Java
linktitle: Портфель
type: docs
weight: 20
url: /java/portfolio/
description: Узнайте, как создавать портфолио PDF и управлять им на Java с помощью Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создавайте и редактируйте портфолио PDF со встроенными файлами на Java.
Abstract: В этой статье объясняется, как создавать и управлять портфолио PDF с помощью Aspose.PDF для Java. Узнайте, как включить коллекцию в документе, добавить в портфолио файлы нескольких типов и удалить все элементы коллекции из существующего портфолио PDF.
---
Портфолио PDF может объединять несколько файлов в один PDF-контейнер, сохраняя каждый файл в исходном формате.

## Создайте портфолио PDF

Используйте этот пример, если вам нужно упаковать несколько файлов в коллекцию портфолио PDF.

1. Создайте новый PDF-[Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и включите его [Коллекцию](https://reference.aspose.com/pdf/java/com.aspose.pdf/collection/).
1. Создайте объекты [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) для каждого входного файла и задайте их описания.
1. Добавьте файлы в коллекцию портфолио и сохраните выходной документ.

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

## Удаление файлов из портфолио PDF

Используйте этот пример, когда необходимо очистить существующую коллекцию портфолио PDF.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Удалите записи коллекции документов.
1. Сохраните очищенный выходной документ.

```java
public static void removeFilesFromPdfPortfolio(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getCollection().delete();
        document.save(outputFile.toString());
    }
}
```
