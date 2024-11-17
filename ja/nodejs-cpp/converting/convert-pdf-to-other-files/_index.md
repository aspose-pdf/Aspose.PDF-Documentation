---
title: Node.jsでPDFをEPUB、TeX、Text、XPSに変換する
linktitle: PDFを他のフォーマットに変換する
type: docs
weight: 90
url: /ja/nodejs-cpp/convert-pdf-to-other-files/
lastmod: "2023-11-16"
description: このトピックでは、Node.js環境でPDFファイルをEPUB、LaTeX、Text、XPSなどの他のファイル形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

{{% alert color="success" %}}
**PDFをEPUBにオンラインで変換してみる**

Aspose.PDF for Node.jsは、オンラインで無料アプリケーション["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)を提供しており、機能や品質を調査することができます。

[![Aspose.PDF Convertion PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## PDFをEPUBに変換する

**<abbr title="Electronic Publication">EPUB</abbr>**は、国際デジタル出版フォーラム（IDPF）による無料でオープンな電子書籍の規格です。
 ファイルには拡張子.epubが付いています。  
EPUBはリフロー可能なコンテンツ用に設計されており、EPUBリーダーが特定の表示デバイスに最適化されたテキストを表示できます。EPUBは固定レイアウトのコンテンツもサポートしています。このフォーマットは、出版社や変換ハウスが社内で使用するため、また配布や販売のための単一のフォーマットとして意図されています。これはOpen eBook標準に取って代わります。

PDFドキュメントを変換したい場合は、[AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/)関数を使用できます。  
Node.js環境で変換するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換するPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイルを変換する操作を実行します。成功した場合、オブジェクトを受け取ります。
1. 関数[AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0であれば、操作の結果は"ResultPDFtoEPUB.epub"に保存されます。json.errorCodeパラメーターが0でない場合、つまりファイルにエラーが発生した場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルをePubに変換して"ResultPDFtoEPUB.epub"に保存する*/
      const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
      console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数[AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/)を呼び出します。

1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPDFtoEPUB.epub"に保存されます。json.errorCodeパラメータが0でない場合、およびそれに応じてファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /* PDFファイルをePubに変換し、"ResultPDFtoEPUB.epub"を保存します */
  const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
  console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**PDFをLaTeX/TeXにオンラインで変換してみてください**

Node.js用Aspose.PDFは、オンラインの無料アプリケーション["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)を提供しており、機能性とその動作の品質を調査することができます。


[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## PDFをTeXに変換する

**Aspose.PDF for Node.js**はPDFをTeXに変換することをサポートしています。
PDFドキュメントを変換したい場合は、[AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/)関数を使用できます。
Node.js環境で変換するための以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出して`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイルを変換する操作を実行します。成功すればオブジェクトを受け取ります。
1. 関数[AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPDFtoTeX.tex"に保存されます。json.errorCodeのパラメータが0でなく、ファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルをTeXに変換し"ResultPDFtoTeX.tex"として保存します*/
      const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
      console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数[AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPDFtoTeX.tex"に保存されます。もしjson.errorCodeパラメータが0でなく、ファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをTeXに変換し、"ResultPDFtoTeX.tex"に保存します*/
  const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
  console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**PDFをテキストにオンラインで変換してみてください**

Aspose.PDF for Node.jsは、オンラインで無料のアプリケーション["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion PDF to Text with Free App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDFをTXTに変換

PDFドキュメントを変換したい場合は、[AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/)関数を使用できます。Node.js環境で変換するためには、以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイル変換の操作を実行します。成功した場合、オブジェクトを受け取ります。
1. 関数[AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/)を呼び出します。

1. PDFファイルを変換します。したがって、'json.errorCode'が0である場合、操作の結果は「ResultPDFtoTxt.txt」に保存されます。json.errorCodeパラメータが0でなく、したがってファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* PDFファイルをTxtに変換し、「ResultPDFtoTxt.txt」に保存 */
      const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
      console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数[AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/)を呼び出します。

1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPDFtoTxt.txt"に保存されます。json.errorCodeパラメーターが0でなく、ファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js
  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをTxtに変換し、"ResultPDFtoTxt.txt"に保存します*/
  const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
  console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**PDFをオンラインでXPSに変換してみてください**

Node.js用Aspose.PDFは、オンラインで無料のアプリケーション["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)を提供しており、そこで機能や品質を調査することができます。


[![Aspose.PDF Convertion PDF to XPS with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## PDFをXPSに変換

XPSファイルタイプは、主にMicrosoft CorporationによるXML Paper Specificationに関連付けられています。XML Paper Specification（XPS）は、かつてMetroというコードネームで呼ばれ、次世代印刷パス（NGPP）マーケティングコンセプトを包含し、Windowsオペレーティングシステムに文書作成と表示を統合するためのMicrosoftの取り組みです。

**Aspose.PDF for Node.js**は、PDFファイルを<abbr title="XML Paper Specification">XPS</abbr>形式に変換する可能性を提供します。Node.jsを使用してPDFファイルをXPS形式に変換するために示されたコードスニペットを試してみましょう。

PDFドキュメントを変換したい場合は、[AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/)関数を使用することができます。
Node.js環境で変換を行うための次のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換されるPDFファイルの名前を指定します。

1. `AsposePdf`をPromiseとして呼び出し、ファイル変換の操作を行います。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPDFtoXps.xps"に保存されます。json.errorCodeパラメータが0でなく、ファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルをXpsに変換し、"ResultPDFtoXps.xps"に保存*/
      const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
      console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 変換するPDFファイルの名前を指定します。

1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPDFtoXps.xps"に保存されます。json.errorCodeパラメータが0でなく、したがってファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをXpsに変換し、"ResultPDFtoXps.xps"として保存します*/
  const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
  console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## PDFをグレースケールPDFに変換

Aspose.PDF for Node.js via C++ツールキットでPDFを白黒に変換します。
なぜPDFをグレースケールに変換する必要があるのか？
 PDFファイルに多くのカラー画像が含まれていて、ファイルサイズがカラーよりも重要な場合、変換はスペースを節約します。PDFファイルを白黒で印刷する場合、変換することで最終結果がどのように見えるかを視覚的に確認できます。

PDFドキュメントを変換したい場合は、[AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/)関数を使用できます。Node.js環境で変換するための以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイルを変換する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0である場合、操作の結果は「ResultConvertToGrayscale.pdf」に保存されます。json.errorCodeパラメータが0でなく、ファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

const AsposePdf = require('asposepdfnodejs');
const pdf_file = 'Aspose.pdf';
AsposePdf().then(AsposePdfModule => {
    /* PDFファイルをグレースケールに変換して"ResultConvertToGrayscale.pdf"に保存します */
    const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
    console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
});
```

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。

1. 関数 [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/) を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultConvertToGrayscale.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、つまりファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをグレースケールに変換し、"ResultConvertToGrayscale.pdf"として保存します*/
  const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
  console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```