---
title: Закладки в PDF с использованием JavaScript
linktitle: Закладки в PDF
type: docs
weight: 10
url: /ru/javascript-cpp/bookmark/
description: Вы можете добавлять или удалять закладки в PDF-документе с помощью JavaScript.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Удаление определенной закладки из PDF-документа

Вы можете удалить закладки из PDF-файла с использованием Aspose.PDF для JavaScript через C++. Вы можете получить результат непосредственно в вашем браузере.

1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeletebookmarks/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPdfDeleteBookmarks.pdf".
1. Далее, если 'json.errorCode' равен 0, то вашему DownloadFile присваивается имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле произойдет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.

1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать полученный файл на операционную систему пользователя.

```js

    var ffilePdfDeleteBookmarks = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Удалить закладки из PDF-файла и сохранить как "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfDeleteBookmarks(event.target.result, e.target.files[0].name, "ResultPdfDeleteBookmarks.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Создать ссылку для скачивания полученного файла*/
        DownloadFile(json.fileNameResult, "application/pdf");
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
        (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик событий*/
    const ffilePdfDeleteBookmarks = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Удалить закладки из PDF-файла и сохранить как "ResultPdfDeleteBookmarks.pdf" - Запрос к Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteBookmarks', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteBookmarks.pdf"] }, [event.target.result]);
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Создать ссылку для скачивания полученного файла*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Нажмите здесь, чтобы скачать файл " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
        }
```