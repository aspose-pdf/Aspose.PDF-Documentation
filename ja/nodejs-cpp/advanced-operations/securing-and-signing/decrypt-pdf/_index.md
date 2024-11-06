---
title: Node.jsでPDFを復号化する
linktitle: PDFファイルを復号化する
type: docs
weight: 40
url: ja/nodejs-cpp/decrypt-pdf/
description: Aspose.PDF for Node.js via C++を使用してPDFファイルを復号化します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## オーナーパスワードを使用してPDFファイルを復号化する

最近、インターネット詐欺の被害に遭わないように、ユーザーが暗号化されたドキュメントを交換することが増えています。このため、認証されたユーザーだけがアクセスできる暗号化されたPDFファイルへのアクセスが必要になります。また、人々はPDFファイルを復号化するためのさまざまなソリューションを探しています。

PDFファイルを復号化したい場合は、[AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) 関数を使用できます。
PDFファイルを復号化したい場合は、次のコードスニペットを試してください：

**CommonJS:**

1. `require` を呼び出し、`asposepdfnodejs` モジュールを `AsposePdf` 変数としてインポートします。
1. 復号化されるPDFファイルの名前を指定します。

1. `AsposePdf`をPromiseとして呼び出し、ファイルの暗号解除操作を実行します。成功した場合はオブジェクトを受け取ります。
1. [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) 関数を呼び出します。
1. パスワードが「owner」のPDFファイルを暗号解除します。
1. したがって、'json.errorCode'が0の場合、操作の結果は"ResultDecrypt.pdf"に保存されます。json.errorCodeパラメータが0でない場合、およびそれに応じてファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*パスワードが「owner」のPDFファイルを暗号解除し、「ResultDecrypt.pdf」に保存します*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 復号化されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/)関数を呼び出します。
1. パスワードが「owner」であるPDFファイルを復号化します。
1. したがって、'json.errorCode'が0の場合、操作の結果は "ResultDecrypt.pdf" に保存されます。json.errorCodeパラメータが0でない場合、つまり、ファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*パスワードが「owner」であるPDFファイルを復号化し、「ResultDecrypt.pdf」に保存します*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```