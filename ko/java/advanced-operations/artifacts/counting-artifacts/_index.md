---
title: Java에서 PDF 아티팩트 개수 세기
linktitle: 아티팩트 개수 세기
type: docs
weight: 40
url: /ko/java/counting-artifacts/
description: Aspose.PDF를 사용한 Java로 PDF 문서에서 페이지 매김 아티팩트를 검사하고 개수를 세는 방법을 배웁니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용한 PDF에서 아티팩트 개수 세기
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 페이지 매김 아티팩트를 검사하고 개수를 세는 방법을 설명합니다. 페이지 아티팩트를 반복하여 watermark, background, header, and footer 하위 유형을 계산하는 방법을 보여줍니다.
---
## 페이지에서 페이지 매김 아티팩트 개수 세기

페이지에서 주요 페이지네이션 아티팩트 하위 유형을 빠르게 계산해야 할 때 이 예제를 사용하십시오.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 여세요.
1. 대상 페이지 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)의 [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) 컬렉션을 읽으세요.
1. 페이지의 [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) 컬렉션을 순회하고 보고할 페이지 매김 하위 유형별로 아티팩트 수를 세세요.

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

## 관련 항목

- [Java에서 PDF 아티팩트 작업](/pdf/ko/java/artifacts/)
- [워터마크 세부 정보 추출](/pdf/ko/java/extract-watermarks/)
- [배경 제거](/pdf/ko/java/remove-backgrounds/)
- [워터마크 제거](/pdf/ko/java/remove-watermarks/)
- [베이츠 번호 매기기 제거](/pdf/ko/java/remove-bates-numbering/)
- [머리글 및 바닥글 제거](/pdf/ko/java/remove-headers-footers/)
