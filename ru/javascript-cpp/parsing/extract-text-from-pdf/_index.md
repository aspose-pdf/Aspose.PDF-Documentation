---
title: Извлечение текста из PDF с использованием JavaScript
linktitle: Извлечение текста из PDF
type: docs
weight: 30
url: /ru/javascript-cpp/extract-text-from-pdf/
description: В этой статье описаны различные способы извлечения текста из PDF-документов с использованием Aspose.PDF для JavaScript.
lastmod: "2023-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение текста из PDF-документа

Извлечение текста из PDF-документа — это очень распространенная и полезная задача. Извлечение текста из PDF-файлов служит различным целям, от улучшения поиска и доступности до обеспечения анализа и автоматизации данных в различных областях, таких как бизнес, исследования и управление информацией.

Если вы хотите извлечь текст из PDF-документа, вы можете использовать функцию [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/). Пожалуйста, ознакомьтесь со следующим примером кода для извлечения текста из PDF-файла с использованием JavaScript через C++.

1. Создайте 'FileReader'.

1. Функция [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/) выполняется.
1. Далее, если 'json.errorCode' равен 0, то вы можете получить ссылки на файлы с результатами. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.

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

    /*Создание Web Worker*/
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
        /*Извлечение текста из PDF-файла - Запрос к Web Worker*/
        AsposePDFWebWorker.postMessage(
            { "operation": 'AsposePdfExtractText', "params": [event.target.result, e.target.files[0].name] },
            [event.target.result]
        );
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```