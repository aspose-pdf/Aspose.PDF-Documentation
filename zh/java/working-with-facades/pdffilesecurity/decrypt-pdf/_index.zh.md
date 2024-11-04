---
title: 解密 PDF 文件
type: docs
weight: 20
url: /java/decrypt-pdf-file/
description: 本主题解释如何使用 PdfFileSecurity 类解密 PDF 文件。
lastmod: "2021-06-05"
draft: false
---

## 使用所有者密码解密 PDF 文件

{{% alert color="primary" %}}
在线尝试 <br>
您可以使用 Aspose.PDF 尝试解锁文档，并通过此链接在线获得结果：
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

为了解密 PDF 文件，您需要创建 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) 对象，然后调用 [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-) 方法。您还需要将所有者密码传递给 [DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-) 方法。以下代码片段向您展示了如何解密 PDF 文件。

```java
    public static void DecryptPDFFile() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // 创建 PdfFileSecurity 对象
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            // 解密 PDF 文档
            fileSecurity.decryptFile("User_P@ssw0rd");
            fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
        }
    }
```