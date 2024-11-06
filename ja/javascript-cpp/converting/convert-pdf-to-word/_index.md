---
title: JavaScriptでPDFをWordドキュメントに変換する
linktitle: PDFをWordに変換
type: docs
weight: 10
url: ja/javascript-cpp/convert-pdf-to-doc/
lastmod: "2023-08-04"
description: PDFをDOC(DOCX)に直接Web上で変換するためのJavaScriptコードの書き方を学びます。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

変換操作はドキュメントのページ数によって異なり、非常に時間がかかることがあります。そのため、Web Workersの使用を強くお勧めします。

このコードは、リソース集約型のPDFファイル変換タスクをWebワーカーにオフロードしてメインUIスレッドのブロックを防ぐ方法を示しています。また、変換されたファイルをダウンロードするためのユーザーフレンドリーな方法も提供しています。

Microsoft WordやDOC、DOCXフォーマットをサポートする他のワードプロセッサでPDFファイルの内容を編集するには、PDFファイルは編集可能ですが、DOCおよびDOCXファイルはより柔軟でカスタマイズ可能です。

{{% alert color="success" %}}
**PDFをDOCにオンラインで変換してみてください**

Aspose.PDF for JavaScriptは、オンライン無料アプリケーション["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)を提供しており、その機能と品質を試してみることができます。

[![PDFをDOCに変換](/pdf/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDFをDOCに変換

```js

  /*Web Workerを作成*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? '読み込み完了!' :
      (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/msword", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

  /*イベントハンドラ*/
  const ffileToDoc = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*PDFファイルをDocに変換し、「ResultPDFtoDoc.doc」として保存 - Web Workerに依頼*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDoc', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc"] }, [event.target.result]);
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


以下のJavaScriptコードスニペットは、PDFページをDOCファイルに変換する簡単な例を示しています：

1. 変換用のPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfToDoc](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftodoc/) 関数が実行されます。
1. 結果のファイルの名前が設定されます。この例では「ResultPDFtoDoc.doc」です。
1. 次に、'json.errorCode'が0の場合、結果ファイルは前に指定した名前が付けられます。'json.errorCode'パラメータが0でない場合、ファイルにエラーが発生し、そのエラーに関する情報は'json.errorText'ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数がリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードすることができます。

```js

  var ffileToDoc = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDFファイルをDocに変換し、「ResultPDFtoDoc.doc」として保存する*/
      const json = AsposePdfToDoc(event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*結果ファイルをダウンロードするリンクを作成する*/
      DownloadFile(json.fileNameResult, "application/msword");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


{{% alert color="warning" %}}
**PDFをDOCXにオンラインで変換してみてください**

Aspose.PDF for JavaScriptは、オンラインで無料のアプリケーション["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## PDFをDOCXに変換

Aspose.PDF for JavaScript APIを使用すると、PDFドキュメントをDOCXに読み取り、変換することができます。DOCXは、Microsoft Wordドキュメントのよく知られた形式で、その構造は単純なバイナリからXMLとバイナリファイルの組み合わせに変更されました。DocxファイルはWord 2007およびそれ以降のバージョンで開くことができますが、DOCファイル拡張子をサポートする以前のバージョンのMS Wordでは開くことができません。

```js

  /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileToDocX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルをDocXに変換し、「ResultPDFtoDocX.docx」を保存- Web Workerに依頼*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDocX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx"] }, [event.target.result]);
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
        link.innerHTML = "ファイル " + filename + " をダウンロードするにはここをクリック";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


以下のJavaScriptコードスニペットは、PDFページをDOCXファイルに変換する簡単な例を示しています：

1. 変換するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfToDocX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftodocx/) 関数が実行されます。
1. 結果ファイルの名前が設定されます。この例では「ResultPDFtoDocX.docx」です。
1. 次に、'json.errorCode'が0であれば、結果ファイルには前に指定した名前が付けられます。'json.errorCode'パラメータが0でない場合、ファイルにエラーが発生し、そのエラーに関する情報は'json.errorText'ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数がリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードすることを可能にします。

```js

  var ffileToDocX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDFファイルをDocXに変換し、「ResultPDFtoDocX.docx」として保存*/
      const json = AsposePdfToDocX(event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*結果ファイルをダウンロードするためのリンクを作成*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```