---
title:  JavaScriptを使用してPDFを暗号化
linktitle: PDFファイルを暗号化
type: docs
weight: 50
url: /ja/javascript-cpp/encrypt-pdf/
description: Aspose.PDF for JavaScript via C++を使用してPDFファイルを暗号化します。
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## ユーザーまたはオーナーパスワードを使用してPDFファイルを暗号化

機密情報を含むPDF添付ファイルを誰かにメールで送信する場合、誤った手に渡らないように、まずセキュリティを追加したいかもしれません。PDFドキュメントへの不正アクセスを制限する最良の方法は、パスワードで保護することです。ドキュメントを簡単かつ安全に暗号化するには、Aspose.PDF for JavaScript via C++を使用できます。

> PDFファイルを暗号化する際には、異なるユーザーとオーナーパスワードを指定してください。

- **ユーザーパスワード**を設定すると、PDFを開くために提供する必要があります。Acrobat/Readerはユーザーにユーザーパスワードの入力を促します。正しくない場合、ドキュメントは開きません。
- **オーナーパスワード**を設定すると、印刷、編集、抽出、コメントなどの権限を制御します。
 Acrobat/Readerは、権限設定に基づいてこれらのことを許可しません。権限を設定/変更したい場合、Acrobatはこのパスワードを要求します。

次のコードスニペットは、PDFファイルを暗号化する方法を示しています。

1. 暗号化するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfEncrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfencrypt/) 関数が実行されます。
1. 結果ファイルの名前が設定されます。この例では "ResultEncrypt.pdf" です。
1. 次に、'json.errorCode' が0の場合、DownloadFileには前に指定した名前が与えられます。'json.errorCode' パラメータが0でない場合、つまりファイルにエラーがある場合、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードできるようにします。

```js

  var ffileEncrypt = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDFファイルを"ユーザー"と"オーナー"のパスワードで暗号化し、"ResultDecrypt.pdf"として保存*/
      const json = AsposePdfEncrypt(event.target.result, e.target.files[0].name, "user", "owner", Module.Permissions.PrintDocument, Module.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*結果ファイルをダウンロードするためのリンクを作成*/
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
    const ffileEncrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password_user = 'user';
        const password_owner = 'owner';
        const permissions = 'Module.Permissions.PrintDocument';
        const algorithm = 'Module.CryptoAlgorithm.RC4x40';
        /*PDFファイルをパスワード"user"と"owner"で暗号化し、"ResultEncrypt.pdf"として保存する - Web Workerに依頼する*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfEncrypt',
            "params": [event.target.result, e.target.files[0].name, password_user, password_owner,
                      permissions, algorithm, "ResultEncrypt.pdf"] },
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