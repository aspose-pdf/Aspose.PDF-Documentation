---
title: PDF/AをPDF形式に変換する方法（Node.js）
linktitle: PDF/AをPDF形式に変換
type: docs
weight: 110
url: /ja/nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-16"
description: このトピックでは、Aspose.PDFを使用してNode.js環境でPDF/AファイルをPDFドキュメントに変換する方法を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF/AをPDF形式に変換

PDFドキュメントを変換したい場合は、[AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/)関数を使用できます。
Node.js環境での変換のため、以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイルを変換する操作を実行します。成功した場合はオブジェクトを受け取ります。

1. 関数 [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/) を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultConvertToPDF.pdf" に保存されます。json.errorCode パラメーターが 0 でない場合、およびそれに応じてファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* PDF/AファイルをPDFに変換して"ResultConvertToPDF.pdf"に保存します */
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。
1. 変換されるPDF/Aファイルの名前を指定します。

1. AsposePdfモジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数[AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultConvertToPDF.pdf"に保存されます。json.errorCodeパラメータが0でない場合、ファイルにエラーが表示されると、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /* PDF/AファイルをPDFに変換し、"ResultConvertToPDF.pdf"として保存します */
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```