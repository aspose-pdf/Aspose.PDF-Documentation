---
title: Поиск и получение текста со страниц PDF
linktitle: Поиск и получение текста
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ru/net/search-and-get-text-from-pdf/
description: Узнайте, как искать и извлекать текст из PDF-файла в .NET с использованием Aspose.PDF для анализа и извлечения текста.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Search and Get Text from Pages of PDF",
    "alternativeHeadline": "Search and Extract Text from PDF Pages",
    "abstract": "Aspose.PDF for .NET позволяет пользователям эффективно искать и извлекать текст со всех страниц PDF-документа. Эта функциональность использует класс TextFragmentAbsorber для поиска заданных фраз или текстовых сегментов, а также предоставляет расширенную поддержку регулярных выражений, что позволяет точно извлекать и манипулировать текстом. Идеально подходит для разработчиков, эта функция улучшает возможности работы с PDF-документами, упрощая процессы извлечения текста.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2762",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2024-11-26",
    "description": "В этой статье объясняется, как использовать различные инструменты для поиска и получения текста из Aspose.PDF for .NET."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Поиск и получение текста со всех страниц PDF-документа

Класс [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber) позволяет находить текст, соответствующий определенной фразе, со всех страниц PDF-документа. Чтобы искать текст по всему документу, необходимо вызвать метод Accept коллекции Pages. Метод [Accept](https://reference.aspose.com/pdf/net/aspose.pdf.page/accept/methods/3) принимает объект TextFragmentAbsorber в качестве параметра, который возвращает коллекцию объектов TextFragment. Вы можете пройтись по всем фрагментам и получить их свойства, такие как Text, Position (XIndent, YIndent), FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor и т.д.

Следующий фрагмент кода показывает, как искать текст со всех страниц.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
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
    }
}
```

В случае, если вам нужно искать текст внутри конкретной страницы PDF, укажите номер страницы из коллекции страниц экземпляра Document и вызовите метод Accept для этой страницы (как показано в строке кода ниже).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for a particular page
        document.Pages[2].Accept(textFragmentAbsorber);
    }
}
```

### Поиск по списку фраз в TextFragmentAbsorber

Библиотека C# может передавать только одну фразу в TextFragmentAbsorber, но начиная с релиза 24.2 Aspose.PDF, был реализован новый алгоритм для поиска по списку.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // Create resular expressions
    var regexes = new Regex[]
    {
        new Regex(@"(?s)document\s+(?:(?:no\(?s?\)?\.?)|(?:number(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|and)*)", RegexOptions.IgnoreCase),
        new Regex(@"[\s\r\n]+Tract[\s\r\n]+of:? ", RegexOptions.IgnoreCase),
        new Regex(@"vested[\s\r\n]+in", RegexOptions.IgnoreCase),
        new Regex("Vested in:", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+(?:nos?|numbers?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
    };

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(regexes, new Aspose.Pdf.Text.TextSearchOptions(true));
        document.Pages.Accept(absorber);
        // Get result
        var result = absorber.RegexResults;
    }
}
```

Фрагмент кода ищет конкретные шаблоны, такие как номера документов, ключевые слова и номера файлов в PDF-документе с использованием регулярных выражений. Он загружает PDF, применяет поиск и извлекает совпадающие результаты для дальнейшей обработки.

## Поиск и получение текстовых сегментов со всех страниц PDF-документа

Чтобы искать текстовые сегменты со всех страниц, сначала необходимо получить объекты TextFragment из документа. TextFragmentAbsorber позволяет находить текст, соответствующий определенной фразе, со всех страниц PDF-документа. Чтобы искать текст по всему документу, необходимо вызвать метод Accept коллекции Pages. Метод Accept принимает объект TextFragmentAbsorber в качестве параметра, который возвращает коллекцию объектов TextFragment. После того как коллекция TextFragmentCollection будет получена из документа, вам нужно пройтись по этой коллекции и получить TextSegmentCollection каждого объекта TextFragment. После этого вы можете получить все свойства отдельного объекта TextSegment. Следующий фрагмент кода показывает, как искать текстовые сегменты со всех страниц.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextPage.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Figure");

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            foreach (var textSegment in textFragment.Segments)
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
    }
}
```

