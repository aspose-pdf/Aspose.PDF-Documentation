---
title: PDF 메타데이터 가져오기
linktitle: PDF 메타데이터 가져오기
type: docs
weight: 20
url: /java/get-pdf-metadata/
description: PdfFileInfo 파사드를 사용하여 Java에서 PDF 메타데이터를 읽는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java용 Aspose.PDF를 사용하여 PDF 메타데이터 검색.
Abstract: Java용 Aspose.PDF를 사용하여 PDF 메타데이터를 검색하는 방법을 알아보세요. Java 예제에서는 파일 상태 플래그 및 사용자 정의 `Reviewer` 메타데이터 항목과 함께 제목, 제목, 키워드, 작성자, 생성 날짜 및 수정 날짜와 같은 표준 필드를 읽습니다.
---
## PDF 메타데이터 가져오기



이 예에서는 표준 문서 정보, 파일 상태 플래그 및 사용자 정의 메타데이터 키를 읽습니다.


### 
단계


1. 
소스 PDF에 대한 `PdfFileInfo` 개체를 만듭니다.

2. 
주제, 제목, 키워드, 작성자 등 표준 메타데이터 필드를 읽어보세요.
3. 파일이 유효한지, 암호화되었는지, 비밀번호로 보호되었는지, 포트폴리오인지 등의 파일 상태 플래그를 검사합니다.

4. 
`getMetaInfo`을 사용하여 사용자 정의 메타데이터 값을 읽습니다.

5. 
`PdfFileInfo` 인스턴스를 닫습니다.


### 
자바 예

```java
public static void getPdfMetadata(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Subject: " + pdfInfo.getSubject());
    System.out.println("Title: " + pdfInfo.getTitle());
    System.out.println("Keywords: " + pdfInfo.getKeywords());
    System.out.println("Creator: " + pdfInfo.getCreator());
    System.out.println("Creation Date: " + pdfInfo.getCreationDate());
    System.out.println("Modification Date: " + pdfInfo.getModDate());
    System.out.println("Is Valid PDF: " + pdfInfo.isPdfFile());
    System.out.println("Is Encrypted: " + pdfInfo.isEncrypted());
    System.out.println("Has Open Password: " + pdfInfo.hasOpenPassword());
    System.out.println("Has Edit Password: " + pdfInfo.hasEditPassword());
    System.out.println("Is Portfolio: " + pdfInfo.hasCollection());
    String reviewer = pdfInfo.getMetaInfo("Reviewer");
    System.out.println("Reviewer: " + (reviewer == null || reviewer.isBlank() ? "No Reviewer metadata found." : reviewer));
    pdfInfo.close();
}
```
