---
title: Node.js で PDF ファイルのパスワードを変更する
linktitle: パスワードを変更する
type: docs
weight: 50
url: /ja/nodejs-cpp/change-password-pdf/
description: C++ を使用した Node.js 用 Aspose.PDF で PDF ファイルのパスワードを変更する。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF ファイルのパスワードを変更する

PDF のパスワードを変更したい場合は、次のように使用できます [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/) function。所有者パスワードでユーザーパスワードと所有者パスワードを変更し、元のセキュリティ設定を保持します。
PDF ファイルのパスワードを "owner" から "newowner" または "newuser" に変更したい場合は、次のコードスニペットを試してください：

**CommonJS:**

1. 呼び出し `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. パスワードを変更する PDF ファイルの名前を指定します。
1. 呼び出し `AsposePdf` Promise としてパスワード変更の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. パスワードを変更します。既存のオーナーパスワードは "owner," に設定されており、新しいユーザーパスワード "newuser" とともに "newowner" に変更されます。
1. したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfChangePassword.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに伴いファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

パスワードが空文字列の場合はご注意ください：

1. ユーザーパスワードが空の場合、PDFはパスワードの入力を求めずに開きます（ただし、暗号化はされたままです）。
1. 所有者のパスワードが空の場合、PDF はユーザーパスワードの入力を求めて開きます。
1. 両方が空の場合  - PDF はパスワードの入力を求めずに開きます（ただし暗号化はされます）。


**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. パスワードを変更する PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを取得します。
1. 関数を呼び出す [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. パスワードを変更します。既存のオーナーパスワードは "owner," に設定されており、新しいユーザーパスワード "newuser" とともに "newowner" に変更されます。
1. したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfChangePassword.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに伴いファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```