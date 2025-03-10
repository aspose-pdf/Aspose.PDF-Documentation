---
title: Форматирование PDF документа с использованием C#
linktitle: Форматирование PDF документа
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/formatting-pdf-document/
description: Создайте и отформатируйте PDF документ с Aspose.PDF for .NET. Используйте следующий фрагмент кода для решения ваших задач.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formatting Document using C#",
    "alternativeHeadline": "Enhance PDF Formatting with Aspose.PDF for .NET",
    "abstract": "Откройте для себя мощную новую функцию Aspose.PDF for .NET, которая позволяет пользователям создавать и форматировать PDF документы без проблем. С полным контролем над свойствами документа, такими как настройки отображения окна, параметры встраивания шрифтов и настраиваемые коэффициенты масштабирования, разработчики могут улучшить пользовательский опыт и сохранить целостность документа на разных платформах. Оптимизируйте свои задачи манипуляции с PDF с помощью этой надежной функциональности, которая значительно повышает эффективность ваших .NET приложений.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Formatting PDF Document, Aspose.PDF for .NET, PDF document properties, embed fonts, font substitution, set zoom factor, document window properties, PDF manipulation library, PDF document generation, C# PDF formatting",
    "wordcount": "2526",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Создайте и отформатируйте PDF документ с Aspose.PDF for .NET. Используйте следующий фрагмент кода для решения ваших задач."
}
</script>

## Форматирование PDF документа

### Получение свойств окна документа и отображения страниц

Эта тема поможет вам понять, как получить свойства окна документа, приложения просмотра и как отображаются страницы. Чтобы установить эти свойства:

Откройте PDF файл с помощью класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Теперь вы можете установить свойства объекта Document, такие как

- CenterWindow – Центрировать окно документа на экране. По умолчанию: false.
- Direction – Порядок чтения. Это определяет, как страницы располагаются при отображении рядом. По умолчанию: слева направо.
- DisplayDocTitle – Отображать заголовок документа в строке заголовка окна документа. По умолчанию: false (заголовок отображается).
- HideMenuBar – Скрыть или отобразить панель меню окна документа. По умолчанию: false (панель меню отображается).
- HideToolBar – Скрыть или отобразить панель инструментов окна документа. По умолчанию: false (панель инструментов отображается).
- HideWindowUI – Скрыть или отобразить элементы окна документа, такие как полосы прокрутки. По умолчанию: false (элементы интерфейса отображаются).
- NonFullScreenPageMode – Как документ отображается, когда он не отображается в полноэкранном режиме.
- PageLayout – Макет страницы.
- PageMode – Как документ отображается при первом открытии. Опции: показать миниатюры, полноэкранный режим, показать панель вложений.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

