---
title: Node.jsでPDFをWord文書に変換
linktitle: PDFをWordに変換
type: docs
weight: 10
url: ja/nodejs-cpp/convert-pdf-to-doc/
lastmod: "2023-11-16"
description: Node.js環境でPDFをDOC(DOCX)に変換する方法を学びます。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDFファイルの内容をMicrosoft WordやDOCおよびDOCX形式をサポートする他のワードプロセッサで編集するには。PDFファイルは編集可能ですが、DOCおよびDOCXファイルの方が柔軟でカスタマイズ可能です。

{{% alert color="success" %}}
**PDFをDOCにオンラインで変換してみる**

Aspose.PDF for Node.jsは、オンラインで無料のアプリケーション["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)を提供しており、その機能と品質を調査することができます。

[![PDFをDOCに変換](/pdf/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDFをDOCに変換

PDFドキュメントを変換したい場合は、[AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/)関数を使用できます。
 
次のコードスニペットを確認し、Node.js環境で変換してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイルを変換する操作を実行します。成功した場合にオブジェクトを受け取ります。
1. 関数[AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPDFtoDoc.doc"に保存されます。json.errorCodeパラメータが0でなく、ファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* PDFファイルをDocに変換し、"ResultPDFtoDoc.doc"に保存する */
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。
1. 変換するPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数 [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/) を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode' が0の場合、操作の結果は "ResultPDFtoDoc.doc" に保存されます。json.errorCode パラメータが0でない場合、またはエラーがファイルに表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをDocに変換し、"ResultPDFtoDoc.doc"に保存します*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**PDFをDOCXにオンラインで変換してみてください**


Node.js用Aspose.PDFは、オンライン無料アプリケーション ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx) を提供しており、その機能と動作の品質を調査することができます。

[![Aspose.PDF 変換 PDF から Word 無料アプリ](/pdf/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## PDF を DOCX に変換

Aspose.PDF for Node.js via C++ ツールキットを使用すると、PDF ドキュメントを読み取り、DOCX に変換できます。DOCX は、Microsoft Word ドキュメントのよく知られた形式で、その構造はプレーンなバイナリから XML とバイナリ ファイルの組み合わせに変更されました。Docx ファイルは Word 2007 およびそれ以降のバージョンで開くことができますが、DOC ファイルの拡張子をサポートする以前のバージョンの MS Word では開くことができません。

PDF ドキュメントを変換したい場合は、[AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/) 関数を使用できます。Node.js 環境で変換するには、以下のコードスニペットを確認してください。

**CommonJS:**

1. `require` を呼び出して、`asposepdfnodejs` モジュールを `AsposePdf` 変数としてインポートします。
1. 変換される PDF ファイルの名前を指定します。

1. `AsposePdf` を Promise として呼び出し、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数 [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/) を呼び出します。
1. PDF ファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPDFtoDocX.docx" に保存されます。json.errorCode パラメータが 0 でない場合、つまりファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルをDocXに変換し、"ResultPDFtoDocX.docx"に保存します*/
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。
1. 変換する PDF ファイルの名前を指定します。

1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/)を呼び出します。
1. PDFファイルを変換します。このようにして、'json.errorCode'が0の場合、操作の結果は"ResultPDFtoDocX.docx"に保存されます。json.errorCodeパラメータが0でない場合、およびそれに応じてファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをDocXに変換し、"ResultPDFtoDocX.docx"を保存します*/
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```