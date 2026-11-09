---
title: Java에서 PDF 워터마크 세부 정보 추출
linktitle: 워터마크 세부 정보 추출
type: docs
weight: 50
url: /ko/java/extract-watermarks/
description: Java에서 PDF 첫 페이지에 있는 워터마크 아티팩트의 텍스트와 경계 사각형을 읽습니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 워터마크 세부 정보 추출
Abstract: Java에서 PDF 첫 페이지에 있는 워터마크 아티팩트의 텍스트와 경계 사각형을 읽습니다.
---
Java에서 PDF 첫 페이지에 있는 워터마크 아티팩트의 텍스트와 경계 사각형을 읽습니다.

## PDF에서 워터마크 아티팩트 추출

기존 워터마크 아티팩트를 검사하고 텍스트나 위치를 읽어야 할 때 이 예제를 사용하십시오.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 여세요.
1. 대상 페이지의 아티팩트 컬렉션을 반복하세요.
1. 워터마크 페이지 매김 아티팩트를 필터링하고 해당 텍스트와 사각형을 출력하세요.

```java
public static void extractWatermarkFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                System.out.println(artifact.getText() + " " + artifact.getRectangle());
            }
        }
    }
}
```

## 관련 항목

- [워터마크 추가](/pdf/ko/java/add-watermarks/)
- [워터마크 제거](/pdf/ko/java/remove-watermarks/)
- [Java에서 PDF 아티팩트 작업](/pdf/ko/java/artifacts/)
