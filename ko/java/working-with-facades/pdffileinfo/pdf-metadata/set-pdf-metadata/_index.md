---
title: PDF 메타데이터 설정
linktitle: PDF 메타데이터 설정
type: docs
weight: 50
url: /ko/java/set-pdf-metadata/
description: PdfFileInfo 파사드를 사용하여 Java에서 PDF 메타데이터를 업데이트하는 방법을 알아보세요.
lastmod: "2026-09-24"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Java를 사용하여 PDF 메타데이터 업데이트
Abstract: Aspose.PDF for Java를 사용하여 PDF 메타데이터를 업데이트하는 방법을 알아보세요. Java 예제에서는 PdfFileInfo를 사용하여 제목, 제목, 키워드 및 작성자와 같은 표준 메타데이터 필드를 설정하고, 사용자 정의 메타데이터 항목을 추가하고, 결과를 새 PDF에 저장합니다.
---
## PDF 메타데이터 설정

PDF를 저장하기 전에 문서 정보를 정규화하거나 강화해야 할 때 이 작업 흐름을 사용하세요.

### 단계

1. 소스 PDF에 대한 `PdfFileInfo` 개체를 만드세요.
2. 업데이트하려는 표준 메타데이터 필드를 설정하세요.
3. `setMetaInfo`를 사용하여 사용자 정의 메타데이터를 추가하세요.
4. 업데이트된 문서를 `save()`으로 저장하세요.
5. `PdfFileInfo` 인스턴스를 닫으세요.

### Java 예제```java
public static void setPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.setMetaInfo("CustomKey", "CustomValue");
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
