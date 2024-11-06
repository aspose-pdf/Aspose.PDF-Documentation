---
title: PDFをPDF/A形式に変換する
linktitle: PDFをPDF/A形式に変換する
type: docs
weight: 100
url: ja/javascript-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-01"
description: このトピックでは、Aspose.PDFを使用してPDFファイルをPDF/A準拠のPDFファイルに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for JavaScript**は、PDFファイルを<abbr title="Portable Document Format / A">PDF/A</abbr>準拠のPDFファイルに変換することができます。

変換操作はドキュメント内のページ数に依存し、非常に時間がかかる場合があります。したがって、Web Workersの使用を強くお勧めします。

このコードは、リソース集約型のPDFファイル変換タスクをWeb Workerにオフロードして、メインUIスレッドのブロックを防ぐ方法を示しています。また、変換されたファイルをダウンロードするユーザーフレンドリーな方法も提供します。

{{% alert color="success" %}}
**オンラインでPDFをPDF/Aに変換してみてください**

Aspose.PDF for JavaScriptでは、オンラインの無料アプリケーション["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF コンバージョン PDF を PDF/A へ変換 無料アプリで](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## PDF を PDF/A 形式に変換

```js

  /*Web Worker を作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Worker からのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}\n${DownloadFile(evt.data.json.fileNameLogResult, "application/xml", evt.data.params[1])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffilePdfConvertToPDFA = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pdfFormat = 'Module.PdfFormat.PDF_A_1A';
        /*PDFファイルをPDF/A(1A)に変換して"ResultConvertToPDFA.pdf"として保存*/
        /*変換プロセス中に検証も行われ、"ResultConvertToPDFA.xml" - Web Worker に問い合わせ*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToPDFA', "params": [event.target.result, e.target.files[0].name, pdfFormat, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml"] }, [event.target.result]);
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
        link.innerHTML = "ファイルをダウンロードするにはここをクリック " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


以下のJavaScriptコードスニペットは、PDFをPDF/Aファイルに変換する単純な例を示しています：

1. 変換するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttopdfa/) 関数が実行されます。
1. 結果ファイルの名前が設定されます。この例では "ResultConvertToPDFA.pdf" です。変換プロセス中に、"ResultConvertToPDFA.xml" というバリデーションも実行されます。
1. 次に、'json.errorCode' が0の場合、DownloadFileは前に指定した名前が付けられます。'json.errorCode' パラメータが0でない場合、ファイルにエラーがあり、そのエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、結果ファイルのダウンロードとログ（xml）ファイルをユーザーのオペレーティングシステムにダウンロードすることを可能にします。

```js

  var ffilePdfConvertToPDFA = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDFファイルをPDF/A(1A)に変換し、"ResultConvertToPDFA.pdf"として保存*/
      /*変換プロセス中に、"ResultConvertToPDFA.xml"というバリデーションも実行される*/
      const json = AsposePdfConvertToPDFA(event.target.result, e.target.files[0].name, Module.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml");
      if (json.errorCode == 0)
      {
        document.getElementById('output').textContent = json.fileNameResult + "\nログファイル (xml形式): " + json.fileNameLogResult;
        /*結果ファイルをダウンロードするリンクを作成*/
        DownloadFile(json.fileNameResult, "application/pdf");
      }
      else document.getElementById('output').textContent = json.errorText + "\nログファイル (xml形式): " + json.fileNameLogResult;
      /*ログ (xml) をダウンロードするリンクを作成*/
      DownloadFile(json.fileNameLogResult, "application/xml");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```