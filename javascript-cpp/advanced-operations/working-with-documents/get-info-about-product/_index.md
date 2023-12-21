---
title: Get info about Product using JavaScript
linktitle: Get info about Product
type: docs
weight: 70
url: /javascript-cpp/get-info-about-product/
description: This topic shows how to get info about Product with Aspose.PDF for JavaScript via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

This topic explain how to get info about Product using JavaScript.

```js

    /*Create Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error from Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode !== 0) ? `Error: ${evt.data.json.errorText}` :
                          "Product      : " + evt.data.json.product
                      + "\nFamily       : " + evt.data.json.family
                      + "\nVersion      : " + evt.data.json.version
                      + "\nRelease date : " + evt.data.json.releasedate
                      + "\nProducer     : " + evt.data.json.producer
                      + "\nIs licensed  : " + evt.data.json.islicensed;

    /*Event handler*/
    const onAsposePdfAbout = e => {
      /*Get info about Product - Ask Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAbout', "params": [] }, []);
    };
```

The following JavaScript code snippet shows simple example of getting info about Product:

1. The [AsposePdfAbout](https://reference.aspose.com/pdf/javascript-cpp/misc/asposepdfabout/) function is executed.
1. Product Information that can be obtained:
- Product name
- Product family
- Product version
- Date release
- Full name/producer
- Product is licensed
1. Next, if the 'json.errorCode' is 0, then you can get information about Product. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.

```js

  var onAsposePdfAbout = function () {
    /*Get info about Product*/
    const json = AsposePdfAbout();
    /* JSON
    Product name       : json.product
    Product family     : json.family
    Product version    : json.version
    Date release       : json.releasedate
    Full name/producer : json.producer
    Product is licensed: json.islicensed
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





