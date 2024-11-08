---
title: JavaScriptでPDFをExcelに変換
linktitle: PDFをExcelに変換
type: docs
weight: 20
url: /ja/javascript-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-01"
keywords: JavaScriptを使用してPDFをExcelに変換, PDFをXLSXに変換, PDFをCSVに変換
description: Aspose.PDF for JavaScriptはPDFをXLSXおよびCSV形式に変換することができます。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## JavaScriptを使用してPDFからスプレッドシートを作成

**Aspose.PDF for JavaScript**は、PDFファイルをExcelおよびCSV形式に変換する機能をサポートしています。

{{% alert color="success" %}}
**PDFをExcelにオンラインで変換してみてください**

Aspose.PDF for JavaScriptは、オンラインの無料アプリケーション["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)を提供しており、機能性や品質を確認することができます。

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

変換操作はドキュメント内のページ数に依存し、非常に時間がかかる可能性があります。
 したがって、Web Workersの使用を強くお勧めします。

このコードは、リソース集約型のPDFファイル変換タスクをWeb Workerにオフロードして、メインUIスレッドのブロックを防ぐ方法を示しています。また、変換されたファイルをダウンロードするためのユーザーフレンドリーな方法を提供します。

## PDFをXLSXに変換

```js

  /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileToXlsX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルをXlsXに変換して"ResultPDFtoXlsX.xlsx"として保存 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXlsX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx"] }, [event.target.result]);
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
        link.innerHTML = "ここをクリックしてファイルをダウンロード " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```

以下のJavaScriptコードスニペットは、PDFページをXlsXファイルに変換するシンプルな例を示しています：

1. 変換するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfToXlsX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftoxlsx/) 関数を実行します。
1. 結果ファイルの名前を設定します。この例では"ResultPDFtoXlsX.xlsx"です。
1. 次に、'json.errorCode'が0の場合、結果ファイルに前述の名前が付けられます。'json.errorCode'パラメータが0と異なる場合、ファイルにエラーがあり、そのエラーに関する情報は'json.errorText'ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードすることを可能にします。

```js

  var ffileToXlsX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDFファイルをXlsXに変換し、"ResultPDFtoXlsX.xlsx"として保存*/
      const json = AsposePdfToXlsX(event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*結果ファイルをダウンロードするためのリンクを作成*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


## PDFをCSVに変換

```js

    /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? 
          `ファイル（テーブル）の数: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "text/csv", element) ) ?? ""}` : 
          `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileToCSV = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルをCSVに変換（テーブルを抽出）し、テンプレート"ResultPdfTablesToCSV{0:D2}.csv"で保存（{0}, {0:D2}, {0:D3}, ... の形式でページ番号を付ける）、区切り文字はTAB - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfTablesToCSV', "params": [event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

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


以下のJavaScriptコードスニペットは、PDFをCSVに変換する簡単な例を示しています：

1. 変換するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftablestocsv/) 関数が実行されます。
1. 結果のファイルの名前が設定され、この例では "ResultPdfTablesToCSV{0:D2}.csv" です。
1. 次に、'json.errorCode'が0の場合、結果ファイルには先に指定した名前が付けられます。'json.errorCode'パラメータが0でない場合、つまりファイルにエラーがある場合、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. 結果として、 [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードできるようにします。

```js

  var ffileToCSV = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*テンプレート "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... フォーマットページ番号) を使用してPDFファイルをCSVに変換（テーブルを抽出）、区切り文字はTAB*/
        const json = AsposePdfTablesToCSV(event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "ファイル（テーブル）数: " + json.filesCount.toString();
          /*結果ファイルへのリンクを作成*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "text/csv");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```