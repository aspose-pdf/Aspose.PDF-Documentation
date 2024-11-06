---
title: PDFファイルのパスワードを変更
type: docs
weight: 40
url: ja/java/change-password/
description: このトピックでは、PdfFileSecurityクラスを使用してPDFファイルのパスワードを変更する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFファイルのパスワードを変更

PDFファイルのパスワードを変更するには、[PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity)オブジェクトを作成し、その後[ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-)メソッドを呼び出す必要があります。既存のオーナーパスワードと新しいユーザーおよびオーナーパスワードを[ChangePassword](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#changePassword-java.lang.String-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-)メソッドに渡す必要があります。

以下のコードスニペットは、PDFファイルのパスワードを変更する方法を示しています。

```java
    public static void ChangePassword() {
        PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
        // PdfFileSecurityオブジェクトを作成
        if (pdfFileInfo.isEncrypted()) {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.bindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.changePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.getPrint(),
                    KeySize.x256);
            fileSecurity.save(_dataDir + "sample_encrtypted1.pdf");
        }
    }
```