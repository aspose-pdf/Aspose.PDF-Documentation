---
title: Node.jsでPDFリソースを最適化
linktitle: PDFリソースを最適化
type: docs
weight: 15
url: /nodejs-cpp/optimize-pdf-resources/
description: Node.jsツールを使用してPDFファイルのリソースを最適化し、Web表示を高速化します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFリソースを最適化

ドキュメントのリソースを最適化します:

1. ドキュメントページで使用されていないリソースは削除されます
1. 同一のリソースは単一のオブジェクトに統合されます
1. 使用されていないオブジェクトは削除されます

PDFリソースを最適化したい場合は、[AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/)関数を使用できます。Node.js環境でPDFリソースを最適化するための次のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. リソースを最適化するPDFファイルの名前を指定します。

1. `AsposePdf`をPromiseとして呼び出し、ファイルの最適化操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/)を呼び出します。
1. PDFリソースを最適化します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfOptimizeResource.pdf"に保存されます。json.errorCodeパラメータが0でない場合、およびそれに応じてファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルのリソースを最適化し、"ResultPdfOptimizeResource.pdf"を保存します*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。
1. リソースを最適化するPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数 [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/) を呼び出します。
1. PDFリソースを最適化します。したがって、'json.errorCode' が0の場合、操作の結果は "ResultPdfOptimizeResource.pdf" に保存されます。json.errorCode パラメータが0でない場合、およびそれに応じてファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルのリソースを最適化し、"ResultPdfOptimizeResource.pdf" として保存します*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```