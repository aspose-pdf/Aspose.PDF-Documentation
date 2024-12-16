---
title: Форматирование текста внутри PDF с использованием C#
linktitle: Форматирование текста внутри PDF
type: docs
weight: 30
url: /ru/net/text-formatting-inside-pdf/
description: Эта страница объясняет, как форматировать текст внутри вашего файла PDF. Здесь рассмотрены добавление отступа строки, добавление границы текста, добавление подчеркивания текста и т.д.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Форматирование текста внутри PDF с использованием C#",
    "alternativeHeadline": "Как форматировать текст в файле PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, форматирование текста в pdf",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-formatting-inside-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта страница объясняет, как форматировать текст внутри вашего файла PDF. Здесь рассмотрены добавление отступа строки, добавление границы текста, добавление подчеркивания текста и т.д."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Как добавить отступ в PDF

Aspose.PDF для .NET предлагает свойство SubsequentLinesIndent в классе [TextFormattingOptions](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions). Оно может быть использовано для указания отступа строк при генерации PDF с использованием TextFragment и коллекции Paragraphs.

Пожалуйста, используйте следующий фрагмент кода для использования свойства:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Создать новый объект документа
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

string textFragment = string.Concat(Enumerable.Repeat("Быстрая коричневая лиса перепрыгнула через ленивого пса. ", 10));

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

// Инициализируйте TextFormattingOptions для фрагмента текста и укажите значение SubsequentLinesIndent
text.TextState.FormattingOptions = new Aspose.Pdf.Text.TextFormattingOptions()
{
    SubsequentLinesIndent = 20
};

page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Строка2");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Строка3");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Строка4");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Строка5");
page.Paragraphs.Add(text);

document.Save(dataDir + "SubsequentIndent_out.pdf");
```
## Как добавить границу к тексту

Следующий фрагмент кода показывает, как добавить границу к тексту с использованием TextBuilder и установкой свойства DrawTextRectangleBorder объекта TextState:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Создание нового объекта документа
Document pdfDocument = new Document();
// Получение конкретной страницы
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Создание текстового фрагмента
TextFragment textFragment = new TextFragment("основной текст");
textFragment.Position = new Position(100, 600);
// Установка свойств текста
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// Установка свойства StrokingColor для рисования границы (обводки) вокруг текстового прямоугольника
textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
// Установка значения свойства DrawTextRectangleBorder в true
textFragment.TextState.DrawTextRectangleBorder = true;
TextBuilder tb = new TextBuilder(pdfPage);
tb.AppendText(textFragment);
// Сохранение документа
pdfDocument.Save(dataDir + "PDFWithTextBorder_out.pdf");
```
## Как добавить подчеркнутый текст

Следующий фрагмент кода показывает, как добавить подчеркнутый текст при создании нового файла PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Создать объект документации
Document pdfDocument = new Document();
// Добавить страницу в PDF документ
pdfDocument.Pages.Add();
// Создать TextBuilder для первой страницы
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// TextFragment с примером текста
TextFragment fragment = new TextFragment("Test message");
// Установить шрифт для TextFragment
fragment.TextState.Font = FontRepository.FindFont("Arial");
fragment.TextState.FontSize = 10;
// Установить форматирование текста как подчеркнутый
fragment.TextState.Underline = true;
// Указать позицию, где нужно разместить TextFragment
fragment.Position = new Position(10, 800);
// Добавить TextFragment в PDF файл
tb.AppendText(fragment);

dataDir = dataDir + "AddUnderlineText_out.pdf";

// Сохранить результат в PDF документ.
pdfDocument.Save(dataDir);
```
## Как добавить рамку вокруг добавленного текста

У вас есть контроль над внешним видом добавляемого текста. Пример ниже показывает, как добавить рамку вокруг текста, нарисовав вокруг него прямоугольник. Узнайте больше о классе [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

PdfContentEditor editor = new PdfContentEditor();
editor.BindPdf(dataDir + "input.pdf");
LineInfo lineInfo = new LineInfo();
lineInfo.LineWidth = 2;
lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
lineInfo.Visibility = true;
editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

dataDir = dataDir + "AddingBorderAroundAddedText_out.pdf";

// Сохранить результат в PDF документ.
editor.Save(dataDir);
```

## Как добавить перевод строки
## Как добавить перевод строки

TextFragment не поддерживает перевод строки внутри текста. Однако для добавления текста с переводом строки используйте TextFragment с TextParagraph:

