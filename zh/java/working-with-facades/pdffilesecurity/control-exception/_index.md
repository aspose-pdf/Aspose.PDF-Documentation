---
title: 控制异常PDF文件
type: docs
weight: 30
url: /zh/java/control-exception/
description: 本主题解释如何使用 PdfFileSecurity 类控制 PDF 文件上的异常。
lastmod: "2021-06-05"
draft: false
---

[PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) 类允许您控制异常。为此，您需要将 [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) 设置为 false 或 true。如果您将操作设置为 false，则 [decryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-) 的结果将根据密码的正确性返回 true 或 false。

如果您将 [setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) 设置为 true，那么您可以使用 try-catch 操作符获取操作结果。

```java
    public static void ControlExceptionPDFFile() {
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
        fileSecurity.setAllowExceptions(false);
        // 解密PDF文档

        if (!fileSecurity.decryptFile("IncorrectPassword")) {
            System.out.println("出了些问题...");
            System.out.println("最后的异常: " + fileSecurity.getLastException().getMessage());
        }
        fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
    }
```