---
title: Node.js で PDF からテーブルを抽出する
linktitle: PDF からテーブルを抽出する
type: docs
weight: 10
url: /ja/nodejs-cpp/extract-tables-from-the-pdf-file/
description: C++ ツールキット経由で Node.js 用 Aspose.PDF を使用して PDF を CSV に変換する方法。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF を CSV ファイルに変換しながらテーブルを抽出する

### PDF を CSV に変換する

PDF にテーブルがある場合、それらは別々の CSV ファイルに保存されます。PDF ドキュメントを変換したい場合は、使用できます [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/) 関数。 
Node.js 環境で PDF ファイルを変換するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換される PDF ファイルの名前を指定します。
1. 呼び出す `AsposePdf` Promise として、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. PDF ファイルを変換します。そのため、'json.errorCode' が 0 の場合、操作の結果は "ResultPDFtoXlsX.xlsx" に保存されます。'json.errorCode' パラメータが 0 でない場合、ファイルにエラーが表示され、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to CSV (extract tables) with template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format page number), TAB as delimiter and save*/
      const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
      console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポートする `asposepdfnodejs` モジュール。
1. 変換される PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. PDF ファイルを変換します。そのため、'json.errorCode' が 0 の場合、操作の結果は "ResultPDFtoXlsX.xlsx" に保存されます。'json.errorCode' パラメータが 0 でない場合、ファイルにエラーが表示され、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to CSV (extract tables) with template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format page number), TAB as delimiter and save*/
  const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
  console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```