---
title: Node.js で PDF/A を PDF 形式に変換する
linktitle: PDF/A を PDF 形式に変換する
type: docs
weight: 110
url: /ja/nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2026-07-18"
description: このトピックでは、Aspose.PDF が Node.js 環境で PDF/A ファイルを PDF ドキュメントに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF/A を PDF 形式に変換する

PDF ドキュメントを変換したい場合は、次を使用できます [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/) 関数。 
Node.js 環境で変換するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換する PDF ファイルの名前を指定します。
1. 呼び出す `AsposePdf` Promiseとして、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. PDF ファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultConvertToPDF.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換される PDF/A ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを取得します。
1. 関数を呼び出す [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. PDF ファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultConvertToPDF.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```