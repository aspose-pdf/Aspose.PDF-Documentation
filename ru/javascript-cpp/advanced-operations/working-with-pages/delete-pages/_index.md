---
title: Удаление страниц PDF с помощью JavaScript через C++ 
linktitle: Удаление страниц PDF
type: docs
weight: 30
url: ru/javascript-cpp/delete-pages/
description: Вы можете удалить страницы из вашего PDF файла, используя Aspose.PDF для JavaScript через C++.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Вы можете удалить страницы из PDF файла, используя Aspose.PDF для JavaScript через C++. Вы можете получить результат непосредственно в вашем браузере.

1. Создайте 'FileReader'.
1. Укажите номера страниц для удаления.
1. Выполняется функция [AsposePdfDeletePages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdeletepages/).
1. Устанавливается имя результирующего файла, в этом примере "ResultDeletePages.pdf".
1. Далее, если 'json.errorCode' равен 0, то ваш DownloadFile получает имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.

1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) создает ссылку и позволяет загрузить полученный файл в операционную систему пользователя.

```js

  var ffileDeletePages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*строка, включает номера страниц с интервалом: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      const numPages = "1-3";
      /*массив, массив номеров страниц*/
      /*const numPages = [1,3];*/
      /*число, номер страницы*/
      /*const numPages = 1;*/
      /*удалить страницы 1-3 из PDF-файла и сохранить как "ResultOptimize.pdf"*/
      const json = AsposePdfDeletePages(event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages);
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*создать ссылку для загрузки файла результата*/
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
        (evt.data.json.errorCode == 0) ?
          `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик события*/
    const ffileDeletePages = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*строка, включает номера страниц с интервалом: "7, 20, 22, 30-32, 33, 36-40, 46"*/
        const numPages = "1-3";
        /*массив, массив номеров страниц*/
        /*const numPages = [1,3];*/
        /*число, номер страницы*/
        /*const numPages = 1;*/
        /*Удалить страницы из PDF-файла и сохранить "ResultDeletePages.pdf - Запрос Web Worker"*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDeletePages',
            "params": [event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Создать ссылку для загрузки результирующего файла*/
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