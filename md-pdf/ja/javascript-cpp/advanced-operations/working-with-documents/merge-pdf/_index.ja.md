---

title: JavaScriptを介してC++でPDFをマージする方法  
linktitle: PDFファイルをマージする  
type: docs  
weight: 20  
url: /javascript-cpp/merge-pdf/  
description: このページでは、Aspose.PDF for JavaScriptを介してC++でPDF文書を単一のPDFファイルにマージする方法を説明します  
lastmod: "2022-12-15"  
sitemap:  
    changefreq: "monthly"  
    priority: 0.7  

---

## JavaScriptで2つのPDFを単一のPDFにマージまたは結合する

ファイルを結合およびマージすることは、多数の文書を扱う際に非常に一般的なタスクです。時には、文書や画像を扱う際に、それらがスキャンされ、処理され、整理されると、いくつかのファイルが作成されます。しかし、すべてを1つのファイルに保存する必要がある場合はどうしますか？または、複数の文書を印刷したくない場合はどうしますか？Aspose.PDF for JavaScriptを介してC++で2つのPDFファイルを連結します。

このJavaScriptツールを使用すると、Aspose.PDF for JavaScriptを介してC++を使用して2つのPDFファイルを単一のPDF文書にマージできます。この例はJavaScriptで書かれています。

1. マージするPDFファイルを選択します。
1. 'FileReader'を作成します。

1. [AsposePdfMerge2Files](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfmerge2files/) 関数が実行されます。
1. 結果ファイルの名前が設定されます。この例では「ResultMerge.pdf」です。
1. 次に、'json.errorCode' が 0 の場合、DownloadFile が前に指定した名前になります。'json.errorCode' パラメータが 0 でない場合、つまりファイルにエラーがある場合、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードすることを可能にします。

以下のコードスニペットは、PDF ファイルを連結する方法を示しています:

```js

  var ffileMerge = function (e) {
    const file_reader = new FileReader();
    function readFile(index) {
      /*2つのファイルのみ*/
      if (index >= e.target.files.length || index >= 2) {
        /*2つの PDF ファイルをマージして「ResultMerge.pdf」として保存*/
        const json = AsposePdfMerge2Files(undefined, undefined, e.target.files[0].name, e.target.files[1].name, "ResultMerge.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするためのリンクを作成*/
        DownloadFile(json.fileNameResult, "application/pdf");
        return;
      }
      const file = e.target.files[index];
      file_reader.onload = function (event) {
        /*BLOBからファイルを準備（保存）*/
        AsposePdfPrepare(event.target.result, file.name);
        readFile(index + 1)
      }
      file_reader.readAsArrayBuffer(file);
    }
    readFile(0);
  }
```


### Web ワーカーの使用

```js

    /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了！' :
        (evt.data.json.errorCode == 0) ? 
          `結果:\n${(evt.data.operation == 'AsposePdfPrepare') ? 
                      fileProcess('AsposePdfMerge2Files', evt.data.json.optdata[0].file, {"fileName2": evt.data.json.fileNameResult}) ?? 'お待ちください...' : 
                      DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0]) /*AsposePdfMerge2Files*/
                    }` :
          `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ。2つのファイルのみが結合されます。1つのファイルのみが選択された場合、それを使用します。2番目のファイルにはAsposePdfPrepareを実行する必要があります*/
    const ffileMerge = evt => fileProcess('AsposePdfPrepare',  evt.target.files[(evt.target.files.length == 1) ? 0 : 1],
                                          [{"operation": 'AsposePdfMerge2Files', "file": evt.target.files[0]}])
    /* Web Workerに問い合わせる */
    const fileProcess = (operation, ffile, optdata) => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        if (operation == 'AsposePdfPrepare')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, "params": [event.target.result, ffile.name, optdata] },
                  [event.target.result]
                );
        else if (operation == 'AsposePdfMerge2Files')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, 
                    "params": [event.target.result, undefined, ffile.name, (optdata === undefined) ? ffile.name : optdata.fileName2,
                                `Result${operation}.pdf`] },
                  [event.target.result]
                );
      }
      file_reader.readAsArrayBuffer(ffile);
    }

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