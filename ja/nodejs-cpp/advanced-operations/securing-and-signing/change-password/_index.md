---
title: Node.jsでPDFファイルのパスワードを変更する
linktitle: パスワードを変更
type: docs
weight: 50
url: /ja/nodejs-cpp/change-password-pdf/
description: Aspose.PDF for Node.js via C++を使用してPDFファイルのパスワードを変更します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFファイルのパスワードを変更する

PDFのパスワードを変更したい場合は、[AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/)関数を使用できます。これは、元のセキュリティ設定を保持しつつ、オーナーパスワードによってユーザーパスワードとオーナーパスワードを変更します。PDFファイルのパスワードを「owner」から「newowner」または「newuser」に変更したい場合は、次のコードスニペットを試してください。

**CommonJS:**

1. `require`を呼び出して`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. パスワードを変更するPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、パスワードを変更する操作を実行します。成功した場合はオブジェクトを受け取ります。

1. 関数 [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/) を呼び出します。
1. パスワードを変更します。既存のオーナーパスワードは "owner" に設定されており、新しいオーナーパスワード "newowner" に、そして新しいユーザーパスワード "newuser" に変更されます。
1. したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfChangePassword.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、したがってファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルのパスワードを "owner" から "newowner" に変更し、"ResultPdfChangePassword.pdf" として保存します*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


パスワードが空の文字列である場合に注意してください:

1. ユーザーパスワードが空の場合 - PDFはパスワードを求めずに開きます（しかし、依然として暗号化されています）。
2. オーナーパスワードが空の場合、PDFはユーザーパスワードを要求します。
3. 両方が空の場合 - PDFはパスワードを求めずに開きます（しかし、依然として暗号化されています）。

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
2. パスワードを変更するPDFファイルの名前を指定します。
3. AsposePdfモジュールを初期化します。成功した場合、オブジェクトを受け取ります。
4. 関数[AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/)を呼び出します。
5. パスワードの変更を行います。既存のオーナーパスワードは"owner"に設定され、新しいオーナーパスワード"newowner"と新しいユーザーパスワード"newuser"に変更されます。

1. したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfChangePassword.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、およびそれに応じて、ファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /* PDFファイルのパスワードを "owner" から "newowner" に変更し、"ResultPdfChangePassword.pdf" として保存する */
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```