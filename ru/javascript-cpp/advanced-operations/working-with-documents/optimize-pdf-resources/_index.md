---
title: Оптимизация ресурсов PDF с использованием JavaScript через C++
linktitle: Оптимизация ресурсов PDF
type: docs
weight: 15
url: /ru/javascript-cpp/optimize-pdf-resources/
description: Оптимизация ресурсов PDF файлов для быстрого просмотра в интернете с использованием инструмента JavaScript.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Оптимизация ресурсов PDF

Оптимизация ресурсов в документе:

  1. Ресурсы, которые не используются на страницах документа, удаляются
  1. Одинаковые ресурсы объединяются в один объект
  1. Неиспользуемые объекты удаляются
 
1. Выберите PDF файл для оптимизации.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfoptimizeresource/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPdfOptimizeResource.pdf".

1. Далее, если 'json.errorCode' равен 0, то ваш DownloadFile получает имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать полученный файл в операционную систему пользователя.

Следующий фрагмент кода показывает, как оптимизировать PDF-документ.

```js

    var ffilePdfOptimizeResource = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Оптимизировать ресурсы PDF-файла и сохранить как "ResultPdfOptimizeResource.pdf"*/
        const json = AsposePdfOptimizeResource(event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Создать ссылку для скачивания результирующего файла*/
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
    const ffilePdfOptimizeResource = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Оптимизировать ресурсы PDF-файла и сохранить как "ResultPdfOptimizeResource.pdf" - Запросить Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfOptimizeResource', "params": [event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Фрагмент кода]

    /*Создать ссылку для загрузки результатирующего файла*/
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