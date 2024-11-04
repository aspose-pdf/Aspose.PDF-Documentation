---
title: Добавить номер страницы в PDF с помощью JavaScript через C++
linktitle: Добавить номер страницы
type: docs
weight: 100
url: /javascript-cpp/add-page-number/
description: Aspose.PDF for JavaScript через C++ позволяет добавить штамп с номером страницы в ваш PDF файл, используя AsposePdfAddPageNum.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Все документы должны иметь номера страниц. Номер страницы облегчает читателю поиск различных частей документа.

**Aspose.PDF for JavaScript через C++** позволяет вам добавлять номера страниц с помощью [AsposePdfAddPageNum](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddpagenum/).

1. Создайте 'FileReader'.
1. Функция [AsposePdfAddPageNum](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddpagenum/) выполняется.
1. Устанавливается имя результирующего файла, в этом примере "ResultAddPageNum.pdf".

1. Далее, если 'json.errorCode' равен 0, то ваш DownloadFile получает имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет вам скачать полученный файл в операционной системе пользователя.

```js
  var ffileAddPageNum = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*добавить номер страницы в PDF-файл и сохранить "ResultAddPageNum.pdf"*/
      const json = AsposePdfAddPageNum(event.target.result, e.target.files[0].name, "ResultAddPageNum.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*создать ссылку для скачивания результата*/
      DownloadFile(json.fileNameResult, "application/pdf");
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
          `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик события*/
    const ffileAddPageNum = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Добавить номер страницы в PDF-файл и сохранить как "ResultAddPageNum.pdf" - Запрос к Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddPageNum', "params": [event.target.result, e.target.files[0].name, "ResultAddPageNum.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Создать ссылку для скачивания файла с результатом*/
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