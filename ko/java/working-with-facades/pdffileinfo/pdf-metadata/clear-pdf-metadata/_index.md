---
title: PDF 메타데이터 지우기
linktitle: PDF 메타데이터 지우기
type: docs
weight: 10
url: /java/clear-pdf-metadata/
description: PdfFileInfo 파사드를 사용하여 Java에서 PDF 메타데이터를 지우는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java용 Aspose.PDF를 사용하여 PDF 메타데이터 지우기
Abstract: Java용 Aspose.PDF를 사용하여 PDF 메타데이터를 지우는 방법을 알아보세요. Java 예제에서는 PdfFileInfo를 사용하여 `clearInfo()`으로 저장된 문서 정보를 제거한 다음 정리된 PDF를 새 파일에 저장합니다.
---
## 
PDF 메타데이터 지우기



PDF를 공유하거나 보관하기 전에 저장된 문서 정보를 제거해야 할 때 이 작업 과정을 사용하십시오.


### 
단계


1. 
입력 PDF에 대한 `PdfFileInfo` 개체를 만듭니다.

2. 
문서 메타데이터를 제거하려면 `clearInfo()`으로 전화하세요.

3. 
`save()`을 사용하여 결과를 새 파일에 저장합니다.

4. 
`PdfFileInfo` 인스턴스를 닫습니다.


### 
자바 예

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
