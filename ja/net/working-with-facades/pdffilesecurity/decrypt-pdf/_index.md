---
title: PDFファイルの復号化
type: docs
weight: 20
url: ja/net/decrypt-pdf-file/
description: このトピックでは、PdfFileSecurityクラスを使用してPDFファイルを復号化する方法について説明します。
lastmod: "2021-06-05"
draft: false
---

パスワードまたは証明書で暗号化されたPDFドキュメントは、他の操作を行う前に解除する必要があります。暗号化されたPDFドキュメントで操作を試みると、例外が発生します。暗号化されたPDFを解除した後、1つ以上の操作を実行することができます。

## オーナーパスワードを使用してPDFファイルを復号化する

{{% alert color="primary" %}}
オンラインで試す <br>
Aspose.PDFを使用してドキュメントを解除し、次のリンクでオンラインで結果を得ることができます:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

PDFファイルを復号化するには、[PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity)オブジェクトを作成し、その後に[DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile)メソッドを呼び出す必要があります。 あなたはまた、[DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) メソッドにオーナーパスワードを渡す必要があります。次のコードスニペットは、PDFファイルを復号化する方法を示しています。

```csharp
    public static void DecryptPDFFile()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // PdfFileSecurityオブジェクトを作成
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                // PDFドキュメントを復号化
                fileSecurity.DecryptFile("P@ssw0rd");
                fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
            }
        }
```