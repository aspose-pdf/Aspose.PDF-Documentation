---
title: Aspose.PDF for Node.js via C++ を使用して PDF を最適化する
linktitle: PDF ファイルを最適化する
type: docs
weight: 10
url: /ja/nodejs-cpp/optimize-pdf/
description: Node.js 環境を使用して、速い Web 表示のために PDF ファイルを最適化および圧縮する。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF ドキュメントを最適化する

Aspose.PDF for Node.js via C++ のツールキットを使用すると、Node.js 環境向けに PDF コンテンツを最適化できます。 

最適化（またはリニアリゼーション）は、Web ブラウザーでのオンライン閲覧に適した PDF ファイルにするプロセスを指します。

PDF を最適化したい場合は、利用できます [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/) 関数。 
Node.js 環境で PDF ファイルを最適化するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 最適化される PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promiseとして、ファイル最適化の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. PDF ファイルを最適化します。したがって、‘json.errorCode’ が 0 の場合、操作の結果は “ResultOptimize.pdf” に保存されます。json.errorCode パラメータが 0 でなく、ファイルにエラーが発生した場合、エラー情報は ‘json.errorText’ に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 最適化される PDF ファイルの名前を指定してください。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. PDF ファイルを最適化します。したがって、‘json.errorCode’ が 0 の場合、操作の結果は “ResultOptimize.pdf” に保存されます。json.errorCode パラメータが 0 でなく、ファイルにエラーが発生した場合、エラー情報は ‘json.errorText’ に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```