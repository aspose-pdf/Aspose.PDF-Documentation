---
title: PDF 파일 암호화
type: docs
weight: 10
url: ko/net/encrypt-pdf-file/
description: 이 주제는 PdfFileSecurity 클래스를 사용하여 PDF 파일을 암호화하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

PDF 문서를 암호화하면 특히 파일 공유 또는 보관 중에 외부의 무단 액세스로부터 콘텐츠를 보호할 수 있습니다.

기밀 PDF 문서는 암호화되어 비밀번호로 보호될 수 있습니다. 비밀번호를 아는 사용자만이 이러한 문서를 해독하고 열람할 수 있습니다.

Aspose.PDF 라이브러리를 사용한 PDF 암호화 작동 방식을 살펴보겠습니다.

## 다양한 암호화 유형 및 알고리즘을 사용하여 PDF 파일 암호화

PDF 파일을 암호화하려면 [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) 객체를 생성한 다음 [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile) 메서드를 호출해야 합니다. 사용자 비밀번호, 소유자 비밀번호 및 권한을 [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile) 메서드에 전달할 수 있습니다. 이 메서드에 KeySize 및 Algorithm 값을 전달해야 합니다.

이러한 [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm)의 가능한 목록을 검토하십시오:

|**멤버 이름**|**값**|**설명**|
| :- | :- | :- |
|RC4x40|0|키 길이가 40인 RC4.|
|RC4x128|1|키 길이가 128인 RC4.|
|AESx128|2|키 길이가 128인 AES.|
|AESx256|3|키 길이가 256인 AES.|

다음 코드 스니펫은 PDF 파일을 암호화하는 방법을 보여줍니다.

```csharp
public static void EncryptPDFFile()
        {
            // PdfFileSecurity 객체 생성
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample.pdf");
            // 256비트 암호화를 사용하여 파일 암호화
            fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.Print, KeySize.x256, Algorithm.AES);
            fileSecurity.Save(_dataDir + "sample_encrypted.pdf");
        }
```