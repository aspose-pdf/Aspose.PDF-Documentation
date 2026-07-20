---
title: Node.js で PDF にデジタル署名を追加する
linktitle: PDF にデジタル署名する
type: docs
weight: 70
url: /ja/nodejs-cpp/sign-pdf/
description: Node.js 環境で PDF ドキュメントにデジタル署名する。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


PDF ドキュメントにおけるデジタル署名は、文書の真正性と完全性を検証する方法です。これは、プライベートキーとデジタル証明書を使用して PDF ドキュメントに電子署名を行うプロセスです。この署名は、署名後に文書が変更されていないこと、そして署名者がその文書の承認者であることを保証します。Node.js で PDF に署名するには、Aspose.PDF ツールを使用します。

PDF ファイルに署名したい場合は、次のものを使用できます [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) function.

署名に関連する **parameters** を使用できます:

- fileName
- pageNum
- fileSign
- pswSign
- setXIndent
- setYIndent
- setHeight
- setWidth
- 理由
- 連絡先
- 場所
- isVisible
- signatureAppearance
- fileNameResult 

このコードスニペットは、Node.js 環境で AsposePDFforNode.js モジュールを使用して、PKCS7 署名を用いて PDF ファイルにデジタル署名を行います。

**CommonJS:**

1. 呼び出す `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 署名対象の PDF ファイル名、PKCS7 鍵ファイル、署名外観画像ファイルを指定します。証明書と画像は、PDF 署名のためにアップロードする任意のファイルシステム上の場所に配置できます。
1. 呼び出す `AsposePdf` Promiseとして、ファイルの署名操作を実行します。成功した場合、オブジェクトを受け取ります。
1. 呼び出す [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) function. 
1. デジタル署名で PDF ファイルに署名します。署名に関連するパラメータ（鍵ファイル、パスワード、座標、理由、連絡先、場所など）。 
1. したがって、‘json.errorCode’ が 0 の場合、操作の結果は “ResultSignPKCS7.pdf” に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は ‘json.errorText’ に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Key PKCS7*/
      const test_pfx_file = 'test.pfx';
      /*Signature appearance*/
      const sign_img_file = 'Aspose.jpg';
      /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 署名対象の PDF ファイル名、PKCS7 キーファイル、および署名外観画像ファイルを指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 呼び出す [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) function. 
1. デジタル署名で PDF ファイルに署名します。署名に関連するパラメータ（鍵ファイル、パスワード、座標、理由、連絡先、場所など）。 
1. したがって、‘json.errorCode’ が 0 の場合、操作の結果は “ResultSignPKCS7.pdf” に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は ‘json.errorText’ に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Key PKCS7*/
  const test_pfx_file = 'test.pfx';
  /*Signature appearance*/
  const sign_img_file = 'Aspose.jpg';
  /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
  const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
  console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```