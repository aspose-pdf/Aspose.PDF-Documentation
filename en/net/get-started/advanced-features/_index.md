---
title: Advanced Features
type: docs
weight: 140
url: /net/advanced-features/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Advanced Features",
    "alternativeHeadline": "Streamlined PDF Handling and Mathematical Expression Support in C#",
    "abstract": "Discover the latest enhancement in Aspose.PDF for .NET that allows seamless sending of PDF documents to web browsers for direct download without the need for physical storage. This feature not only simplifies file delivery but also includes advanced capabilities to extract embedded files and incorporate complex mathematical expressions using LaTeX, making it an essential tool for developers working with PDF formats",
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
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Sending Pdf to Browser for Download

Sometimes when you are developing an ASP.NET application, you need to send PDF file(s) to web browser(s) for download without saving them physically. In order to achieve that you can save PDF document into MemoryStream object after generating it and pass bytes from that MemoryStream to Response object. Doing this will make the browser to download the generated PDF document.

Following code snippet demonstrate the above functionality:
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

## Use of Latex Script to Add Mathematical Expressions

With Aspose.PDF, you can add mathematical expressions/formulas inside PDF document using latex script. Following examples show how this feature can be used in two different ways, in order to add a mathematical formula inside a table cell:

### Without preamble and document environment

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET      
private static void LatexWithoutPreambleAndDocEnvironment()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add Page in Pages Collection
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

### With preamble and document environment

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LatexWithPreambleAndDocEnvironment()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add Page in Pages Collection
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

### Support for Latex Tags

The align environment is defined in amsmath package, and proof environment is defined in amsthm package. Thus, you have to specify these packages using \usepackage command in the document preamble. And this means that you have to enclose the LaTeX text into document environment either as shown in the following code sample.

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
    string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = doc.Pages.Add();
        var latex = new Aspose.Pdf.TeXFragment(s);
        page.Paragraphs.Add(latex);
        // Save PDF document
        document.Save(dataDir + "Script_out.pdf");
    }
}
```
