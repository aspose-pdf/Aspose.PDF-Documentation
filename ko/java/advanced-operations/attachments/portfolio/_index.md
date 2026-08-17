---
title: Java에서 PDF 포트폴리오 만들기
linktitle: 포트폴리오
type: docs
weight: 20
url: /java/portfolio/
description: Aspose.PDF를 사용하여 Java에서 PDF 포트폴리오를 만들고 관리하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에 포함된 파일을 사용하여 PDF 포트폴리오 구축 및 편집
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 포트폴리오를 만들고 관리하는 방법을 설명합니다. 문서에서 컬렉션을 활성화하고, 포트폴리오에 여러 파일 형식을 추가하고, 기존 PDF 포트폴리오에서 모든 컬렉션 항목을 제거하는 방법을 알아보세요.
---

PDF 포트폴리오는 각 파일을 원본 형식으로 유지하면서 단일 PDF 컨테이너 내에 여러 파일을 묶을 수 있습니다.


## 
PDF 포트폴리오 만들기



여러 파일을 하나의 PDF 포트폴리오 컬렉션으로 패키징해야 하는 경우 이 예를 사용하세요.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 해당 [컬렉션](https://reference.aspose.com/pdf/java/com.aspose.pdf/collection/)을 활성화합니다.

1. 
각 입력 파일에 대한 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) 개체를 생성하고 설명을 설정합니다.

1. 
포트폴리오 컬렉션에 파일을 추가하고 출력 문서를 저장합니다.


```java
public static void createPdfPortfolio(Path[] inputFiles, Path outputFile) {
    try (Document document = new Document()) {
        document.setCollection(new Collection());

        FileSpecification excel = new FileSpecification(inputFiles[0].toString());
        FileSpecification word = new FileSpecification(inputFiles[1].toString());
        FileSpecification image = new FileSpecification(inputFiles[2].toString());

        excel.setDescription("Excel File");
        word.setDescription("Word File");
        image.setDescription("Image File");

        document.getCollection().add(excel);
        document.getCollection().add(word);
        document.getCollection().add(image);

        document.save(outputFile.toString());
    }
}
```

## 
PDF 포트폴리오에서 파일 제거



기존 PDF 포트폴리오 컬렉션을 지워야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
문서 컬렉션 항목을 삭제합니다.

1. 
정리된 출력 문서를 저장합니다.

```java
public static void removeFilesFromPdfPortfolio(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getCollection().delete();
        document.save(outputFile.toString());
    }
}
```
