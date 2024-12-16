---
title: JavaScriptを使用して製品情報を取得する
linktitle: 製品情報を取得する
type: docs
weight: 70
url: /ja/javascript-cpp/get-info-about-product/
description: このトピックでは、C++経由でAspose.PDF for JavaScriptを使用して製品情報を取得する方法を示します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

このトピックでは、JavaScriptを使用して製品情報を取得する方法を説明します。

```js

    /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode !== 0) ? `エラー: ${evt.data.json.errorText}` :
                          "製品         : " + evt.data.json.product
                      + "\nファミリー   : " + evt.data.json.family
                      + "\nバージョン   : " + evt.data.json.version
                      + "\nリリース日   : " + evt.data.json.releasedate
                      + "\n製作者       : " + evt.data.json.producer
                      + "\nライセンス済?: " + evt.data.json.islicensed;

    /*イベントハンドラ*/
    const onAsposePdfAbout = e => {
      /*製品情報を取得 - Web Workerに問い合わせ*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAbout', "params": [] }, []);
    };
```


以下のJavaScriptコードスニペットは、製品に関する情報を取得する簡単な例を示しています：

1. [AsposePdfAbout](https://reference.aspose.com/pdf/javascript-cpp/misc/asposepdfabout/) 関数が実行されます。
1. 取得可能な製品情報：
- 製品名
- 製品ファミリー
- 製品バージョン
- リリース日
- フルネーム/製作者
- 製品がライセンスされているかどうか
1. 次に、'json.errorCode' が0の場合、製品に関する情報を取得できます。'json.errorCode' パラメータが0でない場合、つまりファイルにエラーがある場合、そのエラーに関する情報は 'json.errorText' ファイルに含まれます。

```js

  var onAsposePdfAbout = function () {
    /*製品に関する情報を取得*/
    const json = AsposePdfAbout();
    /* JSON
    製品名              : json.product
    製品ファミリー      : json.family
    製品バージョン      : json.version
    リリース日          : json.releasedate
    フルネーム/製作者   : json.producer
    製品がライセンスされているか: json.islicensed
    */
    if (json.errorCode == 0) document.getElementById('output').textContent = 
                    "Product      : " + json.product
                + "\nFamily       : " + json.family
                + "\nVersion      : " + json.version
                + "\nRelease date : " + json.releasedate
                + "\nProducer     : " + json.producer
                + "\nIs licensed  : " + json.islicensed;
    else document.getElementById('output').textContent = json.errorText;
  }
```