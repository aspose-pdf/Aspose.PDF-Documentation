---
title: Генератор таблиц
type: docs
weight: 130
url: /net/plugins/tablegenerator/
description: Позволяет добавлять/вставлять таблицу на указанную страницу PDF-документа.
lastmod: "2024-01-24"
draft: false
---

Вам нужно создать динамичные и визуально привлекательные таблицы в ваших PDF-документах с помощью .NET? Aspose.PDF для .NET предоставляет мощный класс TableGenerator, который упрощает этот процесс. В этой главе мы рассмотрим шаги по созданию таблиц в PDF-документе с использованием [Aspose.PDF Table Generator](https://products.aspose.org/pdf/net/table-generator/), начиная с создания демонстрационного документа и заканчивая генерацией таблиц с помощью класса TableGenerator.
Погрузимся в изучение процесса создания таблиц шаг за шагом.

## Предварительные требования

Вам потребуется следующее:

* Visual Studio 2019 или более поздняя версия
* Aspose.PDF для .NET 24.3 или более поздняя версия
* Образец PDF-файла

## Создание демонстрационного документа

Прежде чем приступить к созданию таблиц, давайте создадим демонстрационный документ с пустыми страницами, на которые будут вставлены наши таблицы.
Перед тем как приступить к созданию таблиц, создадим демонстрационный документ с пустыми страницами, куда будут вставляться наши таблицы.

* Создайте новый PDF-документ.
* Добавьте пустые страницы в документ.
* Сохраните документ в указанный файл.

```cs
// <summary>
// Создает демонстрационный документ с пустыми страницами.
//
// Параметры:
// - fileName: Путь и имя выходного файла.
// </summary>
internal static void CreateDemoDocument(string fileName)
{
    // Создайте новый PDF-документ.
    var document = new Aspose.Pdf.Document();

    // Добавьте четыре пустые страницы в документ.
    for (int i = 0; i < 2; i++)
    {
        document.Pages.Add();
    }

    // Сохраните документ в указанный файл.
    document.Save(fileName);
}
```

## Генерация таблиц

Как только наш демонстрационный документ готов, мы можем начать генерировать таблицы с помощью класса `TableGenerator`. Следующий фрагмент демонстрирует, как генерировать таблицы с различными типами содержимого и параметрами форматирования. Вот как генерировать таблицы:

* Создайте новый экземпляр класса `TableGenerator`.
* Создайте новый экземпляр класса `TableGenerator`.
* Создайте параметры таблицы и укажите источники данных для входных и выходных файлов.
* Добавьте в параметры таблицы с рядами и ячейками, указав содержимое и форматирование.
* Обработайте генерацию таблицы с помощью метода `Process` и получите контейнер с результатом.

### Создание таблиц

Чтобы создать таблицу с использованием Aspose.PDF, выполните следующие шаги:

```cs
// Создайте новый экземпляр класса TableGenerator.
var generator = new TableGenerator();

// Создайте параметры таблицы и добавьте демонстрационные таблицы.
var options = new TableOptions();

// Добавьте в параметры источники данных для входного и выходного файлов.
options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

// Добавьте первую таблицу в параметры.
options
    .InsertPageAfter(1)
    .AddTable()
```

В приведенном выше коде мы создаем экземпляр `TableOptions` и указываем источники данных для входных и выходных файлов документа PDF.
В приведенном выше коде мы создаем экземпляр `TableOptions` и указываем источники данных входного и выходного файлов для PDF документа.

### Добавление содержимого в таблицы

После создания таблицы вы можете заполнить ее строками и ячейками, содержащими различные типы содержимого, такие как текст, HTML, изображения и т.д. Вот как добавить содержимое в таблицу:

```csharp
options
    .AddTable()
        .AddRow()
            .AddCell()
                .AddParagraph(new HtmlFragment("<h1>Заголовок 1</h1>")) // Добавить HTML содержимое в ячейку.
            .AddCell()
                .AddParagraph(new HtmlFragment("<h2>Заголовок 2</h2>"))
            .AddCell()
                .AddParagraph(new HtmlFragment("<h3>Заголовок 3</h3>"));
```

В этом примере мы добавляем строку в таблицу и заполняем ее ячейками, содержащими HTML фрагменты, представляющие заголовки.

Полезные методы:

* **InsertPageAfter**: Вставляет страницу после указанного номера страницы.
* **InsertPageBefore**: Вставляет страницу перед указанным номером страницы.
* **AddTable**: Добавляет таблицу в документ.
* **AddTable**: Добавляет таблицу в документ.
* **AddRow**: Добавляет строку в таблицу.
* **AddCell**: Добавляет ячейки в строку.
* **AddParagraph**: Добавляет содержимое в ячейку.

Вы можете добавить следующие типы содержимого в параграф:

* **HtmlFragment** - содержимое на основе HTML-разметки
* **TeXFragment** - содержимое на основе разметки TeX/LaTeX
* **TextFragment** - простой текстовый контент
* **Image** - графическое изображение

## Выполнение генерации таблицы

После добавления содержимого мы можем начать создание таблицы.

```cs
// Обработка генерации таблицы и получение контейнера с результатами.
var resultContainer = generator.Process(options);

// Вывод количества результатов в коллекции результатов.
Console.WriteLine(resultContainer.ResultCollection.Count);
```

Метод `Process` выполняет генерацию таблицы. Этот метод также может быть обернут в try-catch для обработки ошибок.

Ниже вы можете увидеть полный код примера:

```cs
using Aspose.Pdf;
using Aspose.Pdf.Plugins;
using Aspose.Pdf.Text;

namespace AsposePluginsNet8.Documentation
{
    // <summary>
    // Представляет класс, демонстрирующий использование генерации таблиц в Aspose.Pdf.
    // </summary>
    internal static class TableDemo
    {
        // <summary>
        // Запускает демонстрацию генерации таблицы.
        // </summary>
        internal static void Run()
        {
            // Создание демонстрационного документа и генерация таблиц.
            CreateDemoDocument(@"C:\Samples\Results\table-generator-demo.pdf");
            CreateDemoTable();
        }

        // <summary>
        // Создает демонстрационный документ с четырьмя пустыми страницами.
        //
        // Параметры:
        // - fileName: Путь и имя выходного файла.
        // </summary>
        internal static void CreateDemoDocument(string fileName)
        {
            // Создание нового PDF документа.
            var document = new Aspose.Pdf.Document();

            // Добавление четырех пустых страниц в документ.
            for (int i = 0; i < 2; i++)
            {
                document.Pages.Add();
            }

            // Сохранение документа в указанный файл.
            document.Save(fileName);
        }

        // <summary>
        // Генерирует таблицы с использованием класса TableGenerator.
        // </summary>
        internal static void CreateDemoTable()
        {
            // Создание нового экземпляра класса TableGenerator.
            var generator = new TableGenerator();

            // Создание параметров таблицы и добавление демонстрационных таблиц.
            var options = new TableOptions();

            // Добавление источников данных входных и выходных файлов к параметрам.
            options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
            options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

            // Добавление первой таблицы к параметрам.
            options
                .InsertPageAfter(1)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h1>Заголовок 1</h1>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h2>Заголовок 2</h2>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h3>Заголовок 3</h3>"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TeXFragment("{\\small Уравнение $E=mc^2$, открытое в 1905 году Альбертом Эйнштейном.}", true))
                        .AddCell()
                            .AddParagraph(new TextFragment("Ячейка 2 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Ячейка 2 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Ячейка 3 1а"))
                            .AddParagraph(new TextFragment("Ячейка 3 1б"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Ячейка 3 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Ячейка 3 3"));

            // Добавление второй таблицы к параметрам.
            options
                .InsertPageBefore(2)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Заголовок 1 1"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Заголовок 1 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Заголовок 1 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\logo.png",
                                FixWidth = 75,
                                FixHeight = 75,
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\sample.svg",
                                FileType = ImageFileType.Svg,
                                FixWidth = 75,
                                FixHeight = 75
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                ImageStream = File.OpenRead(@"C:\Samples\Conversion\Demo.dcm"),
                                FileType = ImageFileType.Dicom,
                                FixWidth = 75,
                                FixHeight = 75
                            });

            // Обработка генерации таблицы и получение контейнера с результатами.
            var resultContainer = generator.Process(options);

            // Вывод количества результатов в коллекции результатов.
            Console.WriteLine(resultContainer.ResultCollection.Count);
        }
    }
}
```

