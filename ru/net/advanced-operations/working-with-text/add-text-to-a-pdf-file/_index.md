---
title: Добавление текста в PDF с использованием C#
linktitle: Добавление текста в PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/add-text-to-pdf-file/
description: Узнайте, как добавить текст в PDF-документ в .NET с использованием Aspose.PDF для улучшения содержания и редактирования документов.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text to PDF using C#",
    "alternativeHeadline": "Add Custom Text to Existing PDFs with C#",
    "abstract": "Функция добавления текста в PDF с использованием C# в Aspose.PDF позволяет разработчикам бесшовно интегрировать и манипулировать текстом в существующих PDF-документах. С такими возможностями, как добавление текстовых фрагментов, использование пользовательских шрифтов OTF и добавление HTML-содержимого, эта функциональность улучшает форматирование и представление документов, упрощая создание профессиональных, индивидуализированных PDF-программно.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "5625",
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
    "url": "/net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-to-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "В этой статье описаны различные аспекты работы с текстом в Aspose.PDF. Узнайте, как добавить текст в PDF, добавить HTML-фрагменты или использовать пользовательские шрифты OTF."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Чтобы добавить текст в существующий PDF-файл:

1. Откройте входной PDF с помощью объекта Document.
2. Получите конкретную страницу, на которую вы хотите добавить текст.
3. Создайте объект TextFragment с входным текстом и другими свойствами текста. Объект TextBuilder, созданный из этой конкретной страницы, на которую вы хотите добавить текст, позволяет вам добавить объект TextFragment на страницу с помощью метода AppendText.
4. Вызовите метод Save объекта Document и сохраните выходной PDF-файл.

## Добавление текста

Следующий фрагмент кода показывает, как добавить текст в существующий PDF-файл.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get particular page
        var page = document.Pages.Add();

        // Create text fragment
        var textFragment = new Aspose.Pdf.Text.TextFragment("main text");
        textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);

        // Set text properties
        textFragment.TextState.FontSize = 12;
        textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
        textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray);
        textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Red);

        // Create TextBuilder object
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(page);

        // Append the text fragment to the PDF page
        textBuilder.AppendText(textFragment);

        // Save PDF document
        document.Save(dataDir + "AddText_out.pdf");
    }
}
```

## Загрузка шрифта из потока

Следующий фрагмент кода показывает, как загрузить шрифт из объекта Stream при добавлении текста в PDF-документ.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LoadingFontFromStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    var fontFile = dataDir + "HPSimplified.ttf";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "LoadFonts.pdf"))
    {
        // Create text builder object for first page of document
        var textBuilder = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
        // Create text fragment with sample string
        var textFragment = new Aspose.Pdf.Text.TextFragment("Hello world");

        if (File.Exists(fontFile))
        {
            // Load the TrueType font into stream object
            using (FileStream fontStream = File.OpenRead(fontFile))
            {
                // Set the font name for text string
                textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.OpenFont(fontStream, Aspose.Pdf.Text.FontTypes.TTF);
                // Specify the position for Text Fragment
                textFragment.Position = new Aspose.Pdf.Text.Position(10, 10);
                // Add the text to TextBuilder so that it can be placed over the PDF file
                textBuilder.AppendText(textFragment);
            }

            // Save PDF document
            document.Save(dataDir + "LoadingFontFromStream_out.pdf");
        }
    }
}
```

## Добавление текста с использованием TextParagraph

