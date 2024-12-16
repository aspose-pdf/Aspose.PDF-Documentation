---
title: 예외 제어 PDF 파일
type: docs
weight: 30
url: /ko/java/control-exception/
description: 이 주제는 PdfFileSecurity 클래스 클래스를 사용하여 PDF 파일에서 예외를 제어하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

[PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) 클래스는 예외를 제어할 수 있도록 합니다. 이를 위해서는 [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-)을 false 또는 true로 설정해야 합니다. 작업을 false로 설정하면, [decryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-)의 결과는 비밀번호의 정확성에 따라 true 또는 false를 반환합니다.

[setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-)을 true로 설정하면, try-catch 연산자를 사용하여 작업의 결과를 얻을 수 있습니다.

```java
    public static void ControlExceptionPDFFile() {
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
        fileSecurity.setAllowExceptions(false);
        // PDF 문서 해독

        if (!fileSecurity.decryptFile("IncorrectPassword")) {
            System.out.println("문제가 발생했습니다...");
            System.out.println("마지막 예외: " + fileSecurity.getLastException().getMessage());
        }
        fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
    }
```