Чтобы искать и получать TextSegments с конкретной страницы PDF, вам нужно указать конкретный индекс страницы при вызове метода Accept(..). Пожалуйста, посмотрите на следующие строки кода.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("text");

        // Accept the absorber for a particular page
        document.Pages[2].Accept(textFragmentAbsorber);
    }
}
```

## Поиск и получение текста со всех страниц с использованием регулярного выражения

TextFragmentAbsorber помогает вам искать и извлекать текст со всех страниц на основе регулярного выражения. Сначала вам нужно передать регулярное выражение в конструктор TextFragmentAbsorber в качестве фразы. После этого вы должны установить свойство TextSearchOptions объекта TextFragmentAbsorber. Это свойство требует объект TextSearchOptions, и вам нужно передать true в качестве параметра его конструктора при создании новых объектов. Поскольку вы хотите извлечь совпадающий текст со всех страниц, вам нужно вызвать метод Accept коллекции Pages. TextFragmentAbsorber возвращает TextFragmentCollection, содержащую все фрагменты, соответствующие критериям, указанным регулярным выражением. Следующий фрагмент кода показывает, как искать и получать текст со всех страниц на основе регулярного выражения.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionAll.pdf"))
    {
        // Create TextAbsorber object to find all the phrases matching the regular expression
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}"); // Like 1999-2000

        // Set text search option to specify regular expression usage
        var textSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

        textFragmentAbsorber.TextSearchOptions = textSearchOptions;

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
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
    }
}
```

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TextFragmentAbsorberCtor()
{
    Aspose.Pdf.Text.TextFragmentAbsorber textFragmentAbsorber;
    // In order to search exact match of a word, you may consider using regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"\bWord\b", new Aspose.Pdf.Text.TextSearchOptions(true));

    // In order to search a string in either upper case or lowercase, you may consider using regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("(?i)Line", new Aspose.Pdf.Text.TextSearchOptions(true));

    // In order to search all the strings (parse all strings) inside PDF document, please try using following regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"[\S]+");

    // Find match of search string and get anything after the string till line break
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"(?i)the ((.)*)");

    // Please use following regular expression to find text following to the regex match
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"(?<=word).*");

    // In order to search Hyperlink/URL's inside PDF document, please try using following regular expression
    textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
}
```

## Поиск текста на основе регулярного выражения и добавление гиперссылки

Если вы хотите добавить гиперссылку к текстовой фразе на основе регулярного выражения, сначала найдите все фразы, соответствующие этому регулярному выражению, с помощью TextFragmentAbsorber и добавьте гиперссылку к этим фразам.

Чтобы найти фразу и добавить гиперссылку к ней:

1. Передайте регулярное выражение в качестве параметра конструктору TextFragmentAbsorber.
2. Создайте объект TextSearchOptions, который указывает, используется ли регулярное выражение или нет.
3. Получите совпадающие фразы в TextFragments.
4. Пройдитесь по совпадениям, чтобы получить их прямоугольные размеры, измените цвет переднего плана на синий (по желанию - чтобы он выглядел как гиперссылка) и создайте ссылку с помощью метода CreateWebLink(..) класса PdfContentEditor.
5. Сохраните обновленный PDF с помощью метода Save объекта Document.
Следующий фрагмент кода показывает, как искать текст внутри PDF-файла с использованием регулярного выражения и добавлять гиперссылки к совпадениям.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create absorber object to find all instances of the input search phrase
    var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("\\d{4}-\\d{4}");

    // Enable regular expression search
    absorber.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);

    // Create the editor
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");

        // Accept the absorber for the page
        editor.Document.Pages[1].Accept(absorber);

        int[] dashArray = { };
        String[] LEArray = { };
        System.Drawing.Color blue = System.Drawing.Color.Blue;

        // Loop through the fragments
        foreach (var textFragment in absorber.TextFragments)
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

        // Save PDF document
        editor.Save(dataDir + "SearchTextAndAddHyperlink_out.pdf");
    }
}
```

## Поиск и рисование прямоугольника вокруг каждого TextFragment

Aspose.PDF for .NET поддерживает функцию поиска и получения координат каждого символа или текстовых фрагментов. Поэтому, чтобы быть уверенным в координатах, возвращаемых для каждого символа, мы можем рассмотреть возможность выделения (добавления прямоугольника) вокруг каждого символа.

