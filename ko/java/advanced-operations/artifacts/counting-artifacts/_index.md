---
title: Java에서 PDF 아티팩트 계산
linktitle: 유물 계산
type: docs
weight: 40
url: /java/counting-artifacts/
description: Aspose.PDF와 함께 Java를 사용하여 PDF 문서의 페이지 매김 아티팩트를 검사하고 계산하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF의 아티팩트 계산하기
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서의 페이지 매김 아티팩트를 검사하고 계산하는 방법을 설명합니다. 페이지 아티팩트를 반복하고 워터마크, 배경, 머리글 및 바닥글 하위 유형을 계산하는 방법을 보여줍니다.
---
## 
페이지의 페이지 매기기 아티팩트 계산



페이지의 기본 페이지 매기기 아티팩트 하위 유형을 빠르게 계산해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)에서 [아티팩트](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) 컬렉션을 읽어옵니다.

1. 
페이지 [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) 컬렉션을 반복하고 보고해야 하는 각 페이지 매김 하위 유형의 수를 계산합니다.

```java
public static void countPdfArtifacts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int watermarks = 0;
        int backgrounds = 0;
        int headers = 0;
        int footers = 0;

        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination) {
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                    watermarks++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                    backgrounds++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Header) {
                    headers++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Footer) {
                    footers++;
                }
            }
        }

        System.out.println("Watermarks: " + watermarks);
        System.out.println("Backgrounds: " + backgrounds);
        System.out.println("Headers: " + headers);
        System.out.println("Footers: " + footers);
    }
}
```
