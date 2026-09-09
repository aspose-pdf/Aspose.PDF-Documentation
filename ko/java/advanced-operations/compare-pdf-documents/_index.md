---
title: Java에서 PDF 문서 비교
linktitle: PDF 비교
type: docs
weight: 130
url: /java/compare-pdf-documents/
description: Aspose.PDF를 사용하여 병렬 및 그래픽 차이 출력을 사용하여 Java에서 PDF 문서를 비교하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 페이지와 전체 문서를 Java의 시각적 차이 출력과 비교
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서를 비교하는 방법을 설명합니다. 특정 페이지 또는 전체 PDF 파일을 나란히 출력하여 비교하고, 그래픽 PDF 차이 보고서를 생성하고, 페이지 수준 이미지 차이를 내보내는 방법을 알아보세요.
---
Aspose.PDF for Java는 PDF 파일 간의 차이점을 감지하기 위한 병렬 및 그래픽 비교 API를 모두 제공합니다.


## 
페이지 비교 및 차이점 이미지 내보내기



특정 PDF 페이지 쌍에 대해 이미지 기반 차이 출력이 필요한 경우 이 예를 사용하십시오.


1. 
두 소스 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 개체를 모두 엽니다.

1. 
[GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/)를 사용하여 페이지 수준 [ImagesDifference](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/imagesdifference/)를 가져옵니다.
1. 페이지 수준 'ImagesDifference'를 얻으려면 'GraphicalPdfComparer'를 사용하십시오.

1. 
생성된 차이 이미지를 내보내고 비교 결과를 폐기합니다.


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

## 
특정 페이지를 나란히 비교



선택한 페이지만 비교하고 병렬 PDF 결과로 저장해야 하는 경우 이 예를 사용합니다.


1. 
두 소스 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 개체를 모두 엽니다.
1. 필요한 비교 모드에 대해 [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/)를 구성합니다.

1. 
선택한 페이지를 비교하고 출력 PDF를 저장합니다.


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

## 
전체 PDF 문서를 그래픽으로 비교



이 예에서는 전체 문서의 시각적 차이점을 강조하는 그래픽 PDF 보고서를 생성합니다.


1. 
두 소스 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 개체를 모두 엽니다.
1. [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) 임계값, 색상 및 해상도를 구성합니다.

1. 
전체 문서를 비교하고 그래픽 출력 PDF를 저장하십시오.


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

## 
전체 문서를 나란히 비교



전체 문서를 나란히 PDF 출력하여 페이지별로 비교해야 하는 경우 이 예를 사용하십시오.


1. 
두 소스 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 개체를 모두 엽니다.
1. 원하는 비교 동작에 맞게 [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/)를 구성합니다.

1. 
전체 문서를 비교하고 결과를 PDF로 저장하세요.

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
