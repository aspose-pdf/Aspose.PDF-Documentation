---
title: Node.js で PDF を Word 文書に変換する
linktitle: PDF を Word に変換する
type: docs
weight: 10
url: /ja/nodejs-cpp/convert-pdf-to-doc/
lastmod: "2026-07-18"
description: Node.js 環境で PDF を DOC（DOCX）に変換する方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Microsoft Word や DOC および DOCX フォーマットに対応した他のワードプロセッサで PDF ファイルの内容を編集するために。PDF ファイルは編集可能ですが、DOC および DOCX ファイルの方が柔軟でカスタマイズしやすいです。

{{% alert color="success" %}}
**PDF を DOC にオンラインで変換してみてください**

Aspose.PDF for Node.js はオンラインの無料アプリケーションを提供します ["PDF から DOC へ"](https://products.aspose.app/pdf/conversion/pdf-to-doc), 機能と品質がどのように機能するかを調査できる場所です。

[![PDF を DOC に変換](/pdf/ja/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDF を DOC に変換

PDF 文書を変換したい場合は、使用できます [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/) 関数。 
Node.js 環境で変換するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出し `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換する PDF ファイルの名前を指定します。
1. 呼び出し `AsposePdf` Promiseとして、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出します。 [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. PDF ファイルを変換します。そのため、'json.errorCode' が 0 の場合、操作の結果は "ResultPDFtoDoc.doc" に保存されます。json.errorCode パラメータが 0 でない場合、つまりファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc"*/
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポートする `asposepdfnodejs` モジュール。
1. 変換される PDF ファイルの名前を指定します
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトが返されます。
1. 関数を呼び出します。 [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. PDF ファイルを変換します。そのため、'json.errorCode' が 0 の場合、操作の結果は "ResultPDFtoDoc.doc" に保存されます。json.errorCode パラメータが 0 でない場合、つまりファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc"*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**PDF を DOCX にオンラインで変換してみてください**

Aspose.PDF for Node.js はオンラインの無料アプリケーションを提供します ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), 機能と品質がどのように機能するかを調査できる場所です。

[![Aspose.PDF 変換 PDF to Word 無料アプリ](/pdf/ja/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## PDF を DOCX に変換

Aspose.PDF for Node.js via C++ ツールキットを使用すると、PDF ドキュメントを DOCX に読み取りおよび変換できます。DOCX は、構造がプレーンなバイナリから XML とバイナリファイルの組み合わせに変更された、Microsoft Word ドキュメント用のよく知られた形式です。DOCX ファイルは Word 2007 およびそれ以降のバージョンで開くことができますが、DOC ファイル拡張子をサポートする以前の MS Word バージョンでは開けません。

PDF 文書を変換したい場合は、使用できます [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/) 関数。 
Node.js 環境で変換するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出し `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換する PDF ファイルの名前を指定します。
1. 呼び出し `AsposePdf` Promiseとして、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出します。 [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPDFtoDocX.docx" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、そのエラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx"*/
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポートする `asposepdfnodejs` モジュール。
1. 変換される PDF ファイルの名前を指定します
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトが返されます。
1. 関数を呼び出します。 [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPDFtoDocX.docx" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、そのエラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx"*/
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