Следующий фрагмент кода показывает, как получить свойства с использованием класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetDocumentWindow.pdf"))
    {
        // Get different document properties
        // Position of document's window - Default: false
        Console.WriteLine("CenterWindow : {0}", document.CenterWindow);

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        Console.WriteLine("Direction : {0}", document.Direction);

        // Whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        Console.WriteLine("DisplayDocTitle : {0}", document.DisplayDocTitle);

        // Whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        Console.WriteLine("FitWindow : {0}", document.FitWindow);

        // Whether to hide menu bar of the viewer application - Default: false
        Console.WriteLine("HideMenuBar : {0}", document.HideMenubar);

        // Whether to hide tool bar of the viewer application - Default: false
        Console.WriteLine("HideToolBar : {0}", document.HideToolBar);

        // Whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        Console.WriteLine("HideWindowUI : {0}", document.HideWindowUI);

        // Document's page mode. How to display document on exiting full-screen mode.
        Console.WriteLine("NonFullScreenPageMode : {0}", document.NonFullScreenPageMode);

        // The page layout i.e. single page, one column
        Console.WriteLine("PageLayout : {0}", document.PageLayout);

        // How the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        Console.WriteLine("PageMode : {0}", document.PageMode);
    }
}
```

### Установка свойств окна документа и отображения страниц

Эта тема объясняет, как установить свойства окна документа, приложения просмотра и отображения страниц. Чтобы установить эти различные свойства:

1. Откройте PDF файл с помощью класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Установите свойства объекта Document.
1. Сохраните обновленный PDF файл с помощью метода Save.

Доступные свойства:

- CenterWindow.
- Direction.
- DisplayDocTitle.
- FitWindow.
- HideMenuBar.
- HideToolBar.
- HideWindowUI.
- NonFullScreenPageMode.
- PageLayout.
- PageMode.

Каждое из них используется и описано в коде ниже. Следующий фрагмент кода показывает, как установить свойства с использованием класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDocumentWindowProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetDocumentWindow.pdf"))
    {
        // Set different document properties
        // Specify to position document's window - Default: false
        document.CenterWindow = true;

        // Predominant reading order; determines the position of page
        // When displayed side by side - Default: L2R
        document.Direction = Aspose.Pdf.Direction.R2L;

        // Specify whether window's title bar should display document title
        // If false, title bar displays PDF file name - Default: false
        document.DisplayDocTitle = true;

        // Specify whether to resize the document's window to fit the size of
        // First displayed page - Default: false
        document.FitWindow = true;

        // Specify whether to hide menu bar of the viewer application - Default: false
        document.HideMenubar = true;

        // Specify whether to hide tool bar of the viewer application - Default: false
        document.HideToolBar = true;

        // Specify whether to hide UI elements like scroll bars
        // And leaving only the page contents displayed - Default: false
        document.HideWindowUI = true;

        // Document's page mode. Specify how to display document on exiting full-screen mode.
        document.NonFullScreenPageMode = Aspose.Pdf.PageMode.UseOC;

        // Specify the page layout i.e. single page, one column
        document.PageLayout = Aspose.Pdf.PageLayout.TwoColumnLeft;

        // Specify how the document should display when opened
        // I.e. show thumbnails, full-screen, show attachment panel
        document.PageMode = Aspose.Pdf.PageMode.UseThumbs;

        // Save PDF document
        document.Save(dataDir + "SetDocumentWindow_out.pdf");
    }
}
```

### Встраивание шрифтов в существующий PDF файл

