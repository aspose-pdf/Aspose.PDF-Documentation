---
title: Создание сложного PDF
linktitle: Создание сложного PDF
type: docs
weight: 60
url: /net/complex-pdf-example/
description: Aspose.PDF для .NET позволяет создавать более сложные документы, содержащие изображения, фрагменты текста и таблицы в одном документе.
aliases:
    - /net/complex-pdf/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Пример [Привет, мир](/pdf/net/hello-world-example/) показал простые шаги для создания PDF-документа с использованием C# и Aspose.PDF. В этой статье мы рассмотрим создание более сложного документа с использованием C# и Aspose.PDF для .NET. В качестве примера возьмем документ из вымышленной компании, которая занимается пассажирскими паромными услугами.
Наш документ будет содержать изображение, два текстовых фрагмента (заголовок и абзац) и таблицу. Для создания такого документа мы будем использовать подход на основе DOM. Дополнительные сведения см. в разделе [Основы DOM API](/pdf/net/basics-of-dom-api/).

Если мы создаем документ с нуля, нам нужно следовать определенным шагам:

1.
1. Добавьте [Страницу](https://reference.aspose.com/pdf/net/aspose.pdf/page) к объекту документа. Теперь наш документ будет содержать одну страницу.
1. Добавьте [Изображение](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index) на Страницу.
1. Создайте [Текстовый Фрагмент](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) для заголовка. Для заголовка мы будем использовать шрифт Arial размером 24pt и выравнивание по центру.
1. Добавьте заголовок на страницу в [Параграфы](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs).
1. Создайте [Текстовый Фрагмент](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) для описания. Для описания мы будем использовать шрифт Arial размером 24pt и выравнивание по центру.
1. Добавьте (описание) на страницу в Параграфы.
1. Создайте таблицу, добавьте свойства таблицы.
1. Добавьте (таблицу) на страницу в [Параграфы](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs).
1. Сохраните документ под названием "Complex.pdf".

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
using Aspose.Pdf.Text;
using System;
using System.IO;

namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
public static void MakeComplexDocument()
        {
            // Инициализация объекта документа
            Document document = new Document();
            // Добавление страницы
            Page page = document.Pages.Add();

            // -------------------------------------------------------------
            // Добавление изображения
            var imageFileName = System.IO.Path.Combine(_dataDir, "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // Добавление заголовка
            var header = new TextFragment("Новые маршруты паромов осенью 2020");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // Добавление описания
            var descriptionText = "Посетители должны покупать билеты онлайн, и количество билетов ограничено 5,000 в день. Паромная служба работает с половинной загрузкой и по сокращенному графику. Ожидайте очереди.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // Добавление таблицы
            var table = new Table
            {
                ColumnWidths = "200",
                Border = new BorderInfo(BorderSide.Box, 1f, Color.DarkSlateGray),
                DefaultCellBorder = new BorderInfo(BorderSide.Box, 0.5f, Color.Black),
                DefaultCellPadding = new MarginInfo(4.5, 4.5, 4.5, 4.5),
                Margin =
                {
                    Bottom = 10
                },
                DefaultCellTextState =
                {
                    Font =  FontRepository.FindFont("Helvetica")
                }
            };

            var headerRow = table.Rows.Add();
            headerRow.Cells.Add("Отправление из города");
            headerRow.Cells.Add("Отправление с острова");
            foreach (Cell headerRowCell in headerRow.Cells)
            {
                headerRowCell.BackgroundColor = Color.Gray;
                headerRowCell.DefaultCellTextState.ForegroundColor = Color.WhiteSmoke;
            }

            var time = new TimeSpan(6, 0, 0);
            var incTime = new TimeSpan(0, 30, 0);
            for (int i = 0; i < 10; i++)
            {
                var dataRow = table.Rows.Add();
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
                time=time.Add(incTime);
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            }

            page.Paragraphs.Add(table);

            document.Save(System.IO.Path.Combine(_dataDir, "Complex.pdf"));

        }
    }
}
```

