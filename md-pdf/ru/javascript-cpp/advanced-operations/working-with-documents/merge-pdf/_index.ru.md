---
title: Как объединить PDF с использованием JavaScript через C++
linktitle: Объединить PDF файлы
type: docs
weight: 20
url: /javascript-cpp/merge-pdf/
description: Эта страница объясняет, как объединить PDF документы в один файл с помощью Aspose.PDF для JavaScript через C++
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Объединение или комбинирование двух PDF в один PDF на JavaScript

Комбинирование и объединение файлов — это очень популярная задача при работе с большим количеством документов. Иногда, при работе с документами и изображениями, когда они сканируются, обрабатываются и организуются, создается несколько файлов. 
Но что, если вам нужно сохранить все в одном файле? Или вы не хотите печатать несколько документов? Объедините два PDF файла с помощью Aspose.PDF для JavaScript через C++.

Этот инструмент JavaScript позволяет объединить два PDF файла в один PDF документ с использованием Aspose.PDF для JavaScript через C++. Пример написан на JavaScript.

1. Выберите PDF файлы для объединения.
1. Создайте 'FileReader'.

1. Функция [AsposePdfMerge2Files](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfmerge2files/) выполняется.
1. Имя результирующего файла устанавливается, в этом примере "ResultMerge.pdf".
1. Далее, если 'json.errorCode' равен 0, то вашему DownloadFile присваивается ранее указанное вами имя. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация об этой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет вам загрузить результирующий файл на операционную систему пользователя.

Следующий фрагмент кода показывает, как объединить файлы PDF:

```js

  var ffileMerge = function (e) {
    const file_reader = new FileReader();
    function readFile(index) {
      /*только два файла*/
      if (index >= e.target.files.length || index >= 2) {
        /*объединить два PDF-файла и сохранить как "ResultMerge.pdf"*/
        const json = AsposePdfMerge2Files(undefined, undefined, e.target.files[0].name, e.target.files[1].name, "ResultMerge.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*создать ссылку для загрузки результирующего файла*/
        DownloadFile(json.fileNameResult, "application/pdf");
        return;
      }
      const file = e.target.files[index];
      file_reader.onload = function (event) {
        /*подготовить(сохранить) файл из BLOB*/
        AsposePdfPrepare(event.target.result, file.name);
        readFile(index + 1)
      }
      file_reader.readAsArrayBuffer(file);
    }
    readFile(0);
  }
```


### Использование Web Workers

```js

    /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? 
          `Результат:\n${(evt.data.operation == 'AsposePdfPrepare') ? 
                      fileProcess('AsposePdfMerge2Files', evt.data.json.optdata[0].file, {"fileName2": evt.data.json.fileNameResult}) ?? 'пожалуйста, подождите...' : 
                      DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0]) /*AsposePdfMerge2Files*/
                    }` :
          `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик событий. Объединяются только два файла. Если выбран только один файл, используйте его. Для второго файла необходимо выполнить AsposePdfPrepare */
    const ffileMerge = evt => fileProcess('AsposePdfPrepare',  evt.target.files[(evt.target.files.length == 1) ? 0 : 1],
                                          [{"operation": 'AsposePdfMerge2Files', "file": evt.target.files[0]}])
    /* Запрос к Web Worker */
    const fileProcess = (operation, ffile, optdata) => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        if (operation == 'AsposePdfPrepare')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, "params": [event.target.result, ffile.name, optdata] },
                  [event.target.result]
                );
        else if (operation == 'AsposePdfMerge2Files')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, 
                    "params": [event.target.result, undefined, ffile.name, (optdata === undefined) ? ffile.name : optdata.fileName2,
                                `Result${operation}.pdf`] },
                  [event.target.result]
                );
      }
      file_reader.readAsArrayBuffer(ffile);
    }

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