Читатели PDF поддерживают [ядро из 14 шрифтов](https://en.wikipedia.org/wiki/PDF#Text), чтобы документы могли отображаться одинаково независимо от платформы, на которой документ отображается. Когда PDF содержит шрифт, который не является одним из 14 основных шрифтов, встраивайте шрифт в PDF файл, чтобы избежать замены шрифта.

Aspose.PDF for .NET поддерживает встраивание шрифтов в существующие PDF файлы. Вы можете встроить полный шрифт или подмножество шрифта. Чтобы встроить шрифт, откройте PDF файл с помощью класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Затем используйте класс [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/net/aspose.pdf.text), чтобы встроить шрифт в PDF файл. Чтобы встроить полный шрифт, используйте свойство IsEmbeded класса Font; чтобы использовать подмножество шрифта, используйте свойство IsSubset.

{{% alert color="primary" %}}

Подмножество шрифта встраивает только те символы, которые используются, и полезно, когда шрифты используются для коротких предложений или слоганов, например, когда корпоративный шрифт используется для логотипа, но не для основного текста. Использование подмножества уменьшает размер выходного PDF файла. Однако, если для основного текста используется пользовательский шрифт, встраивайте его полностью.

{{% /alert %}}

Следующий фрагмент кода показывает, как встроить шрифт в PDF файл.

### Встраивание стандартных шрифтов типа 1

Некоторые PDF документы имеют шрифты из специального набора шрифтов Adobe. Шрифты из этого набора называются "Стандартные шрифты типа 1". Этот набор включает 14 шрифтов, и встраивание шрифтов этого типа требует использования специальных флагов, т.е. [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts). Следующий фрагмент кода можно использовать для получения документа со всеми встроенными шрифтами, включая стандартные шрифты типа 1:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontsType1ToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Set EmbedStandardFonts property of document
        document.EmbedStandardFonts = true;

        // Iterate through each page
        foreach (var page in document.Pages)
        {
            if (page.Resources.Fonts != null)
            {
                foreach (var pageFont in page.Resources.Fonts)
                {
                    // Check if font is already embedded
                    if (!pageFont.IsEmbedded)
                    {
                        pageFont.IsEmbedded = true;
                    }
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "EmbeddedFontsUpdated_out.pdf");
    }
}
```

### Встраивание шрифтов при создании PDF

Если вам нужно использовать любой шрифт, кроме 14 основных шрифтов, поддерживаемых Adobe Reader, вы должны встроить описание шрифта при генерации PDF файла. Если информация о шрифте не встроена, Adobe Reader возьмет ее из операционной системы, если она установлена на системе, или создаст заменяющий шрифт в соответствии с дескриптором шрифта в PDF.

> Пожалуйста, обратите внимание, что встроенный шрифт должен быть установлен на хост-машине, т.е. в случае следующего кода шрифт 'Univers Condensed' установлен на системе.

Мы используем свойство IsEmbedded класса Font, чтобы встроить информацию о шрифте в PDF файл. Установка значения этого свойства в 'True' встроит полный файл шрифта в PDF, зная, что это увеличит размер PDF файла. Следующий фрагмент кода можно использовать для встраивания информации о шрифте в PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EmbedFontWhileCreatingPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Create a section in the Pdf object
        var page = document.Pages.Add();

        // Create a TextFragment
        var fragment = new Aspose.Pdf.Text.TextFragment("");

        // Create a TextSegment with sample text
        var segment = new Aspose.Pdf.Text.TextSegment(" This is a sample text using Custom font.");

        // Create and configure TextState
        var ts = new Aspose.Pdf.Text.TextState();
        ts.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        ts.Font.IsEmbedded = true;
        segment.TextState = ts;

        // Add the segment to the fragment
        fragment.Segments.Add(segment);

        // Add the fragment to the page
        page.Paragraphs.Add(fragment);

        // Save PDF Document
        document.Save(dataDir + "EmbedFontWhileDocCreation_out.pdf");
    }
}
```

### Установка имени шрифта по умолчанию при сохранении PDF

Когда PDF документ содержит шрифты, которые недоступны в самом документе и на устройстве, API заменяет эти шрифты на шрифт по умолчанию. Когда шрифт доступен (установлен на устройстве или встроен в документ), выходной PDF должен иметь тот же шрифт (не должен заменяться на шрифт по умолчанию). Значение шрифта по умолчанию должно содержать имя шрифта (не путь к файлам шрифтов). Мы реализовали функцию установки имени шрифта по умолчанию при сохранении документа в PDF. Следующий фрагмент кода можно использовать для установки шрифта по умолчанию:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetDefaultFontOnDocumentSave(string documentName, string newName)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var fs = new FileStream(dataDir + "GetDocumentWindow.pdf", FileMode.Open))
    {
        using (var document = new Aspose.Pdf.Document(fs))
        {
            // Create PdfSaveOptions and specify Default Font Name
            var pdfSaveOptions = new Aspose.Pdf.PdfSaveOptions
            {
                DefaultFontName = newName
            };

            // Save PDF document
            document.Save(dataDir + "DefaultFont_out.pdf", pdfSaveOptions);
        }
    }
}
```

### Получение всех шрифтов из PDF документа

В случае, если вы хотите получить все шрифты из PDF документа, вы можете использовать метод FontUtilities.GetAllFonts(), предоставленный в классе [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Пожалуйста, проверьте следующий фрагмент кода, чтобы получить все шрифты из существующего PDF документа:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllFontsFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get all fonts used in the document
        var fonts = document.FontUtilities.GetAllFonts();

        // Iterate through each font and print its name
        foreach (var font in fonts)
        {
            Console.WriteLine(font.FontName);
        }
    }
}
```

### Получение предупреждений о замене шрифтов

