---
title: Java에서 PDF에 Bates 번호 매기기 추가
linktitle: 베이츠 번호 매기기 추가
type: docs
weight: 10
url: /java/add-bates-numbering/
description: Aspose.PDF와 함께 Java를 사용하여 PDF 문서에서 Bates 번호 매기기를 추가하고 제거하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 통해 Bates 번호 매기기 추가
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 Bates 번호 지정 아티팩트를 생성하고 제거하는 방법을 설명합니다. `BatesNArtifact` 구성, Bates 번호 매기기 도우미 또는 일반 페이지 매기기 도우미를 통해 적용, 문서에서 Bates 번호 매기기 제거에 대해 다룹니다.
---

Bates 번호 매기기 아티팩트는 각 페이지에 지속적인 페이지 수준 식별자가 필요한 법적, 보관 및 문서 제어 작업 흐름에 유용합니다.


## 
전용 도우미를 사용하여 Bates 번호 매기기 추가



전용 페이지 컬렉션 도우미를 통해 Bates 번호 매기기를 적용하려는 경우 이 예를 사용하십시오.


1. 
소스 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 샘플에 필요한 추가 페이지를 추가하세요.

1. 
[BatesNAtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) 구성을 생성합니다.

1. 
페이지 컬렉션에 Bates 번호 매기기를 적용하고 출력 파일을 저장합니다.


```java
public static void addBatesNArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        PageCollectionExtensions.addBatesNumbering(document.getPages(), batesArtifact);
        document.save(outputFile.toString());
    }
}
```

## 
페이지 매김 아티팩트를 통해 Bates 번호 매기기 추가



이 예에서는 일반 페이지 매김 API를 통해 Bates 아티팩트를 전달하여 Bates 번호 매기기를 적용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 열고 필요한 페이지를 추가하세요.

1. 
[BatesNAtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/)를 생성하고 페이지 매김 아티팩트 목록에 추가합니다.

1. 
페이지 컬렉션에 페이지 매김 아티팩트를 적용하고 문서를 저장합니다.


```java
public static void addBatesNArtifactPagination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 0; i < 2; i++) {
            document.getPages().add();
        }

        BatesNArtifact batesArtifact = createBatesArtifact();
        List<PaginationArtifact> paginationArtifacts = new ArrayList<>();
        paginationArtifacts.add(batesArtifact);
        PageCollectionExtensions.addPagination(document.getPages(), paginationArtifacts);
        document.save(outputFile.toString());
    }
}
```

## 
Bates 번호 매기기 삭제



기존 Bates 번호 매기기 가공물을 문서에서 제거해야 하는 경우 이 방법을 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
Bates 번호 매기기를 삭제하는 페이지 컬렉션 도우미를 호출합니다.

1. 
정리된 출력 파일을 저장합니다.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```
