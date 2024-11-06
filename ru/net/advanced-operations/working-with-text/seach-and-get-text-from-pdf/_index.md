---
title: Поиск и извлечение текста со страниц PDF
linktitle: Поиск и извлечение текста
type: docs
weight: 60
url: ru/net/search-and-get-text-from-pdf/
description: Эта статья объясняет, как использовать различные инструменты для поиска и извлечения текста из Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Поиск и извлечение текста со страниц PDF",
    "alternativeHeadline": "Инструменты для поиска и извлечения текста со страниц PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, поиск текста, извлечение текста из pdf",
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
                "contactType": "продажи",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта статья объясняет, как использовать различные инструменты для поиска и извлечения текста из Aspose.PDF для .NET."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Поиск и получение текста со всех страниц PDF документа

Класс [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) позволяет вам находить текст, соответствующий определенной фразе, со всех страниц PDF документа. Для поиска текста по всему документу, вам необходимо вызвать метод Accept коллекции Pages. Метод [Accept](https://reference.aspose.com/pdf/net/aspose.pdf.page/accept/methods/3) принимает объект TextFragmentAbsorber в качестве параметра, который возвращает коллекцию объектов TextFragment. Вы можете пройтись по всем фрагментам и получить их свойства, такие как Текст, Позиция (XIndent, YIndent), FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor и т.д.

Следующий фрагмент кода показывает, как искать текст со всех страниц.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// Создать объект TextAbsorber для поиска всех экземпляров вводимой поисковой фразы
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// Принять absorber для всех страниц
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Получить извлеченные текстовые фрагменты
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Пройтись по фрагментам
foreach (TextFragment textFragment in textFragmentCollection)
{

    Console.WriteLine("Текст : {0} ", textFragment.Text);
    Console.WriteLine("Позиция : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Шрифт - Название : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Шрифт - Доступен : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Шрифт - Встроен : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Шрифт - Подмножество : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Размер шрифта : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Цвет переднего плана : {0} ", textFragment.TextState.ForegroundColor);
}
```
Если вам нужно искать текст на конкретной странице PDF, укажите номер страницы из коллекции страниц экземпляра Document и вызовите метод Accept для этой страницы (как показано в строке кода ниже).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Применить поглотитель для конкретной страницы
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Поиск и получение текстовых сегментов со всех страниц PDF-документа

Для того чтобы искать текстовые сегменты на всех страницах, вам сначала нужно получить объекты TextFragment из документа.
Для поиска текстовых сегментов со всех страниц сначала необходимо получить объекты TextFragment из документа.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// Создать объект TextAbsorber для поиска всех вхождений искомой фразы
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figure");
// Применить absorber ко всем страницам
pdfDocument.Pages.Accept(textFragmentAbsorber);
// Получить извлеченные текстовые фрагменты
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Пройтись по фрагментам
foreach (TextFragment textFragment in textFragmentCollection)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        Console.WriteLine("Текст : {0} ", textSegment.Text);
        Console.WriteLine("Позиция : {0} ", textSegment.Position);
        Console.WriteLine("XIndent : {0} ", textSegment.Position.XIndent);
        Console.WriteLine("YIndent : {0} ", textSegment.Position.YIndent);
        Console.WriteLine("Шрифт - Название : {0}", textSegment.TextState.Font.FontName);
        Console.WriteLine("Шрифт - Доступен : {0} ", textSegment.TextState.Font.IsAccessible);
        Console.WriteLine("Шрифт - Встроен : {0} ", textSegment.TextState.Font.IsEmbedded);
        Console.WriteLine("Шрифт - Подмножество : {0} ", textSegment.TextState.Font.IsSubset);
        Console.WriteLine("Размер шрифта : {0} ", textSegment.TextState.FontSize);
        Console.WriteLine("Цвет переднего плана : {0} ", textSegment.TextState.ForegroundColor);
    }
}
```
Для поиска и получения TextSegments с определенной страницы PDF, вам необходимо указать индекс нужной страницы при вызове метода Accept(..). Пожалуйста, ознакомьтесь со следующими строками кода.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Применить абсорбер ко всем страницам
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## Поиск и получение текста со всех страниц с использованием регулярных выражений

TextFragmentAbsorber помогает вам искать и извлекать текст со всех страниц на основе регулярного выражения.
TextFragmentAbsorber помогает вам искать и извлекать текст со всех страниц на основе регулярного выражения.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// Создать объект TextAbsorber для поиска всех фраз, соответствующих регулярному выражению
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Например, 1999-2000

// Установить опции поиска текста для указания использования регулярного выражения
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// Применить absorber ко всем страницам
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Получить извлеченные текстовые фрагменты
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Перебор фрагментов
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Текст : {0} ", textFragment.Text);
    Console.WriteLine("Позиция : {0} ", textFragment.Position);
    Console.WriteLine("Смещение по X : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("Смещение по Y : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Шрифт - Название : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Шрифт - Доступен : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Шрифт - Встроен : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Шрифт - Часть : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Размер шрифта : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Цвет переднего плана : {0} ", textFragment.TextState.ForegroundColor);
}
```
```csharp
// Для полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-.NET
TextFragmentAbsorber textFragmentAbsorber;
// Чтобы найти точное совпадение слова, вы можете использовать регулярное выражение.
textFragmentAbsorber = new TextFragmentAbsorber(@"\bWord\b", new TextSearchOptions(true));

// Чтобы искать строку в верхнем или нижнем регистре, вы можете использовать регулярное выражение.
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));

