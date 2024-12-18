---
title: PDF 파일 암호화
type: docs
weight: 10
url: /ko/java/encrypt-pdf-file/
description: 이 주제는 PdfFileSecurity 클래스를 사용하여 PDF 파일을 암호화하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 다양한 암호화 유형 및 알고리즘을 사용하여 PDF 파일 암호화

PDF 파일을 암호화하려면 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) 객체를 생성한 다음, [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-) 메서드를 호출해야 합니다. 사용자 비밀번호, 소유자 비밀번호 및 권한을 [EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-) 메서드에 전달할 수 있습니다. 이 메서드에는 KeySize와 Algorithm 값도 전달해야 합니다.

다음 코드 스니펫은 PDF 파일을 암호화하는 방법을 보여줍니다.

```java
    public static void EncryptPDFFile() {
        // PdfFileSecurity 객체 생성
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        // 256비트 암호화를 사용하여 파일 암호화
        fileSecurity.encryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.getPrint(), KeySize.x256,
                Algorithm.AES);
        fileSecurity.save(_dataDir + "sample_encrypted.pdf");
    }
```