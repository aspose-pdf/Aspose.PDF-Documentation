---
title: PDFファイルを暗号化
type: docs
weight: 10
url: /ja/java/encrypt-pdf-file/
description: このトピックでは、PdfFileSecurityクラスを使用してPDFファイルを暗号化する方法について説明します。
lastmod: "2021-06-05"
draft: false
---

## 異なる暗号化タイプとアルゴリズムを使用してPDFファイルを暗号化

PDFファイルを暗号化するためには、[PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity)オブジェクトを作成し、それから[EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-)メソッドを呼び出す必要があります。[EncryptFile](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity#encryptFile-java.lang.String-java.lang.String-com.aspose.pdf.facades.DocumentPrivilege-int-)メソッドには、ユーザーパスワード、オーナーパスワード、および特権を渡すことができます。また、このメソッドにはKeySizeとAlgorithmの値を渡す必要があります。

次のコードスニペットは、PDFファイルを暗号化する方法を示しています。

```java
    public static void EncryptPDFFile() {
        // PdfFileSecurityオブジェクトを作成
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        // 256ビット暗号化を使用してファイルを暗号化
        fileSecurity.encryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.getPrint(), KeySize.x256,
                Algorithm.AES);
        fileSecurity.save(_dataDir + "sample_encrypted.pdf");
    }
```