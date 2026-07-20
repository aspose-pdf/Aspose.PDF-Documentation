---
title: Node.jsでPDFを暗号化
linktitle: PDFファイルを暗号化
type: docs
weight: 50
url: /ja/nodejs-cpp/encrypt-pdf/
description: Aspose.PDF for Node.js via C++ を使用してPDFファイルを暗号化。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## ユーザーまたはオーナーパスワードを使用してPDFファイルを暗号化

機密情報を含むPDF添付ファイルをメールで送信する場合、まずそれにセキュリティを追加して不正な手に渡らないようにしたいと思うかもしれません。PDF文書への不正アクセスを制限する最善の方法は、パスワードで保護することです。文書を簡単かつ安全に暗号化するには、Aspose.PDF for Node.js via C++ を使用できます。

>PDFファイルを暗号化する際に、ユーザーとオーナーのパスワードを異なるものに指定してください。

- 設定されている場合、**User password** は PDF を開くために提供する必要があるものです。Acrobat/Reader はユーザーにユーザーパスワードの入力を求めます。正しくない場合、ドキュメントは開きません。
- 設定されている場合、**Owner password** は印刷、編集、抽出、コメントなどの権限を制御します。Acrobat/Reader は権限設定に基づきこれらの操作を許可しません。権限を設定/変更したい場合、Acrobat はこのパスワードを要求します。

PDF ファイルを暗号化したい場合は、次のものを使用できます [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) 関数。 
PDF ファイルを暗号化したい場合は、次のコードスニペットを試してください：

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 暗号化する PDF ファイルの名前を指定します。
1. 呼び出す `AsposePdf` Promiseとして、ファイルを暗号化する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 呼び出す [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) 関数。 
1. パスワード “user” と “owner” を使用して PDF ファイルを暗号化します。
1. したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultEncrypt.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが出た場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

異なるものがあります [暗号化権限](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c):

- AsposePdfModule.Permissions.PrintDocument
- AsposePdfModule.Permissions.ModifyContent
- AsposePdfModule.Permissions.ContentCopy
- AsposePdfModule.Permissions.ModifyTextAnnotations
- AsposePdfModule.Permissions.FillForm
- AsposePdfModule.Permissions.ContentCopyForAccessibility
- AsposePdfModule.Permissions.AssembleDocument
- AsposePdfModule.Permissions.PrintingQuality

さまざまがあります [暗号化アルゴリズム](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66):

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 暗号化された PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 呼び出す [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) 関数。 
1. パスワード "user" と "owner" を使用して PDF ファイルを暗号化します。
1. したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultEncrypt.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが出た場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```