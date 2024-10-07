---
title: Экспортер форм
type: docs
weight: 50
url: /net/plugins/formexpoter/
description: Как экспортировать значения полей формы в файлы CSV с помощью плагина Aspose.PDF Form Exporter
lastmod: "2024-01-24"
draft: false
---

В этой статье мы покажем вам, как использовать [плагин Form Exporter](https://products.aspose.org/pdf/net/form-exporter/), который может экспортировать значения полей форм из файлов PDF в файлы CSV.

## Требования

Вам потребуется следующее:

* Visual Studio 2019 или новее
* Aspose.PDF для .NET 21.1 или новее
* Пример файла PDF, содержащего некоторые поля форм

Вы можете скачать библиотеку Aspose.PDF для .NET с официального сайта или установить ее с помощью менеджера пакетов NuGet в Visual Studio.

## Шаги

Основные шаги для экспорта значений полей формы в файлы CSV с использованием плагина FormExporter:

1. Создать объект класса `FormExporter`
1. Создать объект класса `FormExporterValuesToCsvOptions` и указать предикат и разделитель
1.
1.
1. Запустите метод `Process` объекта `FormExporter`

Давайте посмотрим, как реализовать эти шаги на C#.

### Шаг 1: Создание объекта класса FormExporter

Класс FormExporter — это основной класс, который предоставляет функциональность экспорта значений полей формы в файлы CSV. Чтобы использовать его, вам нужно создать экземпляр с помощью конструктора по умолчанию:

```cs
// Создание экземпляра плагина FormExporter
var plugin = new FormExporter();
```

### Шаг 2: Создание объекта класса FormExporterValuesToCsvOptions и указание предиката и разделителя

Класс FormExporterValuesToCsvOptions — это вспомогательный класс, который позволяет указать различные опции и параметры для процесса экспорта, такие как предикат и разделитель.
Класс FormExporterValuesToCsvOptions - это вспомогательный класс, который позволяет вам указывать различные параметры и настройки для процесса экспорта, такие как предикат и разделитель.

```cs
// Создание параметров для экспорта значений полей формы в CSV
var options = new FormExporterValuesToCsvOptions(
(field) => { return field is TextBoxField && field.PageIndex == 2; }, ';');
```

### Шаг 3: Добавьте источники входных и выходных данных в объект параметров

Источниками входных и выходных данных являются PDF-файлы, из которых вы хотите экспортировать данные, и CSV-файл, в который вы хотите сохранить данные.
Исходные и результирующие данные представлены в виде файлов PDF, которые вы хотите экспортировать, и файла CSV, который вы хотите сохранить.

```cs
// Добавление входных и выходных файлов в параметры
options.AddInput(new FileDataSource("inputFileNameWithFields-1.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-2.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-3.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-4.pdf"));
options.AddOutput(new FileDataSource("outputFileName.csv"));

```

### Шаг 4: Запуск метода Process объекта FormExporter

Последний шаг - запустить метод Process объекта FormExporter, передав объект параметров в качестве аргумента.
Последний шаг - выполнить метод Process объекта FormExporter, передав объект options в качестве параметра.

```cs
// Обработать значения полей формы с помощью плагина
var resultContainer = plugin.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);

```

Результат будет содержать информацию, такую как пути к входному и выходному файлам.
