---
title: XMP로 메타데이터 저장
linktitle: XMP로 메타데이터 저장
type: docs
weight: 30
url: /java/save-metadata-with-xmp/
description: PdfFileInfo 파사드를 사용하여 Java에서 XMP로 PDF 메타데이터를 저장하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java용 Aspose.PDF를 사용하여 XMP로 PDF 메타데이터 저장
Abstract: Aspose.PDF for Java를 사용하여 XMP로 PDF 메타데이터를 저장하는 방법을 알아보세요. Java 예제에서는 PdfFileInfo로 핵심 메타데이터 필드를 업데이트하고 `saveNewInfoWithXmp()`을 사용하여 다시 기록하므로 출력 문서는 정보를 XMP 형식으로 저장합니다.
---
## XMP로 메타데이터 저장



업데이트된 문서 정보를 XMP 형식으로 저장해야 하는 경우 이 작업 흐름을 사용하십시오.


### 
단계


1. 
소스 PDF에 대한 `PdfFileInfo` 개체를 만듭니다.

2. 
제목, 제목, 키워드, 작성자 등 업데이트하려는 메타데이터 필드를 설정합니다.
3. 출력 파일 경로를 사용하여 `saveNewInfoWithXmp()`을 호출합니다.

4. 
`PdfFileInfo` 인스턴스를 닫습니다.


### 
자바 예

```java
public static void saveInfoWithXmp(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.saveNewInfoWithXmp(outputFile.toString());
    pdfInfo.close();
}
```
