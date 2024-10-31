---
title: Поиск и Извлечение Текста со Страниц PDF
linktitle: Поиск и Извлечение Текста
type: docs
weight: 60
url: /python-net/search-and-get-text-from-pdf/
description: Эта статья объясняет, как использовать различные инструменты для поиска и извлечения текста из Aspose.PDF для .NET.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Поиск и Извлечение Текста со Страниц PDF",
    "alternativeHeadline": "Инструменты для поиска и извлечения текста со страниц PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, python, поиск текста, извлечение текста из PDF",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда Документации Aspose.PDF",
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
    "url": "/python-net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "Эта статья объясняет, как использовать различные инструменты для поиска и извлечения текста из Aspose.PDF для .NET."
}
</script>


## Поиск и Получение Текста со Всех Страниц PDF Документа

Класс [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber) позволяет находить текст, соответствующий определенной фразе, на всех страницах PDF документа. Для поиска текста по всему документу необходимо вызвать метод Accept коллекции Pages. Метод [Accept](https://reference.aspose.com/pdf/python-net/aspose.pdf.page/accept/methods/3) принимает объект TextFragmentAbsorber в качестве параметра, который возвращает коллекцию объектов TextFragment. Вы можете пройтись по всем фрагментам и получить их свойства, такие как Text, Position (XIndent, YIndent), FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor и т.д.

Следующий фрагмент кода показывает, как осуществить поиск текста на всех страницах.

```csharp
// Для полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// Создать объект TextAbsorber для поиска всех экземпляров вводимой фразы
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// Применить абсорбер для всех страниц
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Получить извлеченные текстовые фрагменты
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Пройтись по фрагментам
foreach (TextFragment textFragment in textFragmentCollection)
{

    Console.WriteLine("Text : {0} ", textFragment.Text);
    Console.WriteLine("Position : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Font - Name : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Font - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Font - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Font - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Font Size : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Foreground Color : {0} ", textFragment.TextState.ForegroundColor);
}
```


В случае, если вам нужно искать текст на определенной странице PDF, укажите номер страницы из коллекции страниц экземпляра Document и вызовите метод Accept для этой страницы (как показано в строке кода ниже).

```csharp
// Для полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Примените абсорбер для конкретной страницы
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Поиск и получение текстовых сегментов со всех страниц PDF-документа

Для поиска текстовых сегментов со всех страниц, вам сначала нужно получить объекты TextFragment из документа.
 TextFragmentAbsorber позволяет находить текст, соответствующий определенной фразе, на всех страницах PDF-документа. Чтобы выполнить поиск текста во всем документе, необходимо вызвать метод Accept коллекции Pages. Метод Accept принимает объект TextFragmentAbsorber в качестве параметра, который возвращает коллекцию объектов TextFragment. Как только TextFragmentCollection извлекается из документа, необходимо пройтись по этой коллекции и получить TextSegmentCollection каждого объекта TextFragment. После этого можно получить все свойства отдельного объекта TextSegment. Следующий фрагмент кода показывает, как искать текстовые сегменты на всех страницах.

```csharp
// Для полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// Создать объект TextAbsorber для поиска всех вхождений искомой фразы
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figure");
// Принять абсорбер для всех страниц
pdfDocument.Pages.Accept(textFragmentAbsorber);
// Получить извлеченные фрагменты текста
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Перебрать фрагменты
foreach (TextFragment textFragment in textFragmentCollection)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        Console.WriteLine("Text : {0} ", textSegment.Text);
        Console.WriteLine("Position : {0} ", textSegment.Position);
        Console.WriteLine("XIndent : {0} ", textSegment.Position.XIndent);
        Console.WriteLine("YIndent : {0} ", textSegment.Position.YIndent);
        Console.WriteLine("Font - Name : {0}", textSegment.TextState.Font.FontName);
        Console.WriteLine("Font - IsAccessible : {0} ", textSegment.TextState.Font.IsAccessible);
        Console.WriteLine("Font - IsEmbedded : {0} ", textSegment.TextState.Font.IsEmbedded);
        Console.WriteLine("Font - IsSubset : {0} ", textSegment.TextState.Font.IsSubset);
        Console.WriteLine("Font Size : {0} ", textSegment.TextState.FontSize);
        Console.WriteLine("Foreground Color : {0} ", textSegment.TextState.ForegroundColor);
    }
}
```

Для поиска и получения TextSegments с определенной страницы PDF, вам нужно указать индекс этой страницы при вызове метода Accept(..). Пожалуйста, ознакомьтесь с приведенными ниже строками кода.

```csharp
// Для получения полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Применить абсорбер для всех страниц
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Поиск и получение текста со всех страниц с использованием регулярного выражения

