---
title: Node.jsでPDFをExcelに変換する
linktitle: PDFをExcelに変換
type: docs
weight: 20
url: ja/nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-16"
keywords: node.jsを使用してPDFをExcelに変換, PDFをXLSXに変換
description: Aspose.PDF for Node.jsを使ってPDFをXLSX形式に変換します。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Node.jsを使用してPDFからスプレッドシートを作成する

**Aspose.PDF for Node.js via C++**は、PDFファイルをExcelファイルに変換する機能をサポートしています。

{{% alert color="success" %}}
**PDFをExcelにオンラインで変換してみてください**

Aspose.PDF for Node.jsは、オンラインで無料アプリケーション["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDFで無料アプリを使用してPDFをExcelに変換](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## PDFをXLSXに変換

PDFドキュメントを変換したい場合は、[AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/)関数を使用できます。
 
次のコードスニペットを確認して、Node.js環境に変換してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイル変換の操作を行います。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は「ResultPDFtoXlsX.xlsx」に保存されます。json.errorCodeパラメータが0でなく、それに応じてファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルをXlsXに変換し、「ResultPDFtoXlsX.xlsx」に保存する*/
      const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
      console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPDFtoXlsX.xlsx"に保存されます。json.errorCodeパラメータが0でない場合で、ファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをXlsXに変換し、"ResultPDFtoXlsX.xlsx"として保存*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```