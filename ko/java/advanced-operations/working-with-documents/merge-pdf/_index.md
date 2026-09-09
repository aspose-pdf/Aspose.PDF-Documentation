---
title: Java에서 PDF 파일 병합
linktitle: PDF 파일 병합
type: docs
weight: 50
url: /java/merge-pdf-documents/
description: Java에서 여러 PDF 파일을 단일 문서로 병합하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 전체 문서, 선택한 범위 및 교대 페이지를 Java와 결합
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서를 병합하는 방법을 설명합니다. 두 개의 파일 결합, 여러 문서 병합, 페이지 범위 선택, 특정 위치에 한 문서를 다른 문서에 삽입, 페이지 교체, 섹션 책갈피를 사용하여 병합된 출력 작성 등을 다룹니다.
---
Aspose.PDF for Java는 출력을 조합하는 방법에 따라 여러 병합 전략을 지원합니다.


## 
두 개의 PDF 문서 병합



가장 간단한 병합 흐름이 필요하고 하나의 완전한 문서를 다른 문서에 추가하려는 경우 이 접근 방식을 사용하십시오.


1. 
두 소스 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 개체를 모두 엽니다.

1. 
두 번째 문서의 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 컬렉션을 첫 번째 문서에 추가합니다.
1. 업데이트된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.


```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```

## 
문서 간에 선택한 페이지 범위 복사



이 도우미 메서드는 페이지 범위 병합 논리를 한 곳에 유지하므로 다른 예제에서는 동일한 검증된 복사 루틴을 재사용할 수 있습니다.


1. 
소스 및 대상 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 개체를 열거나 받습니다.

1. 
사용 가능한 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 컬렉션 내에 유지되도록 요청된 페이지 범위를 정규화합니다.
1. 검증된 범위의 각 페이지를 대상 문서에 추가합니다.


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

## 
여러 PDF 문서를 하나의 파일로 병합



입력 파일 목록을 단일 출력 문서로 순서대로 결합해야 하는 경우 이 패턴을 사용합니다.


1. 
빈 출력 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만듭니다.

1. 
각 입력 파일을 한 번에 하나씩 열고 전체 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 범위를 출력 문서에 복사합니다.
1. 모든 소스 파일을 처리한 후 병합된 결과를 저장합니다.


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

## 
두 문서에서 선택한 페이지 범위 병합



이 예에서는 각 소스 문서에서 특정 페이지 범위만 가져와 사용자 정의 출력 파일을 만듭니다.


1. 
두 소스 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 개체를 모두 열고 새 출력 문서를 만듭니다.

1. 
각 소스 문서에서 필수 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 범위만 추가하세요.
1. 조립된 출력 문서를 저장합니다.


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

## 
특정 위치에 하나의 PDF 문서를 다른 문서에 삽입



한 문서가 문서 앞이나 뒤에만 표시되는 것이 아니라 다른 문서 안에 표시되어야 하는 경우 이 접근 방식을 사용하세요.


1. 
기본 및 삽입된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 개체를 열고 새 출력 문서를 만듭니다.

1. 
기본 문서의 첫 번째 부분을 복사한 다음 삽입된 전체 문서를 추가하고 마지막으로 나머지 기본 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 범위를 추가합니다.
1. 재정렬된 결과를 새 파일에 저장합니다.


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

## 
페이지를 번갈아 가며 두 개의 PDF 문서를 병합합니다.



이 예제는 두 문서의 페이지를 인터리브합니다. 이는 두 입력이 모두 최종 출력에 페이지별로 기여해야 할 때 유용합니다.


1. 
두 소스 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 개체를 모두 열고 새 출력 문서를 만듭니다.

1. 
사용 가능한 최대 페이지 수를 반복하고 첫 번째 및 두 번째 문서에서 사용 가능한 각 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 차례로 추가합니다.
1. 인터리브된 출력 문서를 저장합니다.


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

## 
구분 페이지 및 책갈피를 사용하여 문서 병합



병합된 파일을 쉽게 탐색하고 각 소스 문서가 시작되는 위치를 명확하게 표시해야 하는 경우 이 패턴을 사용하세요.


1. 
빈 출력 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 각 소스 파일을 차례로 엽니다.

1. 
제목과 함께 구분 기호 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가한 다음 해당 섹션에 대한 [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) 북마크를 만듭니다.
1. 소스 페이지를 추가하고 선택적으로 첫 번째 콘텐츠 페이지를 가리키는 책갈피를 추가한 다음 병합된 최종 문서를 저장합니다.

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