TextFragmentAbsorber помогает вам искать и извлекать текст со всех страниц, используя регулярное выражение.
 Сначала вам нужно передать регулярное выражение в конструктор TextFragmentAbsorber в качестве фразы. После этого необходимо установить свойство TextSearchOptions объекта TextFragmentAbsorber. Это свойство требует объект TextSearchOptions, и вам нужно передать true в качестве параметра в его конструктор при создании новых объектов. Поскольку вы хотите извлечь совпадающий текст со всех страниц, вам нужно вызвать метод Accept коллекции Pages. TextFragmentAbsorber возвращает TextFragmentCollection, содержащий все фрагменты, соответствующие критериям, указанным в регулярном выражении. Следующий фрагмент кода показывает, как искать и получать текст со всех страниц на основе регулярного выражения.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// Создать объект TextAbsorber для поиска всех фраз, соответствующих регулярному выражению
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Например, 1999-2000

// Установить параметры поиска текста для указания использования регулярного выражения
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// Применить абсорбер для всех страниц
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Получить извлеченные текстовые фрагменты
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Перебрать фрагменты
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Текст : {0} ", textFragment.Text);
    Console.WriteLine("Позиция : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Шрифт - Имя : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Шрифт - Доступен : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Шрифт - Встроен : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Шрифт - Подмножество : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Размер шрифта : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Цвет переднего плана : {0} ", textFragment.TextState.ForegroundColor);
}
```

```csharp
// Для получения полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-.NET
TextFragmentAbsorber textFragmentAbsorber;
// Чтобы найти точное совпадение слова, вы можете рассмотреть возможность использования регулярного выражения.
textFragmentAbsorber = new TextFragmentAbsorber(@"\bWord\b", new TextSearchOptions(true));

// Чтобы искать строку в верхнем или нижнем регистре, вы можете рассмотреть возможность использования регулярного выражения.
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));

// Чтобы искать все строки (разбирать все строки) внутри PDF документа, пожалуйста, попробуйте использовать следующее регулярное выражение.
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// Найдите совпадение строки поиска и получите все после строки до разрыва строки.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)the ((.)*)");

// Пожалуйста, используйте следующее регулярное выражение, чтобы найти текст, следующий за совпадением регулярного выражения.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=word).*");

// Чтобы искать гиперссылки/URL внутри PDF документа, пожалуйста, попробуйте использовать следующее регулярное выражение.
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
```


## Поиск текста на основе Regex и добавление гиперссылки

Если вы хотите добавить гиперссылку к текстовой фразе на основе регулярного выражения, сначала найдите все фразы, соответствующие этому регулярному выражению, используя TextFragmentAbsorber, и добавьте гиперссылку к этим фразам.

Чтобы найти фразу и добавить гиперссылку:

1. Передайте регулярное выражение в качестве параметра конструктору TextFragmentAbsorber.
2. Создайте объект TextSearchOptions, который указывает, используется регулярное выражение или нет.
3. Получите совпадающие фразы в TextFragments.
4. Переберите совпадения, чтобы получить их прямоугольные размеры, измените цвет переднего плана на синий (опционально - чтобы он выглядел как гиперссылка) и создайте ссылку с помощью метода CreateWebLink(..) класса PdfContentEditor.
5. Сохраните обновленный PDF, используя метод Save объекта Document. Следующий фрагмент кода показывает, как искать текст внутри PDF-файла с использованием регулярного выражения и добавлять гиперссылки поверх совпадений.

```csharp
// Для получения полных примеров и файлов данных перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Создайте объект абсорбера для поиска всех экземпляров входной поисковой фразы
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// Включите поиск по регулярным выражениям
absorber.TextSearchOptions = new TextSearchOptions(true);
// Открыть документ
PdfContentEditor editor = new PdfContentEditor();
// Привязать исходный PDF файл
editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");
// Принять абсорбер для страницы
editor.Document.Pages[1].Accept(absorber);

