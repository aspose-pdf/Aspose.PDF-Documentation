---
title: JavaScriptを使用してPDFを分割する
linktitle: PDFファイルを分割する
type: docs
weight: 30
url: /ja/javascript-cpp/split-pdf/
description: このトピックでは、Aspose.PDF for JavaScript via C++を使用してPDFページを個別のPDFファイルに分割する方法を示します。
lastmod: "2022-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## JavaScriptを使用してPDFを2つのファイルに分割する

このトピックでは、JavaScriptを使用してPDFページを個別のPDFファイルに分割する方法を示します。現在、2つの部分に分割することをサポートしています。つまり、`pageToSplit`は区切りのマーカーです。最初のファイルには、1から`pageToSplit`までのすべてのページが含まれ、2番目のファイルには残りのページが含まれます。

分割操作はドキュメント内のページ数に依存し、非常に時間がかかることがあります。したがって、Web Workersの使用を強くお勧めします。

提供されたコードスニペットは、JavaScriptでWeb Workerを使用してPDFファイルを2つの別々のPDFファイルに分割し、ユーザーに結果ファイルをダウンロードするオプションを提供する例です。
 Here's a steps of the code:

1. Web Workerの作成。Web Workerは"AsposePDFforJS.js"スクリプトファイルを使用して初期化されます。このWeb Workerは、バックグラウンドでPDFファイル分割のタスクを処理します。我々の例では、Worker内で発生したエラーはすべてキャプチャされ、コンソールに記録されます。
1. メッセージ処理。Web Workerは、onmessageイベントハンドラを使用してメッセージを受信するために設定されています。ウェブページからメッセージを受信すると、そのリクエストを処理し、メインスレッドに応答を送信します。
1. ファイル分割イベントハンドラー。ユーザーが分割するPDFファイルを選択すると、ffileSplitというイベントハンドラーがトリガーされます。FileReaderを使用して選択されたPDFファイルを読み取り、ファイルの内容と関連するパラメータ（分割するページ数や出力ファイル名など）をWeb WorkerにpostMessageコールを介して送信します。
1. ファイルダウンロード関数。[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数は、ユーザーがファイルをダウンロードできるリンクを生成する役割を担っています。この関数は、ファイル名、MIMEタイプ、ファイルコンテンツを受け取ります。ダウンロードリンクを作成し、ファイルコンテンツをそれに関連付け、ファイル名を設定してドキュメントに追加します。これにより、ユーザーは生成されたPDFファイルをダウンロードすることができます。

1. Web Workerでのメッセージ処理。次に、'json.errorCode' が0の場合、json.fileNameResultには以前に指定した名前が含まれます。'json.errorCode' パラメータが0でない場合、つまりファイルにエラーがある場合、'json.errorText' プロパティにそのようなエラーに関する情報が含まれます。

1. 結果表示。メインページにはIDが「output」の要素が含まれています。Webワーカーが結果を含むメッセージを送信すると、「output」要素が更新されます。操作が成功した場合、二つに分割されたPDFファイルのダウンロードリンクが表示されます。エラーがある場合、エラーメッセージが表示されます。

このコードは、リソース集約型のPDFファイル分割タスクをWebワーカーにオフロードしてメインUIスレッドのブロックを防ぐ方法を示しています。また、分割されたPDFファイルをダウンロードするためのユーザーフレンドリーな方法も提供します。

```js

    /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ?
          `結果:\n${DownloadFile(evt.data.json.fileNameResult1, "application/pdf", evt.data.params[0])}
                  \n${DownloadFile(evt.data.json.fileNameResult2, "application/pdf", evt.data.params[1])}` :
          `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileSplit = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*分割するページ数を設定*/
        const pageToSplit = 1;
        /*2つのPDFファイルに分割し、"ResultSplit1.pdf", "ResultSplit2.pdf"を保存 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSplit2Files',
            "params": [event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするリンクを作成*/
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

次のJavaScriptコードスニペットは、PDFページを個々のPDFファイルに分割する簡単な例を示しています：

1. 分割するPDFファイルを選択します。
1. ハンドラーで「FileReader」オブジェクトを作成します。
1. 分割するページ数を設定します。
1. 最後のハンドラーで[AsposePdfSplit2Files](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsplit2files/)を呼び出します。
1. 結果を分析します。この例では、生成されるファイルの名前は「ResultSplit2.pdf」に設定されています。
1. 次に、「json.errorCode」が0の場合、「json.fileNameResult」に以前に指定した名前が含まれます。「json.errorCode」パラメータが0でない場合、したがってあなたのファイルにエラーがある場合は、そのようなエラーに関する情報が「json.errorText」プロパティに含まれます。
1. ヘルパー関数[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/)を使用することができます。

```js

  var ffileSplit = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*分割するページ数を設定*/
      const pageToSplit = 1;
      /*2つのPDFファイルに分割し、「ResultSplit1.pdf」、「ResultSplit2.pdf」を保存する*/
      const json = AsposePdfSplit2Files(event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = e.target.files[0].name + " split: " + json.fileNameResult1 + ", " + json.fileNameResult2;
      else document.getElementById('output').textContent = json.errorText;
      /*最初の結果ファイルをダウンロードするリンクを作成する*/
      DownloadFile(json.fileNameResult1, "application/pdf");
      /*2番目の結果ファイルをダウンロードするリンクを作成する*/
      DownloadFile(json.fileNameResult2, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```