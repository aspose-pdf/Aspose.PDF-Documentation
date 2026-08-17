---
title: PDF 파일의 비밀번호 변경
linktitle: PDF 파일의 비밀번호 변경
type: docs
weight: 10
url: /java/change-password/
description: PdfFileSecurity 파사드를 사용하여 Java에서 PDF 비밀번호를 변경하는 방법을 알아보세요.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java에서 PDF 사용자 및 소유자 비밀번호 업데이트
Abstract: Java용 Aspose.PDF를 사용하여 PDF 비밀번호를 변경하는 방법을 알아보세요. Java 예제 세트에서는 사용자 및 소유자 비밀번호를 직접 변경하는 방법, 보안 설정을 재설정하는 동안 비밀번호를 변경하는 방법, 성공 플래그를 반환하는 시도 스타일 비밀번호 변경 워크플로를 다룹니다.
---
## 
PDF 파일의 비밀번호 변경



이미 보안이 설정된 PDF에서 자격 증명을 교체해야 하는 경우 `PdfFileSecurity`을 사용하세요.


### 
단계


1. 
`PdfFileSecurity` 인스턴스를 생성합니다.

2. 
`bindPdf`으로 보안된 PDF를 바인딩합니다.

3. 
권한과 키 크기도 재설정할지 여부에 따라 적절한 `changePassword` 오버로드를 호출하세요.

4. 
업데이트된 파일을 저장하고 보안 개체를 닫습니다.


### 
자바 예제

```java
public static void changeUserAndOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void changePasswordAndResetSecurity(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryChangePasswordWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryChangePassword("owner_password", "new_user_password", "new_owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Password change failed. Check owner password or document security.");
    }
    fileSecurity.close();
}
```
