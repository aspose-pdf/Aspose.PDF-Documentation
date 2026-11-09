---
title: Java에서 PDF에 Bates 번호 매기기 추가
linktitle: Bates 번호 매기기 추가
type: docs
weight: 10
url: /ko/java/add-bates-numbering/
description: 전용 Bates 번호 매기기 도우미 또는 일반 페이지 매김 API를 사용하여 Java에서 PDF 페이지에 순차적인 Bates 식별자를 추가합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 Bates 번호 매기기 추가
Abstract: 전용 Bates 번호 매기기 도우미 또는 일반 페이지 매김 API를 사용하여 Java에서 PDF 페이지에 순차적인 Bates 식별자를 추가합니다.
---
Bates 번호 매기기 아티팩트는 각 페이지에 지속적인 페이지 수준 식별자가 필요한 법률, 보관 및 문서 관리 워크플로에서 유용합니다.

## 전용 도우미를 사용하여 Bates 번호 매기기 추가

전용 페이지 컬렉션 도우미를 사용하여 베이츠 번호 매기를 적용하려는 경우 이 예제를 사용하십시오.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 열고 예제에 필요한 페이지를 추가하세요.
1. [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) 개체를 구성하세요.
1. 페이지 컬렉션에 Bates 번호 매기기를 적용하고 출력 파일을 저장하세요.

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

## 페이지 매김 아티팩트를 통해 베이츠 번호 매기기 추가

이 예제는 베이츠 아티팩트를 일반 페이지 매김 API에 전달하여 베이츠 번호 매기기를 적용합니다.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 열고 예제에 필요한 페이지를 추가하세요.
1. [BatesNArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/batesnartifact/) 개체를 만들고 페이지 매김 아티팩트 목록에 추가하세요.
1. 페이지 컬렉션에 페이지 매김 아티팩트를 적용하고 문서를 저장하세요.

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

## 관련 항목

- [Bates 번호 제거](/pdf/ko/java/remove-bates-numbering/)
- [Java에서 PDF 아티팩트 작업](/pdf/ko/java/artifacts/)
