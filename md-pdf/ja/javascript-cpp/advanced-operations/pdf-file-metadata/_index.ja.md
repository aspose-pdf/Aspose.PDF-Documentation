---
title: JavaScript経由でC++を使用したPDFファイルメタデータの操作
linktitle: PDFファイルメタデータ
type: docs
weight: 130
url: /javascript-cpp/pdf-file-metadata/
description: このセクションでは、PDFファイル情報の取得方法、PDFファイルからのメタデータの取得方法、PDFファイル情報の設定方法について説明します。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイル情報の取得

1. 'FileReader'を作成します。
1. [AsposePdfGetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetinfo/) 関数が実行されます。
1. 取得可能なPDFメタデータ:
- title - タイトル
- creator - 作成者
- author - 著者
- subject - 件名
- keywords - キーワード
- creation - 作成日
- mod - 修正日
1. 次に、'json.errorCode'が0の場合、PDFファイル情報のリストを取得できます。'json.errorCode'パラメータが0でない場合、ファイルにエラーが存在し、そのエラーに関する情報は'json.errorText'ファイルに含まれます。

```js

  var ffilePdfGetInfo = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDFファイルから情報（メタデータ）を取得します。*/
      const json = AsposePdfGetInfo(event.target.result, e.target.files[0].name);
      /* JSON
      title - タイトル
      creator - 作成者
      author - 著者
      subject - 件名
      keywords - キーワード
      format - PDF形式
      version - PDFバージョン
      ispdfa - PDFはPDF/A
      ispdfua - PDFはPDF/UA
      islinearized - PDFは線形化されている
      isencrypted - PDFは暗号化されている
      permission - PDF許可
      size - PDFページサイズ
      pagecount - ページ数
      сreation Date: json.creation
      modify Date:   json.mod
      annotationcount - 注釈数
      bookmarkcount - ブックマーク数
      attachmentcount - 添付ファイル数
      metadatacount - メタデータ数
      javascriptcount - JavaScript数
      imagecount - 画像数
      */
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


### Webワーカーの使用

```js

    /*Webワーカーを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Webワーカーからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了！' :
        (evt.data.json.errorCode == 0) ?
          `情報:\n${JSON.stringify(evt.data.json, null, 4)}` :
          `エラー: ${evt.data.json.errorText}`; 

    /*イベントハンドラー*/
    const ffilePdfGetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルから情報（メタデータ）を取得 - Webワーカーに依頼*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetInfo', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## すべてのフォントを取得

PDFファイルからフォントを取得することは、他の文書やアプリケーションでフォントを再利用するのに役立ちます。
 
PDFドキュメントからすべてのフォントを取得したい場合は、[AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/)を使用できます。JavaScriptを介してC++を使用し、既存のPDFドキュメントからすべてのフォントを取得するために、次のコードスニペットを確認してください。

1. 'FileReader'を作成します。
1. [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/) 関数が実行されます。
1. 次に、'json.errorCode'が0の場合は、PDFファイルからフォントのリストを取得できます。'json.errorCode'パラメータが0でない場合、およびそれに応じてファイルにエラーがある場合、そのようなエラーに関する情報は'json.errorText'ファイルに含まれます。

```js

  var ffilePdfGetAllFonts = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDFファイルからフォントのリストを取得します。*/
      const json = AsposePdfGetAllFonts(event.target.result, e.target.files[0].name);
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

## Web ワーカーの使用

```js

    /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ?
          `フォント:\n${JSON.stringify(evt.data.json.fonts, null, 4)}` :
          `エラー: ${evt.data.json.errorText}`; 

    /*イベントハンドラ*/
    const ffilePdfGetAllFonts = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルのフォントリストを取得 - Web Workerに要求*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetAllFonts', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```
## PDFファイル情報の設定

Aspose.PDF for JavaScript via C++を使用すると、PDFの作成者、作成日、件名、タイトルなどのファイル固有の情報を設定できます。
 この情報を設定するには:

1. 'FileReader'を作成します。
1. 値を設定する必要がない場合は、undefinedまたは""（空文字列）を使用します。
1. [AsposePdfSetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsetinfo/) 関数が実行されます。
1. 結果のファイルの名前が設定され、この例では "ResultSetInfo.pdf" です。
1. 次に、'json.errorCode' が0の場合、DownloadFileには先に指定した名前が付けられます。'json.errorCode' パラメーターが0でない場合、ファイルにエラーが発生し、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数がリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードすることができます。

```js

    var ffilePdfSetInfo = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF情報を設定: タイトル、作成者、著者、主題、キーワード、作成日、変更日*/
        /*値を設定する必要がない場合は、undefinedまたは""（空文字列）を使用します*/
        /*PDFファイルに情報（メタデータ）を設定し、"ResultSetInfo.pdf"として保存します*/
        const json = AsposePdfSetInfo(event.target.result, e.target.files[0].name, "PDFドキュメント情報の設定", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "16/02/2023 11:55 PM", "ResultSetInfo.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするためのリンクを作成します*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

### Web ワーカーの使用

```js

    /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ?
          `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffilePdfSetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF情報: タイトル、作成者、著者、件名、キーワード、作成日、変更日*/
        const title = 'PDFドキュメント情報の設定';
        const creator = ''; /*値を設定する必要がない場合は、undefinedまたは""/''（空の文字列）を使用*/
        const author = 'Aspose';
        const subject = undefined;
        const keywords = 'Aspose.Pdf, DOM, API';
        const creation = undefined; /*作成日*/
        const mod = '16/02/2023 11:55 PM'; /*変更日*/
        /*PDFファイルに情報（メタデータ）を設定し、「ResultSetInfo.pdf」を保存 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSetInfo',
            "params": [event.target.result, e.target.files[0].name, title, creator, author, subject, keywords, creation, mod, "ResultSetInfo.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするためのリンクを作成*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "このファイルをダウンロードするにはここをクリックしてください " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


## PDFファイル情報の削除

Aspose.PDF for JavaScript via C++を使用すると、PDFファイルのメタデータを削除できます：

1. 'FileReader'を作成します。
1. [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/javascript-cpp/metadata/asposepdfremovemetadata/)関数が実行されます。
1. 結果ファイルの名前が設定され、この例では"ResultPdfRemoveMetadata.pdf"とします。
1. 次に、'json.errorCode'が0の場合、DownloadFileに先ほど指定した名前が付けられます。'json.errorCode'パラメータが0でない場合、つまりファイルにエラーがある場合、そのエラーに関する情報は'json.errorText'ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/)関数がリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードすることができます。

```js

    var ffilePdfRemoveMetadata = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDFファイルのメタデータを削除し、「ResultPdfRemoveMetadata.pdf」として保存*/
        const json = AsposePdfRemoveMetadata(event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするリンクを作成*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


### Web Workersの使用

```js

    /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了！' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffilePdfRemoveMetadata = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルのメタデータを削除し、"ResultPdfRemoveMetadata.pdf"として保存 - Web Workerにリクエスト*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRemoveMetadata', "params": [event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf"] }, [event.target.result]);
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
        link.innerHTML = filename + " をダウンロードするにはここをクリック";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```