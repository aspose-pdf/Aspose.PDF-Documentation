---
title: 문서 권한 얻기
linktitle: 문서 권한 얻기
type: docs
weight: 10
url: /java/get-document-privileges/
description: PdfFileInfo 파사드를 사용하여 Java에서 PDF 문서 권한을 검사하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java용 Aspose.PDF를 사용하여 PDF 문서 권한 검색
Abstract: Aspose.PDF for Java를 사용하여 문서 권한을 검색하는 방법을 알아보세요. Java 예제에서는 PdfFileInfo 개체를 만들고, 해당 DocumentPrivilege 설정을 읽고, 인쇄, 복사, 수정, 주석, 양식 채우기, 화면 판독기 및 어셈블리에 대한 권한 플래그를 인쇄합니다.
---
## 
문서 권한 얻기



현재 PDF에서 허용하는 작업을 검사하려면 `PdfFileInfo.getDocumentPrivilege()`을 사용하세요.


### 
단계


1. 
입력 PDF에 대한 `PdfFileInfo` 개체를 만듭니다.

2. 
권한 범위를 검색하려면 `getDocumentPrivilege()`을 호출하세요.

3. 
반환된 `DocumentPrivilege` 개체에서 관련 부울 플래그를 읽습니다.

4. 
완료되면 `PdfFileInfo` 인스턴스를 닫습니다.


### 
자바 예

```java
public static void getDocumentPrivileges(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    DocumentPrivilege privileges = pdfInfo.getDocumentPrivilege();

    System.out.println("Document Privileges:");
    System.out.println("  Can Print: " + privileges.isAllowPrint());
    System.out.println("  Can Degraded Print: " + privileges.isAllowDegradedPrinting());
    System.out.println("  Can Copy: " + privileges.isAllowCopy());
    System.out.println("  Can Modify Contents: " + privileges.isAllowModifyContents());
    System.out.println("  Can Modify Annotations: " + privileges.isAllowModifyAnnotations());
    System.out.println("  Can Fill In: " + privileges.isAllowFillIn());
    System.out.println("  Can Screen Readers: " + privileges.isAllowScreenReaders());
    System.out.println("  Can Assembly: " + privileges.isAllowAssembly());
    pdfInfo.close();
}
```
