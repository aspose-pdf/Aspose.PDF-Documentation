---
title: JavaScriptを使用してPDFを復号化
linktitle: PDFファイルの復号化
type: docs
weight: 40
url: /ja/javascript-cpp/decrypt-pdf/
description: Aspose.PDF for JavaScript via C++を使用してPDFファイルを復号化します。
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## オーナーパスワードを使用してPDFファイルを復号化

最近、インターネット詐欺の被害に遭わないように、暗号化された文書を交換するユーザーが増えています。このため、暗号化されたPDFファイルにアクセスする必要がありますが、そのようなアクセスは認可されたユーザーのみが取得できます。また、人々はPDFファイルを復号化するためのさまざまなソリューションを探しています。

この問題を一度に解決するには、ブラウザで直接Aspose.PDF for JavaScript via C++を使用するのが最適です。以下のコードスニペットは、PDFファイルを復号化する方法を示しています。

1. 復号化するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfDecrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdecrypt/) 関数が実行されます。

1. 結果のファイルの名前が設定されます。この例では「ResultDecrypt.pdf」となります。
1. 次に、'json.errorCode'が0の場合、DownloadFileに先ほど指定した名前が付けられます。'json.errorCode'パラメータが0でない場合、つまりファイルにエラーがある場合、そのようなエラーに関する情報は'json.errorText'ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/)関数はリンクを生成し、結果のファイルをユーザーのオペレーティングシステムにダウンロードできるようにします。

```js

    var ffileDecrypt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /* パスワードが"owner"のPDFファイルを復号化し、"ResultDecrypt.pdf"として保存する */
        const json = AsposePdfDecrypt(event.target.result, e.target.files[0].name, "owner", "ResultDecrypt.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /* 結果ファイルをダウンロードするためのリンクを作成する */
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


## Web Workersの使用

```js

    /*Web Workerを作成する*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ?
          `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileDecrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*PDFファイルを"owner"というパスワードで復号し、"ResultDecrypt.pdf"として保存する - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDecrypt',
            "params": [event.target.result, e.target.files[0].name, password, "ResultDecrypt.pdf"] }, 
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするリンクを作成する*/
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