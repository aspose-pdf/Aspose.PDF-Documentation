---
title: JavaScriptでPDFを画像形式に変換
linktitle: PDFを画像に変換
type: docs
weight: 70
url: ja/javascript-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-01"
description: この記事では、Aspose.PDFを使用してPDFをTIFF、BMP、JPEG、PNG、SVGなどのさまざまな画像形式に数行のコードで変換する方法を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## JavaScriptでPDFを画像に変換

この記事では、PDFを画像形式に変換するオプションを紹介します。

以前にスキャンされたドキュメントは、しばしばPDFファイル形式で保存されます。しかし、グラフィックエディタで編集したり、画像形式で送信したりする必要がありますか？PDFを画像に変換するためのユニバーサルツールをご用意しています。
最も一般的なタスクは、PDFドキュメント全体または特定のページを一連の画像として保存する必要があるときです。**Aspose for JavaScript via C++**を使用すると、特定のPDFファイルから画像を取得するために必要な手順を簡素化するために、PDFをJPGおよびPNG形式に変換できます。

**Aspose.PDF for JavaScript via C++**は、さまざまなPDFから画像形式への変換をサポートしています。
 Please checks the section [Aspose.PDF Supported File Formats](https://docs.aspose.com/pdf/javascript-cpp/supported-file-formats/) を確認してください。

変換操作はドキュメント内のページ数に依存し、非常に時間がかかる場合があります。そのため、Web Workers の使用を強くお勧めします。

このコードは、リソースを多く消費する PDF ファイルの変換タスクを Web Worker にオフロードして、メインの UI スレッドのブロックを防ぐ方法を示しています。また、変換されたファイルをダウンロードするユーザーフレンドリーな方法も提供しています。

{{% alert color="success" %}}
**PDF を JPEG にオンラインで変換してみてください**

Aspose.PDF for JavaScript は無料のオンラインアプリケーション ["PDF to JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg) を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF conversion PDF to JPEG with Free App](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## PDF を JPEG に変換する

```js
  /*Web Worker を作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Worker からのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? 
          `ファイル（ページ）数: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラー*/
    const ffileToJpg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*PDF ファイルを jpg ファイルに変換し、テンプレート "ResultPdfToJpg{0:D2}.jpg" で保存する（{0}, {0:D2}, {0:D3}, ... ページ番号をフォーマット）、解像度 150 DPI - Web Worker に依頼*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToJpg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [コードスニペット]

    /*結果ファイルをダウンロードするためのリンクを作成*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "ファイルをダウンロードするにはここをクリック " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```

次のJavaScriptコードスニペットは、PDFページをJpegファイルに変換する簡単な例を示しています：

1. 変換するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestojpg/) 関数が実行されます。
1. 結果として得られるファイルの名前が設定されます。この例では "ResultPdfToJpg{0:D2}.jpg" です。
1. 次に、'json.errorCode' が0の場合、結果ファイルには以前に指定した名前が付けられます。'json.errorCode' パラメータが0でない場合、従ってファイルにエラーがある場合、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数がリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードできるようにします。

```js

  var ffileToJpg = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDFファイルをjpgファイルに変換し、テンプレート "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... ページ番号の形式)、解像度150DPIで保存*/
      const json = AsposePdfPagesToJpg(event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "ファイル(ページ)数: " + json.filesCount.toString();
        /*結果ファイルへのリンクを作成*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**PDFをTIFFにオンラインで変換してみてください**

Aspose.PDF for JavaScriptは、オンライン無料アプリケーション["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)を提供しており、機能とその品質を確認できます。

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## PDFをTIFFに変換

```js

  /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'ロード完了！' :
        (evt.data.json.errorCode == 0) ? 
          `ファイル(ページ)数: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/tiff", element) ) ?? ""}` : 
          `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラー*/
    const ffileToTiff = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルをテンプレート"ResultPdfToTiff{0:D2}.tiff"（{0}, {0:D2}, {0:D3}, ... 形式のページ番号）、解像度150 DPIでTIFFに変換し保存 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToTiff', "params": [event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするリンクを作成*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "ファイルをダウンロードするにはここをクリック: " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


以下のJavaScriptコードスニペットは、PDFページをTiffファイルに変換する簡単な例を示しています。

1. 変換するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestotiff/) 関数が実行されます。
1. 結果のファイルの名前が設定され、この例では"ResultPdfToTiff{0:D2}.tiff"です。
1. 次に、'json.errorCode'が0の場合、あなたのDownloadFileには前に指定した名前が付けられます。 'json.errorCode'パラメータが0でない場合、したがってファイルにエラーがある場合、そのようなエラーに関する情報は'json.errorText'ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数がリンクを生成し、ユーザーのオペレーティングシステムに結果のファイルをダウンロードできるようにします。

```js

    var ffileToTiff = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*テンプレート"ResultPdfToTiff{0:D2}.tiff"（{0}, {0:D2}, {0:D3}, ... ページ番号の形式）、150 DPIの解像度でPDFファイルをTIFFに変換し、保存する*/
        const json = AsposePdfPagesToTiff(event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "ファイル(ページ)の数: " + json.filesCount.toString();
          /*結果ファイルへのリンクを作成する*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/tiff");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


{{% alert color="success" %}}
**PDFをPNGにオンラインで変換してみてください**

無料アプリケーションがどのように機能するかの例として、次の機能を確認してください。

Aspose.PDF for JavaScriptは、オンラインで無料のアプリケーション["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)を提供しており、その機能と品質を調査することができます。

[![無料アプリを使用してPDFをPNGに変換する方法](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## PDFをPNGに変換

```js

  /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? 
          `ファイル(ページ)数: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/png", element) ) ?? ""}` : 
          `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileToPng = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*PDFファイルをテンプレート "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... フォーマットページ番号)、解像度150 DPIでpngファイルに変換し保存 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToPng', "params": [event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [コードスニペット]

    /*結果ファイルをダウンロードするためのリンクを作成*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "ファイル " + filename + " をダウンロードするにはここをクリックしてください";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


以下のJavaScriptコードスニペットは、PDFページをPNGファイルに変換する簡単な例を示しています。

1. 変換するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfPagesToPng](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestopng/) 関数が実行されます。
1. 結果ファイルの名前が設定され、この例では「ResultPdfToPng{0:D2}.png」となっています。
1. 次に、'json.errorCode'が0の場合、指定した名前でDownloadFileが提供されます。'json.errorCode'パラメータが0でない場合、つまり、ファイルにエラーがある場合、そのエラーに関する情報は'json.errorText'ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数がリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードできるようにします。

```js

  var ffileToPng = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDFファイルをテンプレート"ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... ページ番号フォーマット)で、解像度150 DPIでpngファイルに変換して保存*/
      const json = AsposePdfPagesToPng(event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "ファイル(ページ)数: " + json.filesCount.toString();
        /*結果ファイルへのリンクを作成*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/png");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**PDFをSVGにオンラインで変換してみる**

Aspose.PDF for JavaScriptは、オンライン無料アプリケーション["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion PDF to SVG with Free App](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**スケーラブルベクターグラフィックス (SVG)** は、二次元ベクターグラフィックスのためのXMLベースのファイル形式の仕様のファミリーで、静的および動的（インタラクティブまたはアニメーション）に対応しています。SVG仕様は、1999年からワールドワイドウェブコンソーシアム (W3C) によって開発されているオープンスタンダードです。

## PDFをSVGに変換

```js

  /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? 
          `ファイル（ページ）数: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/svg", element) ) ?? ""}` : 
          `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileToSvg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルをSVGに変換 - Web Workerに問い合わせる*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするためのリンクを作成*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "ファイル " + filename + " をダウンロードするにはここをクリック";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


以下のJavaScriptコードスニペットは、PDFページをSVGファイルに変換する簡単な例を示しています：

1. 変換するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvg/) 関数が実行されます。
1. 結果ファイルの名前が設定されます。この例では "ResultPdfToSvg.svg" です。
1. 次に、'json.errorCode'が0の場合、DownloadFileには前に指定した名前が与えられます。'json.errorCode'パラメータが0でない場合、つまりファイルにエラーがある場合、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、結果ファイルをユーザーのオペレーティングシステムにダウンロードできるようにします。

```js

    var ffileToSvg = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDFファイルをSVGに変換*/
        const json = AsposePdfPagesToSvg(event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "ファイル(ページ)数: " + json.filesCount.toString();
          /*結果ファイルへのリンク作成*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/svg");
        }
        else document.getElementById('output').textContent = json.errorText;
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


### PDFを圧縮されたSVGに変換

```js

  /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/zip", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileToSvgZip = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルをSVG(zip)に変換し、"ResultPdfToSvgZip.zip"として保存 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvgZip', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするリンクを作成*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "ファイルをダウンロードするにはここをクリック " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


以下のJavaScriptコードスニペットは、PDFページをSVG(zip)ファイルに変換する簡単な例を示しています：

1. 変換するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvgzip/) 関数が実行されます。
1. 結果ファイルの名前が設定されます。この例では "ResultPdfToSvgZip.zip" です。
1. 次に、'json.errorCode'が0であれば、DownloadFileには前に指定した名前が与えられます。'json.errorCode'パラメータが0でない場合、ファイルにエラーがあることになり、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードすることを可能にします。

```js

    var ffileToSvgZip = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDFファイルをSVG(zip)に変換し、"ResultPdfToSvgZip.zip"として保存する*/
        const json = AsposePdfPagesToSvgZip(event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするためのリンクを作成する*/
        DownloadFile(json.fileNameResult, "application/zip");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## PDFをDICOMに変換

```js

  /*Web Workerを作成*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? '読み込み完了!' :
      (evt.data.json.errorCode == 0) ?
        `ファイル(ページ)の数: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
          (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "application/dicom", element) ) ?? ""}` :
        `エラー: ${evt.data.json.errorText}`;

  /*イベントハンドラ*/
  const ffileToDICOM = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*PDFファイルをDICOMに変換、テンプレート"ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... ページ番号形式)を使用し、解像度150 DPIで保存 - Web Workerに依頼*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToDICOM', "params": [event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150] }, [event.target.result]);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

  /*結果ファイルをダウンロードするリンクを作成*/
  const DownloadFile = (filename, mime, content) => {
      mime = mime || "application/octet-stream";
      var link = document.createElement("a"); 
      link.href = URL.createObjectURL(new Blob([content], {type: mime}));
      link.download = filename;
      link.innerHTML = "ファイルをダウンロードするにはここをクリック " + filename;
      document.body.appendChild(link); 
      document.body.appendChild(document.createElement("br"));
      return filename;
    }
```


以下のJavaScriptコードスニペットは、PDFページをDICOMファイルに変換する簡単な例を示しています:

1. 変換するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestodicom/) 関数が実行されます。
1. 結果ファイルの名前が設定され、この例では「ResultPdfToDICOM{0:D2}.dcm」となります。
1. 次に、'json.errorCode'が0の場合、結果ファイルには前に指定した名前が付きます。'json.errorCode'パラメータが0でない場合、ファイルにエラーが生じることになり、そのエラーに関する情報は'json.errorText'ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数がリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードできるようにします。

```js

  var ffileToDICOM = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDFファイルをDICOMに変換し、テンプレート "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... ページ番号形式)、解像度150 DPIで保存*/
      const json = AsposePdfPagesToDICOM(event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "ファイル(ページ)数: " + json.filesCount.toString();
        /*結果ファイルへのリンクを作成*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "application/dicom");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## PDFをBMPに変換

```js

    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? 
          `ファイル（ページ）数: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/bmp", element) ) ?? ""}` : 
          `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラー*/
    const ffileToBmp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルをBMPに変換し、テンプレート "ResultPdfToBmp{0:D2}.bmp"（{0}, {0:D2}, {0:D3} などのページ番号形式）、解像度150 DPIで保存 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToBmp', "params": [event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするリンクを作成*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "ファイル " + filename + " をダウンロードするにはここをクリック";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


以下のJavaScriptコードスニペットは、PDFページをBMPファイルに変換する簡単な例を示しています。

1. 変換するPDFファイルを選択します。
2. 'FileReader'を作成します。
3. [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestobmp/)関数が実行されます。
4. 結果のファイル名が設定されます。この例では"ResultPdfToBmp{0:D2}.bmp"です。
5. 次に、'json.errorCode'が0の場合、指定した名前でDownloadFileが提供されます。'json.errorCode'パラメータが0でない場合、つまりファイルにエラーがある場合、そのようなエラーに関する情報は'json.errorText'ファイルに含まれます。
6. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/)関数はリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードすることを可能にします。

```js

    var ffileToBmp = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDFファイルをBMPに変換し、テンプレート"ResultPdfToBmp{0:D2}.bmp"（{0}, {0:D2}, {0:D3}, ...ページ番号形式）、解像度150 DPIで保存*/
        const json = AsposePdfPagesToBmp(event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "ファイル（ページ）数: " + json.filesCount.toString();
          /*結果ファイルへのリンクを作成*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/bmp");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```