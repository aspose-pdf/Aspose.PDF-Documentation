---
title: Node.jsでPDFをEPUB、TeX、テキスト、XPSに変換する
linktitle: PDFを他の形式に変換する
type: docs
weight: 90
url: /ja/nodejs-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-18"
description: このトピックでは、Node.js 環境で PDF ファイルを EPUB、LaTeX、テキスト、XPS 等の他のファイル形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

{{% alert color="success" %}}
**PDF をオンラインで EPUB に変換してみる**

Aspose.PDF for Node.js はオンラインの無料アプリケーションを提供します ["PDFからEPUBへ"](https://products.aspose.app/pdf/conversion/pdf-to-epub), そこで、機能と品質がどのように動作するかを調査しようとすることができます。

[![Aspose.PDF 無料アプリで PDF を EPUB に変換](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## PDF を EPUB に変換する

**<abbr title="Electronic Publication">EPUB</abbr>**は、International Digital Publishing Forum (IDPF) が策定した自由かつオープンな電子書籍標準です。ファイルの拡張子は .epub です。
EPUBはリフロー可能なコンテンツ向けに設計されており、EPUBリーダーが特定の表示デバイスに合わせてテキストを最適化できることを意味します。EPUBは固定レイアウトのコンテンツもサポートしています。このフォーマットは、出版社やコンバージョンハウスが社内で使用できる単一のフォーマットであると同時に、配布や販売にも利用できるよう意図されています。Open eBook規格に取って代わります。

PDF ドキュメントを変換したい場合は、次のものを使用できます [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/) 関数。 
Node.js 環境で変換するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換される PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promise として、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. PDFファイルを変換します。したがって、'json.errorCode' が0の場合、操作の結果は "ResultPDFtoEPUB.epub" に保存されます。json.errorCode パラメータが0でない場合、そしてそれに応じてファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
      const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
      console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換される PDF ファイルの名前を指定してください
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. PDFファイルを変換します。したがって、'json.errorCode' が0の場合、操作の結果は "ResultPDFtoEPUB.epub" に保存されます。json.errorCode パラメータが0でない場合、そしてそれに応じてファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
  const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
  console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**PDFをオンラインでLaTeX/TeXに変換してみる**

Aspose.PDF for Node.js はオンラインの無料アプリケーションを提供します ["PDF を LaTeX に"](https://products.aspose.app/pdf/conversion/pdf-to-tex), そこで、機能と品質がどのように動作するかを調査しようとすることができます。

[![Aspose.PDF 変換 PDF を LaTeX/TeX に無料アプリで](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## PDFをTeXに変換する

**Aspose.PDF for Node.js** は PDF を TeX に変換することをサポートしています。
PDF ドキュメントを変換したい場合は、次のものを使用できます [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/) 関数。 
Node.js 環境で変換するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換される PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promise として、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPDFtoTeX.tex" に保存されます。json.errorCode パラメータが 0 でなく、したがってファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
      const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
      console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換される PDF ファイルの名前を指定してください
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPDFtoTeX.tex" に保存されます。json.errorCode パラメータが 0 でなく、したがってファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
  const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
  console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**PDFをテキストに変換するオンラインツールを試す**

Aspose.PDF for Node.js はオンラインの無料アプリケーションを提供します ["PDFからテキストへ"](https://products.aspose.app/pdf/conversion/pdf-to-txt), そこで、機能と品質がどのように動作するかを調査しようとすることができます。

[![Aspose.PDF を使用した PDF からテキストへの無料アプリでの変換](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDF を TXT に変換

PDF ドキュメントを変換したい場合は、次のものを使用できます [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/) 関数。 
Node.js 環境で変換するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換される PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promise として、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPDFtoTxt.txt" に保存されます。json.errorCode パラメーターが 0 でない場合、そしてそれに応じてファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
      const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
      console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換される PDF ファイルの名前を指定してください
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPDFtoTxt.txt" に保存されます。json.errorCode パラメーターが 0 でない場合、そしてそれに応じてファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
  const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
  console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**PDF を XPS にオンラインで変換してみよう**

Aspose.PDF for Node.js はオンラインの無料アプリケーションを提供します ["PDF から XPS へ"](https://products.aspose.app/pdf/conversion/pdf-to-xps), そこで、機能と品質がどのように動作するかを調査しようとすることができます。

[![Aspose.PDF 無料アプリによる PDF から XPS への変換](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## PDF を XPS に変換

XPSファイルタイプは主にMicrosoft CorporationによるXML Paper Specificationに関連付けられています。XML Paper Specification（XPS）は、かつてコードネーム「Metro」と呼ばれ、Next Generation Print Path（NGPP）というマーケティングコンセプトを包括していたMicrosoftの取り組みであり、文書の作成と閲覧をWindowsオペレーティングシステムに統合することを目的としています。

**Aspose.PDF for Node.js** は PDF ファイルを変換する可能性を提供します <abbr title="XML Paper Specification">XPS</abbr> 形式です。Node.js で PDF ファイルを XPS 形式に変換するために、提示されたコードスニペットを使用してみましょう。

PDF ドキュメントを変換したい場合は、次のものを使用できます [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/) 関数。 
Node.js 環境で変換するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換される PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promise として、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPDFtoXps.xps" に保存されます。json.errorCode パラメータが 0 でなく、結果としてファイルにエラーが出る場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
      const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
      console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換される PDF ファイルの名前を指定してください。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPDFtoXps.xps" に保存されます。json.errorCode パラメータが 0 でなく、結果としてファイルにエラーが出る場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
  const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
  console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## PDF をグレースケール PDF に変換

Aspose.PDF for Node.js via C++ ツールキットを使用して PDF を白黒に変換する。 
PDFをグレースケールに変換すべき理由は何ですか？ PDFファイルに多数のカラー画像が含まれており、カラーよりもファイルサイズが重要な場合、変換により容量を節約できます。 PDFファイルを白黒で印刷する場合、変換しておくことで最終的な結果がどのようになるかを視覚的に確認できます。 

PDF ドキュメントを変換したい場合は、次のものを使用できます [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/) 関数。 
Node.js 環境で変換するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換される PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promise として、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultConvertToGrayscale.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

const AsposePdf = require('asposepdfnodejs');
const pdf_file = 'Aspose.pdf';
AsposePdf().then(AsposePdfModule => {
    /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
    const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
    console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
});
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換される PDF ファイルの名前を指定してください。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultConvertToGrayscale.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
  const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
  console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```






