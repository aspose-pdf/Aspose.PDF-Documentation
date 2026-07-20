---
title: Node.js で PDF を Excel に変換する
linktitle: PDF を Excel に変換する
type: docs
weight: 20
url: /ja/nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2026-07-18"
description: Aspose.PDF for Node.js は、PDF を XLSX 形式に変換することを可能にします。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Node.js を使用して PDF からスプレッドシートを作成する 

**Aspose.PDF for Node.js via C++** は、PDF ファイルを Excel ファイルに変換する機能をサポートしています。

{{% alert color="success" %}}
**PDFをExcelにオンラインで変換してみましょう**

Aspose.PDF for Node.js はオンラインの無料アプリケーションを提供します ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), その機能と品質を試すことができます。

[![Aspose.PDF 無料アプリでPDFからExcelへの変換](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## PDF を XLSX に変換

PDF ドキュメントを変換したい場合は、次のものを使用できます [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/) 関数。 
Node.js 環境で変換するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換対象となる PDF ファイルの名前を指定します。
1. 呼び出す `AsposePdf` Promise として、ファイル変換の操作を実行します。成功した場合は、オブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. PDF ファイルを変換します。したがって、‘json.errorCode’ が 0 の場合、操作結果は “ResultPDFtoXlsX.xlsx” に保存されます。‘json.errorCode’ パラメータが 0 でない場合、ファイルにエラーが表示され、そのエラー情報は ‘json.errorText’ に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
      console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換対象となる PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトが返されます。
1. 関数を呼び出す [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. PDF ファイルを変換します。したがって、‘json.errorCode’ が 0 の場合、操作結果は “ResultPDFtoXlsX.xlsx” に保存されます。‘json.errorCode’ パラメータが 0 でない場合、ファイルにエラーが表示され、そのエラー情報は ‘json.errorText’ に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

