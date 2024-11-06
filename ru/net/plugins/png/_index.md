---
title: PNG конвертер
type: docs
weight: 110
url: ru/net/plugins/png/
description: Конвертирование PDF в изображения PNG с помощью плагина Aspose.PDF PNG
lastmod: "2024-01-24"
---

Если вы хотите [конвертировать документы PDF в изображения PNG](https://products.aspose.org/pdf/net/png-converter/) с использованием .NET, Aspose.PDF для .NET предлагает надежное решение. В этой статье мы рассмотрим основные шаги по созданию объекта, добавлению источника данных и выполнению метода обработки с использованием библиотеки Aspose.PDF.

## Предварительные требования

Вам потребуется следующее:

* Visual Studio 2019 или новее
* Aspose.PDF для .NET 24.1 или новее
* Образец файла PDF

## Обзор кода

Ниже приведен код, демонстрирующий демонстрацию конвертации PNG с использованием плагина Aspose.PDF PNG:

```csharp
using Aspose.Pdf.Plugins;

//....

// Создайте новый экземпляр класса PngOptions.
var convertorOptions = new PngOptions();

// Добавьте входные и выходные пути в PngOptions.
convertorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
convertorOptions.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", "images")));

// Установите выходное разрешение в 300 DPI.
convertorOptions.OutputResolution = 300;

// Создайте новый экземпляр класса Png.
Png converter = new ();

// Обработайте конвертацию PNG и получите контейнер с результатами.
ResultContainer resultContainer = converter.Process(convertorOptions);

// Выведите результат в консоль.
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
      Console.WriteLine(operationResult.Data.ToString());
}
```
Давайте разберем основные шаги:

1. **Создание объекта (PngOptions и Png)**

   Код начинается с создания экземпляра класса `PngOptions` для настройки конвертации в PNG. Кроме того, создается экземпляр класса `Png` для дальнейшей обработки.

2. **Добавление источника данных**

   Путь к входному файлу PDF добавляется в `PngOptions` с использованием метода `AddInput`. Аналогично, путь для выходных изображений PNG добавляется с использованием метода `AddOutput`.

3. **Установка разрешения вывода**

   Код устанавливает разрешение вывода в 300 DPI с использованием свойства `OutputResolution` класса `PngOptions`.

4. **Запуск метода Process**

   Конвертация в PNG инициируется вызовом метода `Process` в классе `Png`, передавая настроенные `PngOptions`. Результат сохраняется в `resultContainer`.

5. **Обработка результата**

   Код выводит результат в консоль, демонстрируя путь(и) конвертированного файла.
