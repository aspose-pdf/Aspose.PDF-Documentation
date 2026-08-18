---
title: Сравнить PDF-документы в Java
linktitle: Сравнить PDF
type: docs
weight: 130
url: /java/compare-pdf-documents/
description: Узнайте, как сравнивать PDF-документы на Java, используя параллельный и графический вывод различий с помощью Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Сравнивайте PDF-страницы и полные документы с визуальным выводом различий в Java
Abstract: В этой статье объясняется, как сравнивать PDF-документы с помощью Aspose.PDF для Java. Узнайте, как сравнивать отдельные страницы или целые PDF-файлы с параллельным выводом, создавать графические отчеты о различиях PDF и экспортировать различия изображений на уровне страниц.
---
Aspose.PDF для Java предоставляет API как параллельного, так и графического сравнения для обнаружения различий между PDF-файлами.

## Сравнивайте страницы и экспортируйте изображения различий

Используйте этот пример, если вам нужен вывод различий на основе изображений для определенной пары страниц PDF.

1. Откройте оба исходных объекта PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Используйте [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/), чтобы получить [ImagesDifference](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/imagesdifference/) уровня страницы.
1. Используйте «GraphicalPdfComparer», чтобы получить «ImagesDifference» на уровне страницы.
1. Экспортируйте сгенерированные разностные изображения и разместите результат сравнения.

```java
public static void comparePdfWithGetDifferenceMethod(
        Path inputFile1, Path inputFile2, Path diffOutputFile, Path destinationOutputFile) throws Exception {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer comparer = new GraphicalPdfComparer();
        ImagesDifference imagesDifference = comparer.getDifference(document1.getPages().get_Item(1),
                document2.getPages().get_Item(1));

        ImageIO.write(imagesDifference.differenceToImage(Color.getRed(), Color.getWhite()),
                "png", diffOutputFile.toFile());
        ImageIO.write(imagesDifference.getDestinationImage(), "png", destinationOutputFile.toFile());
        imagesDifference.dispose();
    }
    System.out.println("Difference images saved to " + diffOutputFile + " and " + destinationOutputFile);
}
```

## Сравнивайте отдельные страницы рядом

Используйте этот пример, когда необходимо сравнить только выбранные страницы и сохранить их в виде параллельного PDF-файла.

1. Откройте оба исходных объекта PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Настройте [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) для требуемого режима сравнения.
1. Сравните выбранные страницы и сохраните выходной PDF-файл.

```java
public static void comparingSpecificPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(document1.getPages().get_Item(1), document2.getPages().get_Item(1),
                outputFile.toString(), options);
    }
    System.out.println("Specific pages comparison saved to " + outputFile);
}
```

## Сравнивайте полные PDF-документы графически

В этом примере создается графический отчет в формате PDF, в котором подчеркиваются визуальные различия во всех документах.

1. Откройте оба исходных объекта PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Настройте пороговое значение [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/), цвет и разрешение.
1. Сравните полные документы и сохраните графический вывод в формате PDF.

```java
public static void comparePdfWithCompareDocumentsToPdfMethod(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer pdfComparer = new GraphicalPdfComparer();
        pdfComparer.setThreshold(3.0);
        pdfComparer.setColor(Color.getBlue());
        pdfComparer.setResolution(new Resolution(300));
        pdfComparer.compareDocumentsToPdf(document1, document2, outputFile.toString());
    }
    System.out.println("Graphical comparison saved to " + outputFile);
}
```

## Сравнивайте целые документы рядом

Используйте этот пример, когда необходимо сравнить все документы постранично в параллельном выводе PDF.

1. Откройте оба исходных объекта PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Настройте [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) для желаемого поведения сравнения.
1. Сравните полные документы и сохраните результат в формате PDF.

```java
public static void comparingEntireDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(document1, document2, outputFile.toString(), options);
    }
    System.out.println("Entire document comparison saved to " + outputFile);
}
```
