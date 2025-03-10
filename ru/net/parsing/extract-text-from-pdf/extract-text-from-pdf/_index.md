---
title: Извлечение текста из PDF C#
linktitle: Извлечение текста из PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/extract-text-from-all-pdf/
description: Эта статья описывает различные способы извлечения текста из PDF-документов с использованием Aspose.PDF в C#.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF C#",
    "alternativeHeadline": "Effortlessly Extract Text from PDFs in C#",
    "abstract": "Откройте для себя мощную новую функциональность в Aspose.PDF for .NET, которая позволяет разработчикам легко извлекать текст из PDF-документов. Эта функция поддерживает извлечение со всех страниц или из определенных областей, учитывает многостолбцовые макеты и даже позволяет извлекать выделенный текст всего за несколько строк кода. Улучшите свои возможности обработки документов и упростите извлечение контента с помощью этого универсального инструмента.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2005",
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
    "url": "/net/extract-text-from-all-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text-from-all-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Извлечение текста со всех страниц PDF-документа

Извлечение текста из PDF-документа является распространенной задачей. В этом примере вы увидите, как Aspose.PDF for .NET позволяет извлекать текст со всех страниц PDF-документа. Вам нужно создать объект класса **TextAbsorber**. После этого откройте PDF с помощью класса **Document** и вызовите метод **Accept** коллекции **Pages**. Класс **TextAbsorber** поглощает текст из документа и возвращает его в свойстве **Text**. Следующий фрагмент кода показывает, как извлечь текст со всех страниц PDF-документа.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for all the pages
        document.Pages.Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

Вызовите метод **Accept** на конкретной странице объекта Document. Индекс — это номер конкретной страницы, с которой нужно извлечь текст.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for a particular page
        document.Pages[1].Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text_out.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## Извлечение текста со страниц с использованием Text Device

Вы можете использовать класс **TextDevice** для извлечения текста из PDF-файла. TextDevice использует TextAbsorber в своей реализации, таким образом, на самом деле они делают одно и то же, но TextDevice просто реализован для унификации подхода "Device" для извлечения всего из страницы ImageDevice, PageDevice и т.д. TextAbsorber может извлекать текст со страницы, всего PDF или XForm, этот TextAbsorber более универсален.

### Извлечение текста со всех страниц

Следующие шаги и фрагмент кода показывают, как извлечь текст из PDF с использованием текстового устройства.

1. Создайте объект класса Document с указанным входным PDF-файлом.
1. Создайте объект класса TextDevice.
1. Используйте объект класса TextExtractOptions для указания параметров извлечения.
1. Используйте метод Process класса TextDevice для преобразования содержимого в текст.
1. Сохраните текст в выходной файл.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPagesWithTextDevice()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var builder = new System.Text.StringBuilder();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {
        // String to hold extracted text
        string extractedText = "";

        foreach (var page in document.Pages)
        {
            using (MemoryStream textStream = new MemoryStream())
            {
                // Create text device
                var textDevice = new Aspose.Pdf.Devices.TextDevice();

                // Set text extraction options - set text extraction mode (Raw or Pure)
                var textExtOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
                textDevice.ExtractionOptions = textExtOptions;

                // Convert a particular page and save text to the stream
                textDevice.Process(page, textStream);
                // Convert a particular page and save text to the stream
                textDevice.Process(document.Pages[1], textStream);

                // Get text from memory stream
                extractedText = System.Text.Encoding.Unicode.GetString(textStream.ToArray());
            }
            builder.Append(extractedText);
        }
    }

    // Save the extracted text in text file
    File.WriteAllText(dataDir + "input_Text_Extracted_out.txt", builder.ToString());
}
```

## Извлечение текста из определенной области страницы

Класс **TextAbsorber** предоставляет возможность извлекать текст из определенной или всех страниц PDF-документа. Этот класс возвращает извлеченный текст в свойстве **Text**. Однако, если у нас есть необходимость извлечь текст из определенной области страницы, мы можем использовать свойство **Rectangle** класса **TextSearchOptions**. Свойство Rectangle принимает объект Rectangle в качестве значения, и с помощью этого свойства мы можем указать область страницы, из которой нам нужно извлечь текст.

Метод **Accept** страницы вызывается для извлечения текста. Создайте объекты классов **Document** и **TextAbsorber**. Вызовите метод **Accept** на отдельной странице, как индекс **Page**, объекта **Document**. Индекс — это номер конкретной страницы, с которой нужно извлечь текст. Вы можете получить текст из свойства **Text** класса **TextAbsorber**. Следующий фрагмент кода показывает, как извлечь текст с отдельной страницы.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromParticularPageRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var absorber = new Aspose.Pdf.Text.TextAbsorber();
        absorber.TextSearchOptions.LimitToPageBounds = true;
        absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

        // Accept the absorber for first page
        document.Pages[1].Accept(absorber);

        // Get the extracted text
        string extractedText = absorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## Извлечение текста на основе колонок

PDF-файл может состоять из элементов текста, изображений, аннотаций, вложений, графиков и т.д., и Aspose.PDF for .NET предлагает возможность добавлять и манипулировать всеми этими элементами. Этот API замечателен, когда речь идет о добавлении текста и извлечении его из PDF-документа, и мы можем столкнуться со сценарием, когда PDF-документ состоит из более чем одной колонки (многостолбцовый) и нам нужно извлечь содержимое страницы, сохраняя тот же макет, тогда Aspose.PDF for .NET — правильный выбор для выполнения этой задачи. Один из подходов — уменьшить размер шрифта содержимого внутри PDF-документа, а затем выполнить извлечение текста. Следующий фрагмент кода показывает шаги по уменьшению размера текста и затем попытке извлечь текст из PDF-документа.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextBasedOnColumns()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var extractedText = string.Empty;
    // Open PDF document
    using (var sourceDocument = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        sourceDocument.Pages.Accept(textFragmentAbsorber);
        Aspose.Pdf.Text.TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
        foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentCollection)
        {
            // Need to reduce font size at least for 70%
            textFragment.TextState.FontSize = textFragment.TextState.FontSize * 0.7f;
        }
        using (Stream sourceStream = new MemoryStream())
        {
            sourceDocument.Save(sourceStream);
            using (var destDocument = new Aspose.Pdf.Document(sourceStream))
            {
                var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
                destDocument.Pages.Accept(textAbsorber);
                extractedText = textAbsorber.Text;
                textAbsorber.Visit(destDocument);
            }
        }

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractColumnsText_out.txt", extractedText);
    }
}
```

