---
title: Java에서 PDF 배경 제거
linktitle: 배경 제거
type: docs
weight: 80
url: /ko/java/remove-backgrounds/
description: Java에서 PDF의 첫 페이지에서 배경 잡음을 제거합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 배경 제거
Abstract: Java에서 PDF의 첫 페이지에서 배경 잡음을 제거합니다.
---
Java에서 PDF의 첫 페이지에서 배경 잡음을 제거합니다.

## 배경 잡음 제거

페이지에서 기존 배경 잡음을 삭제해야 할 때 이 방법을 사용하십시오.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 여세요.
1. 페이지 아티팩트 컬렉션을 역순으로 반복하세요.
1. 유형이 pagination이고 서브타입이 background인 아티팩트를 삭제한 다음 문서를 저장하세요.

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 관련 항목

- [배경 추가](/pdf/ko/java/add-backgrounds/)
- [Java에서 PDF 아티팩트 작업](/pdf/ko/java/artifacts/)
