---
title: 고급 기능
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 140
url: /ko/net/advanced-features/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Advanced Features",
    "alternativeHeadline": "Streamlined PDF Handling and Mathematical Expression Support in C#",
    "abstract": "물리적 저장소 없이 웹 브라우저로 PDF 문서를 직접 다운로드할 수 있도록 하는 Aspose.PDF for .NET의 최신 개선 사항을 발견하십시오. 이 기능은 파일 전송을 단순화할 뿐만 아니라 LaTeX를 사용하여 복잡한 수학적 표현을 포함하고 내장된 파일을 추출하는 고급 기능도 포함되어 있어 PDF 형식으로 작업하는 개발자에게 필수 도구입니다.",
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
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## 브라우저에 PDF 전송하여 다운로드

때때로 ASP.NET 애플리케이션을 개발할 때 PDF 파일을 물리적으로 저장하지 않고 웹 브라우저로 전송하여 다운로드해야 할 필요가 있습니다. 이를 달성하기 위해 PDF 문서를 생성한 후 MemoryStream 객체에 저장하고 해당 MemoryStream에서 바이트를 Response 객체로 전달할 수 있습니다. 이렇게 하면 브라우저가 생성된 PDF 문서를 다운로드하게 됩니다.

다음 코드 스니펫은 위 기능을 보여줍니다:
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

## 수학적 표현 추가를 위한 LaTeX 스크립트 사용

Aspose.PDF를 사용하면 LaTeX 스크립트를 사용하여 PDF 문서 내에 수학적 표현/공식을 추가할 수 있습니다. 다음 예제는 테이블 셀 내에 수학 공식을 추가하기 위해 이 기능을 두 가지 다른 방법으로 사용하는 방법을 보여줍니다:

### 전주 및 문서 환경 없이

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

### 전주 및 문서 환경 포함

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

### LaTeX 태그 지원

정렬 환경은 amsmath 패키지에서 정의되며, 증명 환경은 amsthm 패키지에서 정의됩니다. 따라서 문서 전주에서 \usepackage 명령을 사용하여 이러한 패키지를 지정해야 합니다. 이는 다음 코드 샘플에 표시된 것처럼 LaTeX 텍스트를 문서 환경에 포함해야 함을 의미합니다.

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