Следующий фрагмент кода показывает, как добавить текст в PDF-документ с использованием класса [TextParagraph](https://reference.aspose.com/pdf/net/aspose.pdf.text/textparagraph).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextWithTextParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document object
        var page = document.Pages.Add();
        var builder = new Aspose.Pdf.Text.TextBuilder(page);
        // Create text paragraph
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        // Set subsequent lines indent
        paragraph.SubsequentLinesIndent = 20;
        // Specify the location to add TextParagraph
        paragraph.Rectangle = new Aspose.Pdf.Rectangle(100, 300, 200, 700);
        // Specify word wraping mode
        paragraph.FormattingOptions.WrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        // Create text fragment
        var fragment = new Aspose.Pdf.Text.TextFragment("the quick brown fox jumps over the lazy dog");
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
        fragment.TextState.FontSize = 12;
        // Add fragment to paragraph
        paragraph.AppendLine(fragment);
        // Add paragraph
        builder.AppendParagraph(paragraph);

        // Save PDF document
        document.Save(dataDir + "AddTextUsingTextParagraph_out.pdf");
    }
}
```

## Добавление гиперссылки к TextSegment

Страница PDF может состоять из одного или нескольких объектов TextFragment, где каждый объект TextFragment может иметь один или несколько экземпляров TextSegment. Чтобы установить гиперссылку для TextSegment, можно использовать свойство Hyperlink класса [TextSegment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textsegment), предоставив объект экземпляра Aspose.Pdf.WebHyperlink. Пожалуйста, попробуйте использовать следующий фрагмент кода для выполнения этого требования.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlinkToTextSegment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create TextFragment instance
        var fragment = new Aspose.Pdf.Text.TextFragment("Sample Text Fragment");
        // Set horizontal alignment for TextFragment
        fragment.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
        // Create a textsegment with sample text
        var segment = new Aspose.Pdf.Text.TextSegment(" ... Text Segment 1...");
        // Add segment to segments collection of TextFragment
        fragment.Segments.Add(segment);
        // Create a new TextSegment
        segment = new Aspose.Pdf.Text.TextSegment("Link to Google");
        // Add segment to segments collection of TextFragment
        fragment.Segments.Add(segment);
        // Set hyperlink for TextSegment
        segment.Hyperlink = new Aspose.Pdf.WebHyperlink("www.google.com");
        // Set forground color for text segment
        segment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
        // Set text formatting as italic
        segment.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        // Create another TextSegment object
        segment = new Aspose.Pdf.Text.TextSegment("TextSegment without hyperlink");
        // Add segment to segments collection of TextFragment
        fragment.Segments.Add(segment);
        // Add TextFragment to paragraphs collection of page object
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "AddHyperlinkToTextSegment_out.pdf");
    }
}
```

## Использование шрифта OTF

Aspose.PDF for .NET предлагает возможность использовать пользовательские/TrueType шрифты при создании/манипуляции содержимым PDF-файлов, чтобы содержимое файлов отображалось с использованием шрифтов, отличных от шрифтов системы по умолчанию. Начиная с версии Aspose.PDF for .NET 10.3.0, мы предоставили поддержку шрифтов Open Type.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UseOTFFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create TextFragment instnace with sample text
        var fragment = new Aspose.Pdf.Text.TextFragment("Sample Text in OTF font");
        // Find font inside system font directory
        // Fragment.TextState.Font = FontRepository.FindFont("HelveticaNeueLT Pro 45 Lt");
        // Or you can even specify the path of OTF font in system directory
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.OpenFont(dataDir + "space age.otf");
        // Specify to emend font inside PDF file, so that its displayed properly,
        // Even if specific font is not installed/present over target machine
        fragment.TextState.Font.IsEmbedded = true;
        // Add TextFragment to paragraphs collection of Page instance
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "OTFFont_out.pdf");
    }
}
```

## Добавление HTML-строки с использованием DOM

Класс Aspose.Pdf.Generator.Text содержит свойство IsHtmlTagSupported, которое позволяет добавлять HTML-теги/содержимое в PDF-файлы. Добавленное содержимое отображается в родных HTML-тегах, а не как простая текстовая строка. Чтобы поддержать аналогичную функцию в новой модели объектов документа (DOM) пространства имен Aspose.Pdf, был введен класс HtmlFragment.

Экземпляр [HtmlFragment](https://reference.aspose.com/pdf/net/aspose.pdf/htmlfragment) может использоваться для указания HTML-содержимого, которое должно быть помещено внутри PDF-файла. Подобно TextFragment, HtmlFragment является объектом уровня абзаца и может быть добавлен в коллекцию абзацев объекта Page. Следующие фрагменты кода показывают шаги по размещению HTML-содержимого внутри PDF-файла с использованием подхода DOM.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHTMLStringUsingDOM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a page to pages collection of PDF file
        var page = document.Pages.Add();
        // Instantiate HtmlFragment with HTML contnets
        var title = new Aspose.Pdf.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");
        // Set bottom margin information
        title.Margin.Bottom = 10;
        // Set top margin information
        title.Margin.Top = 200;
        // Add HTML Fragment to paragraphs collection of page
        page.Paragraphs.Add(title);

        // Save PDF document
        document.Save(dataDir + "AddHTMLUsingDOM_out.pdf");
    }
}
```

