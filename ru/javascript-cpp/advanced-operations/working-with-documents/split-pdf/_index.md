---
title: Разделение PDF с использованием JavaScript
linktitle: Разделение PDF файлов
type: docs
weight: 30
url: /ru/javascript-cpp/split-pdf/
description: Эта тема показывает, как разделить страницы PDF на отдельные PDF файлы с помощью Aspose.PDF для JavaScript через C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Разделение PDF на два файла с использованием JavaScript

Эта тема показывает, как разделить страницы PDF на отдельные PDF файлы с использованием JavaScript. В настоящее время мы поддерживаем разделение на две части. Это означает, что `pageToSplit` является маркером для деления. Первый файл будет содержать все страницы с 1 до `pageToSplit` включительно, а второй файл будет содержать остальные страницы.

Операция разделения зависит от количества страниц в документе и может быть очень трудоемкой. Поэтому мы настоятельно рекомендуем использовать Web Workers.

Предоставленный фрагмент кода является примером использования Web Worker в JavaScript для разделения PDF файла на два отдельных PDF файла и предоставления пользователю возможности скачать полученные файлы.
 Here's a steps of the code:

1. Создание веб-воркера. Веб-воркер инициализируется с использованием файла скрипта "AsposePDFforJS.js". Этот веб-воркер будет обрабатывать задачи по разделению PDF файлов в фоновом режиме. В нашем примере любые ошибки, возникающие в воркере, фиксируются и выводятся в консоль.
1. Обработка сообщений. Веб-воркер настроен на прослушивание сообщений с использованием обработчика событий onmessage. Когда он получает сообщение с веб-страницы, он обрабатывает запрос и отправляет ответ обратно в основной поток.
1. Обработчик события разделения файла. Существует обработчик события ffileSplit, который срабатывает, когда пользователь выбирает PDF файл для разделения. Он читает выбранный PDF файл с помощью FileReader и отправляет содержимое файла и соответствующие параметры (такие как количество страниц для разделения и имена выходных файлов) веб-воркеру через вызов postMessage.
1. Функция загрузки файла. Функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) отвечает за создание ссылки, которая позволяет пользователю загрузить файл. Она принимает имя файла, MIME-тип и содержимое файла. Функция создает ссылку для загрузки, связывает с ней содержимое файла, устанавливает имя файла и добавляет его в документ. Это позволяет пользователю загружать полученные PDF файлы.

1. Обработка сообщений в веб-воркере. Далее, если 'json.errorCode' равно 0, то json.fileNameResult будет содержать имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в свойстве 'json.errorText'.

1. Отображение результата. Главная страница включает элемент с ID 'output'. Когда веб-воркер отправляет сообщение с результатом, оно обновляет элемент 'output'. Если операция прошла успешно, отображаются ссылки для скачивания двух разделенных PDF-файлов. В случае ошибки отображается сообщение об ошибке.

Этот код демонстрирует способ разгрузки ресурсоемких задач по разделению PDF-файлов с помощью веб-воркера, чтобы избежать блокировки основного потока пользовательского интерфейса. Он также предлагает удобный способ загрузки разделенных PDF-файлов.

```js

    /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ?
          `Результат:\n${DownloadFile(evt.data.json.fileNameResult1, "application/pdf", evt.data.params[0])}
                  \n${DownloadFile(evt.data.json.fileNameResult2, "application/pdf", evt.data.params[1])}` :
          `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик события*/
    const ffileSplit = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Установить номер страницы для разделения*/
        const pageToSplit = 1;
        /*Разделить на два PDF-файла и сохранить "ResultSplit1.pdf", "ResultSplit2.pdf" - Запросить у Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSplit2Files',
            "params": [event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf"] },
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

Следующий фрагмент кода JavaScript показывает простой пример разделения страниц PDF на отдельные PDF файлы:

1. Выберите PDF файл для разделения.
1. Создайте объект 'FileReader' в обработчике.
1. Установите номер страницы для разделения.
1. Вызовите [AsposePdfSplit2Files](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsplit2files/) в последнем обработчике.
1. Проанализируйте результат. Имя результирующего файла будет установлено, в этом примере "ResultSplit2.pdf".
1. Далее, если 'json.errorCode' равен 0, то json.fileNameResult будет содержать имя, указанное вами ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле возникнет ошибка, то информация о такой ошибке будет содержаться в свойстве 'json.errorText'.
1. Вы можете использовать вспомогательную функцию [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/).

```js

  var ffileSplit = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Установите номер страницы для разделения*/
      const pageToSplit = 1;
      /*Разделите на два PDF файла и сохраните "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfSplit2Files(event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = e.target.files[0].name + " разделен: " + json.fileNameResult1 + ", " + json.fileNameResult2;
      else document.getElementById('output').textContent = json.errorText;
      /*Создайте ссылку для загрузки первого результирующего файла*/
      DownloadFile(json.fileNameResult1, "application/pdf");
      /*Создайте ссылку для загрузки второго результирующего файла*/
      DownloadFile(json.fileNameResult2, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```