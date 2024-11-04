---
title: Aspose.PDF for Node.jsによるPDFの最適化 C++経由
linktitle: PDFファイルの最適化
type: docs
weight: 10
url: /nodejs-cpp/optimize-pdf/
description: Node.js環境を使用してPDFファイルを最適化および圧縮し、Webビューを高速化します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFドキュメントの最適化

Aspose.PDF for Node.js via C++のツールキットを使用すると、Node.js環境向けにPDFコンテンツを最適化できます。

最適化、または線形化とは、PDFファイルをWebブラウザを使用したオンライン閲覧に適したものにするプロセスを指します。

PDFを最適化したい場合は、[AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/)関数を使用できます。 Node.js環境でPDFファイルを最適化するための以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 最適化されるPDFファイルの名前を指定します。

1. `AsposePdf`をPromiseとして呼び出し、ファイルの最適化操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/)を呼び出します。
1. PDFファイルを最適化します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultOptimize.pdf"に保存されます。json.errorCodeパラメータが0でない場合、つまりファイルにエラーが発生した場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルを最適化し"ResultOptimize.pdf"に保存*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 最適化されるPDFファイルの名前を指定します。

1. AsposePdfモジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数[AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/)を呼び出します。
1. PDFファイルを最適化します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultOptimize.pdf"に保存されます。json.errorCodeパラメータが0でない場合、およびファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルを最適化して"ResultOptimize.pdf"に保存する*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```