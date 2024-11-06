---
title: Optimizer 
type: docs
weight: 80
url: ru/net/plugins/optimizer/
description: Как оптимизировать и изменять PDF файлы с помощью Aspose.PDF Optimizer
lastmod: "2024-01-24"
---

В этой главе мы рассмотрим, как использовать [Aspose.PDF Optimizer](https://products.aspose.org/pdf/net/optimizer/) для оптимизации, изменения размера и поворота PDF файлов в ваших C# приложениях.
Давайте погрузимся и узнаем, как выполнить эти задачи шаг за шагом.

## Предварительные требования

Вам потребуется следующее:

* Visual Studio 2019 или более поздняя версия
* Aspose.PDF для .NET 24.1 или более поздняя версия
* Образец PDF файла, содержащего некоторые поля формы

## Оптимизация PDF файлов

Оптимизация PDF файла включает в себя уменьшение его размера и повышение производительности. Следующие фрагменты кода показывают, как достичь этой задачи. Вот как вы можете оптимизировать PDF файл:

* Создайте новый источник данных файла для входного PDF файла.
* Создайте новый источник данных файла для оптимизированного выходного PDF файла.
* Создайте экземпляр `OptimizeOptions`.
* Добавьте входные и выходные источники данных в опции оптимизации.
* Добавьте источники входных и выходных данных в параметры оптимизации.
* Создайте экземпляр `Optimizer` и выполните оптимизацию, используя настройки оптимизации.

```cs
// Создайте новый источник данных файла для входного PDF файла.
var inputDataSource = new FileDataSource(inputPath);

// Создайте новый источник данных файла для оптимизированного выходного PDF файла.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// Создайте новый экземпляр OptimizeOptions.
var options = new OptimizeOptions();

// Добавьте источники входных и выходных данных в параметры оптимизации.
options.AddInput(inputDataSource);
options.AddOutput(outputDataSource);

// Создайте новый экземпляр Optimizer.
var optimizer = new Optimizer();

// Выполните оптимизацию с использованием настроек оптимизации.
optimizer.Process(options);
```

## Изменение размера PDF файлов

Изменение размера файла PDF включает изменение размера его страницы. Следующий код показывает, как выполнить эту задачу. Следуйте этим шагам для изменения размера файла PDF:

* Создайте новый источник данных файла для входного файла PDF.
* Создайте новый источник данных файла для входного PDF-файла.
* Создайте новый источник данных файла для изменённого по размеру выходного PDF-файла.
* Создайте экземпляр `ResizeOptions` и установите желаемый размер страницы.
* Добавьте входные и выходные источники данных к параметрам изменения размера.
* Создайте экземпляр `Optimizer` и обработайте изменение размера с использованием заданных опций.

```cs
// Создайте новый источник данных файла для входного PDF-файла.
var inputDataSource = new FileDataSource("sample.pdf");

// Создайте новый источник данных файла для изменённого по размеру выходного PDF-файла.
var outputDataSource = new FileDataSource("sample_resized.pdf");

// Создайте новый экземпляр ResizeOptions и установите желаемый размер страницы.
var opt = new ResizeOptions
{
    PageSize = PageSize.PageLetter
};

// Добавьте входные и выходные источники данных к параметрам изменения размера.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// Создайте новый экземпляр Optimizer.
var optimizer = new Optimizer();

// Обработайте изменение размера с использованием заданных опций.
optimizer.Process(opt);
```

## Вращение страниц PDF
## Поворот страниц PDF

Поворот страниц PDF позволяет изменить ориентацию страниц в документе PDF. Вот как можно повернуть страницы PDF:

* Создайте новый источник данных файла для входного файла PDF.
* Создайте новый источник данных файла для выходного файла PDF.
* Создайте экземпляр `RotateOptions` и установите значение поворота.
* Добавьте входные и выходные источники данных в параметры поворота.
* Создайте экземпляр `Optimizer` и обработайте поворот с использованием параметров поворота.

```cs
// Создайте новый источник данных файла для входного файла PDF.
var inputDataSource = new FileDataSource(inputPath);

// Создайте новый источник данных файла для оптимизированного выходного файла PDF.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// Создайте новый экземпляр OptimizeOptions.
var opt = new RotateOptions();

// Добавьте входной и выходной источники данных к параметрам оптимизации.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// Установите значение поворота
opt.Rotation = Rotation.on180;

// Создайте новый экземпляр Optimizer.
var optimizer = new Optimizer();

// Обработайте оптимизацию с использованием параметров оптимизации.
optimizer.Process(opt)
```
## Заключение

Вы научились оптимизировать, изменять размер и поворачивать файлы PDF с помощью плагина Aspose.PDF Optimizer в C#. Внедряйте эти техники в свои приложения для эффективной работы с PDF документами в соответствии с вашими требованиями.