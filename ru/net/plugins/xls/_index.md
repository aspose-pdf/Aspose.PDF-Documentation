---
title: XLS Converter
type: docs
weight: 20
url: /ru/net/plugins/xls/
description: Как конвертировать PDF в таблицы Excel с помощью плагинов Aspose.Pdf
lastmod: "2024-01-24"
---

{{% alert color="primary" %}}

В этой статье мы покажем вам, как использовать [плагин PdfXls](https://products.aspose.org/pdf/net/xls-converter/), который может конвертировать PDF файлы в формат Excel с высокой точностью и достоверностью.

{{% /alert %}}

## Предварительные условия

Вам потребуются следующие компоненты:

* Visual Studio 2019 или позднее
* Aspose.PDF для .NET 24.1 или позднее
* Пример PDF файла, который вы хотите конвертировать в формат Excel

Вы можете скачать библиотеку Aspose.PDF для .NET с официального сайта или установить ее с помощью NuGet Package Manager в Visual Studio.

## Шаги

Основные шаги для конвертации PDF файла в формат Excel с помощью плагина PdfXls:

1. Создайте объект класса PdfXls
1. Добавьте исходные и выходные данные в объект PdfToXlsOptions
1. Запустите метод Process объекта PdfXls

Давайте посмотрим, как реализовать эти шаги на C# коде.
Давайте посмотрим, как реализовать эти шаги на C#.

### Шаг 1: Создание объекта класса PdfXls

Класс PdfXls — это основной класс, который предоставляет функциональность конвертации PDF в Excel. Чтобы использовать его, вам нужно создать экземпляр с помощью конструктора по умолчанию:

```csharp
// Создание экземпляра плагина PdfXls
var plugin = new PdfXls();
```

### Шаг 2: Добавление входных и выходных источников данных в объект PdfToXlsOptions

Класс PdfToXlsOptions — это вспомогательный класс, который позволяет указывать различные опции и параметры для процесса конвертации. Чтобы использовать его, вам нужно создать экземпляр и добавить входные и выходные источники данных с помощью методов `AddInput` и `AddOutput`. Источниками данных могут быть либо пути к файлам, либо потоки. Например, для конвертации PDF-файла с именем `sample.pdf` в папке `C:\Samples` в Excel-файл с именем `sample.xlsx` в той же папке, вы можете использовать следующий код:

```csharp
// Указание путей к входному и выходному файлам
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.xlsx");

// Создание экземпляра класса PdfToXlsOptions
var options = new PdfToXlsOptions();

// Добавление путей к входному и выходному файлам в опции
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```
Вы также можете установить другие параметры, такие как формат вывода, диапазон страниц, имя листа и т.д., используя свойства класса PdfToXlsOptions. Например, чтобы конвертировать PDF файл в формат XLSX, вставить пустой столбец в первую позицию и назвать лист "MySheet", вы можете использовать следующий код:

```csharp
// Установить формат вывода в XLSX
options.Format = PdfToXlsOptions.ExcelFormat.XLSX;

// Вставить пустой столбец в первую позицию
options.InsertBlankColumnAtFirst = true;
```

### Шаг 3: Запустить метод Process объекта PdfXls

Последний шаг - запустить метод Process объекта PdfXls, передав объект PdfToXlsOptions в качестве параметра.
Последний шаг - запустить метод Process объекта PdfXls, передав объект PdfToXlsOptions в качестве параметра.

```csharp
// Обработать конвертацию PDF в Excel с использованием плагина и параметров
var resultContainer = plugin.Process(options);

// Получить первый результат из коллекции результатов
var result = resultContainer.ResultCollection[0];

// Вывести результат
Console.WriteLine(result);
```

Результат будет содержать информацию, такую как пути к выходным файлам.
