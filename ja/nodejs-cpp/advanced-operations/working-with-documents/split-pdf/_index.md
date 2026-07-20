---
title: Node.jsでPDFを分割する
linktitle: PDFファイルを分割する
type: docs
weight: 30
url: /ja/nodejs-cpp/split-pdf/
description: このトピックでは、Aspose.PDF for Node.js via C++ を使用して、PDFページを個別のPDFファイルに分割する方法を示します。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Node.jsを使用してPDFを2つのファイルに分割する

単一のPDFを分割したい場合は、次の方法を使用できます [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/) 関数。 
Node.js 環境で 2 つの PDF を分割するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出し `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 分割する PDF ファイルの名前を指定します。
1. 呼び出し `AsposePdf` Promiseとして、ファイル分割の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. 2つの PDF ファイルを分割します。変数 pageToSplit を 1 に設定し、PDF ファイルがページ 1 で分割されることを示します。 
1. したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultSplit1.pdf" および "ResultSplit2.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが表示され、そのエラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set number a page to split*/
      const pageToSplit = 1;
      /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 分割する PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. 2つの PDF ファイルを分割します。変数 pageToSplit を 1 に設定し、PDF ファイルがページ 1 で分割されることを示します。 
1. したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultSplit1.pdf" および "ResultSplit2.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが表示され、そのエラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set number a page to split*/
  const pageToSplit = 1;
  /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```