---
title: Java에서 PDF 파일 분할
linktitle: PDF 파일 분할
type: docs
weight: 60
url: /java/split-pdf-document/
description: Java에서 PDF 페이지를 별도의 PDF 파일로 분할하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 페이지, 범위, 그룹 및 파일 이름 패턴별로 PDF 문서를 분할합니다.
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서를 분할하는 방법을 설명합니다. 단일 페이지, 두 개 또는 세 개의 부분, 홀수 및 짝수 페이지, 고정 크기 청크, 사용자 정의 범위, 첫 번째 또는 마지막 페이지와 나머지 페이지, 사용자 정의 페이지 그룹 및 안정적인 파일 이름 생성으로 분할을 다룹니다.
---
Aspose.PDF for Java는 파일당 한 페이지 출력 이상의 여러 분할 패턴을 지원합니다.


## 
PDF를 단일 페이지 파일로 분할



각 소스 페이지가 별도의 출력 문서가 되어야 하는 경우 이 접근 방식을 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
내보내려는 각 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)에 대해 새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.
1. 선택한 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 새 문서에 추가합니다.

1. 
각 출력 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.


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

## 
PDF를 두 부분으로 분할



이 예에서는 소스 문서를 중간점을 기준으로 두 개의 순차적 출력 파일로 나눕니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.
1. 사용 가능한 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 컬렉션의 중간점을 계산합니다.

1. 
페이지의 첫 번째 절반을 하나의 출력 문서에 복사하고 나머지 페이지를 다른 출력 문서에 복사합니다.

1. 
두 결과 문서를 모두 저장합니다.


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

## 
PDF를 고정 크기 페이지 그룹으로 분할



마지막 부분을 제외하고 모든 출력 파일에 동일한 수의 페이지가 포함되어야 하는 경우 이 패턴을 사용합니다.

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
`pagesPerPart` 그룹으로 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 컬렉션을 반복합니다.

1. 
각 그룹에 대한 새 출력 문서를 만들고 계산된 페이지 범위를 복사합니다.

1. 
생성된 파일 이름으로 각 부분을 저장합니다.


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

## 
사용자 정의 페이지 범위로 PDF 분할

이 예를 사용하면 각 출력 문서의 시작 및 끝 페이지를 명시적으로 정의할 수 있습니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
배열 또는 다른 컬렉션에서 필수 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 범위를 정의합니다.

1. 
소스 페이지 수와 비교하여 각 범위의 유효성을 검사하고 일치하는 페이지를 새 문서에 복사합니다.

1. 
각 범위 기반 출력 파일을 저장합니다.

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

## 첫 번째 페이지와 나머지 페이지를 분할합니다.



표지를 문서의 나머지 부분과 별도로 내보내야 하는 경우 이 방법을 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 페이지가 포함되어 있는지 확인하세요.

1. 
첫 번째 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)에 대해 하나의 출력 문서를 만듭니다.

1. 
두 페이지 이상을 사용할 수 있는 경우 나머지 페이지 범위에 대해 다른 문서를 만듭니다.
1. 두 결과를 모두 저장합니다.


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

## 
마지막 페이지와 이전 페이지를 분할합니다.



이 예는 최종 페이지를 문서의 나머지 부분과 분리하므로 요약 또는 서명 페이지를 추출하는 데 유용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 비어 있지 않은지 확인하세요.

1. 
마지막 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 새 출력 문서에 복사합니다.
1. 이전 페이지가 아직 남아 있으면 원본 문서에서 해당 페이지를 제거합니다.

1. 
마지막 페이지와 나머지 페이지를 별도의 파일로 저장하세요.


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

## 
PDF를 세 부분으로 분할



문서를 대략 동일한 크기의 세 개의 연속 섹션으로 나누어야 하는 경우 이 패턴을 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 총 페이지 수를 확인합니다.
1. 각 출력 부분의 대략적인 크기를 계산합니다.

1. 
최대 3개의 문서를 생성하고 일치하는 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 범위를 복사하세요.

1. 
생성된 각 부분을 저장합니다.


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

## 
PDF를 사용자 정의 페이지 그룹으로 분할



이 예에서는 연속 범위 대신 비순차적 페이지 세트에서 출력 파일을 빌드하는 방법을 보여줍니다.

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 번호의 사용자 정의 그룹을 정의합니다.

1. 
각 그룹에 대한 새 출력 문서를 만들고 해당 그룹의 유효한 페이지만 추가합니다.

1. 
비어 있지 않은 각 그룹 문서를 저장합니다.


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

## 
PDF를 안정적인 파일 이름을 사용하여 단일 페이지로 분할

예를 들어 자동화된 파이프라인에서 출력 이름을 어휘적으로 정렬할 수 있어야 하는 경우 이 버전을 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
각 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)에 대해 하나의 출력 문서를 만듭니다.

1. 
0으로 채워진 페이지 번호를 사용하여 각 파일을 저장합니다.


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

## 
PDF를 홀수 페이지와 짝수 페이지로 분할

이 예에서는 페이지 번호 패리티에 따라 페이지를 분리하여 두 개의 출력을 생성합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
홀수 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 번호에 대한 출력 문서 하나와 짝수 페이지 번호에 대한 출력 문서를 하나씩 만듭니다.

1. 
각 출력 문서에 필요한 증분으로 소스 페이지를 반복합니다.

1. 
홀수 페이지와 짝수 페이지 결과를 별도로 저장합니다.

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
