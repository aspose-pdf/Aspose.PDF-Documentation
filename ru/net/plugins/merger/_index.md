---
title: Слияние
type: docs
weight: 100
url: ru/net/plugins/merger/
description: Как объединить несколько PDF-файлов в один с помощью плагина Aspose.PDF Merger
lastmod: "2024-01-24"
---

В этой статье мы покажем вам, как использовать [плагин Merger](https://products.aspose.org/pdf/net/merger/), который может объединить несколько PDF-файлов в один и сохранить его как новый файл.

## Предварительные требования

Вам потребуется следующее:

* Visual Studio 2019 или более поздняя версия
* Aspose.PDF для .NET 21.1 или более поздняя версия
* Три образца PDF-файла, которые вы хотите объединить

Вы можете скачать библиотеку Aspose.PDF для .NET с официального сайта или установить ее с помощью NuGet Package Manager в Visual Studio.

## Шаги

Основные шаги для объединения нескольких PDF-файлов в один с помощью плагина Merger:

1. Создайте объект класса Merger
2. Создайте объект класса MergeOptions и добавьте пути к входному и выходному файлам
3. Запустите метод Process объекта Merger

Давайте посмотрим, как реализовать эти шаги на языке C#.

### Шаг 1: Создайте объект класса Merger
### Шаг 1: Создание объекта класса Merger

Класс Merger - это основной класс, который предоставляет функциональность объединения нескольких PDF файлов в один. Для его использования вам необходимо создать экземпляр с помощью конструктора по умолчанию:

```cs
// Создание нового экземпляра Merger
var pdfMerger = new Merger();
```

### Шаг 2: Создание объекта класса MergeOptions и добавление путей к входному и выходному файлам

Класс MergeOptions - это вспомогательный класс, который позволяет указать различные опции и параметры для процесса слияния, такие как диапазон страниц, порядок, безопасность и т.д.
Класс MergeOptions - это вспомогательный класс, который позволяет указывать различные параметры для процесса слияния, такие как диапазон страниц, порядок, безопасность и т.д.

```cs
// Укажите пути к входным и выходным файлам
string inputFilePath1 = Path.Combine(@"C:\Samples\", "sample1.pdf");
string inputFilePath2 = Path.Combine(@"C:\Samples\", "sample2.pdf");
string inputFilePath3 = Path.Combine(@"C:\Samples\", "sample3.pdf");
var outputFilePath = "TestMerge.pdf";

// Создайте экземпляр класса MergeOptions
var mergeOptions = new MergeOptions();

// Добавьте пути к входным и выходным файлам в параметры
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath1));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath2));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath3));
mergeOptions.AddOutput(new FileDataSource(outputFilePath));
```

### Шаг 3: Запустите метод Process объекта Merger

Последний шаг - запустить метод Process объекта Merger, передав объект mergeOptions в качестве параметра.
Финальным шагом является выполнение метода Process объекта Merger, передавая объект mergeOptions в качестве параметра.

```cs
// Обработать слияние и сохранить объединенный файл
pdfMerger.Process(mergeOptions);

// Вывести сообщение о подтверждении
Console.WriteLine("PDF файлы были успешно объединены.");
```
