---
title: PDFをEPUB、TeX、Text、XPSにJavaScriptで変換
linktitle: PDFを他の形式に変換
type: docs
weight: 90
url: /ja/javascript-cpp/convert-pdf-to-other-files/
lastmod: "2023-11-01"
description: このトピックでは、JavaScriptまたはJavaScriptを使用してPDFファイルをEPUB、LaTeX、Text、XPSなどの他のファイル形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

変換操作はドキュメント内のページ数に依存し、非常に時間がかかることがあります。したがって、Web Workersの使用を強くお勧めします。

このコードは、リソース集約型のPDFファイル変換タスクをWeb Workerにオフロードして、メインUIスレッドをブロックしないようにする方法を示しています。また、変換されたファイルをダウンロードするためのユーザーフレンドリーな方法も提供します。

{{% alert color="success" %}}
**PDFをEPUBにオンラインで変換してみてください**

Aspose.PDF for JavaScriptは、オンラインで無料で利用できるアプリケーション「[PDF to EPUB](https://products.aspose.app/pdf/conversion/pdf-to-epub)」を提供しており、その機能と品質を試してみることができます。

[![Aspose.PDF Convertion PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## PDFをEPUBに変換

**<abbr title="Electronic Publication">EPUB</abbr>**は、国際デジタル出版フォーラム（IDPF）による自由でオープンな電子書籍標準です。ファイルには拡張子.epubが付きます。  
EPUBはリフロー可能なコンテンツ用に設計されており、EPUBリーダーは特定の表示デバイスにテキストを最適化できます。EPUBは固定レイアウトのコンテンツもサポートしています。この形式は、出版社や変換ハウスが社内で使用するための単一の形式として、また配布や販売のために意図されています。これはOpen eBook標準に取って代わるものです。

```js

    /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/epub+zip", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileToEPUB = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルをePubに変換し、"ResultPDFtoEPUB.epub"として保存 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToEPUB', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoEPUB.epub"] }, [event.target.result]);
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


次のJavaScriptコードスニペットは、PDFページをEPUBファイルに変換する簡単な例を示しています：

1. 変換するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfToEPUB](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftoepub/) 関数が実行されます。
1. 結果ファイルの名前が設定されます。この例では "ResultPDFtoEPUB.epub" です。
1. 次に、'json.errorCode' が0の場合、結果ファイルには前に指定した名前が付けられます。'json.errorCode' パラメータが0でない場合、ファイルにエラーがあり、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードできるようにします。

```js

    var ffileToEPUB = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDFファイルをEPUBに変換し、「ResultPDFtoEPUB.epub」として保存する*/
        const json = AsposePdfToEPUB(event.target.result, e.target.files[0].name, "ResultPDFtoEPUB.epub");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするリンクを作成する*/
        DownloadFile(json.fileNameResult, "application/epub+zip");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**PDFをLaTeX/TeXにオンラインで変換してみてください**

Aspose.PDF for JavaScriptは、オンラインで無料アプリケーション["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)を提供しており、機能性と品質を試すことができます。

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## PDFをTeXに変換する

**Aspose.PDF for JavaScript**はPDFをTeXに変換することをサポートしています。
LaTeXファイル形式は、特殊なマークアップを持つテキストファイル形式で、高品質な組版のためにTeXベースのドキュメント準備システムで使用されます。

```js

  /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了！' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/x-tex", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileToTeX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルをTeXに変換し、"ResultPDFtoTeX.tex"を保存 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToTeX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoTeX.tex"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするためのリンクを作成*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "ここをクリックしてファイル " + filename + " をダウンロード";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


以下のJavaScriptコードスニペットは、PDFページをTEXファイルに変換する簡単な例を示しています。

1. 変換するPDFファイルを選択します。
2. 'FileReader'を作成します。
3. [AsposePdfToTeX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftotex/) 関数が実行されます。
4. 結果ファイルの名前が設定されます。この例では「ResultPDFtoTeX.tex」です。
5. 次に、'json.errorCode'が0の場合、結果ファイルは前に指定した名前が付けられます。'json.errorCode'パラメータが0でない場合、それに応じてファイルにエラーが生じた場合、そのようなエラーに関する情報は'json.errorText'ファイルに含まれます。
6. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数がリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードできるようにします。

```js

    var ffileToTeX = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDFファイルをTeXに変換し「ResultPDFtoTeX.tex」に保存*/
        const json = AsposePdfToTeX(event.target.result, e.target.files[0].name, "ResultPDFtoTeX.tex");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするためのリンクを作成*/
        DownloadFile(json.fileNameResult, "application/x-tex");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**PDFをテキストにオンラインで変換してみてください**

Aspose.PDF for JavaScriptは、オンラインで無料で利用できるアプリケーション["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)を提供しており、その機能と品質を確認することができます。

[![Aspose.PDF Convertion PDF to Text with Free App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDFをTXTに変換

```js

    /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "text/plain", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileToTxt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルをTxtに変換して"ResultPDFtoTxt.txt"として保存 - Web Workerに要求*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToTxt', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoTxt.txt"] }, [event.target.result]);
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


以下のJavaScriptコードスニペットは、PDFページをTXTファイルに変換する簡単な例を示しています：

1. 変換するPDFファイルを選択します。
2. 'FileReader'を作成します。
3. [AsposePdfToTxt](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftotxt/) 関数が実行されます。
4. 結果ファイルの名前が設定されます。この例では "ResultPDFtoTxt.txt" です。
5. 次に、'json.errorCode' が0の場合、結果ファイルには先に指定した名前が付けられます。'json.errorCode' パラメータが0でない場合、ファイルにエラーが発生し、そのエラーに関する情報は 'json.errorText' ファイルに含まれます。
6. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数がリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードできるようにします。

```js

    var ffileToTxt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDFファイルをTxtに変換し、"ResultPDFtoTxt.txt"として保存する*/
        const json = AsposePdfToTxt(event.target.result, e.target.files[0].name, "ResultPDFtoTxt.txt");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするリンクを作成する*/
        DownloadFile(json.fileNameResult, "text/plain");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**PDFをXPSにオンラインで変換してみてください**

Aspose.PDF for JavaScriptは、オンラインで無料で使用できるアプリケーション["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion PDF to XPS with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## PDFをXPSに変換する

XPSファイル形式は、主にMicrosoft CorporationによるXML Paper Specificationに関連しています。XML Paper Specification（XPS）は、以前はMetroというコードネームで呼ばれており、次世代印刷パス（NGPP）マーケティングコンセプトを包含し、MicrosoftがWindowsオペレーティングシステムに文書作成と表示を統合するための取り組みです。

**Aspose.PDF for JavaScript**は、PDFファイルを<abbr title="XML Paper Specification">XPS</abbr>形式に変換する可能性を提供します。JavaScriptを使用してPDFファイルをXPS形式に変換するために提示されたコードスニペットを試してみましょう。

```js

    /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了！' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.ms-xpsdocument", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileToXps = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルをXpsに変換して"ResultPDFtoXps.xps"を保存 - Web Workerに問い合わせ*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXps', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXps.xps"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするリンクを作成*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "ここをクリックしてファイルをダウンロード " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


次のJavaScriptコードスニペットは、PDFページをXPSファイルに変換する簡単な例を示しています。

1. 変換するPDFファイルを選択します。
2. 'FileReader'を作成します。
3. [AsposePdfToXps](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftoxps/) 関数が実行されます。
4. 結果のファイルの名前が設定され、この例では "ResultPDFtoXps.xps" です。
5. 次に、'json.errorCode' が0の場合、結果のファイルには先に指定した名前が付けられます。'json.errorCode' パラメータが0でない場合、ファイルにエラーが発生し、そのエラーに関する情報は 'json.errorText' ファイルに含まれます。
6. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数がリンクを生成し、結果のファイルをユーザーのオペレーティングシステムにダウンロードすることができます。

```js

    var ffileToXps = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDFファイルをXpsに変換し、"ResultPDFtoXps.xps"として保存*/
        const json = AsposePdfToXps(event.target.result, e.target.files[0].name, "ResultPDFtoXps.xps");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするリンクを作成*/
        DownloadFile(json.fileNameResult, "application/vnd.ms-xpsdocument");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## PDFをグレースケールPDFに変換

Aspose.PDF for JavaScript via C++ Webツールキットを使用してPDFを白黒に変換します。 なぜPDFをグレースケールに変換する必要があるのですか？PDFファイルに多くのカラフルな画像が含まれており、ファイルサイズが重要であれば、グレースケールに変換することでスペースを節約できます。PDFファイルを白黒で印刷する場合、変換することで最終結果がどのように見えるかを視覚的に確認することができます。

```js

  /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了！' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileConvertToGrayscale = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルをグレースケールに変換して"ResultConvertToGrayscale.pdf"として保存 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToGrayscale', "params": [event.target.result, e.target.files[0].name, "ResultConvertToGrayscale.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [コードスニペット]

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


以下のJavaScriptコードスニペットは、PDFページをグレースケールPDFに変換する簡単な例を示しています：

1. 変換するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttograyscale/) 関数が実行されます。
1. 結果ファイルの名前が設定されます。この例では "ResultConvertToGrayscale.pdf" です。
1. 次に、'json.errorCode'が0であれば、指定した名前でDownloadFileが生成されます。'json.errorCode'パラメータが0でない場合、つまりファイルにエラーがある場合、そのエラーに関する情報が'json.errorText'ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードできるようにします。

```js

  var ffileConvertToGrayscale = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /* PDFファイルをグレースケールに変換して "ResultConvertToGrayscale.pdf" として保存 */
      const json = AsposePdfConvertToGrayscale(event.target.result, e.target.files[0].name, "ResultConvertToGrayscale.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /* 結果ファイルをダウンロードするためのリンクを作成 */
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```