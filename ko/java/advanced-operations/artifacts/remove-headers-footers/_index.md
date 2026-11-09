---
title: Java에서 PDF 헤더 및 푸터 제거
linktitle: 헤더 및 푸터 제거
type: docs
weight: 110
url: /ko/java/remove-headers-footers/
description: Java에서 PDF 첫 페이지의 헤더 및 푸터 아티팩트를 제거합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 헤더 및 푸터 제거
Abstract: Java에서 PDF 첫 페이지의 헤더 및 푸터 아티팩트를 제거합니다.
---
Java에서 PDF 첫 페이지의 헤더 및 푸터 아티팩트를 제거합니다.

## 헤더 및 푸터 아티팩트 삭제

페이지에서 기존 헤더 및 푸터 아티팩트를 제거해야 할 경우 이 접근 방식을 사용하십시오.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 여세요.
1. 페이지 아티팩트 컬렉션을 역순으로 반복하세요.
1. 하위 유형이 머리글 또는 바닥글인 페이지 매김 아티팩트를 삭제하고 문서를 저장하세요.

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 관련 항목

- [머리글 및 바닥글 추가](/pdf/ko/java/artifacts-header-footer/)
- [Java에서 PDF 아티팩트 작업](/pdf/ko/java/artifacts/)
