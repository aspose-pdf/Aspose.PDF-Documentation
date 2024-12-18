---
title: Форматирование текста в PDF с использованием Python
linktitle: Форматирование текста в PDF
type: docs
weight: 30
url: /ru/python-net/text-formatting-inside-pdf/
description: Эта страница объясняет, как форматировать текст в вашем PDF файле. Есть добавление отступа строки, добавление границы текста, добавление подчеркивания текста и т.д.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Форматирование текста в PDF с использованием Python",
    "alternativeHeadline": "Как форматировать текст в PDF файле",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация pdf документов",
    "keywords": "pdf, python, форматирование текста в pdf",
    "wordcount": "302",
    "proficiencyLevel":"Начальный",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-formatting-inside-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "Эта страница объясняет, как форматировать текст в вашем PDF файле. Есть добавление отступа строки, добавление границы текста, добавление подчеркивания текста и т.д."
}
</script>


## Как добавить отступ строки в PDF

Aspose.PDF для .NET предлагает свойство SubsequentLinesIndent в классе [TextFormattingOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textformattingoptions). Оно может быть использовано для указания отступа строки в сценариях генерации PDF с использованием TextFragment и коллекции Paragraphs.

Пожалуйста, используйте следующий фрагмент кода, чтобы использовать это свойство:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Создать новый объект документа
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

string textFragment = string.Concat(Enumerable.Repeat("Быстрая коричневая лиса перепрыгнула через ленивую собаку. ", 10));

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

// Инициализировать TextFormattingOptions для текстового фрагмента и указать значение SubsequentLinesIndent
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


## Как добавить границу текста

Следующий фрагмент кода показывает, как добавить границу к тексту, используя TextBuilder и устанавливая свойство DrawTextRectangleBorder в TextState:

```csharp
// Для полноценных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Создать новый объект документа
Document pdfDocument = new Document();
// Получить конкретную страницу
Page pdfPage = (Page)pdfDocument.Pages.Add();
// Создать текстовый фрагмент
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);
// Установить свойства текста
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// Установить свойство StrokingColor для рисования границы (обводки) вокруг прямоугольника текста
textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
// Установить значение свойства DrawTextRectangleBorder в true
textFragment.TextState.DrawTextRectangleBorder = true;
TextBuilder tb = new TextBuilder(pdfPage);
tb.AppendText(textFragment);
// Сохранить документ
pdfDocument.Save(dataDir + "PDFWithTextBorder_out.pdf");
```


## Как добавить подчеркнутый текст

Следующий фрагмент кода показывает, как добавить подчеркнутый текст при создании нового PDF файла.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Создать объект документа
Document pdfDocument = new Document();
// Добавить страницу в PDF документ
pdfDocument.Pages.Add();
// Создать TextBuilder для первой страницы
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// TextFragment с примером текста
TextFragment fragment = new TextFragment("Тестовое сообщение");
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

// Сохранить полученный PDF документ.
pdfDocument.Save(dataDir);
```


## Как добавить границу вокруг добавленного текста

Вы можете контролировать внешний вид добавляемого текста. Пример ниже показывает, как добавить границу вокруг текста, нарисовав прямоугольник вокруг него. Узнайте больше о классе [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

PdfContentEditor editor = new PdfContentEditor();
editor.BindPdf(dataDir + "input.pdf");
LineInfo lineInfo = new LineInfo();
lineInfo.LineWidth = 2;
lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
lineInfo.Visibility = true;
editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

dataDir = dataDir + "AddingBorderAroundAddedText_out.pdf";

// Сохранить итоговый PDF документ.
editor.Save(dataDir);
```

## Как добавить перевод строки

TextFragment не поддерживает перевод строки внутри текста. Однако, чтобы добавить текст с переводом строки, пожалуйста, используйте TextFragment с TextParagraph:

- используйте "\r\n" или Environment.NewLine в TextFragment вместо одиночного "\n";
- создайте объект TextParagraph. Он добавит текст с разбиением на строки;
- добавьте TextFragment с помощью TextParagraph.AppendLine;
- добавьте TextParagraph с помощью TextBuilder.AppendParagraph.
Пожалуйста, используйте приведенный ниже фрагмент кода.

```csharp
// Для получения полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Инициализируйте новый TextFragment с текстом, содержащим необходимые маркеры новой строки
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

// Настройте свойства текстового фрагмента, если необходимо
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Создайте объект TextParagraph
TextParagraph par = new TextParagraph();

// Добавьте новый TextFragment в параграф
par.AppendLine(textFragment);

// Установите позицию параграфа
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Создайте объект TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Добавьте TextParagraph, используя TextBuilder
textBuilder.AppendParagraph(par);

dataDir = dataDir + "AddNewLineFeed_out.pdf";

// Сохраните получившийся PDF-документ.
pdfApplicationDoc.Save(dataDir);
```


## Как добавить зачеркнутый текст

Класс TextState предоставляет возможности для установки форматирования для TextFragments, которые размещаются внутри PDF-документа. Вы можете использовать этот класс для установки форматирования текста как Жирный, Курсив, Подчеркнутый, и начиная с этого выпуска, API предоставляет возможности для пометки форматирования текста как Зачеркнутый. Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы добавить TextFragment с форматированием зачеркнутого текста.

Пожалуйста, используйте полный фрагмент кода:

```csharp
// Для полноценных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Открыть документ
Document pdfDocument = new Document();
// Получить конкретную страницу
Page pdfPage = (Page)pdfDocument.Pages.Add();

// Создать текстовый фрагмент
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);

// Установить свойства текста
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// Установить свойство зачеркнутого текста
textFragment.TextState.StrikeOut = true;
// Пометить текст как жирный
textFragment.TextState.FontStyle = FontStyles.Bold;

// Создать объект TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);
// Добавить текстовый фрагмент на страницу PDF
textBuilder.AppendText(textFragment);


dataDir = dataDir + "AddStrikeOutText_out.pdf";

// Сохранить результирующий PDF-документ.
pdfDocument.Save(dataDir);
```


## Применение градиентной заливки к тексту

Форматирование текста было дополнительно улучшено в API для сценариев редактирования текста, и теперь вы можете добавлять текст с цветовым пространством шаблона внутри PDF-документа. Класс Aspose.Pdf.Color был дополнительно улучшен путем введения нового свойства PatternColorSpace, которое можно использовать для задания оттенков цвета для текста. Это новое свойство добавляет различные градиентные заливки к тексту, например осевую заливку, радиальную (Тип 3) заливку, как показано в следующем фрагменте кода:

```csharp
// Для полноценных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

using (Document pdfDocument = new Document(dataDir + "text_sample4.pdf"))
{
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("Lorem ipsum");
    pdfDocument.Pages.Accept(absorber);

    TextFragment textFragment = absorber.TextFragments[1];

    // Создать новый цвет с цветовым пространством шаблона
    textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
    {
        PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Color.Red, Color.Blue)
    };
    textFragment.TextState.Underline = true;

    pdfDocument.Save(dataDir + "text_out.pdf");
}
```


>Чтобы применить радиальный градиент, вы можете установить свойство ‘PatternColorSpace’ равным ‘Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)’ в приведенном выше фрагменте кода.

## Как выровнять текст относительно содержимого плавающего элемента

Aspose.PDF поддерживает установку выравнивания текста для содержимого внутри элемента Floating Box. Свойства выравнивания экземпляра Aspose.Pdf.FloatingBox могут быть использованы для достижения этого, как показано в следующем примере кода.

```csharp
// Для получения полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
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
    "name": "Библиотека Aspose.PDF для .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
                "areaServed": "США",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF для .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>