---
title: الحصول على معلومات حول المنتج باستخدام JavaScript
linktitle: الحصول على معلومات حول المنتج
type: docs
weight: 70
url: /javascript-cpp/get-info-about-product/
description: يوضح هذا الموضوع كيفية الحصول على معلومات حول المنتج باستخدام Aspose.PDF لـ JavaScript عبر C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

هذا الموضوع يشرح كيفية الحصول على معلومات حول المنتج باستخدام JavaScript.

```js

    /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode !== 0) ? `خطأ: ${evt.data.json.errorText}` :
                          "المنتج      : " + evt.data.json.product
                      + "\nالعائلة     : " + evt.data.json.family
                      + "\nالإصدار     : " + evt.data.json.version
                      + "\nتاريخ الإصدار: " + evt.data.json.releasedate
                      + "\nالمنتج      : " + evt.data.json.producer
                      + "\nمرخص        : " + evt.data.json.islicensed;

    /*معالج الحدث*/
    const onAsposePdfAbout = e => {
      /*الحصول على معلومات حول المنتج - طلب من عامل الويب*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAbout', "params": [] }, []);
    };
```


The following JavaScript code snippet shows simple example of getting info about Product:

1. يتم تنفيذ دالة [AsposePdfAbout](https://reference.aspose.com/pdf/javascript-cpp/misc/asposepdfabout/).
1. معلومات المنتج التي يمكن الحصول عليها:
- اسم المنتج
- عائلة المنتج
- إصدار المنتج
- تاريخ الإصدار
- الاسم الكامل/المنتج
- المنتج مرخص
1. بعد ذلك، إذا كانت قيمة 'json.errorCode' تساوي 0، يمكنك الحصول على معلومات حول المنتج. إذا كانت قيمة 'json.errorCode' لا تساوي 0، وبالتالي، سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.

```js

  var onAsposePdfAbout = function () {
    /*الحصول على معلومات حول المنتج*/
    const json = AsposePdfAbout();
    /* JSON
    اسم المنتج       : json.product
    عائلة المنتج     : json.family
    إصدار المنتج    : json.version
    تاريخ الإصدار   : json.releasedate
    الاسم الكامل/المنتج : json.producer
    المنتج مرخص      : json.islicensed
    */
    if (json.errorCode == 0) document.getElementById('output').textContent = 
                    "المنتج      : " + json.product
                + "\nالعائلة       : " + json.family
                + "\nالإصدار      : " + json.version
                + "\nتاريخ الإصدار : " + json.releasedate
                + "\nالمنتج     : " + json.producer
                + "\nمرخص  : " + json.islicensed;
    else document.getElementById('output').textContent = json.errorText;
  }
```