---
title: Node.js で PDF を復号化
linktitle: PDF ファイルを復号化
type: docs
weight: 40
url: /ja/nodejs-cpp/decrypt-pdf/
description: Aspose.PDF for Node.js via C++ を使用して PDF ファイルを復号化。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 所有者パスワードを使用して PDF ファイルを復号化

近年、インターネット詐欺の被害に遭わず、文書を保護するために、暗号化された文書をやり取りするユーザーがますます増えています。
この点において、暗号化された PDF ファイルにアクセスする必要がありますが、アクセスできるのは権限のあるユーザーだけです。また、PDF ファイルを復号化するさまざまなソリューションが求められています。 

PDF ファイルを復号したい場合は、次を使用できます [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) 関数。 
PDF ファイルを復号したい場合は、次のコードスニペットを試してください:

**CommonJS:**

1. 呼び出し `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 復号化される PDF ファイルの名前を指定してください。
1. 呼び出し `AsposePdf` Promiseとして、ファイルの復号化操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 呼び出す [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) 関数。
1. パスワードが "owner" の PDF ファイルを復号化します。
1. したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultDecrypt.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポートする `asposepdfnodejs` モジュール。
1. 復号化される PDF ファイルの名前を指定してください。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 呼び出す [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) 関数。
1. パスワードが "owner" の PDF ファイルを復号化します。
1. したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultDecrypt.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```