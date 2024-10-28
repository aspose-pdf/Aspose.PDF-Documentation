---
title: 기존 PDF 파일에 권한 설정
type: docs
weight: 50
url: /java/set-privileges/
description: 이 주제는 PdfFileSecurity 클래스를 사용하여 기존 PDF 파일에 권한을 설정하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 기존 PDF 파일에 권한 설정 (facades)

PDF 파일의 권한을 설정하려면 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) 클래스 개체를 생성하고 binPdf 메서드를 사용하여 입력 PDF를 바인딩합니다. 그런 다음 setPrivilege 메서드를 호출하여 권한을 설정해야 합니다. [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/DocumentPrivilege) 객체를 사용하여 권한을 지정한 후 이 객체를 setPrivilege 메서드에 전달하고 save 메서드를 사용하여 출력 PDF를 저장할 수 있습니다.

다음 코드 스니펫은 PDF 파일의 권한을 설정하는 방법을 보여줍니다.

```java
public static void SetPrivilege1() {
        // DocumentPrivileges 객체 생성
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // PdfFileSecurity 객체 생성
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege(privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```


다음 비밀번호를 지정하는 방법을 참조하세요:

```java
 public static void SetPrivilege2() {
        // DocumentPrivileges 객체 생성
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // PdfFileSecurity 객체 생성
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege("", "P@ssw0rd", privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```