Следующий фрагмент кода демонстрирует шаги, как добавить упорядоченные списки HTML в документ:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHTMLOrderedListIntoDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Instantiate HtmlFragment object with corresponding HTML fragment 
        var fragment = new Aspose.Pdf.HtmlFragment("`<body style='line-height: 100px;'><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul>Text after the list.<br/>Next line<br/>Last line</body>`");
        // Add Page in Pages Collection 
        var page = document.Pages.Add();
        // Add HtmlFragment inside page 
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf");
    }
}
```

Вы также можете установить форматирование HTML-строки с использованием объекта TextState следующим образом:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetHTMLStringFormatting()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var fragment = new Aspose.Pdf.HtmlFragment("some text");
        fragment.TextState = new Aspose.Pdf.Text.TextState();
        fragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Calibri");
        // Add Page in Pages Collection 
        var page = document.Pages.Add();
        // Add HtmlFragment inside page 
        page.Paragraphs.Add(fragment);

        // Save PDF document
        document.Save(dataDir + "SetHTMLStringFormatting_out.pdf");
    }
}
```

В случае, если вы установите некоторые значения атрибутов текста через HTML-разметку, а затем предоставите те же значения в свойствах TextState, они перезапишут параметры HTML свойствами экземпляра TextState. Следующие фрагменты кода показывают описанное поведение.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHTMLUsingDOMAndOverwrite()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a page to pages collection of PDF file
        var page = document.Pages.Add();
        // Instantiate HtmlFragment with HTML contnets
        var title = new Aspose.Pdf.HtmlFragment("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");
        //Font-family from 'Verdana' will be reset to 'Arial'
        title.TextState = new Aspose.Pdf.Text.TextState("Arial");
        title.TextState.FontSize = 20;
        // Set bottom margin information
        title.Margin.Bottom = 10;
        // Set top margin information
        title.Margin.Top = 400;
        // Add HTML Fragment to paragraphs collection of page
        page.Paragraphs.Add(title);
        
        // Save PDF document
        document.Save(dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf");
    }
}
```

## Сноски и концевые сноски (DOM)

Сноски указывают на заметки в тексте вашей работы, используя последовательные надстрочные номера. Фактическая заметка отступает и может появляться как сноска внизу страницы.

### Добавление сноски

В системе ссылок сноски указывают на ссылку следующим образом:

- Поместите маленький номер над строкой текста, непосредственно следующей за исходным материалом. Этот номер называется идентификатором заметки. Он находится немного выше строки текста.
- Поместите тот же номер, за которым следует ссылка на ваш источник, внизу страницы. Сноски должны быть числовыми и хронологическими: первая ссылка — 1, вторая — 2 и так далее.

Преимущество сносок заключается в том, что читатель может просто взглянуть вниз по странице, чтобы узнать источник ссылки, которая его интересует.

Пожалуйста, следуйте указанным ниже шагам, чтобы создать сноску:

- Создайте экземпляр Document.
- Создайте объект Page.
- Создайте объект TextFragment.
- Создайте экземпляр Note и передайте его значение в свойство TextFragment.FootNote.
- Добавьте TextFragment в коллекцию абзацев экземпляра страницы.

### Пользовательский стиль линии для сноски

Следующий пример демонстрирует, как добавить сноски внизу страницы PDF и определить пользовательский стиль линии.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomLineStyleForFootNote()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create GraphInfo object
        var graph = new Aspose.Pdf.GraphInfo();
        // Set line width as 2
        graph.LineWidth = 2;
        // Set the color for graph object
        graph.Color = Aspose.Pdf.Color.Red;
        // Set dash array value as 3
        graph.DashArray = new int[] { 3 };
        // Set dash phase value as 1
        graph.DashPhase = 1;
        // Set footnote line style for page as graph
        page.NoteLineStyle = graph;
        // Create TextFragment instance
        var text = new Aspose.Pdf.Text.TextFragment("Hello World");
        // Set FootNote value for TextFragment
        text.FootNote = new Aspose.Pdf.Note("foot note for test text 1");
        // Add TextFragment to paragraphs collection of first page of document
        page.Paragraphs.Add(text);
        // Create second TextFragment
        text = new Aspose.Pdf.Text.TextFragment("Aspose.PDF for .NET");
        // Set FootNote for second text fragment
        text.FootNote = new Aspose.Pdf.Note("foot note for test text 2");
        // Add second text fragment to paragraphs collection of PDF file
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CustomLineStyleForFootNote_out.pdf");
    }
}
```

