---
title: PDFをNode.jsで暗号化する
linktitle: PDFファイルを暗号化
type: docs
weight: 50
url: /ja/nodejs-cpp/encrypt-pdf/
description: Aspose.PDF for Node.js via C++を使用してPDFファイルを暗号化します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## ユーザーまたはオーナーパスワードを使用してPDFファイルを暗号化する

PDFファイルを添付したメールを誰かに送る際、その内容が機密情報を含んでいる場合、不正な手に渡らないようにするために、まず何らかのセキュリティを追加したいと思うかもしれません。PDFドキュメントへの不正アクセスを制限する最良の方法は、パスワードで保護することです。ドキュメントを簡単かつ安全に暗号化するために、Aspose.PDF for Node.js via C++を使用できます。

>PDFファイルを暗号化する際には、異なるユーザーおよびオーナーパスワードを指定してください。

- **ユーザーパスワード**は、設定されている場合、PDFを開くために提供する必要があるものです。Acrobat/Readerはユーザーにユーザーパスワードの入力を促します。正しくない場合、ドキュメントは開きません。
- **オーナーパスワード**は、設定されている場合、印刷、編集、抽出、コメントなどの権限を制御します。
 Acrobat/Readerは、許可設定に基づいてこれらのことを禁止します。許可を設定/変更したい場合、Acrobatはこのパスワードを要求します。

PDFファイルを暗号化したい場合は、[AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/)機能を使用できます。
PDFファイルを暗号化したい場合は、次のコードスニペットを試してください：

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 暗号化されるPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイルを暗号化する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/)関数を呼び出します。
1. パスワード「user」と「owner」でPDFファイルを暗号化します。
1. したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultEncrypt.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、つまり、ファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* パスワード "user" と "owner" で PDF ファイルを暗号化し、"ResultEncrypt.pdf" に保存 */
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

さまざまな[暗号化権限](https://reference.aspose.com/pdf/cpp/namespace-aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c)があります:

- Module.Permissions.PrintDocument
- Module.Permissions.ModifyContent
- Module.Permissions.ExtractContent

- Module.Permissions.ModifyTextAnnotations
- Module.Permissions.FillForm
- Module.Permissions.ExtractContentWithDisabilities
- Module.Permissions.AssembleDocument
- Module.Permissions.PrintingQuality

さまざまな[暗号化アルゴリズム](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66)があります：

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 暗号化が変更されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/)関数を呼び出します。
1. パスワード「user」と「owner」でPDFファイルを復号化します。

1. したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultEncrypt.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、つまり、ファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルを "user" および "owner" のパスワードで暗号化し、"ResultEncrypt.pdf" に保存*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```