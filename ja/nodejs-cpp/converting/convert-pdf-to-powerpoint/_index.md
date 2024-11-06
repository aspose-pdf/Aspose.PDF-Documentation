---
title: Node.jsでPDFをPPTXに変換
linktitle: PDFをPowerPointに変換
type: docs
weight: 30
url: ja/nodejs-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-16"
description: Aspose.PDFを使用すると、Node.js環境で直接PDFをPPTX形式に変換できます。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert color="success" %}}
**オンラインでPDFをPowerPointに変換してみてください**

Aspose.PDF for Node.jsは、オンラインで無料アプリケーション["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)を提供しており、機能と品質を試すことができます。

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## PDFをPPTXに変換

PDFドキュメントを変換したい場合は、[AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/)関数を使用できます。

Node.js環境で変換するための次のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイルの変換操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数 [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/) を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPDFtoPptX.pptx"に保存されます。json.errorCodeパラメータが0でない場合、つまりファイルにエラーが発生した場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* PDFファイルをPptXに変換し、"ResultPDFtoPptX.pptx"として保存 */
      const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
      console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPDFtoPptX.pptx"に保存されます。json.errorCodeパラメータが0でない場合、ファイルにエラーが表示され、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをPptXに変換し、"ResultPDFtoPptX.pptx"に保存します*/
  const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
  console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```