int[] dashArray = { };
String[] LEArray = { };
System.Drawing.Color blue = System.Drawing.Color.Blue;

// Перебрать фрагменты
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle((int)textFragment.Rectangle.LLX,
        (int)Math.Round(textFragment.Rectangle.LLY), (int)Math.Round(textFragment.Rectangle.Width + 2),
        (int)Math.Round(textFragment.Rectangle.Height + 1));
    Enum[] actionName = new Enum[2] { Aspose.Pdf.Annotations.PredefinedAction.Document_AttachFile, Aspose.Pdf.Annotations.PredefinedAction.Document_ExtractPages };
    editor.CreateWebLink(rect, "http:// Www.aspose.com", 1, blue, actionName);
    editor.CreateLine(rect, "", (float)textFragment.Rectangle.LLX + 1, (float)textFragment.Rectangle.LLY - 1,
        (float)textFragment.Rectangle.URX, (float)textFragment.Rectangle.LLY - 1, 1, 1, blue, "S", dashArray, LEArray);
}

dataDir = dataDir + "SearchTextAndAddHyperlink_out.pdf";
editor.Save(dataDir);
editor.Close();
```


## Поиск и Рисование Прямоугольника вокруг каждого TextFragment

Aspose.PDF для .NET поддерживает функцию поиска и получения координат каждого символа или фрагментов текста. Чтобы быть уверенным в том, что координаты для каждого символа возвращаются правильно, мы можем выделить (добавив прямоугольник) вокруг каждого символа.

В случае абзаца текста, вы можете использовать некоторые регулярные выражения для определения разрыва абзаца и нарисовать прямоугольник вокруг него. Пожалуйста, обратите внимание на следующий фрагмент кода. Следующий фрагмент кода получает координаты каждого символа и создает прямоугольник вокруг каждого символа.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открытие документа
Document document = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// Создание объекта TextAbsorber для поиска всех фраз, соответствующих регулярному выражению

TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber(@"[\S]+");

TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textAbsorber.TextSearchOptions = textSearchOptions;

document.Pages.Accept(textAbsorber);

var editor = new PdfContentEditor(document);

foreach (TextFragment textFragment in textAbsorber.TextFragments)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        DrawBox(editor, textFragment.Page.Number, textSegment, System.Drawing.Color.Red);
    }

}
dataDir = dataDir + "SearchTextAndDrawRectangle_out.pdf";
document.Save(dataDir);
```


## Подсветка каждого символа в PDF документе

{{% alert color="primary" %}}

Вы можете попробовать поиск текста в документе с использованием Aspose.PDF и получить результаты онлайн по этой [ссылке](https://products.aspose.app/pdf/search)

{{% /alert %}}

Aspose.PDF для .NET поддерживает функцию поиска и получения координат каждого символа или текстовых фрагментов. Чтобы быть уверенным в координатах, возвращаемых для каждого символа, мы можем рассмотреть возможность подсветки (добавления прямоугольника) вокруг каждого символа. Следующий фрагмент кода получает координаты каждого символа и создает прямоугольник вокруг каждого символа.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

int resolution = 150;

Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "input.pdf");

