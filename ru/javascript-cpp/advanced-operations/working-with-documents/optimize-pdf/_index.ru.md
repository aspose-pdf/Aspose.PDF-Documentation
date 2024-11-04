---
title: Optimize PDF using Aspose.PDF for JavaScript via C++ 
linktitle: Optimize PDF File
type: docs
weight: 10
url: /javascript-cpp/optimize-pdf/
description: Оптимизируйте и сжимайте PDF файлы для быстрого просмотра в интернете с помощью инструмента JavaScript.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Оптимизация PDF документа

Инструментарий Aspose.PDF для JavaScript через C++ позволяет оптимизировать содержимое PDF для веба.

Оптимизация, или линеаризация для веба, относится к процессу подготовки PDF файла для онлайн-просмотра через веб-браузер. Для оптимизации файла для веб-отображения:

1. Выберите PDF файл для оптимизации.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfOptimize](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfoptimize/).
1. Устанавливается имя результирующего файла, в этом примере "ResultOptimize.pdf".

1. Далее, если 'json.errorCode' равен 0, то ваш DownloadFile получает имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет загрузить полученный файл в операционную систему пользователя.

Следующий фрагмент кода показывает, как оптимизировать PDF-документ.

```js

  var ffileOptimize = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*оптимизировать PDF-файл и сохранить как "ResultOptimize.pdf"*/
      const json = AsposePdfOptimize(event.target.result, e.target.files[0].name, "ResultOptimize.pdf");
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

    /*Обработчик событий*/
    const ffileOptimize = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Оптимизировать PDF-файл и сохранить как "ResultOptimize.pdf" - Запрос к Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfOptimize', "params": [event.target.result, e.target.files[0].name, "ResultOptimize.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Создать ссылку для скачивания файла результата*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Кликните здесь, чтобы скачать файл " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```