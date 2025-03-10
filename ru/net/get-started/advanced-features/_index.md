---
title: Расширенные функции
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 140
url: /ru/net/advanced-features/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Advanced Features",
    "alternativeHeadline": "Streamlined PDF Handling and Mathematical Expression Support in C#",
    "abstract": "Узнайте о последнем улучшении в Aspose.PDF for .NET, которое позволяет без проблем отправлять PDF-документы в веб-браузеры для прямой загрузки без необходимости физического хранения. Эта функция не только упрощает доставку файлов, но и включает в себя расширенные возможности извлечения встроенных файлов и интеграции сложных математических выражений с использованием LaTeX, что делает ее незаменимым инструментом для разработчиков, работающих с форматами PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "386",
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
    "url": "/net/advanced-features/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/advanced-features/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Отправка PDF в браузер для загрузки

Иногда, когда вы разрабатываете приложение ASP.NET, вам нужно отправить PDF-файл(ы) в веб-браузер(ы) для загрузки без их физического сохранения. Чтобы достичь этого, вы можете сохранить PDF-документ в объекте MemoryStream после его генерации и передать байты из этого MemoryStream в объект Response. Это заставит браузер загрузить сгенерированный PDF-документ.

Следующий фрагмент кода демонстрирует вышеуказанную функциональность:
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private void Page_Load(object sender, EventArgs e)
{
    // Clear the response before writing to it
    Response.Clear();
    // Set content type for PDF
    Response.ContentType = "application/pdf";
    // Set the response header for file download
    Response.AddHeader("content-disposition", "attachment; filename=TestDocument.pdf");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add Page in Pages Collection
        var page = document.Pages.Add();
        var textFragment = new Aspose.Pdf.Text.TextFragment("Hello World");
        page.Paragraphs.Add(textFragment);
        
        // Save PDF document to a MemoryStream
        using (var ms = new MemoryStream())
        {
            document.Save(ms);
             // Reset the stream position to the beginning
            ms.Position = 0;

            // Write the MemoryStream to the response
            ms.CopyTo(Response.OutputStream);
            Response.AddHeader("content-length", ms.Length.ToString());
            Response.Flush();
            // Suppress the remaining content
            Response.SuppressContent = true; 
        }
    }
    // End the response to prevent further processing
    Response.End(); 
}
```

## Использование скрипта LaTeX для добавления математических выражений

С помощью Aspose.PDF вы можете добавлять математические выражения/формулы в PDF-документ, используя скрипт LaTeX. Следующие примеры показывают, как эта функция может быть использована двумя различными способами для добавления математической формулы в ячейку таблицы:

### Без преамбулы и окружения документа

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET      
private static void LatexWithoutPreambleAndDocEnvironment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = doc.Pages.Add();
        // Create a Table
        var table = new Aspose.Pdf.Table();
        // Add a row into Table
        var row = table.Rows.Add();
        // Add Cell with Latex Script to add methematical expressions/formulae
        var latexText1 = "$123456789+\\sqrt{1}+\\int_a^b f(x)dx$";
        var cell = row.Cells.Add();
        cell.Margin = new MarginInfo { Left = 20, Right = 20, Top = 20, Bottom = 20 };
        // Second TeXFragment constructor bool parameter provides LaTeX paragraph indents elimination
        var ltext1 = new Aspose.Pdf.TeXFragment(latexText1, true);
        cell.Paragraphs.Add(ltext1);
        // Add table inside page
        page.Paragraphs.Add(table);
        // Save PDF document
        document.Save(dataDir + "LatextScriptInPdf_out.pdf");
    }
}
```

### С преамбулой и окружением документа

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LatexWithPreambleAndDocEnvironment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = doc.Pages.Add();
        // Create a Table
        var table = new Aspose.Pdf.Table();
        // Add a row into Table
        var row = table.Rows.Add();
       // Add Cell with Latex Script to add methematical expressions/formulae
        var latexText2 = @"\documentclass{article}
                            \begin{document}
                            Latex and the document class will normally take care of page layout issues for you. For submission to an academic publication, this entire topic will be out
                            \end{document}";
        var cell = row.Cells.Add();
        cell.Margin = new Aspose.Pdf.MarginInfo { Left = 20, Right = 20, Top = 20, Bottom = 20 };
        var text2 = new Aspose.Pdf.HtmlFragment(latexText2);
        cell.Paragraphs.Add(text2);
        // Add table inside page
        page.Paragraphs.Add(table);
        // Save PDF document
        document.Save(dataDir + "LatextScriptInPdf2_out.pdf");
    }
}
```

### Поддержка тегов LaTeX

Окружение align определяется в пакете amsmath, а окружение proof определяется в пакете amsthm. Таким образом, вам нужно указать эти пакеты с помощью команды \usepackage в преамбуле документа. Это означает, что вам нужно заключить текст LaTeX в окружение документа, как показано в следующем примере кода.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LatexTagsSupport()
{
    var s = @"
    \usepackage{amsmath,amsthm}
    \begin{document}
    \begin{proof} The proof is a follows: 
    \begin{align}
    (x+y)^3&=(x+y)(x+y)^2
    (x+y)(x^2+2xy+y^2)\\
    &=x^3+3x^2y+3xy^3+x^3.\qedhere
    \end{align}
    \end{proof}
    \end{document}";

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var latex = new Aspose.Pdf.TeXFragment(s);
        page.Paragraphs.Add(latex);
        // Save PDF document
        document.Save(dataDir + "Script_out.pdf");
    }
}
```