Мы можем установить форматирование метки сноски (идентификатор заметки) с использованием объекта TextState следующим образом:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FormattingUsingTextStateObject()
{
    var text = new Aspose.Pdf.Text.TextFragment("test text 1");
    text.FootNote = new Aspose.Pdf.Note("foot note for test text 1");
    text.FootNote.Text = "21";
    text.FootNote.TextState = new Aspose.Pdf.Text.TextState();
    text.FootNote.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    text.FootNote.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
}
```

### Настройка метки сноски

По умолчанию номер сноски увеличивается, начиная с 1. Однако у нас может быть требование установить пользовательскую метку сноски. Чтобы выполнить это требование, пожалуйста, попробуйте использовать следующий фрагмент кода.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizeFootNoteLabel()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create GraphInfo object
        var graph = new Aspose.Pdf.GraphInfo();
        // Set line width as 2
        graph.LineWidth = 2;
        // Set the color for graph object
        graph.Color = Aspose.Pdf.Color.Red;
        // Set dash array value as 3
        graph.DashArray = new int[] { 3 };
        // Set dash phase value as 1
        graph.DashPhase = 1;
        // Set footnote line style for page as graph
        page.NoteLineStyle = graph;
        // Create TextFragment instance
        var text = new Aspose.Pdf.Text.TextFragment("Hello World");
        // Set FootNote value for TextFragment
        text.FootNote = new Aspose.Pdf.Note("foot note for test text 1");
        // Specify custom label for FootNote
        text.FootNote.Text = " Aspose(2015)";
        // Add TextFragment to paragraphs collection of first page of document
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CustomizeFootNoteLabel_out.pdf");
    }
}
```

## Добавление изображения и таблицы в сноску

В предыдущих версиях поддержка сносок была предоставлена, но она применялась только к объекту TextFragment. Однако начиная с версии Aspose.PDF for .NET 10.7.0, вы также можете добавлять сноски к другим объектам внутри PDF-документа, таким как таблицы, ячейки и т.д. Следующий фрагмент кода показывает шаги по добавлению сноски к объекту TextFragment, а затем добавлению изображения и объекта таблицы в коллекцию абзацев раздела сноски.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageAndTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var text = new Aspose.Pdf.Text.TextFragment("some text");
        page.Paragraphs.Add(text);

        text.FootNote = new Aspose.Pdf.Note();
        // Create image
        Aspose.Pdf.Image image = new Aspose.Pdf.Image();
        image.File = dataDir + "aspose-logo.jpg";
        image.FixHeight = 20;
        text.FootNote.Paragraphs.Add(image);

        var footNote = new Aspose.Pdf.Text.TextFragment("footnote text");
        footNote.TextState.FontSize = 20;
        footNote.IsInLineParagraph = true;
        text.FootNote.Paragraphs.Add(footNote);

        var table = new Aspose.Pdf.Table();
        table.Rows.Add().Cells.Add().Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Row 1 Cell 1"));
        text.FootNote.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "AddImageAndTable_out.pdf");
    }
}
```

## Как создать концевые сноски

Концевая сноска — это источник цитирования, который указывает читателям на конкретное место в конце работы, где они могут узнать источник информации или слов, процитированных или упомянутых в работе. При использовании концевых сносок ваша процитированная или перефразированная фраза или обобщенный материал сопровождаются надстрочным номером.

Следующий пример демонстрирует, как добавить концевую сноску на страницу PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateEndNotes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create TextFragment instance
        var text = new Aspose.Pdf.Text.TextFragment("Hello World");
        // Set FootNote value for TextFragment
        text.EndNote = new Aspose.Pdf.Note("sample End note");
        // Specify custom label for FootNote
        text.EndNote.Text = " Aspose(2015)";
        // Add TextFragment to paragraphs collection of first page of document
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CreateEndNotes_out.pdf");
    }
}
```

## Текст и изображение как встроенные абзацы

