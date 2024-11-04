---
title: PDF 파일 해독
type: docs
weight: 20
url: /java/decrypt-pdf-file/
description: 이 주제는 PdfFileSecurity 클래스를 사용하여 PDF 파일을 해독하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 소유자 비밀번호를 사용하여 PDF 파일 해독

{{% alert color="primary" %}}
온라인으로 시도해보세요 <br>
Aspose.PDF를 사용하여 문서를 잠금 해제하고 이 링크에서 온라인으로 결과를 확인할 수 있습니다:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

PDF 파일을 해독하려면 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) 객체를 생성한 후 [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-) 메서드를 호출해야 합니다. 또한 [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-) 메서드에 소유자 비밀번호를 전달해야 합니다. 다음 코드 스니펫은 PDF 파일을 해독하는 방법을 보여줍니다.

```java
    public static void DecryptPDFFile() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // PdfFileSecurity 객체 생성
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            // PDF 문서 해독
            fileSecurity.decryptFile("User_P@ssw0rd");
            fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
        }
    }
```