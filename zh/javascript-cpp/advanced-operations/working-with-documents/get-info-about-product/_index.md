---
title: 使用 JavaScript 获取有关产品的信息
linktitle: 获取有关产品的信息
type: docs
weight: 70
url: zh/javascript-cpp/get-info-about-product/
description: 本主题演示如何使用 Aspose.PDF for JavaScript via C++ 获取有关产品的信息。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

本主题解释了如何使用 JavaScript 获取有关产品的信息。

```js

    /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode !== 0) ? `错误: ${evt.data.json.errorText}` :
                          "产品      : " + evt.data.json.product
                      + "\n家族       : " + evt.data.json.family
                      + "\n版本      : " + evt.data.json.version
                      + "\n发布日期 : " + evt.data.json.releasedate
                      + "\n生产者     : " + evt.data.json.producer
                      + "\n是否许可  : " + evt.data.json.islicensed;

    /*事件处理器*/
    const onAsposePdfAbout = e => {
      /*获取有关产品的信息 - 请求 Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAbout', "params": [] }, []);
    };
```


以下的 JavaScript 代码片段展示了获取产品信息的简单示例：

1. 执行 [AsposePdfAbout](https://reference.aspose.com/pdf/javascript-cpp/misc/asposepdfabout/) 函数。
2. 可以获取的产品信息：
- 产品名称
- 产品系列
- 产品版本
- 发布日期
- 全名/生产商
- 产品是否已授权
3. 接下来，如果 'json.errorCode' 为 0，则可以获取产品信息。如果 'json.errorCode' 参数不等于 0，相应地，您的文件中将出现错误，那么关于此类错误的信息将包含在 'json.errorText' 文件中。

```js

  var onAsposePdfAbout = function () {
    /*获取产品信息*/
    const json = AsposePdfAbout();
    /* JSON
    产品名称         : json.product
    产品系列         : json.family
    产品版本         : json.version
    发布日期         : json.releasedate
    全名/生产商      : json.producer
    产品是否已授权    : json.islicensed
    */
    if (json.errorCode == 0) document.getElementById('output').textContent = 
                    "产品      : " + json.product
                + "\n系列       : " + json.family
                + "\n版本      : " + json.version
                + "\n发布日期  : " + json.releasedate
                + "\n生产商     : " + json.producer
                + "\n是否已授权  : " + json.islicensed;
    else document.getElementById('output').textContent = json.errorText;
  }
```