В случае текстового абзаца вы можете рассмотреть возможность использования регулярного выражения для определения разрыва абзаца и рисования прямоугольника вокруг него. Пожалуйста, посмотрите на следующий фрагмент кода. Следующий фрагмент кода получает координаты каждого символа и создает прямоугольник вокруг каждого символа.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SearchAndDraw()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {

        // Create TextAbsorber object to find all the phrases matching the regular expression
        var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(".");

        var textSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);
        textAbsorber.TextSearchOptions = textSearchOptions;

        document.Pages.Accept(textAbsorber);

        foreach (var textFragment in textAbsorber.TextFragments)
        {
            DrawRectangleOnPage(textFragment.Rectangle, textFragment.Page, new Aspose.Pdf.Operators.SetRGBColorStroke(System.Drawing.Color.Red));
        }   
        // Save PDF document
        document.Save(dataDir + "SearchTextAndDrawRectangle_out.pdf");
    }
}

 private static void DrawRectangleOnPage(Aspose.Pdf.Rectangle rectangle, Aspose.Pdf.Page page, Aspose.Pdf.Operators.SetRGBColorStroke colorStroke = null)
 {
     if (colorStroke == null)
     {
         colorStroke = new Aspose.Pdf.Operators.SetRGBColorStroke(0.7, 0, 0);
     }

     page.Contents.Add(new Aspose.Pdf.Operators.GSave());
     page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
     page.Contents.Add(colorStroke);
     page.Contents.Add(
         new Re(rectangle.LLX,
             rectangle.LLY,
             rectangle.Width,
             rectangle.Height));
     page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
     page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
 }
```
{{< /tab >}}
{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SearchAndDraw()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf");
    
     // Create TextAbsorber object to find all the phrases matching the regular expression
     var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(".");

     var textSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(true);
     textAbsorber.TextSearchOptions = textSearchOptions;

     document.Pages.Accept(textAbsorber);

     foreach (var textFragment in textAbsorber.TextFragments)
     {
         DrawRectangleOnPage(textFragment.Rectangle, textFragment.Page, new Aspose.Pdf.Operators.SetRGBColorStroke(System.Drawing.Color.Red));
     }   
     // Save PDF document
     document.Save(dataDir + "SearchTextAndDrawRectangle_out.pdf");
    
}

 private static void DrawRectangleOnPage(Aspose.Pdf.Rectangle rectangle, Aspose.Pdf.Page page, Aspose.Pdf.Operators.SetRGBColorStroke colorStroke = null)
 {
     if (colorStroke == null)
     {
         colorStroke = new Aspose.Pdf.Operators.SetRGBColorStroke(0.7, 0, 0);
     }

     page.Contents.Add(new Aspose.Pdf.Operators.GSave());
     page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 0, 0));
     page.Contents.Add(colorStroke);
     page.Contents.Add(
         new Re(rectangle.LLX,
             rectangle.LLY,
             rectangle.Width,
             rectangle.Height));
     page.Contents.Add(new Aspose.Pdf.Operators.ClosePathStroke());
     page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
 }
```
{{< /tab >}}
{{< /tabs >}}

## Выделение каждого символа в PDF-документе

{{% alert color="primary" %}}

