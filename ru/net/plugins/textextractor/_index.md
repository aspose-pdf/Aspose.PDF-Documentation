---
title: Text Extractor
type: docs
weight: 140
url: ru/net/plugins/textextractor/
description: Извлекает текстовое содержимое из PDF документа.
lastmod: "2024-01-24"
---

У вас есть PDF документ, из которого вам нужно [программно извлечь текст](https://products.aspose.org/pdf/net/text-extractor/)? С помощью Aspose.PDF для .NET вы можете легко выполнить эту задачу, используя класс TextExtractor. В этой статье мы рассмотрим основные шаги создания приложения для извлечения текста на .NET, включая создание объекта TextExtractor, добавление источника данных и выполнение процесса извлечения текста.

## Предварительные условия

Вам понадобится следующее:

* Visual Studio 2019 или более поздняя версия
* Aspose.PDF для .NET 24.1 или более поздняя версия
* Образец PDF файла

Кроме того, ознакомьтесь с классом `TextExtractorOptions` и его функциональными возможностями. Подробную информацию можно найти в [справочнике API Aspose.PDF](https://reference.aspose.com/pdf/net/aspose.pdf/TextExtractorOptions/).

Теперь давайте перейдем к коду и изучим, как извлечь текст из PDF документа.
Теперь давайте погрузимся в код и исследуем, как извлечь текст из PDF документа.

## Обзор кода

Следующий код демонстрирует возможности извлечения текста. Давайте рассмотрим ключевые шаги:

### 1. Создание объекта TextExtractor

Код начинается с создания нового экземпляра класса `TextExtractor`. Этот класс предоставляет методы для извлечения текста из PDF документов.

```csharp
using TextExtractor extractor = new();
```

### 2. Добавление источника данных

Затем создается `FileDataSource` для входного PDF файла. Это файл, из которого будет извлечен текст.

```csharp
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

### 3. Создание TextExtractorOptions

Создается объект `TextExtractorOptions` для настройки процесса извлечения текста. В опции добавляется источник входного файла.

```csharp
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);
```

### 4. Запуск процесса извлечения текста

Затем вызывается метод `Process` объекта `TextExtractor`, передающий настроенные опции.
Метод `Process` затем вызывается для объекта `TextExtractor`, передавая настроенные опции.

```csharp
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;
Console.WriteLine(results[0]);
```

Ниже вы можете увидеть полный код:

``````cs
using Aspose.Pdf.Plugins;
// ...

// Создаем новый экземпляр TextExtractor.
using TextExtractor extractor = new();

// Создаем FileDataSource для входного PDF файла.
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));

// Создаем TextExtractorOptions.
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);

// Обрабатываем извлечение текста.
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;

// Печатаем извлеченный текст.
Console.WriteLine(results[0]);

```
