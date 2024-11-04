---
title: PDFをPDF/A形式に変換する方法 (Node.js)
linktitle: PDFをPDF/A形式に変換
type: docs
weight: 100
url: /nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-16"
description: このトピックでは、Aspose.PDFを使用してNode.js環境でPDFファイルをPDF/A準拠のPDFファイルに変換する方法を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Node.js**は、PDFファイルを<abbr title="電子文書のアーカイブ用ポータブルドキュメントフォーマット">PDF/A</abbr>準拠のPDFファイルに変換することができます。

{{% alert color="success" %}}
**PDFをPDF/Aにオンラインで変換してみましょう**

Aspose.PDF for Node.jsは、オンラインで無料のアプリケーション["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)を提供しており、機能と品質を調査することができます。

[![Aspose.PDFでPDFをPDF/Aに無料アプリで変換](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

## PDFをPDF/A形式に変換する

PDFドキュメントを変換したい場合は、[AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/)関数を使用できます。
 
以下のコードスニペットを確認して、Node.js環境で変換を行ってください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイルを変換する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/)を呼び出します。
1. PDFファイルを修復します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultConvertToPDFA.pdf"に保存されます。変換プロセス中に検証が行われ、検証結果は"ResultConvertToPDFALog.xml"として保存されます。json.errorCodeパラメータが0でない場合、したがってファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルをPDF/A(1A)に変換し、"ResultConvertToPDFA.pdf"に保存します*/
      /*変換プロセス中に検証も行われます。"ResultConvertToPDFALog.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数 [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/) を呼び出します。
1. PDFファイルを修復します。このようにして、 'json.errorCode' が0の場合、操作の結果は "ResultConvertToPDFA.pdf" に保存されます。変換プロセス中に検証が行われ、検証結果は "ResultConvertToPDFALog.xml" に保存されます。json.errorCodeパラメータが0でない場合、したがってファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをPDF/A(1A)に変換して "ResultConvertToPDFA.pdf" に保存します*/
  /*変換プロセス中に検証も行われ、"ResultConvertToPDFA.xml" に保存されます*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```