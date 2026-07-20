---
title: Node.js で PDF リソースを最適化する
linktitle: PDF リソースを最適化する
type: docs
weight: 15
url: /ja/nodejs-cpp/optimize-pdf-resources/
description: Node.js ツールを使用して、PDF ファイルのリソースを最適化し、ウェブ表示を高速化します。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF リソースを最適化する

ドキュメント内のリソースを最適化する:

1. ドキュメントページで使用されていないリソースは削除されます
1. 同一のリソースは単一のオブジェクトに結合されます
1. 未使用のオブジェクトは削除されます
 

PDF リソースを最適化したい場合は、次のものを使用できます [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/) 関数。 
Node.js 環境で PDF リソースを最適化するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. リソースを最適化する PDF ファイルの名前を指定します。
1. 呼び出す `AsposePdf` Promiseとして、ファイルの最適化の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. PDF のリソースを最適化します。したがって、`json.errorCode` が 0 の場合、操作の結果は “ResultPdfOptimizeResource.pdf” に保存されます。`json.errorCode` パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は `json.errorText` に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポートする `asposepdfnodejs` モジュール。
1. リソースを最適化する PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトが返されます。
1. 関数を呼び出す [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. PDF のリソースを最適化します。したがって、`json.errorCode` が 0 の場合、操作の結果は “ResultPdfOptimizeResource.pdf” に保存されます。`json.errorCode` パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は `json.errorText` に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```