Вы можете попробовать искать текст в документе с помощью Aspose.PDF и получить результаты онлайн по этой [ссылке](https://products.aspose.app/pdf/search)

{{% /alert %}}

Aspose.PDF for .NET поддерживает функцию поиска и получения координат каждого символа или текстовых фрагментов. Поэтому, чтобы быть уверенным в координатах, возвращаемых для каждого символа, мы можем рассмотреть возможность выделения (добавления прямоугольника) вокруг каждого символа. Следующий фрагмент кода получает координаты каждого символа и создает прямоугольник вокруг каждого символа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SearchAndHighlight()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    int resolution = 150;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetTextFromAll.pdf"))
    {

        using (MemoryStream stream = new MemoryStream())
        {
            var conv = new Aspose.Pdf.Facades.PdfConverter(document);
            conv.Resolution = new Aspose.Pdf.Devices.Resolution(resolution, resolution);
            conv.GetNextImage(stream, System.Drawing.Imaging.ImageFormat.Png);

            using (var bmp = System.Drawing.Bitmap.FromStream(stream))
            {

                using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
                {
                    float scale = resolution / 72f;
                    gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

                    for (int i = 0; i < document.Pages.Count; i++)
                    {
                        var page = document.Pages[1];
                        // Create TextAbsorber object to find all words
                        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(@"[\S]+");
                        textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
                        page.Accept(textFragmentAbsorber);
                        // Get the extracted text fragments
                        var textFragmentCollection = textFragmentAbsorber.TextFragments;
                        // Loop through the fragments
                        foreach (var textFragment in textFragmentCollection)
                        {
                            if (i == 0)
                            {
                                gr.DrawRectangle(
                                    System.Drawing.Pens.Yellow,
                                    (float)textFragment.Position.XIndent,
                                    (float)textFragment.Position.YIndent,
                                    (float)textFragment.Rectangle.Width,
                                    (float)textFragment.Rectangle.Height);

                                for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
                                {
                                    var segment = textFragment.Segments[segNum];

                                    for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
                                    {
                                        var characterInfo = segment.Characters[charNum];

                                        Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
                                        Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
                                            "   TextFragment URY = " + textFragment.Rectangle.URY);

                                        gr.DrawRectangle(
                                            System.Drawing.Pens.Black,
                                            (float)characterInfo.Rectangle.LLX,
                                            (float)characterInfo.Rectangle.LLY,
                                            (float)characterInfo.Rectangle.Width,
                                            (float)characterInfo.Rectangle.Height);
                                    }

                                    gr.DrawRectangle(
                                        System.Drawing.Pens.Green,
                                        (float)segment.Rectangle.LLX,
                                        (float)segment.Rectangle.LLY,
                                        (float)segment.Rectangle.Width,
                                        (float)segment.Rectangle.Height);
                                }
                            }
                        }
                    }
                }
                
                // Save result
                bmp.Save(dataDir + "HighlightCharacterInPDF_out.png", System.Drawing.Imaging.ImageFormat.Png);
            }
        }
    }
}
```

## Добавление и поиск скрытого текста

Иногда мы хотим добавить скрытый текст в PDF-документ, а затем искать скрытый текст и использовать его положение для последующей обработки. Для вашего удобства Aspose.PDF for .NET предоставляет эти возможности. Вы можете добавить скрытый текст во время генерации документа. Также вы можете найти скрытый текст с помощью TextFragmentAbsorber. Чтобы добавить скрытый текст, установите TextState.Invisible в 'true' для добавленного текста. TextFragmentAbsorber находит весь текст, который соответствует шаблону (если он указан). Это поведение по умолчанию, которое нельзя изменить. Чтобы проверить, действительно ли найденный текст невидим, можно использовать свойство TextState.Invisible. Ниже приведен фрагмент кода, который показывает, как использовать эту функцию.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAndSearchText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var frag1 = new Aspose.Pdf.Text.TextFragment("This is common text.");
        var frag2 = new Aspose.Pdf.Text.TextFragment("This is invisible text.");

        //Set text property - invisible
        frag2.TextState.Invisible = true;

        page.Paragraphs.Add(frag1);
        page.Paragraphs.Add(frag2);
        // Save PDF document
        document.Save(dataDir + "CreateAndSearchText_out.pdf");
    }

    // Search text in the document
    using (var document = new Aspose.Pdf.Document(dataDir + "CreateAndSearchText_out.pdf"))
    {
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);

        foreach (var fragment in absorber.TextFragments)
        {
            //Do something with fragments
            Console.WriteLine("Text '{0}' on pos {1} invisibility: {2} ",
            fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
        }
    }
}
```

## Поиск текста с использованием .NET Regex

Aspose.PDF for .NET предоставляет возможность искать документы с использованием стандартного варианта .NET Regex. Для этой цели можно использовать TextFragmentAbsorber, как показано в приведенном ниже примере кода.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Search()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create Regex object to find all words
    var regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf"))
    {

        // Get a particular page
        var page = document.Pages[1];

        // Create TextAbsorber object to find all instances of the input regex
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber(regex);
        textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

        // Accept the absorber for the page
        page.Accept(textFragmentAbsorber);

        // Get the extracted text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Loop through the fragments
        foreach (var textFragment in textFragmentCollection)
        {
            Console.WriteLine(textFragment.Text);
        }
    }
}
```

## Поиск жирного текста

Aspose.PDF for .NET позволяет пользователям искать документы, используя свойства стиля шрифта. Для этой цели можно использовать TextFragmentAbsorber, как показано в приведенном ниже примере кода.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractBoldText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractBoldText.pdf"))
    {
        // Create TextFragmentAbsorber object to extract text
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // Accept the absorber for all document
        textFragmentAbsorber.Visit(document);

        // Loop through the fragments
        foreach (var textFragment in textFragmentAbsorber.TextFragments)
        {
            // Get the text properties of the text fragment
            var textState = textFragment.TextState;
            // Check if text is bold
            if (textState.FontStyle == FontStyles.Bold)
            {
                // Print the text from the text fragment
                Console.WriteLine("Text :- " + textFragment.Text);
            }
        }
    }
}
```
{{< /tab >}}
{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractBoldText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "ExtractBoldText.pdf");
    
    // Create TextFragmentAbsorber object to extract text
    var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

    // Accept the absorber for all document
    textFragmentAbsorber.Visit(document);

    // Loop through the fragments
    foreach (var textFragment in textFragmentAbsorber.TextFragments)
    {
        // Get the text properties of the text fragment
        var textState = textFragment.TextState;
        // Check if text is bold
        if (textState.FontStyle == FontStyles.Bold)
        {
            // Print the text from the text fragment
            Console.WriteLine("Text :- " + textFragment.Text);
        }
    }
    
}
```
{{< /tab >}}
{{< /tabs >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
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