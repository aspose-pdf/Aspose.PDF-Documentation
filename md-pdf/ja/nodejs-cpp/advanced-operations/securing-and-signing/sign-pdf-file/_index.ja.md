---
title: Node.jsでPDFにデジタル署名を追加
linktitle: PDFにデジタル署名
type: docs
weight: 70
url: /nodejs-cpp/sign-pdf/
description: Node.js環境でPDFドキュメントにデジタル署名を付与します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFドキュメントのデジタル署名は、ドキュメントの真正性と整合性を確認する方法です。これは、プライベートキーとデジタル証明書を使用してPDFドキュメントに電子署名を付けるプロセスです。この署名により、ドキュメントが署名後に変更されていないことと、署名者が承認された人物であることが保証されます。Node.jsでPDFに署名するには、Aspose.PDFツールを使用します。

PDFファイルに署名したい場合は、[AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/)関数を使用できます。

署名に関連する**パラメータ**を使用することが可能です:

- fileName
- pageNum
- fileSign
- pswSign
- setXIndent
- setYIndent
- setHeight
- setWidth
- reason

- contact
- location
- isVisible
- signatureAppearance
- fileNameResult 

このコードスニペットは、Node.js環境でAsposePDFforNode.jsモジュールを使用して、PKCS7署名を使用してPDFファイルにデジタル署名を行います。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 署名するPDFファイルの名前、PKCS7キーのファイル、および署名の外観画像ファイルを指定します。証明書と画像は、PDF署名のためにアップロードするどこからでもファイルシステム上に配置できます。
1. `AsposePdf`をPromiseとして呼び出し、ファイルの署名操作を実行します。成功した場合はオブジェクトを受け取ります。
1. [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/)関数を呼び出します。
1. デジタル署名でPDFファイルに署名します。署名に関連するパラメータ（キーのファイル、パスワード、座標、理由、連絡先、場所など）。

1. したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultSignPKCS7.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、したがって、ファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PKCS7キー*/
      const test_pfx_file = 'test.pfx';
      /*署名の見た目*/
      const sign_img_file = 'Aspose.jpg';
      /*PDFファイルにデジタル署名を付けて "ResultSignPKCS7.pdf" に保存する*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "理由", "連絡先", "場所", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。

1. 署名するPDFファイル、PKCS7キーファイル、および署名の外観画像ファイルの名前を指定します。  
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。  
1. [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) 関数を呼び出します。  
1. デジタル署名でPDFファイルに署名します。署名に関連するパラメータ（キー ファイル、パスワード、座標、理由、連絡先、場所など）。  
1. このようにして、'json.errorCode' が 0 の場合、操作の結果は "ResultSignPKCS7.pdf" に保存されます。json.errorCode パラメータが 0 でなく、それに応じてファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

import AsposePdf from 'asposepdfnodejs';
const AsposePdfModule = await AsposePdf();
const pdf_file = 'Aspose.pdf';
/*キー PKCS7*/
const test_pfx_file = 'test.pfx';
/*署名の外観*/
const sign_img_file = 'Aspose.jpg';
/*デジタル署名でPDFファイルに署名し、"ResultSignPKCS7.pdf"を保存する*/
const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```