Стандартная компоновка PDF-файла — это компоновка потока (сверху вниз, слева направо). Поэтому каждый новый элемент, добавляемый в PDF-файл, добавляется в нижний правый поток. Однако у нас может быть требование отображать различные элементы страницы, т.е. изображение и текст на одном уровне (один за другим). Один из подходов может заключаться в создании экземпляра таблицы и добавлении обоих элементов в отдельные ячейки. Однако другой подход может быть встроенный абзац. Установив свойство IsInLineParagraph для изображения и текста как true, эти абзацы будут отображаться как встроенные к другим элементам страницы.

Следующий фрагмент кода показывает, как добавить текст и изображение как встроенные абзацы в PDF-файл.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TextAndImageAsParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document instance
        var page = document.Pages.Add();
        // Create TextFragmnet
        var text = new Aspose.Pdf.Text.TextFragment("Hello World.. ");
        // Add text fragment to paragraphs collection of Page object
        page.Paragraphs.Add(text);
        // Create an image instance
        var image = new Aspose.Pdf.Image();
        // Set image as inline paragraph so that it appears right after
        // The previous paragraph object (TextFragment)
        image.IsInLineParagraph = true;
        // Specify image file path
        image.File = dataDir + "aspose-logo.jpg";
        // Set image Height (optional)
        image.FixHeight = 30;
        // Set Image Width (optional)
        image.FixWidth = 100;
        // Add image to paragraphs collection of page object
        page.Paragraphs.Add(image);
        // Re-initialize TextFragment object with different contents
        text = new Aspose.Pdf.Text.TextFragment(" Hello Again..");
        // Set TextFragment as inline paragraph
        text.IsInLineParagraph = true;
        // Add newly created TextFragment to paragraphs collection of page
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "TextAndImageAsParagraph_out.pdf");
    }
}
```

## Укажите межсимвольное расстояние при добавлении текста

Текст может быть добавлен в коллекцию абзацев PDF-файлов с использованием экземпляра TextFragment или с использованием объекта TextParagraph, и даже вы можете штамповать текст внутри PDF, используя класс TextStamp. При добавлении текста у нас может быть требование указать межсимвольное расстояние для текстовых объектов. Чтобы выполнить это требование, было введено новое свойство под названием CharacterSpacing. Пожалуйста, ознакомьтесь с следующими подходами для выполнения этого требования.

Следующие подходы показывают шаги по указанию межсимвольного расстояния при добавлении текста внутри PDF-документа.

### Использование TextBuilder и TextFragment

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CharacterSpacingUsingTextBuilderAndFragment()
{            
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document
        document.Pages.Add();
        // Create TextBuilder instance
        var builder = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
        // Create text fragment instance with sample contents
        var wideFragment = new Aspose.Pdf.Text.TextFragment("Text with increased character spacing");
        wideFragment.TextState.ApplyChangesFrom(new Aspose.Pdf.Text.TextState("Arial", 12));
        // Specify character spacing for TextFragment
        wideFragment.TextState.CharacterSpacing = 2.0f;
        // Specify the position of TextFragment
        wideFragment.Position = new Aspose.Pdf.Text.Position(100, 650);
        // Append TextFragment to TextBuilder instance
        builder.AppendText(wideFragment);

        // Save PDF document
        document.Save(dataDir + "CharacterSpacingUsingTextBuilderAndFragment_out.pdf");
    }
}
```

### Использование TextParagraph

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CharacterSpacingUsingTextBuilderAndParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document
        var page = document.Pages.Add();
        // Create TextBuilder instance
        var builder = new Aspose.Pdf.Text.TextBuilder(page);
        // Instantiate TextParagraph instance
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        // Create TextState instance to specify font name and size
        var state = new Aspose.Pdf.Text.TextState("Arial", 12);
        // Specify the character spacing
        state.CharacterSpacing = 1.5f;
        // Append text to TextParagraph object
        paragraph.AppendLine("This is paragraph with character spacing", state);
        // Specify the position for TextParagraph
        paragraph.Position = new Aspose.Pdf.Text.Position(100, 550);
        // Append TextParagraph to TextBuilder instance
        builder.AppendParagraph(paragraph);

        // Save PDF document
        document.Save(dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf");
    }
}
```

### Использование TextStamp

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CharacterSpacingUsingTextStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to pages collection of Document
        var page = document.Pages.Add();
        // Instantiate TextStamp instance with sample text
        var stamp = new Aspose.Pdf.TextStamp("This is text stamp with character spacing");
        // Specify font name for Stamp object
        stamp.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        // Specify Font size for TextStamp
        stamp.TextState.FontSize = 12;
        // Specify character specing as 1f
        stamp.TextState.CharacterSpacing = 1f;
        // Set the XIndent for Stamp
        stamp.XIndent = 100;
        // Set the YIndent for Stamp
        stamp.YIndent = 500;
        // Add textual stamp to page instance
        stamp.Put(page);

        // Save PDF document
        document.Save(dataDir + "CharacterSpacingUsingTextStamp_out.pdf");
    }
}
```

