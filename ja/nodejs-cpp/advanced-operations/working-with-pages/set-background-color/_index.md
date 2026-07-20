---
title: Node.jsでPDFの背景色を設定する
linktitle: 背景色を設定する
type: docs
weight: 80
url: /ja/nodejs-cpp/set-background-color/
description: Node.js経由でC++を使用して、あなたのPDFファイルの背景色を設定する。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFの背景色を設定したい場合は、次を使用できます [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/) 関数。 

Node.js 環境で PDF の背景色を設定するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 背景色を設定したい PDF ファイルの名前を指定します。
1. 呼び出す `AsposePdf` Promiseとして背景色設定の操作を実行し、成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出します [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. PDFファイルの背景色を設定します。この関数には3つの引数を渡す必要があります：入力ファイル名、16進数形式の希望色、そして出力ファイル名です。したがって、‘json.errorCode’が0の場合、操作の結果は“ResultRotation.pdf”に保存されます。json.errorCode パラメータが0でない場合、ファイルにエラーが発生し、そのエラー情報は‘json.errorText’に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 背景色を設定したい PDF ファイルの名前を指定します。
1. `AsposePdf` モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出します [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. PDF ファイルの背景色を設定します。背景色は "#426bf4" に設定されており、これは青系の色を表す 16 進カラーコードです。そのため、'json.errorCode' が 0 の場合、操作の結果は "ResultRotation.pdf" に保存されます。'json.errorCode' パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```