// Чтобы искать все строки (анализировать все строки) внутри PDF-документа, пожалуйста, используйте следующее регулярное выражение.
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// Найти совпадение поисковой строки и получить все после строки до переноса строки.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)the ((.)*)");

// Пожалуйста, используйте следующее регулярное выражение, чтобы найти текст после совпадения с регулярным выражением.
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=word).*");

// Чтобы искать гиперссылки/URL внутри PDF-документа, пожалуйста, используйте следующее регулярное выражение.
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
```
## Поиск текста по регулярному выражению и добавление гиперссылки

Если вы хотите добавить гиперссылку на текстовую фразу на основе регулярного выражения, сначала найдите все фразы, соответствующие этому регулярному выражению, используя TextFragmentAbsorber, и добавьте гиперссылку на эти фразы.

Чтобы найти фразу и добавить на неё гиперссылку:

1. Передайте регулярное выражение в качестве параметра конструктору TextFragmentAbsorber.
2. Создайте объект TextSearchOptions, который указывает, используется ли регулярное выражение.
3. Получите соответствующие фразы в TextFragments.
4. Пройдитесь по совпадениям, чтобы получить их прямоугольные размеры, измените цвет переднего плана на синий (необязательно - чтобы создать впечатление гиперссылки) и создайте ссылку с использованием метода CreateWebLink(..) класса PdfContentEditor.
5. Сохраните обновлённый PDF с помощью метода Save объекта Document.
Следующий фрагмент кода показывает, как искать текст в PDF-файле с использованием регулярного выражения и добавлять гиперссылки на совпадения.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Создайте объект absorber для поиска всех вхождений искомой фразы
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// Включите поиск по регулярному выражению
absorber.TextSearchOptions = new TextSearchOptions(true);
// Откройте документ
PdfContentEditor editor = new PdfContentEditor();
// Привяжите исходный PDF-файл
editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");
// Примените absorber к странице
editor.Document.Pages[1].Accept(absorber);

int[] dashArray = { };
String[] LEArray = { };
System.Drawing.Color blue = System.Drawing.Color.Blue;

// Пройдитесь по фрагментам
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle((int)textFragment.Rectangle.LLX,
        (int)Math.Round(textFragment.Rectangle.LLY), (int)Math.Round(textFragment.Rectangle.Width + 2),
        (int)Math.Round(textFragment.Rectangle.Height + 1));
    Enum[] actionName = new Enum[2] { Aspose.Pdf.Annotations.PredefinedAction.Document_AttachFile, Aspose.Pdf.Annotations.PredefinedAction.Document_ExtractPages };
    editor.CreateWebLink(rect, "http://www.aspose.com", 1, blue, actionName);
    editor.CreateLine(rect, "", (float)textFragment.Rectangle.LLX + 1, (float)textFragment.Rectangle.LLY - 1,
        (float)textFragment.Rectangle.URX, (float)textFragment.Rectangle.LLY - 1, 1, 1, blue, "S", dashArray, LEArray);
}

dataDir = dataDir + "SearchTextAndAddHyperlink_out.pdf";
editor.Save(dataDir);
editor.Close();
```
## Поиск и рисование прямоугольника вокруг каждого фрагмента текста