## Создание многостолбцового PDF-документа

В журналах и газетах мы чаще всего видим, что новости отображаются в нескольких столбцах на одной странице, в отличие от книг, где текстовые абзацы в основном печатаются на целых страницах слева направо. Многие приложения для обработки документов, такие как Microsoft Word и Adobe Acrobat Writer, позволяют пользователям создавать несколько столбцов на одной странице и затем добавлять данные в них.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) также предлагает возможность создавать несколько столбцов внутри страниц PDF-документов. Чтобы создать многостолбцовый PDF-файл, мы можем использовать класс Aspose.Pdf.FloatingBox, так как он предоставляет свойство ColumnInfo.ColumnCount для указания количества столбцов внутри FloatingBox, а также мы можем указать расстояние между столбцами и ширину столбцов с помощью свойств ColumnInfo.ColumnSpacing и ColumnInfo.ColumnWidths соответственно. Пожалуйста, обратите внимание, что FloatingBox является элементом внутри модели объектов документа и может иметь устаревшее позиционирование по сравнению с относительным позиционированием (т.е. текст, графика, изображение и т.д.).

Расстояние между столбцами означает пространство между столбцами, и стандартное расстояние между столбцами составляет 1,25 см. Если ширина столбца не указана, то [Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) автоматически рассчитывает ширину для каждого столбца в зависимости от размера страницы и расстояния между столбцами.

