---
title: Decrypt PDF File
type: docs
weight: 20
url: ko/net/decrypt-pdf-file/
description: 이 주제는 PdfFileSecurity 클래스를 사용하여 PDF 파일을 해독하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

암호나 인증서로 암호화된 PDF 문서는 다른 작업을 수행하기 전에 잠금을 해제해야 합니다. 암호화된 PDF 문서에서 작업을 시도하면 예외가 발생합니다. 암호화된 PDF의 잠금을 해제한 후에는 하나 이상의 작업을 수행할 수 있습니다.

## 소유자 암호를 사용하여 PDF 파일 해독

{{% alert color="primary" %}}
온라인에서 시도해보세요 <br>
Aspose.PDF를 사용하여 문서를 잠금 해제하고 이 링크에서 온라인으로 결과를 얻을 수 있습니다:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

PDF 파일을 해독하려면 [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) 객체를 생성한 다음 [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) 메서드를 호출해야 합니다. 당신은 또한 [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) 메서드에 소유자 비밀번호를 전달해야 합니다. 다음 코드 스니펫은 PDF 파일을 해독하는 방법을 보여줍니다.

```csharp
    public static void DecryptPDFFile()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // PdfFileSecurity 객체 생성
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                // PDF 문서 해독
                fileSecurity.DecryptFile("P@ssw0rd");
                fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
            }
        }
```