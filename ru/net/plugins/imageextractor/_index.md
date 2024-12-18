---
title: Извлекатель изображений
type: docs
weight: 80
url: /ru/net/plugins/imageextractor/
description: Извлечение изображений из PDF легко с плагином ImageExtractor
lastmod: "2024-01-24"
draft: false
---

Если вам когда-либо нужно было извлечь изображения из PDF-файла с помощью .NET, Aspose.PDF для .NET предлагает мощное и простое решение. В этом руководстве мы рассмотрим основные шаги по созданию объекта, добавлению источника данных и выполнению метода процесса с использованием [Aspose.PDF Image Extractor](https://products.aspose.org/pdf/net/image-extractor/).

## Предварительные требования

Вам потребуется следующее:

* Visual Studio 2019 или более поздняя версия
* Aspose.PDF для .NET 21.1 или более поздняя версия
* Образцовый PDF-файл

Вы можете скачать библиотеку Aspose.PDF для .NET с официального сайта или установить ее, используя NuGet Package Manager в Visual Studio.
Теперь давайте погрузимся в код и узнаем, как использовать плагин ImageExtractor.

## Шаги

Предоставленный код демонстрирует использование плагина `ImageExtractor` для извлечения изображений из PDF-файла.
Предоставленный код демонстрирует использование плагина `ImageExtractor` для извлечения изображений из файла PDF.

### 1. Создать объект (ImageExtractor)

Первый шаг включает создание экземпляра плагина `ImageExtractor`. Это достигается с помощью следующего кода:

```csharp
using var plugin = new ImageExtractor();
```

Здесь оператор `using` обеспечивает корректное освобождение ресурсов после завершения операции.

### 2. Добавить источник данных

Далее создается экземпляр класса `ImageExtractorOptions` для настройки процесса извлечения изображений. Путь к файлу ввода добавляется в опции с помощью метода `AddInput`:

```csharp
var imageExtractorOptions = new ImageExtractorOptions();
imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
```

Не забудьте заменить `"C:\Samples\"` и `"sample.pdf"` на соответствующий путь и имя файла вашего PDF.

### 3. Запустить метод обработки

Последний шаг - обработать извлечение изображений с использованием плагина и опций:

```csharp
Результат сохраняется в `resultContainer`, который содержит извлеченные изображения.

### 4. Обработка извлеченных изображений

После выполнения процесса вы можете извлечь изображения из контейнера результатов. Код ниже демонстрирует сохранение первого извлеченного изображения во временное место:

```csharp
var imageExtracted = resultContainer.ResultCollection[0].ToStream();
var someTemporaryPlace = File.OpenWrite("C:\\tmp\\tmp.jpg");
imageExtracted.CopyTo(someTemporaryPlace);
```

Убедитесь, что вы настроили путь назначения и имя файла согласно вашим предпочтениям.

Вы можете скопировать полный пример ниже:

```cs
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation;

internal static class ImageExtractorDemo
{
    // <summary>
    // Демонстрация использования плагина ImageExtractor для извлечения изображений из файла PDF.
    // </summary>
    internal static void Run()
    {
        // Создание экземпляра плагина ImageExtractor.
        using var plugin = new ImageExtractor();

        // Создание экземпляра класса ImageExtractorOptions.
        var imageExtractorOptions = new ImageExtractorOptions();

        // Добавление пути к входному файлу в опции.
        imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));

        // Обработка извлечения изображения с использованием плагина и опций.
        var resultContainer = plugin.Process(imageExtractorOptions);

        // Получение извлеченного изображения из контейнера результатов.
        var imageExtracted = resultContainer.ResultCollection[0].ToStream();
        var someTemporaryPlace = File.OpenWrite(Path.Combine(@"C:\Samples\","tmp.jpg"));
        imageExtracted.CopyTo(someTemporaryPlace);
    }
}
```