Пример приведен ниже, чтобы продемонстрировать создание двух столбцов с объектами графиков (линия), которые добавляются в коллекцию абзацев FloatingBox, которая затем добавляется в коллекцию абзацев экземпляра страницы.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateMultiColumnPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Specify the left margin info for the PDF file
        document.PageInfo.Margin.Left = 40;
        // Specify the Right margin info for the PDF file
        document.PageInfo.Margin.Right = 40;
        var page = document.Pages.Add();

        var graph1 = new Aspose.Pdf.Drawing.Graph(500, 2);
        // Add the line to paraphraphs collection of section object
        page.Paragraphs.Add(graph1);

        // Specify the coordinates for the line
        float[] posArr = new float[] { 1, 2, 500, 2 };
        var line1 = new Aspose.Pdf.Drawing.Line(posArr);
        graph1.Shapes.Add(line1);
        // Create string variables with text containing html tags
        string s = "<font face=\"Times New Roman\" size=4>" +

        "<strong> How to Steer Clear of money scams</<strong> "
        + "</font>";
        // Create text paragraphs containing HTML text
        var heading_text = new Aspose.Pdf.HtmlFragment(s);
        page.Paragraphs.Add(heading_text);

        var box = new Aspose.Pdf.FloatingBox();
        // Add four columns in the section
        box.ColumnInfo.ColumnCount = 2;
        // Set the spacing between the columns
        box.ColumnInfo.ColumnSpacing = "5";

        box.ColumnInfo.ColumnWidths = "105 105";
        var text1 = new Aspose.Pdf.Text.TextFragment("By A Googler (The Official Google Blog)");
        text1.TextState.FontSize = 8;
        text1.TextState.LineSpacing = 2;
        box.Paragraphs.Add(text1);
        text1.TextState.FontSize = 10;

        text1.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;
        // Create a graphs object to draw a line
        var graph2 = new Aspose.Pdf.Drawing.Graph(50, 10);
        // Specify the coordinates for the line
        float[] posArr2 = new float[] { 1, 10, 100, 10 };
        var line2 = new Aspose.Pdf.Drawing.Line(posArr2);
        graph2.Shapes.Add(line2);

        // Add the line to paragraphs collection of section object
        box.Paragraphs.Add(graph2);

        var text2 = new Aspose.Pdf.Text.TextFragment(@"Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.");
        box.Paragraphs.Add(text2);

        page.Paragraphs.Add(box);

        // Save PDF document
        document.Save(dataDir + "CreateMultiColumnPdf_out.pdf");
    }
}
```

## Работа с пользовательскими табуляциями

Табуляция — это точка остановки для табуляции. В текстовых процессорах каждая строка содержит несколько табуляций, расположенных на равных интервалах (например, каждые полдюйма). Однако их можно изменить, так как большинство текстовых процессоров позволяют устанавливать табуляции в любом месте. Когда вы нажимаете клавишу Tab, курсор или точка вставки прыгает к следующей табуляции, которая сама по себе невидима. Хотя табуляции не существуют в текстовом файле, текстовый процессор отслеживает их, чтобы правильно реагировать на клавишу Tab.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) позволяет разработчикам использовать пользовательские табуляции в PDF-документах. Класс Aspose.Pdf.Text.TabStop используется для установки пользовательских табуляций в классе [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment).

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) также предлагает некоторые предопределенные типы табуляции в виде перечисления под названием TabLeaderType, чьи предопределенные значения и их описания приведены ниже:

|**Тип табуляции**|**Описание**|
| :- | :- |
|Нет|Нет табуляции|
|Сплошная|Сплошная табуляция|
|Штриховая|Штриховая табуляция|
|Точечная|Точечная табуляция|

Вот пример того, как установить пользовательские табуляции.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomTabStops()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        var tabStops = new Aspose.Pdf.Text.TabStops();
        var tabStop1 = tabStops.Add(100);
        tabStop1.AlignmentType = Aspose.Pdf.Text.TabAlignmentType.Right;
        tabStop1.LeaderType = Aspose.Pdf.Text.TabLeaderType.Solid;

        var tabStop2 = tabStops.Add(200);
        tabStop2.AlignmentType = Aspose.Pdf.Text.TabAlignmentType.Center;
        tabStop2.LeaderType = Aspose.Pdf.Text.TabLeaderType.Dash;

        var tabStop3 = tabStops.Add(300);
        tabStop3.AlignmentType = Aspose.Pdf.Text.TabAlignmentType.Left;
        tabStop3.LeaderType = Aspose.Pdf.Text.TabLeaderType.Dot;

        var header = new Aspose.Pdf.Text.TextFragment("This is a example of forming table with TAB stops", tabStops);
        var text0 = new Aspose.Pdf.Text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tabStops);
        var text1 = new Aspose.Pdf.Text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tabStops);
        var text2 = new Aspose.Pdf.Text.TextFragment("#$TABdata21 ", tabStops);
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("#$TAB"));
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("data22 "));
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("#$TAB"));
        text2.Segments.Add(new Aspose.Pdf.Text.TextSegment("data23"));

        // Add text fragments to page
        page.Paragraphs.Add(header);
        page.Paragraphs.Add(text0);
        page.Paragraphs.Add(text1);
        page.Paragraphs.Add(text2);

        // Save PDF document
        document.Save(dataDir + "CustomTabStops_out.pdf");
    }
}
```

## Как добавить прозрачный текст в PDF

