---
title: PDF 파일의 비밀번호 변경
type: docs
weight: 40
url: /ko/java/change-password/
description: 이 주제는 PdfFileSecurity 클래스를 사용하여 PDF 파일의 비밀번호를 변경하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## PDF 파일의 비밀번호 변경

PDF 파일의 비밀번호를 변경하려면 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) 객체를 생성한 다음, [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-) 메소드를 호출해야 합니다. 기존 소유자 비밀번호와 새로운 사용자 및 소유자 비밀번호를 [ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-) 메소드에 전달해야 합니다.

다음 코드 스니펫은 PDF 파일의 비밀번호를 변경하는 방법을 보여줍니다.

```java
    public static void ChangePassword() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // PdfFileSecurity 객체 생성
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.changePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.getPrint(),
                    KeySize.x256);
            fileSecurity.save(_dataDir + "sample_encrtypted1.pdf");
        }
    }
```