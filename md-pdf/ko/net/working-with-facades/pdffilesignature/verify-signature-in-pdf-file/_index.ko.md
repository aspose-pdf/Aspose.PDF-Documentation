---
title: PDF 파일에서 서명 검증
type: docs
weight: 30
url: /net/verify-signature-in-pdf/
description: 이 섹션에서는 PdfFileSignature 클래스를 사용하여 PDF 파일에서 서명을 검증하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## PDF 파일이 서명을 사용하여 서명되었는지 확인

특정 [서명](/pdf/net/working-with-signature-in-a-pdf-file/)을 사용하여 PDF 파일이 서명되었는지 확인하려면, [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 클래스의 VerifySigned 메서드를 사용하십시오. 이 메서드는 서명 이름을 필요로 하며, PDF가 해당 서명 이름을 사용하여 서명된 경우 true를 반환합니다. 또한 어떤 서명으로 서명되었는지 확인하지 않고 [PDF가 서명되었는지](/pdf/net/working-with-signature-in-a-pdf-file/) 확인하는 것도 가능합니다.

### 주어진 서명으로 PDF가 서명되었는지 검증

다음 코드 스니펫은 주어진 서명을 사용하여 PDF가 서명되었는지 확인하는 방법을 보여줍니다.

```csharp
public static void IsPdfSigned()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.ContainsSignature())
                Console.WriteLine("Document Signed");
            pdfSign.Close();
        }
```

### PDF가 서명되었는지 확인하기

파일이 서명되었는지 확인하려면 서명 이름을 제공하지 않고 다음 코드를 사용하십시오.

```csharp
 public static void IsPdfSignedWithGivenSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySigned("Signature1"))
            {
                Console.WriteLine("PDF Signed");
            }
            //if (pdfSign.VerifySigned("Signature2"))
            //{
            //    Console.WriteLine("PDF Signed");
            //}
        }
```

## 서명이 유효한지 확인하기

[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 클래스의 [VerifySignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature) 메소드는 특정 서명을 검증할 수 있도록 합니다. 이 방법은 서명 이름을 입력으로 요구하며 서명이 유효한 경우 true를 반환합니다. 다음 코드 스니펫은 서명을 검증하는 방법을 보여줍니다.

```csharp
public static void IsPdfSignatureValid()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySignature("Signature1"))
            {
                Console.WriteLine("Signature Verified");
            }
        }
```