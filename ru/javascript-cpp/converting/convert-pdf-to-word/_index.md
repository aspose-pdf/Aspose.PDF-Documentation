---
title: Конвертировать PDF в Word документы на JavaScript
linktitle: Конвертировать PDF в Word
type: docs
weight: 10
url: ru/javascript-cpp/convert-pdf-to-doc/
lastmod: "2023-08-04"
description: Узнайте, как написать JavaScript код для конвертации PDF в DOC (DOCX) прямо в Интернете.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Операция преобразования зависит от количества страниц в документе и может занять много времени. Поэтому мы настоятельно рекомендуем использовать Web Workers.

Этот код демонстрирует способ разгрузки ресурсоемких задач по преобразованию PDF файла в веб-воркере, чтобы предотвратить блокировку основного потока пользовательского интерфейса. Он также предлагает удобный способ загрузки преобразованного файла.

Для редактирования содержимого PDF файла в Microsoft Word или других текстовых процессорах, поддерживающих форматы DOC и DOCX. PDF файлы редактируемы, но DOC и DOCX файлы более гибкие и настраиваемые.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в DOC онлайн**

Aspose.PDF для JavaScript предлагает вам бесплатное онлайн-приложение ["PDF в DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), где вы можете попробовать изучить его функциональность и качество работы.

[![Convert PDF to DOC](/pdf/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Конвертировать PDF в DOC

```js

  /*Создать Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'загружено!' :
      (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/msword", evt.data.params[0])}` : `Ошибка: ${evt.data.json.errorText}`;

  /*Обработчик события*/
  const ffileToDoc = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*Конвертировать PDF-файл в Doc и сохранить как "ResultPDFtoDoc.doc" - Запрос к Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDoc', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc"] }, [event.target.result]);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

  /*Создать ссылку для загрузки файла результата*/
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


Следующий фрагмент кода JavaScript показывает простой пример преобразования страниц PDF в файлы DOC:

1. Выберите PDF-файл для конвертации.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfToDoc](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftodoc/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPDFtoDoc.doc".
1. Далее, если 'json.errorCode' равен 0, то вашему результату File присваивается имя, указанное ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация об этой ошибке будет содержаться в файле 'json.errorText'.
1. В итоге, функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет вам скачать результирующий файл в операционную систему пользователя.

```js

  var ffileToDoc = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Преобразовать PDF-файл в Doc и сохранить как "ResultPDFtoDoc.doc"*/
      const json = AsposePdfToDoc(event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*Создать ссылку для скачивания результирующего файла*/
      DownloadFile(json.fileNameResult, "application/msword");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


{{% alert color="warning" %}}
**Попробуйте конвертировать PDF в DOCX онлайн**

Aspose.PDF для JavaScript представляет вам бесплатное онлайн-приложение ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), где вы можете исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в Word Бесплатное Приложение](/pdf/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Конвертируйте PDF в DOCX

Aspose.PDF для JavaScript API позволяет вам читать и конвертировать PDF-документы в DOCX. DOCX - это хорошо известный формат для документов Microsoft Word, структура которого была изменена с простого бинарного на комбинацию XML и бинарных файлов. Файлы Docx можно открывать в Word 2007 и более поздних версиях, но не в более ранних версиях MS Word, которые поддерживают расширения файлов DOC.

```js

  /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document", evt.data.params[0])}` : `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик событий*/
    const ffileToDocX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*конвертировать PDF-файл в DocX и сохранить как "ResultPDFtoDocX.docx" - Запросить у Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDocX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Фрагмент кода]

    /*создать ссылку для загрузки результирующего файла*/
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


Следующий пример кода JavaScript показывает простой пример преобразования страниц PDF в файлы DOCX:

1. Выберите PDF файл для преобразования.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfToDocX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftodocx/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPDFtoDocX.docx".
1. Далее, если 'json.errorCode' равен 0, то вашему результирующему файлу присваивается имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0, и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет загрузить результирующий файл на операционную систему пользователя.

```js

  var ffileToDocX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*преобразовать PDF-файл в DocX и сохранить как "ResultPDFtoDocX.docx"*/
      const json = AsposePdfToDocX(event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*создать ссылку для загрузки результирующего файла*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```