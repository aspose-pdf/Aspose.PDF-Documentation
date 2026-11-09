---
title: Java에서 PDF 베이츠 번호 매기기 제거
linktitle: 베이츠 번호 매기기 제거
type: docs
weight: 100
url: /ko/java/remove-bates-numbering/
description: Java에서 PDF의 모든 페이지에서 베이츠 번호 매기기를 제거합니다.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 베이츠 번호 매기기 제거
Abstract: Java에서 PDF의 모든 페이지에서 베이츠 번호 매기기를 제거합니다.
---
Java에서 PDF의 모든 페이지에서 베이츠 번호 매기기를 제거합니다.

## 베이츠 번호 매기기 삭제

문서에서 기존 베이츠 번호 매기기 아티팩트를 제거해야 할 때 이 방법을 사용하십시오.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)로 원본 PDF를 여세요.
1. Bates 번호 매김을 삭제하는 페이지 컬렉션 도우미를 호출하세요.
1. 정리된 출력 파일을 저장하세요.

```java
public static void deleteBatesNumbering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageCollectionExtensions.deleteBatesNumbering(document.getPages());
        document.save(outputFile.toString());
    }
}
```

## 관련 항목

- [Bates 번호 매기기 추가](/pdf/ko/java/add-bates-numbering/)
- [Java에서 PDF 아티팩트 작업](/pdf/ko/java/artifacts/)
