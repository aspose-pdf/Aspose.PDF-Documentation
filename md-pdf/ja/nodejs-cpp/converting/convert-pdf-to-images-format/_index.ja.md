---
title: Node.jsでPDFを画像形式に変換
linktitle: PDFを画像に変換
type: docs
weight: 70
url: /nodejs-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-16"
description: このトピックでは、Aspose.PDFを使用して、PDFをTIFF、BMP、JPEG、PNG、SVGなどのさまざまな画像形式に変換する方法を、Node.js環境で数行のコードで説明します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Node.js PDFを画像に変換

この記事では、PDFを画像形式に変換するためのオプションを紹介します。

以前にスキャンされたドキュメントは、しばしばPDFファイル形式で保存されます。しかし、それをグラフィックエディターで編集したり、画像形式でさらに送信する必要がありますか？私たちは、PDFを画像に変換するためのユニバーサルツールを提供しています。最も一般的なタスクは、PDFドキュメント全体またはドキュメントの特定のページを画像のセットとして保存する必要がある場合です。
 **Aspose for Node.js via C++** は、特定のPDFファイルから画像を取得するための手順を簡素化するために、PDFをJPGおよびPNG形式に変換することを可能にします。

**Aspose.PDF for Node.js via C++** は、さまざまなPDFから画像形式への変換をサポートしています。セクション [Aspose.PDF Supported File Formats](https://docs.aspose.com/pdf/nodejs-cpp/supported-file-formats/) をご確認ください。

{{% alert color="success" %}}
**PDFをJPEGにオンラインで変換してみる**

Aspose.PDF for Node.js は、無料のオンラインアプリケーション ["PDF to JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg) を提供しており、その機能と品質を調査してみることができます。

[![Aspose.PDF conversion PDF to JPEG with Free App](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## PDFをJPEGに変換

PDFドキュメントを変換したい場合は、[AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/) 関数を使用できます。

Node.js環境で変換するための次のコードスニペットを確認してください。
**CommonJS:**

1. `require` を呼び出し、`asposepdfnodejs` モジュールを `AsposePdf` 変数としてインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. `AsposePdf` をPromiseとして呼び出し、ファイルを変換する操作を行います。成功した場合はオブジェクトを受け取ります。
1. 関数 [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/) を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode' が0であれば、操作の結果は "ResultPdfToJpg{0:D2}.jpg" に保存されます。ここで {0:D2} は2桁のフォーマットでページ番号を表します。画像は150 DPIの解像度で保存されます。json.errorCode パラメータが0でない場合、そしてその結果としてエラーがファイルに表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルをJPGに変換。テンプレート "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... フォーマットのページ番号)、解像度150 DPIで保存*/
      const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
      console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数[AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfToJpg{0:D2}.jpg"に保存されます。ここで、{0:D2}はページ番号を2桁の形式で表します。画像は150 DPIの解像度で保存されます。json.errorCodeパラメータが0でなく、したがってファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをJPGに変換し、テンプレート"ResultPdfToJpg{0:D2}.jpg"（{0}, {0:D2}, {0:D3}, ...形式のページ番号）、解像度150 DPIで保存*/
  const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
  console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**PDFをTIFFにオンラインで変換してみる**

Aspose.PDF for Node.jsは、オンライン無料アプリケーション["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)を提供しています。ここで、その機能と動作の品質を調査することができます。

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## PDFをTIFFに変換

PDFドキュメントを変換したい場合は、[AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/)関数を使用できます。
Node.js環境で変換するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイルを変換する操作を実行します。成功した場合はオブジェクトを受け取ります。

1. 関数 [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/) を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode' が0の場合、操作の結果は "ResultPdfToTiff{0:D2}.tiff" に保存されます。ここで、{0:D2} は2桁の形式のページ番号を表します。画像は150 DPIの解像度で保存されます。json.errorCodeパラメーターが0でない場合、およびそれに応じてファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルをテンプレート "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... ページ番号形式)、解像度150 DPIで変換して保存*/
      const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
      console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数[AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfToTiff{0:D2}.tiff"に保存されます。ここで、{0:D2}は2桁の形式でページ番号を表します。画像は150 DPIの解像度で保存されます。json.errorCodeパラメータが0でない場合、したがってファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをTIFFに変換し、テンプレート"ResultPdfToTiff{0:D2}.tiff"（{0}, {0:D2}, {0:D3}, ...形式のページ番号）、解像度150 DPIで保存*/
  const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
  console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**PDFをPNGにオンラインで変換してみる**

無料アプリケーションの動作例として、次の機能を確認してください。

Aspose.PDF for Node.jsは、オンラインの無料アプリケーション["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)を提供しており、機能と品質を調査することができます。

[![無料アプリを使用してPDFをPNGに変換する方法](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## PDFをPNGに変換

PDFドキュメントを変換したい場合は、[AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/)関数を使用できます。
Node.js環境で変換するには、以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイル変換の操作を実行します。成功した場合はオブジェクトを受け取ります。

1. 関数 [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/) を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode' が0の場合、操作の結果は "ResultPdfToPng{0:D2}.png" に保存されます。ここで、{0:D2} は2桁形式のページ番号を表します。画像は150 DPIの解像度で保存されます。json.errorCodeパラメータが0でない場合、したがってファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*テンプレート "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... 形式のページ番号)、解像度150 DPIでPDFファイルをPNGに変換して保存する*/
      const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
      console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfToPng{0:D2}.png"に保存されます。ここで{0:D2}は2桁の形式でページ番号を表します。画像は150 DPIの解像度で保存されます。json.errorCodeパラメータが0でない場合、またはファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをテンプレート"ResultPdfToPng{0:D2}.png"でPNGに変換します（{0}, {0:D2}, {0:D3}, ...形式のページ番号）、解像度150 DPIで保存します*/
  const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
  console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**オンラインでPDFをSVGに変換してみてください**

Aspose.PDF for Node.jsは、無料のオンラインアプリケーション["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)を提供しており、その機能性と品質を調査することができます。

[![Aspose.PDF Convertion PDF to SVG with Free App](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**スケーラブルベクターグラフィックス (SVG)** は、2次元ベクターグラフィックスのためのXMLベースのファイルフォーマットの仕様ファミリーであり、静的および動的（インタラクティブまたはアニメーション）なものがあります。SVG仕様はオープンスタンダードであり、1999年からワールドワイドウェブコンソーシアム（W3C）によって開発されています。

## PDFをSVGに変換

### PDFをクラシックなSVGに変換

PDFドキュメントを変換したい場合は、[AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/)関数を使用できます。
Node.js環境で変換するために、以下のコードスニペットを確認してください。


**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイル変換の操作を実行します。成功した場合、オブジェクトを受け取ります。
1. 関数[AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/)を呼び出します。
1. PDFファイルを変換します。このようにして、'json.errorCode'が0であれば、操作の結果は"ResultPdfToSvg.svg"に保存されます。json.errorCodeパラメータが0でない場合、またはファイルにエラーが発生した場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルをSVGに変換し、"ResultPdfToSvg.svg"として保存*/
      const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
      console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は「ResultPdfToSvg.svg」に保存されます。json.errorCodeパラメーターが0でなく、ファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをSVGに変換し、"ResultPdfToSvg.svg"に保存する*/
  const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
  console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

### PDFを圧縮されたSVGに変換

PDFドキュメントを変換したい場合は、[AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/)関数を使用できます。
 
以下のコードスニペットを確認し、Node.js環境で変換してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイルを変換する操作を行います。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfToSvgZip.zip"に保存されます。json.errorCodeパラメータが0でない場合、ファイルにエラーが表示され、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルをSVG(zip)に変換し、"ResultPdfToSvgZip.zip"に保存します*/
      const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
      console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数[AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfToSvgZip.zip"に保存されます。json.errorCodeパラメータが0でなく、ファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをSVGのzipに変換し、"ResultPdfToSvgZip.zip"に保存します*/
  const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
  console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText)
```

## PDFをDICOMに変換

PDFドキュメントを変換したい場合は、[AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/)関数を使用できます。
 
以下のコードスニペットを確認して、Node.js環境に変換してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
2. 変換されるPDFファイルの名前を指定します。
3. `AsposePdf`をPromiseとして呼び出し、ファイルを変換する操作を実行します。成功した場合はオブジェクトを受け取ります。
4. 関数[AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/)を呼び出します。
5. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfToDICOM{0:D2}.dcm"に保存されます。ここで、{0:D2}は2桁のフォーマットでページ番号を表します。画像は150 DPIの解像度で保存されます。json.errorCodeパラメータが0でない場合は、エラーがファイルに表示され、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルをテンプレート"ResultPdfToDICOM{0:D2}.dcm"（{0}, {0:D2}, {0:D3}, ... フォーマットページ番号）、解像度150 DPIでDICOMに変換して保存*/
      const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
      console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数 [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/) を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode' が0の場合、操作の結果は "ResultPdfToDICOM{0:D2}.dcm" に保存されます。ここで {0:D2} は2桁の形式でページ番号を表します。画像は150 DPIの解像度で保存されます。json.errorCode パラメータが0でない場合、したがってファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをテンプレート "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ...形式のページ番号)、解像度150 DPIでDICOMに変換して保存*/
  const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
  console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


## PDFをBMPに変換

PDFドキュメントを変換したい場合は、[AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/)関数を使用できます。
Node.js環境で変換するための以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 変換されるPDFファイルの名前を指定します。
1. ファイルを変換するための操作を実行し、成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/)を呼び出します。

1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfToBmp{0:D2}.bmp"に保存されます。ここで、{0:D2}は2桁の形式でページ番号を表します。画像は150 DPIの解像度で保存されます。json.errorCodeパラメータが0でない場合、つまりファイルにエラーが発生した場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルをBMPに変換し、テンプレート"ResultPdfToBmp{0:D2}.bmp"（{0}, {0:D2}, {0:D3}, ...形式のページ番号）、解像度150 DPIで保存*/
      const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
      console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 変換されるPDFファイルの名前を指定します。

1. AsposePdfモジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数[AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/)を呼び出します。
1. PDFファイルを変換します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfToBmp{0:D2}.bmp"に保存されます。ここで{0:D2}は2桁の形式でページ番号を表します。画像は150 DPIの解像度で保存されます。json.errorCodeパラメータが0でなく、したがってファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルをテンプレート"ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... 形式のページ番号)、解像度150 DPIでBMPに変換し保存*/
  const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
  console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```