---
title: JavaScriptを介してC++でPDFにヘッダーとフッターを追加 
linktitle: PDFにヘッダーとフッターを追加
type: docs
weight: 70
url: /javascript-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for JavaScript via C++ は、AsposePdfAddTextHeaderFooterを使用してPDFファイルにヘッダーとフッターを追加することができます。
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for JavaScript via C++** は、既存のPDFファイルにヘッダーとフッターを追加することができます。

1. 'FileReader'を作成します。
1. [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddtextheaderfooter/) 関数が実行されます。
1. 結果ファイルの名前が設定されます。この例では "ResultAddHeader.pdf" です。

1. 次に、'json.errorCode' が 0 の場合、DownloadFile には以前に指定した名前が付けられます。 'json.errorCode' パラメータが 0 と等しくない場合、ファイルにエラーがあることになり、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数がリンクを生成し、生成されたファイルをユーザーのオペレーティングシステムにダウンロードできるようにします。

次のコードスニペットは、JavaScript を使用して PDF ファイルのヘッダーにテキストを追加する方法を示しています。

```js

  var ffileAddTextHeaderFooter = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDFファイルにページヘッダーを追加し、"ResultAddHeader.pdf"として保存する*/
      const json = AsposePdfAddTextHeaderFooter(event.target.result, e.target.files[0].name, "Aspose.PDF for JavaScript via C++", "", "ResultAddHeader.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*結果ファイルをダウンロードするためのリンクを作成する*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## Web Workerの使用

```js

    /* Web Workerを作成 */
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'ロード完了!' :
        (evt.data.json.errorCode == 0) ?
          `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `エラー: ${evt.data.json.errorText}`;

    /* イベントハンドラ */
    const ffileAddTextHeaderFooter = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const header = 'Aspose.PDF for JavaScript via C++';
        const footer = 'ASPOSE';
        /* PDFファイルのヘッダー/フッターにテキストを追加し、"ResultAddHeaderFooter.pdf"として保存 - Web Workerに依頼 */
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddTextHeaderFooter',
            "params": [event.target.result, e.target.files[0].name, header, footer, "ResultAddHeaderFooter.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /* 結果ファイルをダウンロードするリンクを作成 */
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