- используйте "\r\n" или Environment.NewLine в TextFragment вместо одиночного "\n";
- создайте объект TextParagraph. Он добавит текст с разделением строк;
- добавьте TextFragment с TextParagraph.AppendLine;
- добавьте TextParagraph с TextBuilder.AppendParagraph.
Пожалуйста, используйте приведенный ниже фрагмент кода.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Инициализируйте новый TextFragment с текстом, содержащим необходимые маркеры новой строки
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Имя заявителя: " + Environment.NewLine + " Джо Смо");

// Установите свойства фрагмента текста, если это необходимо
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Создайте объект TextParagraph
TextParagraph par = new TextParagraph();

// Добавьте новый TextFragment в абзац
par.AppendLine(textFragment);

// Установите позицию абзаца
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Создайте объект TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Добавьте TextParagraph с помощью TextBuilder
textBuilder.AppendParagraph(par);


dataDir = dataDir + "AddNewLineFeed_out.pdf";

// Сохраните результатирующий PDF-документ.
pdfApplicationDoc.Save(dataDir);
```
## Как добавить текст с зачеркиванием

Класс TextState предоставляет возможности для установки форматирования для TextFragments, размещаемых внутри PDF-документа. Вы можете использовать этот класс для установки форматирования текста, такого как Жирный, Курсив, Подчеркнутый и начиная с этого выпуска, API предоставило возможности отмечать форматирование текста как Зачеркнутый. Пожалуйста, попробуйте использовать следующий фрагмент кода для добавления TextFragment с форматированием зачеркивания.

Пожалуйста, используйте полный фрагмент кода:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Открыть документ
Document pdfDocument = new Document();
// Получить конкретную страницу
Page pdfPage = (Page)pdfDocument.Pages.Add();

// Создать фрагмент текста
TextFragment textFragment = new TextFragment("основной текст");
textFragment.Position = new Position(100, 600);

// Установить свойства текста
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// Установить свойство StrikeOut
textFragment.TextState.StrikeOut = true;
// Отметить текст как Жирный
textFragment.TextState.FontStyle = FontStyles.Bold;

// Создать объект TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Добавить фрагмент текста на страницу PDF
textBuilder.AppendText(textFragment);


dataDir = dataDir + "AddStrikeOutText_out.pdf";

// Сохранить результирующий PDF-документ.
pdfDocument.Save(dataDir);
```
## Применение градиентной заливки к тексту

Форматирование текста было дополнительно улучшено в API для сценариев редактирования текста, и теперь вы можете добавлять текст с цветовым пространством узора внутри PDF-документа. Класс Aspose.Pdf.Color был дополнительно усовершенствован за счет введения нового свойства PatternColorSpace, которое можно использовать для указания цветов затенения для текста. Это новое свойство добавляет различные градиентные затенения к тексту, например, осевое затенение, радиальное (тип 3) затенение, как показано в следующем фрагменте кода:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

using (Document pdfDocument = new Document(dataDir + "text_sample4.pdf"))
{
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("Lorem ipsum");
    pdfDocument.Pages.Accept(absorber);

    TextFragment textFragment = absorber.TextFragments[1];

    // Создание нового цвета с цветовым пространством узора
    textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
    {
        PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Color.Red, Color.Blue)
    };
    textFragment.TextState.Underline = true;

    pdfDocument.Save(dataDir + "text_out.pdf");
}
```
>Чтобы применить радиальный градиент, вы можете установить свойство 'PatternColorSpace' равным 'Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)' в приведенном выше фрагменте кода.

## Как выровнять текст, чтобы он соответствовал плавающему содержимому

Aspose.PDF поддерживает настройку выравнивания текста для содержимого внутри элемента Floating Box. Свойства выравнивания экземпляра Aspose.Pdf.FloatingBox могут быть использованы для этого, как показано в следующем примере кода.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document doc = new Document();
doc.Pages.Add();

Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox(100, 100);
floatBox.VerticalAlignment = VerticalAlignment.Bottom;
floatBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox.Paragraphs.Add(new TextFragment("FloatingBox_bottom"));
floatBox.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox);

Aspose.Pdf.FloatingBox floatBox1 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox1.VerticalAlignment = VerticalAlignment.Center;
floatBox1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox1.Paragraphs.Add(new TextFragment("FloatingBox_center"));
floatBox1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox1);

Aspose.Pdf.FloatingBox floatBox2 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox2.VerticalAlignment = VerticalAlignment.Top;
floatBox2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox2.Paragraphs.Add(new TextFragment("FloatingBox_top"));
floatBox2.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox2);

doc.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "продажи",
                "areaServed": "US",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для манипуляции PDF для .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

