---
title: Извлечение текста из PDF с использованием JavaScript
linktitle: Извлечение текста из PDF
type: docs
weight: 10
url: /ru/javascript-cpp/extract-text/
description: В этом разделе описывается, как извлечь текст из PDF-документа с использованием JavaScript-инструментария.
lastmod: "2022-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение текста со всех страниц PDF-документа

Извлечение текста из PDF не является простой задачей. Не многие PDF-ридеры могут извлекать текст из изображений PDF или отсканированных PDF. Но инструмент **Aspose.PDF для JavaScript через C++** позволяет легко извлекать текст из любого PDF-файла.

Посмотрите фрагмент кода и следуйте шагам, чтобы извлечь текст из вашего PDF:

1. Выберите PDF-файл для извлечения текста.
1. Создайте 'FileReader' для чтения текста.
1. Функция [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfextracttext/) выполняется.

1. Далее, если 'json.errorCode' равно 0, то 'json.extractText' будет содержать извлеченный контент. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация об этой ошибке будет содержаться в 'json.errorText'.
1. В результате вы получите строку с извлеченным текстом из вашего PDF.

```js

    var ffileExtract = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Извлечение текста из PDF-файла*/
        const json = AsposePdfExtractText(event.target.result, e.target.files[0].name);
        if (json.errorCode == 0) document.getElementById('output').textContent = json.extractText;
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Использование Web Workers

```js

    /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ?
          evt.data.json.extractText :
          `Ошибка: ${evt.data.json.errorText}`; 

    /*Обработчик событий*/
    const ffileExtract = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Извлечение текста из PDF-файла - запрос Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfExtractText', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```