Aspose.PDF for .NET предоставляет методы для получения уведомлений о замене шрифтов для обработки случаев замены шрифтов. Ниже приведены фрагменты кода, показывающие, как использовать соответствующую функциональность.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void NotificationFontSubstitution()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Attach the FontSubstitution event handler
        document.FontSubstitution += OnFontSubstitution;
        // You can use lambda
        // (oldFont, newFont) => Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        //                                                                        oldFont.FontName, newFont.FontName));

        // Save PDF document
        document.Save(dataDir + "NotificationFontSubstitution_out.pdf");
    }
}
```

Метод **OnFontSubstitution** представлен ниже.

```csharp
private static void OnFontSubstitution(Aspose.Pdf.Text.Font oldFont, Aspose.Pdf.Text.Font newFont)
{
    // Handle the font substitution event here
    Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        oldFont.FontName, newFont.FontName));
}
```

### Улучшение встраивания шрифтов с использованием FontSubsetStrategy

Функция встраивания шрифтов как подмножества может быть достигнута с использованием свойства IsSubset, но иногда вы хотите уменьшить полностью встроенный набор шрифтов только до подмножеств, которые используются в документе. Aspose.Pdf.Document имеет свойство FontUtilities, которое включает метод SubsetFonts(FontSubsetStrategy subsetStrategy). В методе SubsetFonts() параметр subsetStrategy помогает настроить стратегию подмножества. FontSubsetStrategy поддерживает два следующих варианта подмножества шрифтов.

- SubsetAllFonts - Это подмножество всех шрифтов, используемых в документе.
- SubsetEmbeddedFontsOnly - Это подмножество только тех шрифтов, которые полностью встроены в документ.

Следующий фрагмент кода показывает, как установить FontSubsetStrategy:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFontSubsetStrategy()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // All fonts will be embedded as subset into document in case of SubsetAllFonts.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetAllFonts);

        // Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
        document.FontUtilities.SubsetFonts(Aspose.Pdf.FontSubsetStrategy.SubsetEmbeddedFontsOnly);

        // Save PDF document
        document.Save(dataDir + "SetFontSubsetStrategy_out.pdf");
    }
}
```

### Получение-Установка коэффициента масштабирования PDF файла

Иногда вы хотите определить, каков текущий коэффициент масштабирования PDF документа. С помощью Aspose.Pdf вы можете узнать текущее значение, а также установить его.

Свойство Destination класса [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) позволяет получить значение масштабирования, связанное с PDF файлом. Аналогично, оно может быть использовано для установки коэффициента масштабирования файла.

#### Установка коэффициента масштабирования

Следующий фрагмент кода показывает, как установить коэффициент масштабирования PDF файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetZoomFactor.pdf"))
    {
        // Create GoToAction with a specific zoom factor
        var action = new Aspose.Pdf.Annotations.GoToAction(new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 0, 0, 0.5));
        document.OpenAction = action;

        // Save PDF document
        document.Save(dataDir + "ZoomFactor_out.pdf");
    }
}
```

#### Получение коэффициента масштабирования

Следующий фрагмент кода показывает, как получить коэффициент масштабирования PDF файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetZoomFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Zoomed_pdf.pdf"))
    {
        // Create GoToAction object
        if (document.OpenAction is Aspose.Pdf.Annotations.GoToAction action)
        {
            // Get the Zoom factor of PDF file
            if (action.Destination is Aspose.Pdf.Annotations.XYZExplicitDestination destination)
            {
                System.Console.WriteLine(destination.Zoom); // Document zoom value;
            }
        }
    }
}
```

### Установка предустановленных свойств диалогового окна печати

Aspose.PDF позволяет устанавливать предустановленные свойства диалогового окна печати PDF документа. Это позволяет вам изменить свойство DuplexMode для PDF документа, которое по умолчанию установлено на simplex. Это можно сделать с помощью двух различных методик, как показано ниже.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        // Set duplex printing to DuplexFlipLongEdge
        document.Duplex = Aspose.Pdf.PrintDuplex.DuplexFlipLongEdge;

        // Save PDF document
        document.Save(dataDir + "SetPrintDlgPresetProperties_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
    }
}
```

### Установка предустановленных свойств диалогового окна печати с использованием редактора содержимого PDF

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintDialogPresetPropertiesUsingPdfContentEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    string inputFile = dataDir + "input.pdf";

    using (var ed = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        ed.BindPdf(inputFile);

        // Check if the file has duplex flip short edge
        if ((ed.GetViewerPreference() & Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge) > 0)
        {
            Console.WriteLine("The file has duplex flip short edge");
        }

        // Change the viewer preference to duplex flip short edge
        ed.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.DuplexFlipShortEdge);

        // Save PDF document
        ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
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