### Второй подход - Использование ScaleFactor

В этом новом релизе мы также представили несколько улучшений в TextAbsorber и во внутреннем механизме форматирования текста. Теперь при извлечении текста с использованием режима «Чистый» вы можете указать параметр ScaleFactor, и это может быть еще одним подходом для извлечения текста из многостолбцового PDF-документа, помимо вышеуказанного подхода. Этот коэффициент масштаба может быть установлен для настройки сетки, которая используется для внутреннего механизма форматирования текста во время извлечения текста. Указание значений ScaleFactor между 1 и 0.1 (включая 0.1) имеет такой же эффект, как и уменьшение шрифта.

Указание значений ScaleFactor между 0.1 и -0.1 рассматривается как нулевое значение, но это заставляет алгоритм автоматически рассчитывать необходимый коэффициент масштаба во время извлечения текста. Расчет основан на средней ширине глифа самого популярного шрифта на странице, но мы не можем гарантировать, что в извлеченном тексте ни одна строка колонки не достигает начала следующей колонки. Пожалуйста, обратите внимание, что если значение ScaleFactor не указано, будет использоваться значение по умолчанию 1.0. Это означает, что масштабирование не будет выполнено. Если указанное значение ScaleFactor больше 10 или меньше -0.1, будет использоваться значение по умолчанию 1.0.

Мы предлагаем использовать авто-масштабирование (ScaleFactor = 0) при обработке большого количества PDF-файлов для извлечения текстового содержимого. Или вручную установить избыточное уменьшение ширины сетки (около ScaleFactor = 0.5). Однако вы не должны определять, необходимо ли масштабирование для конкретных документов или нет. Если вы установите избыточное уменьшение ширины сетки для документа (который в этом не нуждается), извлеченное текстовое содержимое останется полностью адекватным. Пожалуйста, посмотрите следующий фрагмент кода.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExctractTextWithScaleFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
        textAbsorber.ExtractionOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
        // Setting scale factor to 0.5 is enough to split columns in the majority of documents
        // Setting of zero allows to algorithm choose scale factor automatically
        textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
        document.Pages.Accept(textAbsorber);
        var extractedText = textAbsorber.Text;

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
    }
}
```

{{% alert color="primary" %}}

Пожалуйста, обратите внимание, что нет прямого соответствия между новым ScaleFactor и старым коэффициентом ручного уменьшения шрифта. Однако по умолчанию алгоритм учитывает значение размера шрифта, которое уже было уменьшено по некоторым внутренним причинам. Например, уменьшение размера шрифта с 10 до 7 имеет такой же эффект, как установка коэффициента масштаба на 5/8 (= 0.625).

{{% /alert %}}

## Извлечение выделенного текста из PDF-документа

В различных сценариях извлечения текста из PDF-документа вы можете столкнуться с необходимостью извлечь только выделенный текст из PDF-документа. Для реализации этой функциональности мы добавили методы TextMarkupAnnotation.GetMarkedText() и TextMarkupAnnotation.GetMarkedTextFragments() в API. Вы можете извлечь выделенный текст из PDF-документа, фильтруя TextMarkupAnnotation и используя указанные методы. Следующий фрагмент кода показывает, как вы можете извлечь выделенный текст из PDF-документа.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractHighlightedTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractHighlightedText.pdf"))
    {
        // Loop through all the annotations
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[1].Annotations)
        {
            // Filter TextMarkupAnnotation
            if (annotation is Aspose.Pdf.Annotations.TextMarkupAnnotation)
            {
                var highlightedAnnotation = annotation as Aspose.Pdf.Annotations.TextMarkupAnnotation;
                // Retrieve highlighted text fragments
                Aspose.Pdf.Text.TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
                foreach (Aspose.Pdf.Text.TextFragment textFragment in collection)
                {
                    // Display highlighted text
                    Console.WriteLine(textFragment.Text);
                }
            }
        }
    }
}
```

## Доступ к элементам Text Fragment и Segment из XML

Иногда нам нужно получить доступ к элементам TextFragment или TextSegment при обработке PDF-документов, сгенерированных из XML. Aspose.PDF for .NET предоставляет доступ к таким элементам по имени. Ниже приведен фрагмент кода, который показывает, как использовать эту функциональность.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessTextFragmentAndSegmentElementsFromXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.BindXml(dataDir + "40014.xml");

        // Get page
        var page = (Aspose.Pdf.Page)document.GetObjectById("mainSection");

        // Get elements by Id
        var segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("boldHtml");
        segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("strongHtml");

        // Save PDF document
        document.Save(dataDir + "DocumentFromXML_out.pdf");
    }
}
```