PDF-файл содержит объекты изображений, текста, графиков, вложений, аннотаций, и при создании TextFragment вы можете установить информацию о переднем и заднем фоне, а также форматирование текста. Aspose.PDF for .NET поддерживает возможность добавления текста с альфа-каналом цвета. Следующий фрагмент кода показывает, как добавить текст с прозрачным цветом.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTransparentText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create page to pages collection of PDF file
        var page = document.Pages.Add();

        // Create Graph object
        var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
        // Create rectangle instance with certain dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 400, 400);
        // Create color object from Alpha color channel
        rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
        // Add rectanlge to shapes collection of Graph object
        canvas.Shapes.Add(rect);
        // Add graph object to paragraphs collection of page object
        page.Paragraphs.Add(canvas);
        // Set value to not change position for graph object
        canvas.IsChangePosition = false;

        // Create TextFragment instance with sample value
        var text = new Aspose.Pdf.Text.TextFragment("transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text ");
        // Create color object from Alpha channel
        Aspose.Pdf.Color color = Aspose.Pdf.Color.FromArgb(30, 0, 255, 0);
        // Set color information for text instance
        text.TextState.ForegroundColor = color;
        // Add text to paragraphs collection of page instance
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "AddTransparentText_out.pdf");
    }
}
```

## Укажите межстрочное расстояние для шрифтов

Каждый шрифт имеет абстрактный квадрат, высота которого является предполагаемым расстоянием между строками текста одного и того же размера. Этот квадрат называется квадратом em, и это проектная сетка, на которой определяются контуры глифов. Многие буквы входного шрифта имеют точки, которые расположены за пределами границ квадрата em шрифта, поэтому для правильного отображения шрифта требуется использование специальной настройки. Объект TextFragment имеет набор параметров форматирования текста, которые доступны через свойства TextState.FormattingOptions. Последнее свойство этого пути — это свойство типа Aspose.Pdf.Text.TextFormattingOptions. Этот класс имеет перечисление [LineSpacingMode](https://reference.aspose.com/pdf/net/aspose.pdf.text.textformattingoptions/linespacingmode), которое предназначено для конкретных шрифтов, например, входного шрифта "HPSimplified.ttf". Также класс [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions) имеет свойство [LineSpacing](https://reference.aspose.com/pdf/net/aspose.pdf.text/textformattingoptions/properties/linespacing) типа LineSpacingMode. Вам просто нужно установить LineSpacing в LineSpacingMode.FullSize. Фрагмент кода для правильного отображения шрифта будет выглядеть следующим образом:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyLineSpacing()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    string fontFile = dataDir + "HPSimplified.TTF";

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        //Create TextFormattingOptions with LineSpacingMode.FullSize
        var formattingOptions = new Aspose.Pdf.Text.TextFormattingOptions();
        formattingOptions.LineSpacing = Aspose.Pdf.Text.TextFormattingOptions.LineSpacingMode.FullSize;

        // Create text builder object for first page of document
        //TextBuilder textBuilder = new TextBuilder(document.Pages[1]);
        // Create text fragment with sample string
        var textFragment = new Aspose.Pdf.Text.TextFragment("Hello world");

        if (fontFile != "")
        {
            // Load the TrueType font into stream object
            using (FileStream fontStream = File.OpenRead(fontFile))
            {
                // Set the font name for text string
                textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.OpenFont(fontStream, Aspose.Pdf.Text.FontTypes.TTF);
                // Specify the position for Text Fragment
                textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);
                //Set TextFormattingOptions of current fragment to predefined(which points to LineSpacingMode.FullSize)
                textFragment.TextState.FormattingOptions = formattingOptions;
                // Add the text to TextBuilder so that it can be placed over the PDF file
                //textBuilder.AppendText(textFragment);
                var page = document.Pages.Add();
                page.Paragraphs.Add(textFragment);
            }

            // Save PDF document
            document.Save(dataDir + "SpecifyLineSpacing_out.pdf");
        }
    }
}
```

## Получение ширины текста динамически

Иногда требуется получить ширину текста динамически. Aspose.PDF for .NET включает два метода для измерения ширины строки. Вы можете вызвать метод [MeasureString](https://reference.aspose.com/pdf/net/aspose.pdf.text/font/methods/measurestring) классов Aspose.Pdf.Text.Font или Aspose.Pdf.Text.TextState (или оба). Следующий фрагмент кода показывает, как использовать эту функциональность.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetTextWidthDynamically()
{            
    var font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
    var textState = new Aspose.Pdf.Text.TextState();
    textState.Font = font;
    textState.FontSize = 14;

    if (Math.Abs(font.MeasureString("A", 14) - 9.337) > 0.001)
    {
        Console.WriteLine("Unexpected font string measure!");
    }

    if (Math.Abs(textState.MeasureString("z") - 7.0) > 0.001)
    {
        Console.WriteLine("Unexpected font string measure!");
    }

    for (char c = 'A'; c <= 'z'; c++)
    {
        double fontMeasure = font.MeasureString(c.ToString(), 14);
        double textStateMeasure = textState.MeasureString(c.ToString());

        if (Math.Abs(fontMeasure - textStateMeasure) > 0.001)
        {
            Console.WriteLine("Font and state string measuring doesn't match!");
        }
    }
}
```

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