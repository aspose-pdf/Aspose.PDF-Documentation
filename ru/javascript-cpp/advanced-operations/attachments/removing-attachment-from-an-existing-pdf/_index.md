---
title: Удаление вложения из PDF с помощью JavaScript
linktitle: Удаление вложения из существующего PDF
type: docs
weight: 10
url: /ru/javascript-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF может удалять вложения из ваших PDF документов. Используйте JavaScript Web toolkit для удаления вложений в файлах PDF с помощью Aspose.PDF.
lastmod: "2023-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Вы можете удалить вложения из PDF файла, используя Aspose.PDF для JavaScript через C++. Вы можете получить результат непосредственно в вашем браузере.

1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteattachments/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPdfDeleteAttachments.pdf".

1. Далее, если 'json.errorCode' равен 0, то вашему DownloadFile присваивается имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет загрузить полученный файл в операционную систему пользователя.

```js

    var ffilePdfDeleteAttachments = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Удалить вложения из PDF-файла и сохранить "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfDeleteAttachments(event.target.result, e.target.files[0].name, "ResultPdfDeleteAttachments.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Создать ссылку для загрузки файла результата*/
        DownloadFile(json.fileNameResult, "application/pdf");
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


## Использование Web Workers

```js

    /*Создаем Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
        (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик события*/
    const ffilePdfDeleteAttachments = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Удаляем вложения из PDF-файла и сохраняем "ResultPdfDeleteAttachments.pdf" - Запрос к Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteAttachments', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteAttachments.pdf"] }, [event.target.result]);
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Создаем ссылку для скачивания файла результата*/
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