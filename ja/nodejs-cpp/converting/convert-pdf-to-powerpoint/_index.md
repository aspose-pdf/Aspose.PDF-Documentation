---
title: Node.js で PDF を PPTX に変換する
linktitle: PDF を PowerPoint に変換する
type: docs
weight: 30
url: /ja/nodejs-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-18"
description: Aspose.PDF を使用すると、Node.js 環境で直接 PDF を PPTX 形式に変換できます。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert color="success" %}}
**オンラインで PDF を PowerPoint に変換してみてください**

Aspose.PDF for Node.js はオンラインの無料アプリケーションを提供します ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), 機能と品質を調べてみることができる場所です。

[![Aspose.PDF 無料アプリで PDF を PPTX に変換](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## PDF を PPTX に変換

PDF 文書を変換したい場合は、次のものを使用できます [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/) 関数。 
Node.js 環境で変換するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出し `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換される PDF ファイルの名前を指定してください。
1. 呼び出し `AsposePdf` Promiseとしてファイル変換操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. PDF ファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPDFtoPptX.pptx" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、そのエラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
      console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換されるPDFファイルの名前を指定してください
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトが返されます。
1. 関数を呼び出す [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. PDF ファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPDFtoPptX.pptx" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、そのエラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
  const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
  console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```