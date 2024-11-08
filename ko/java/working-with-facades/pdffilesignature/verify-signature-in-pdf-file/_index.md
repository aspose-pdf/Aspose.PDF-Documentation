---
title: PDF 파일에서 서명 확인
type: docs
weight: 30
url: /ko/java/verify-signature-in-pdf/
description: 이 섹션은 PdfFileSignature 클래스를 사용하여 PDF 파일에서 서명 작업을 수행하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## PDF 파일이 서명되었는지 확인

[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) 클래스의 VerifySigned 메서드를 사용하여 PDF 파일이 서명되었는지 확인할 수 있습니다. 이 메서드는 서명 이름이 필요하며, PDF가 해당 서명 이름으로 서명된 경우 true를 반환합니다. 어떤 서명으로 서명되었는지 확인하지 않고 [PDF가 서명되었는지](/pdf/ko/java/working-with-signature-in-a-pdf-file/) 확인하는 것도 가능합니다.

### 주어진 서명으로 PDF가 서명되었는지 확인

다음 코드 스니펫은 주어진 서명을 사용하여 PDF가 서명되었는지 확인하는 방법을 보여줍니다.

```java
    public static void IsPdfSigned() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.containsSignature())
            System.out.println("Document Signed");

        pdfSign.close();
    }
```


### PDF가 서명되었는지 확인

파일이 서명되었는지 여부를 서명 이름 없이 확인하려면 다음 코드를 사용하세요.

```java
    public static void IsPdfSignedWithGivenSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySigned("Signature1")) {
            System.out.println("PDF Signed");
        }
    }
```

## 서명이 유효한지 확인

[VerifySignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#verifySignature-java.lang.String-) 메서드는 [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) 클래스의 메서드로 특정 서명을 검증할 수 있습니다. 이 메서드는 서명 이름을 입력으로 요구하며, 서명이 유효하면 true를 반환합니다. 다음 코드 조각은 서명을 검증하는 방법을 보여줍니다.

```java
    public static void IsPdfSignatureValid() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySignature("Signature1")) {
            System.out.println("Signature Verified");
        }
    }
```