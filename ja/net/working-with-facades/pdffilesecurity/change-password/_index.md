---
title: PDFファイルのパスワードを変更する
type: docs
weight: 40
url: ja/net/change-password/
description: このトピックでは、PdfFileSecurityクラスを使用してPDFファイルのパスワードを変更する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFファイルのパスワードを変更する

PDFファイルのパスワードを変更するには、[PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity)オブジェクトを作成し、[ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2)メソッドを呼び出す必要があります。既存のオーナーパスワードと新しいユーザーパスワードおよびオーナーパスワードを[ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2)メソッドに渡す必要があります。

{{% alert color="primary" %}}

- **ユーザーパスワード**が設定されている場合、それを提供することでPDFを開くことができます。Acrobat/Readerはユーザーにユーザーパスワードの入力を促します。それが正しくない場合、ドキュメントは開きません。
- **オーナーパスワード**が設定されている場合、印刷、編集、抽出、コメントなどの権限を制御します。 Acrobat/Readerは、権限設定に基づいてこれらのことを禁止します。権限を設定/変更したい場合は、Acrobatがこのパスワードを要求します。

{{% /alert %}}

次のコードスニペットは、PDFファイルのパスワードを変更する方法を示しています。

```csharp
public static void ChangePassword()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // PdfFileSecurityオブジェクトを作成
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.Print, KeySize.x256);
                fileSecurity.Save(_dataDir + "sample_encrtypted1.pdf");
            }
        }
```