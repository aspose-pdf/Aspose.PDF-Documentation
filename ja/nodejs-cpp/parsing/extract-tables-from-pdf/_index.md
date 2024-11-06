---
title: Node.jsでPDFからテーブルを抽出する
linktitle: PDFからテーブルを抽出
type: docs
weight: 10
url: ja/nodejs-cpp/extract-tables-from-the-pdf-file/
description: Aspose.PDF for Node.js via C++ツールキットを使用してPDFをCSVに変換する方法。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFをCSVファイルに変換しながらテーブルを抽出

### PDFをCSVに変換

PDFにテーブルがある場合、それらは別々のCSVファイルに保存されます。PDFドキュメントを変換したい場合は、[AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/)関数を使用できます。Node.js環境でPDFファイルを変換するための以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出して`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換するPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイルを変換する操作を実行します。成功した場合はオブジェクトを受け取ります。

1. 関数 [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/) を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode' が0の場合、操作の結果は "ResultPDFtoXlsX.xlsx" に保存されます。json.errorCode パラメータが0でない場合、およびそれに応じてファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*テンプレート "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... ページ番号形式) を使用して、PDFファイルをCSVに変換（テーブルを抽出）し、TABを区切り文字として保存します*/
      const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
      console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。

1. 変換されるPDFファイルの名前を指定します。  
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数 [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/) を呼び出します。
1. PDFファイルを変換します。このようにして、'json.errorCode'が0の場合、操作の結果は"ResultPDFtoXlsX.xlsx"に保存されます。json.errorCodeパラメータが0でない場合、およびそれに応じてファイルにエラーが発生した場合、エラー情報は'json.errorText'に含まれます。

```js
import AsposePdf from 'asposepdfnodejs';
const AsposePdfModule = await AsposePdf();
const pdf_file = 'Aspose.pdf';
/*PDFファイルをCSVに変換（テンプレート "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... ページ番号フォーマット)、区切り文字としてTABを使用し保存)*/
const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```