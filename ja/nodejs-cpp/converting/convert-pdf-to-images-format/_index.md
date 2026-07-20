---
title: Node.jsでPDFを画像形式に変換する
linktitle: PDFを画像に変換する
type: docs
weight: 70
url: /ja/nodejs-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-18"
description: このトピックでは、Node.js 環境で数行のコードを使用して、Aspose.PDF を利用し、PDF を TIFF、BMP、JPEG、PNG、SVG などのさまざまな画像形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Node.jsでPDFを画像に変換

この記事では、PDF を画像形式に変換するオプションをご紹介します。

以前にスキャンされた文書は、PDF ファイル形式で保存されることが多いです。しかし、グラフィックエディタで編集したり、画像形式でさらに送信したりする必要がありますか？PDF を画像に変換するための汎用ツールをご用意しています。 
最も一般的なタスクは、PDF ドキュメント全体またはドキュメントの特定のページを画像のセットとして保存する必要がある場合です。**Aspose for Node.js via C++** は、PDF を JPG および PNG フォーマットに変換でき、特定の PDF ファイルから画像を取得するために必要な手順を簡素化します。

**Aspose.PDF for Node.js via C++** はさまざまな PDF から画像形式への変換をサポートしています。セクションを確認してください。 [Aspose.PDF 対応ファイル形式](https://docs.aspose.com/pdf/nodejs-cpp/supported-file-formats/).

{{% alert color="success" %}}
**オンラインでPDFをJPEGに変換してみてください**

Aspose.PDF for Node.js は、オンラインで無料のアプリケーションをご提供します [PDFからJPEGへ](https://products.aspose.app/pdf/conversion/pdf-to-jpg)、そこで機能とそれが動作する品質を調査しようと試みることができます。

[![Aspose.PDF 変換: PDF から JPEG へ（無料アプリ）](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## PDF を JPEG に変換

PDF ドキュメントを変換したい場合は、以下を使用できます [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/) 関数。 
Node.js環境で変換するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換される PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promiseとして、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfToJpg{0:D2}.jpg" に保存されます。{0:D2} は2桁形式のページ番号を表します。画像は解像度150 DPIで保存されます。json.errorCode パラメータが 0 でなく、ファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to JPG with template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
      console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換される PDF ファイルの名前を指定してください
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfToJpg{0:D2}.jpg" に保存されます。{0:D2} は2桁形式のページ番号を表します。画像は解像度150 DPIで保存されます。json.errorCode パラメータが 0 でなく、ファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to JPG with template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
  console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**PDF をオンラインで TIFF に変換しよう**

Aspose.PDF for Node.js は、オンラインで無料のアプリケーションをご提供します ["PDFからTIFFへ"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)、そこで機能とそれが動作する品質を調査しようと試みることができます。

[![Aspose.PDF 変換 PDF を TIFF に無料アプリで](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## PDF を TIFF に変換する

PDF ドキュメントを変換したい場合は、以下を使用できます [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/) 関数。 
Node.js環境で変換するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換される PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promiseとして、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfToTiff{0:D2}.tiff" に保存されます。{0:D2} は2桁形式のページ番号を表します。画像は解像度150 DPIで保存されます。json.errorCode パラメータが 0 でなく、ファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to TIFF with template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
      console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換される PDF ファイルの名前を指定してください
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfToTiff{0:D2}.tiff" に保存されます。{0:D2} は2桁形式のページ番号を表します。画像は解像度150 DPIで保存されます。json.errorCode パラメータが 0 でなく、ファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to TIFF with template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
  console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**PDF を PNG にオンラインで変換してみてください**

無料アプリの動作例として、次の機能をご確認ください。

Aspose.PDF for Node.js は、オンラインで無料のアプリケーションをご提供します ["PDF から PNG へ"](https://products.aspose.app/pdf/conversion/pdf-to-png)、そこで機能とそれが動作する品質を調査しようと試みることができます。

[![無料アプリを使用してPDFをPNGに変換する方法](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## PDFをPNGに変換する

PDF ドキュメントを変換したい場合は、以下を使用できます [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/) 関数。 
Node.js環境で変換するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換される PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promiseとして、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. PDFファイルを変換します。そのため、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfToPng{0:D2}.png" に保存されます。{0:D2} は2桁形式のページ番号を表します。画像は 150 DPI の解像度で保存されます。'json.errorCode' パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PNG with template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
      console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換される PDF ファイルの名前を指定してください
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. PDFファイルを変換します。そのため、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfToPng{0:D2}.png" に保存されます。{0:D2} は2桁形式のページ番号を表します。画像は 150 DPI の解像度で保存されます。'json.errorCode' パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PNG with template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
  console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**PDF をオンラインで SVG に変換してみる**

Aspose.PDF for Node.js は、オンラインで無料のアプリケーションをご提供します ["PDF を SVG に変換"](https://products.aspose.app/pdf/conversion/pdf-to-svg)、そこで機能とそれが動作する品質を調査しようと試みることができます。

[![Aspose.PDF 無料アプリで PDF を SVG に変換](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** は、2 次元ベクトルグラフィックス（静的および動的（インタラクティブまたはアニメーション））のための XML ベースのファイル形式の仕様群です。SVG 仕様は、1999 年以来 World Wide Web Consortium (W3C) によって開発が進められているオープンスタンダードです。

## PDFをSVGに変換

### PDFを古典的なSVGに変換する

PDF ドキュメントを変換したい場合は、以下を使用できます [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/) 関数。 
Node.js環境で変換するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換される PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promiseとして、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfToSvg.svg" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが出る場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to SVG and save the "ResultPdfToSvg.svg"*/
      const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
      console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換される PDF ファイルの名前を指定してください
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfToSvg.svg" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが出る場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to SVG and save the "ResultPdfToSvg.svg"*/
  const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
  console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

### PDF を zip 圧縮された SVG に変換する

PDF ドキュメントを変換したい場合は、以下を使用できます [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/) 関数。 
Node.js環境で変換するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換される PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promiseとして、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. PDF ファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfToSvgZip.zip" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to SVG(zip) and save the "ResultPdfToSvgZip.zip"*/
      const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
      console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換される PDF ファイルの名前を指定してください
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. PDF ファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfToSvgZip.zip" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*convert a PDF-file to SVG zip and save the "ResultPdfToSvgZip.zip"*/
  const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
  console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText)
```

## PDF を DICOM に変換

PDF ドキュメントを変換したい場合は、以下を使用できます [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/) 関数。 
Node.js環境で変換するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換される PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promiseとして、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfToDICOM{0:D2}.dcm" に保存されます。{0:D2} は 2 桁形式のページ番号を表します。画像は 150 DPI の解像度で保存されます。json.errorCode パラメータが 0 でなく、ファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to DICOM with template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
      console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換される PDF ファイルの名前を指定してください
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. PDFファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfToDICOM{0:D2}.dcm" に保存されます。{0:D2} は 2 桁形式のページ番号を表します。画像は 150 DPI の解像度で保存されます。json.errorCode パラメータが 0 でなく、ファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to DICOM with template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
  console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

## PDF を BMP に変換

PDF ドキュメントを変換したい場合は、以下を使用できます [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/) 関数。 
Node.js環境で変換するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 変換される PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promiseとして、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. PDF ファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfToBmp{0:D2}.bmp" に保存されます。ここで {0:D2} は 2 桁形式のページ番号を表します。画像は 150 DPI の解像度で保存されます。json.errorCode パラメータが 0 でなく、ファイルにエラーが出た場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to BMP with template "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
      console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 変換される PDF ファイルの名前を指定してください
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. PDF ファイルを変換します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfToBmp{0:D2}.bmp" に保存されます。ここで {0:D2} は 2 桁形式のページ番号を表します。画像は 150 DPI の解像度で保存されます。json.errorCode パラメータが 0 でなく、ファイルにエラーが出た場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to BMP with template "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
  console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```





