---
title: Получить информацию о продукте с использованием JavaScript
linktitle: Получить информацию о продукте
type: docs
weight: 70
url: /javascript-cpp/get-info-about-product/
description: Эта тема показывает, как получить информацию о продукте с помощью Aspose.PDF для JavaScript через C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Эта тема объясняет, как получить информацию о продукте с использованием JavaScript.

```js

    /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode !== 0) ? `Ошибка: ${evt.data.json.errorText}` :
                          "Продукт      : " + evt.data.json.product
                      + "\nСемейство    : " + evt.data.json.family
                      + "\nВерсия       : " + evt.data.json.version
                      + "\nДата выпуска : " + evt.data.json.releasedate
                      + "\nПроизводитель: " + evt.data.json.producer
                      + "\nЛицензировано: " + evt.data.json.islicensed;

    /*Обработчик событий*/
    const onAsposePdfAbout = e => {
      /*Получить информацию о продукте - запросить Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAbout', "params": [] }, []);
    };
```


Следующий фрагмент кода JavaScript показывает простой пример получения информации о продукте:

1. Выполняется функция [AsposePdfAbout](https://reference.aspose.com/pdf/javascript-cpp/misc/asposepdfabout/).
1. Информация о продукте, которую можно получить:
- Название продукта
- Семейство продукта
- Версия продукта
- Дата выпуска
- Полное имя/производитель
- Продукт лицензирован
1. Далее, если 'json.errorCode' равен 0, то вы можете получить информацию о продукте. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.

```js

  var onAsposePdfAbout = function () {
    /*Получить информацию о продукте*/
    const json = AsposePdfAbout();
    /* JSON
    Название продукта  : json.product
    Семейство продукта : json.family
    Версия продукта    : json.version
    Дата выпуска       : json.releasedate
    Полное имя/производитель : json.producer
    Продукт лицензирован: json.islicensed
    */
    if (json.errorCode == 0) document.getElementById('output').textContent = 
                    "Продукт      : " + json.product
                + "\nСемейство    : " + json.family
                + "\nВерсия       : " + json.version
                + "\nДата выпуска : " + json.releasedate
                + "\nПроизводитель: " + json.producer
                + "\nЛицензирован : " + json.islicensed;
    else document.getElementById('output').textContent = json.errorText;
  }
```