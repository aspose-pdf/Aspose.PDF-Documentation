---
title: PDFファイルを暗号化
type: docs
weight: 10
url: /net/encrypt-pdf-file/
description: このトピックでは、PdfFileSecurityクラスを使用してPDFファイルを暗号化する方法について説明します。
lastmod: "2021-06-05"
draft: false
---

PDFドキュメントを暗号化することで、特にファイル共有やアーカイブ時に、外部からの不正アクセスからその内容を保護します。

機密のPDFドキュメントは暗号化され、パスワードで保護されることがあります。パスワードを知っているユーザーだけがこれらのドキュメントを復号化し、開いて閲覧することができます。

Aspose.PDFライブラリを使用してPDFの暗号化がどのように機能するか見てみましょう。

## 異なる暗号化タイプとアルゴリズムを使用してPDFファイルを暗号化する

PDFファイルを暗号化するには、[PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity)オブジェクトを作成し、[EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile)メソッドを呼び出す必要があります。 ```
ユーザーパスワード、オーナーパスワード、および特権を[EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile)メソッドに渡すことができます。また、このメソッドにKeySizeとAlgorithmの値を渡す必要があります。

このような[CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm)の可能なリストを確認してください:

|**メンバー名**|**値**|**説明**|
| :- | :- | :- |
|RC4x40|0|キー長40のRC4。|
|RC4x128|1|キー長128のRC4。|
|AESx128|2|キー長128のAES。|
|AESx256|3|キー長256のAES。|

次のコードスニペットは、PDFファイルを暗号化する方法を示しています。

```csharp
public static void EncryptPDFFile()
        {
            // PdfFileSecurityオブジェクトを作成
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample.pdf");
            // 256ビット暗号化を使用してファイルを暗号化
            fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", DocumentPrivilege.Print, KeySize.x256, Algorithm.AES);
            fileSecurity.Save(_dataDir + "sample_encrypted.pdf");
        }
```
```