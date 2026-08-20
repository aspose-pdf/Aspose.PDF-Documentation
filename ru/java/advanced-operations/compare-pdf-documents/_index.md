---
title: Сравнение PDF‑документов в Java
linktitle: Сравнить PDF
type: docs
weight: 130
url: /ru/java/compare-pdf-documents/
description: Узнайте, как сравнивать PDF документы в Java, используя вывод различий бок о бок и графический, с помощью Aspose.PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Сравните страницы PDF и полные документы с визуальным выводом различий в Java
Abstract: В этой статье объясняется, как сравнивать PDF‑документы с помощью Aspose.PDF for Java. Узнайте, как сравнивать отдельные страницы или целые PDF‑файлы с выводом рядом, создавать графические отчёты о различиях PDF и экспортировать различия изображений на уровне страниц.
---
Aspose.PDF for Java предоставляет API для сравнения рядом и графического сравнения, позволяющие обнаруживать различия между PDF‑файлами.

## Сравнить страницы и экспортировать изображения различий

Используйте этот пример, когда вам нужен вывод различий в виде изображений для конкретной пары страниц PDF.

1. Откройте оба исходных PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) объекты.
1. Используйте [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) чтобы получить уровень страницы [ImagesDifference](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/imagesdifference/).
1. Используйте 'GraphicalPdfComparer' для получения на уровне страницы 'ImagesDifference'.
1. Экспортируйте сгенерированные изображения различий и очистите результат сравнения.

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

## Сравнить конкретные страницы бок о бок

Используйте этот пример, когда необходимо сравнить только выбранные страницы и сохранить результат в виде PDF, расположенного бок о бок.

1. Откройте оба исходных PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) объекты.
1. Настройте [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) для требуемого режима сравнения.
1. Сравните выбранные страницы и сохраните полученный PDF.

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

## Сравнить полные PDF‑документы графически

Этот пример генерирует графический PDF‑отчёт, который выделяет визуальные различия по всем документам.

1. Откройте оба исходных PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) объекты.
1. Настройте [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) порог, цвет и разрешение.
1. Сравните полные документы и сохраните графический PDF‑вывод.

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

## Сравнить полные документы бок о бок

Используйте этот пример, когда нужно сравнивать полные документы постранично в виде PDF‑вывода рядом друг с другом.

1. Откройте оба исходных PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) объекты.
1. Настройте [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) для желаемого поведения сравнения.
1. Сравните полные документы и сохраните результат в виде PDF.

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


