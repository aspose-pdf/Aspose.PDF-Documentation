---
title: PDF 파일의 비밀번호 변경
type: docs
weight: 40
url: /ko/net/change-password/
description: 이 주제는 PdfFileSecurity 클래스를 사용하여 PDF 파일의 비밀번호를 변경하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## PDF 파일의 비밀번호 변경

PDF 파일의 비밀번호를 변경하려면 [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) 객체를 생성한 다음 [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2) 메서드를 호출해야 합니다. 기존 소유자 비밀번호 및 새 사용자와 소유자 비밀번호를 [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2) 메서드에 전달해야 합니다.

{{% alert color="primary" %}}

- **사용자 비밀번호**가 설정된 경우 PDF를 열기 위해 제공해야 하는 비밀번호입니다. Acrobat/Reader는 사용자에게 사용자 비밀번호를 입력하라는 메시지를 표시합니다. 비밀번호가 정확하지 않으면 문서가 열리지 않습니다.
- **소유자 비밀번호**가 설정된 경우 인쇄, 편집, 추출, 주석 등과 같은 권한을 제어합니다. Acrobat/Reader는 권한 설정에 따라 이러한 작업을 허용하지 않습니다. 권한을 설정/변경하려면 Acrobat에서 이 비밀번호가 필요합니다.

{{% /alert %}}

다음 코드 스니펫은 PDF 파일의 비밀번호를 변경하는 방법을 보여줍니다.

```csharp
public static void ChangePassword()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // PdfFileSecurity 객체 생성
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.Print, KeySize.x256);
                fileSecurity.Save(_dataDir + "sample_encrtypted1.pdf");
            }
        }
```