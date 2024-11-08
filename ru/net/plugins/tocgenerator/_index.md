---
title: Генератор оглавления
type: docs
weight: 150
url: /ru/net/plugins/tocgenerator/
description: Создает оглавление с помощью генератора оглавлений Aspose.PDF для .NET
lastmod: "2024-01-24"
draft: false
---

Хотите улучшить свои PDF документы, [добавляя оглавление (TOC)](https://products.aspose.org/pdf/net/toc-generator/) динамически? Aspose.PDF для .NET предоставляет мощный класс `TocGenerator`, который позволяет вам с легкостью генерировать оглавления. В этом руководстве мы рассмотрим основные шаги создания оглавления в документе PDF с использованием Aspose.PDF, включая создание объекта `TocGenerator`, добавление путей ввода/вывода и выполнение процесса генерации оглавления.

## Предварительные требования

Вам потребуется следующее:

* Visual Studio 2019 или более поздняя версия
* Aspose.PDF для .NET 24.1 или более поздняя версия
* Образец файла PDF

Кроме того, ознакомьтесь с классом `TocOptions` и его функциональностью. Подробная информация доступна в [справочнике API Aspose.PDF](https://reference.aspose.com/pdf/net/aspose.pdf/TocOptions/).

Теперь давайте перейдем к коду и рассмотрим, как создать оглавление для вашего документа PDF.
Теперь давайте погрузимся в код и изучим, как сгенерировать оглавление для вашего PDF-документа.

## Обзор кода

Мы будем использовать класс `TocGeneratorDemo` с методом `Run` для демонстрации создания оглавления. Давайте рассмотрим основные шаги:

```csharp
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation
{
    internal static class TocGeneratorDemo
    {
        private const string PathForSamples = @"C:\Samples\";

        // Запускает демонстрацию генерации оглавления.
        internal static void Run()
        {
            // Создаем новый экземпляр класса TocGenerator.
            TocGenerator generator = new();

            // Создаем новый экземпляр класса TocOptions.
            TocOptions options = new();
            // Добавляем входные и выходные пути в TocOptions.
            options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
            options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));

            // Обрабатываем генерацию оглавления и получаем контейнер с результатами.
            var resultContainer = generator.Process(options);

            // Получаем результат из контейнера с результатами.
            var result = resultContainer.ResultCollection[0];

            // Выводим результат в консоль.
            Console.WriteLine(result);
        }
    }
}
```
### 1. Создайте объект TocGenerator

Код начинается с создания нового экземпляра класса `TocGenerator`. Этот класс предоставляет методы для генерации оглавлений для PDF документов.

```csharp
TocGenerator generator = new();
```

### 2. Создайте TocOptions

Далее создается новый экземпляр класса `TocOptions` для настройки процесса генерации оглавления. Пути к входному и выходному файлам добавляются в опции.

```csharp
TocOptions options = new();
options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));
```

### 3. Запустите процесс генерации оглавления

Затем вызывается метод `Process` объекта `TocGenerator`, передавая настроенные опции. Контейнер результатов содержит сгенерированное оглавление, и оно выводится в консоль.

```csharp
var resultContainer = generator.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);
```
