---
title: 例外を制御するPDFファイル
type: docs
weight: 30
url: /ja/java/control-exception/
description: このトピックでは、PdfFileSecurityクラスを使用してPDFファイルの例外を制御する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

[PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) クラスを使用すると、例外を制御できます。これを行うには、[setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) を false または true に設定する必要があります。操作を false に設定した場合、パスワードの正確さに応じて [decryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-) の結果が true または false を返します。

[setAllowExceptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#setAllowExceptions-boolean-) を true に設定した場合、try-catch 演算子を使用して操作の結果を取得できます。

```java
    public static void ControlExceptionPDFFile() {
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
        fileSecurity.setAllowExceptions(false);
        // PDFドキュメントを復号化する

        if (!fileSecurity.decryptFile("IncorrectPassword")) {
            System.out.println("何かが間違っています...");
            System.out.println("最後の例外: " + fileSecurity.getLastException().getMessage());
        }
        fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
    }
```