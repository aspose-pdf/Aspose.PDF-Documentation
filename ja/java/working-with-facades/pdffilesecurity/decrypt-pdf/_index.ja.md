---
title: PDFファイルの復号化
type: docs
weight: 20
url: /java/decrypt-pdf-file/
description: このトピックでは、PdfFileSecurityクラスを使用してPDFファイルを復号化する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## オーナーパスワードを使用してPDFファイルを復号化する

{{% alert color="primary" %}}
オンラインで試す <br>
Aspose.PDFを使用してドキュメントのロックを解除し、このリンクでオンラインで結果を取得できます:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

PDFファイルを復号化するには、[PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity)オブジェクトを作成し、[DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-)メソッドを呼び出す必要があります。また、[DecryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#decryptFile-java.lang.String-)メソッドにオーナーパスワードを渡す必要があります。次のコードスニペットは、PDFファイルを復号化する方法を示しています。

```java
    public static void DecryptPDFFile() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // PdfFileSecurityオブジェクトを作成
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            // PDFドキュメントを復号化
            fileSecurity.decryptFile("User_P@ssw0rd");
            fileSecurity.save(_dataDir + "sample_decrtypted.pdf");
        }
    }
```