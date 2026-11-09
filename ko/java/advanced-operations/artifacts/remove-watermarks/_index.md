---
title: Java에서 PDF 워터마크 제거
linktitle: 워터마크 제거
type: docs
weight: 90
url: /ko/java/remove-watermarks/
description: Java에서 PDF 첫 페이지의 워터마크 아티팩트를 제거합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 워터마크 제거
Abstract: Java에서 PDF 첫 페이지의 워터마크 아티팩트를 제거합니다.
---
Java에서 PDF 첫 페이지의 워터마크 아티팩트를 제거합니다.

## 워터마크 아티팩트 삭제

이 예제는 첫 페이지에서 유형이 `Pagination`이고 하위 유형이 `Watermark`인 아티팩트만 제거합니다. 일반 페이지 텍스트, 이미지 또는 주석으로 저장된 워터마크는 PDF에 남습니다.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 여세요.
1. 페이지 아티팩트 컬렉션을 역순으로 반복하세요.
1. 하위 유형이 워터마크인 페이지 매김 아티팩트를 삭제한 다음 문서를 저장하세요.

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 관련 항목

- [워터마크 추가](/pdf/ko/java/add-watermarks/)
- [워터마크 세부 정보 추출](/pdf/ko/java/extract-watermarks/)
- [Java에서 PDF 아티팩트 작업](/pdf/ko/java/artifacts/)
