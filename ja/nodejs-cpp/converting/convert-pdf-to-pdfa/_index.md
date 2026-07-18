---
title: Node.js で PDF を PDF/A 形式に変換する
linktitle: PDF を PDF/A 形式に変換する
type: docs
weight: 100
url: /ja/nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2026-07-18"
description: このトピックでは、Aspose.PDF が Node.js 環境で PDF ファイルを PDF/A 準拠の PDF ファイルに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Node.js** は PDF ファイルを a に変換できるようにします <abbr title="Portable Document Format for Archiving of electronic documents">PDF/A</abbr> 準拠した PDF ファイル。 

{{% alert color="success" %}}
**PDF を PDF/A にオンラインで変換してみてください**

Aspose.PDF for Node.js はオンラインの無料アプリケーションを提供します ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), 機能と品質を調査できる場所です。

[![Aspose.PDF 無料アプリで PDF から PDF/A への変換](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## PDF を PDF/A 形式に変換

PDF ドキュメントを変換したい場合は、次を使用できます [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/) 関数。 
Node.js 環境で変換するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換する PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promiseとして、ファイル変換の操作を実行します。成功した場合、オブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. PDF ファイルを修復します。したがって、‘json.errorCode’ が 0 の場合、操作の結果は “ResultConvertToPDFA.pdf” に保存されます。変換プロセス中に検証が行われ、検証結果は “ResultConvertToPDFALog.xml” に保存されます。‘json.errorCode’ パラメータが 0 でなく、対応してファイルにエラーが表示される場合、エラー情報は ‘json.errorText’ に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
      /*During conversion process, the validation is also performed, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換する PDF ファイルの名前を指定してください。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. PDF ファイルを修復します。したがって、‘json.errorCode’ が 0 の場合、操作の結果は “ResultConvertToPDFA.pdf” に保存されます。変換プロセス中に検証が行われ、検証結果は “ResultConvertToPDFALog.xml” に保存されます。‘json.errorCode’ パラメータが 0 でなく、対応してファイルにエラーが表示される場合、エラー情報は ‘json.errorText’ に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
  /*During conversion process, the validation is also performed, "ResultConvertToPDFA.xml"*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```