using (MemoryStream ms = new MemoryStream())
{
    PdfConverter conv = new PdfConverter(pdfDocument);
    conv.Resolution = new Resolution(resolution, resolution);
    conv.GetNextImage(ms, System.Drawing.Imaging.ImageFormat.Png);

    Bitmap bmp = (Bitmap)Bitmap.FromStream(ms);

    using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
    {
        float scale = resolution / 72f;
        gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

        for (int i = 0; i < pdfDocument.Pages.Count; i++)
        {
Page page = pdfDocument.Pages[1];
// Создать объект TextAbsorber для поиска всех слов
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
page.Accept(textFragmentAbsorber);
// Получить извлеченные текстовые фрагменты
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Перебрать фрагменты
foreach (TextFragment textFragment in textFragmentCollection)
{
    if (i == 0)
    {
        gr.DrawRectangle(
        Pens.Yellow,
        (float)textFragment.Position.XIndent,
        (float)textFragment.Position.YIndent,
        (float)textFragment.Rectangle.Width,
        (float)textFragment.Rectangle.Height);

        for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
        {
TextSegment segment = textFragment.Segments[segNum];

for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
{
    CharInfo characterInfo = segment.Characters[charNum];

    Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
    Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
          "   TextFragment URY = " + textFragment.Rectangle.URY);

    gr.DrawRectangle(
    Pens.Black,
    (float)characterInfo.Rectangle.LLX,
    (float)characterInfo.Rectangle.LLY,
    (float)characterInfo.Rectangle.Width,
    (float)characterInfo.Rectangle.Height);
}

gr.DrawRectangle(
Pens.Green,
(float)segment.Rectangle.LLX,
(float)segment.Rectangle.LLY,
(float)segment.Rectangle.Width,
(float)segment.Rectangle.Height);
        }
    }
}
        }
    }
    dataDir = dataDir + "HighlightCharacterInPDF_out.png";
    bmp.Save(dataDir, System.Drawing.Imaging.ImageFormat.Png);
}
```


## Добавление и Поиск Скрытого Текста

Иногда мы хотим добавить скрытый текст в PDF-документ, а затем найти скрытый текст и использовать его позицию для постобработки. Для вашего удобства Aspose.PDF for .NET предоставляет эти возможности. Вы можете добавить скрытый текст во время генерации документа. Также вы можете найти скрытый текст, используя TextFragmentAbsorber. Чтобы добавить скрытый текст, установите TextState.Invisible в ‘true’ для добавленного текста. TextFragmentAbsorber находит весь текст, который соответствует шаблону (если указан). Это поведение по умолчанию, которое нельзя изменить. Чтобы проверить, действительно ли найденный текст невидим, можно использовать свойство TextState.Invisible. Пример кода ниже показывает, как использовать эту функцию.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

//Создать документ со скрытым текстом
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("Это обычный текст.");
TextFragment frag2 = new TextFragment("Это невидимый текст.");

//Установить свойство текста - невидимый
frag2.TextState.Invisible = true;

page.Paragraphs.Add(frag1);
page.Paragraphs.Add(frag2);
doc.Save(dataDir + "39400_out.pdf");
doc.Dispose();

//Поиск текста в документе
doc = new Aspose.Pdf.Document(dataDir + "39400_out.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.Visit(doc.Pages[1]);

foreach (TextFragment fragment in absorber.TextFragments)
{
    //Сделать что-то с фрагментами
    Console.WriteLine("Текст '{0}' на позиции {1} невидимость: {2} ",
    fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
}
doc.Dispose();
```


## Поиск текста с помощью .NET Regex

Aspose.PDF для .NET предоставляет возможность поиска документов с использованием стандартного параметра .NET Regex. Для этой цели можно использовать TextFragmentAbsorber, как показано в приведенном ниже примере кода.

```csharp
// Для полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Создать объект Regex для поиска всех слов
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// Открыть документ
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// Получить конкретную страницу
Page page = document.Pages[1];

// Создать объект TextAbsorber для поиска всех вхождений входного regex
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(regex);
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

// Применить абсорбер для страницы
page.Accept(textFragmentAbsorber);

// Получить извлеченные текстовые фрагменты
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Перебрать фрагменты
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine(textFragment.Text);
}
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для .NET Library",
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