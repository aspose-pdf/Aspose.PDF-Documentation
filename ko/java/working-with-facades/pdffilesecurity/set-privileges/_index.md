---
title: 기존 PDF 파일에 대한 권한 설정
linktitle: 기존 PDF 파일에 대한 권한 설정
type: docs
weight: 40
url: /java/set-privileges/
description: PdfFileSecurity 파사드를 사용하여 Java에서 PDF 권한을 설정하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 PDF 권한 및 액세스 제어 관리
Abstract: Java용 Aspose.PDF를 사용하여 PDF 권한을 제어하는 방법을 알아보세요. Java 예제 세트에서는 비밀번호 없이 권한 적용, 사용자 및 소유자 비밀번호로 권한 적용, 성공 플래그를 반환하는 try-style 권한 업데이트 워크플로를 다룹니다.
---
## 기존 PDF 파일에 대한 권한 설정



사용자가 기존 PDF로 수행할 수 있는 작업을 변경해야 하는 경우 이 작업 과정을 사용하십시오.


### 
단계


1. 
`PdfFileSecurity` 인스턴스를 생성합니다.

2. 
`bindPdf`을 사용하여 소스 PDF를 바인딩합니다.
3. `DocumentPrivilege` 객체를 생성하고 허용되는 작업을 구성합니다.

4. 
적절한 `setPrivilege` 또는 `trySetPrivilege` 오버로드를 호출하세요.

5. 
업데이트가 성공하면 결과를 저장한 다음 개체를 닫습니다.


### 
자바 예제

```java
public static void setPdfPrivilegesWithoutPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.setPrivilege(privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void setPdfPrivilegesWithPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    privilege.setAllowCopy(false);
    fileSecurity.setPrivilege("user_password", "owner_password", privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void trySetPdfPrivilegesWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    if (fileSecurity.trySetPrivilege("user_password", "owner_password", privilege)) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Setting privileges failed. Check passwords or document state.");
    }
    fileSecurity.close();
}
```