Aspose.PDF для .NET поддерживает функцию поиска и получения координат каждого символа или текстовых фрагментов. Поэтому, чтобы быть уверенным в возвращаемых координатах для каждого символа, мы можем рассмотреть возможность выделения (добавления прямоугольника) вокруг каждого символа.

В случае текстового абзаца вы можете использовать некоторое регулярное выражение для определения разрыва абзаца и рисования вокруг него прямоугольника. Пожалуйста, посмотрите следующий фрагмент кода. Данный фрагмент кода получает координаты каждого символа и создает вокруг каждого символа прямоугольник.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document document = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// Создать объект TextAbsorber для поиска всех фраз, соответствующих регулярному выражению

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
## Выделите каждый символ в документе PDF

{{% alert color="primary" %}}

Вы можете попробовать поискать текст в документе с помощью Aspose.PDF и получить результаты онлайн по этой [ссылке](https://products.aspose.app/pdf/search)

{{% /alert %}}

Aspose.PDF для .NET поддерживает функцию поиска и получения координат каждого символа или фрагментов текста. Таким образом, для того чтобы быть уверенным в возвращаемых координатах каждого символа, мы можем рассмотреть возможность выделения (добавления прямоугольника) вокруг каждого символа. Следующий фрагмент кода получает координаты каждого символа и создает вокруг каждого символа прямоугольник.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
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
// Создаем объект TextAbsorber для поиска всех слов
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
page.Accept(textFragmentAbsorber);
// Получаем извлеченные фрагменты текста
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// Проходим через фрагменты
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
## Добавление и поиск скрытого текста

Иногда мы хотим добавить скрытый текст в документ PDF, а затем искать скрытый текст и использовать его позицию для последующей обработки. Для вашего удобства Aspose.PDF для .NET предоставляет эти возможности. Вы можете добавлять скрытый текст во время генерации документа. Также вы можете найти скрытый текст с помощью TextFragmentAbsorber. Чтобы добавить скрытый текст, установите TextState.Invisible в значение ‘true’ для добавленного текста. TextFragmentAbsorber находит весь текст, который соответствует шаблону (если он указан). Это поведение по умолчанию, которое не может быть изменено. Чтобы проверить, действительно ли найденный текст невидим, можно использовать свойство TextState.Invisible. Приведенный ниже фрагмент кода показывает, как использовать эту функцию.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

//Создание документа со скрытым текстом
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("Это обычный текст.");
TextFragment frag2 = new TextFragment("Это невидимый текст.");

//Установка свойства текста - невидимый
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
    //Что-то делаем с фрагментами
    Console.WriteLine("Текст '{0}' на позиции {1} невидимость: {2} ",
    fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
}
doc.Dispose();
```
## Поиск текста с использованием .NET Regex

Aspose.PDF для .NET предоставляет возможность поиска документов с использованием стандартной опции .NET Regex. Для этой цели может быть использован TextFragmentAbsorber, как показано в примере кода ниже.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Создайте объект Regex для поиска всех слов
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// Откройте документ
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// Получите конкретную страницу
Page page = document.Pages[1];

// Создайте объект TextAbsorber для поиска всех вхождений введенного regex
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(regex);
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

// Примените absorber к странице
page.Accept(textFragmentAbsorber);

// Получите извлеченные текстовые фрагменты
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Пройдитесь по фрагментам
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine(textFragment.Text);
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для библиотеки .NET",
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
                "areaServed": "США",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для манипулирования PDF для .NET",
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

