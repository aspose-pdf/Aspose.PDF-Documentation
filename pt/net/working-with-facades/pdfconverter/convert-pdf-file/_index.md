---
title: Converter Arquivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /pt/net/convert-pdf-file/
description: Aprenda como converter um arquivo PDF para vários formatos em .NET usando Aspose.PDF para um manuseio flexível de documentos.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF File",
    "alternativeHeadline": "Convert PDF Pages to Image Formats Efficiently",
    "abstract": "Desbloqueie o poder de Aspose.PDF for .NET Facades para converter facilmente páginas PDF em diversos formatos de imagem como JPEG, GIF e PNG com a classe PdfConverter. Este recurso permite controle detalhado sobre o processo de conversão, permitindo que você especifique parâmetros como resolução, tipo de coordenada e intervalo de páginas para uma saída personalizada. Aprimore suas capacidades de manuseio de documentos integrando conversões de PDF para imagem sem costura em suas aplicações.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "561",
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
    "url": "/net/convert-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Converter Páginas PDF para Diferentes Formatos de Imagem (Facades)

Para converter páginas PDF em diferentes formatos de imagem, você precisa criar um objeto [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) e abrir o arquivo PDF usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Depois disso, você precisa chamar o método [DoConvert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) para tarefas de inicialização. Em seguida, você pode percorrer todas as páginas usando os métodos [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) e [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6). O método [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) permite que você crie uma imagem de uma página específica. Você também precisa passar o ImageFormat para este método a fim de criar uma imagem de tipo específico, ou seja, JPEG, GIF ou PNG, etc. Finalmente, chame o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) da classe [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter). O seguinte trecho de código mostra como converter páginas PDF em imagens.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfPagesToImages01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfConverter object
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertPdfPagesToImages.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name with '_out' suffix
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}
```

No próximo trecho de código, mostraremos como você pode alterar alguns parâmetros. Com [CoordinateType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype) definimos o quadro 'CropBox'. Além disso, podemos alterar a [Resolution](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/resolution) especificando o número de pontos por polegada. O próximo é [FormPresentationMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - modo de apresentação do formulário. Em seguida, indicamos a [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/startpage) com a qual o número da página de início da conversão é definido. Também podemos especificar a última página definindo um intervalo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfPagesToImages02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfConverter object
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertPdfPagesToImages.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Set additional conversion settings
        converter.CoordinateType = Aspose.Pdf.PageCoordinateType.CropBox;
        converter.Resolution = new Aspose.Pdf.Devices.Resolution(600);
        converter.FormPresentationMode = Aspose.Pdf.Devices.FormPresentationMode.Production;
        converter.StartPage = 2;

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}
```

## Converter Páginas PDF para Formatos de Imagem com Substituição de Fonte Personalizada

No próximo trecho de código, demonstramos como aplicar substituição de fonte personalizada durante o processo de conversão de PDF para imagem. Usamos a coleção FontRepository.Substitutions para registrar uma regra de substituição personalizada. Neste exemplo, quando a fonte "Helvetica" é encontrada, ela é substituída por "Arial".

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertWithCustomFontSubstitution()
{
    // Add custom font substitution
    Aspose.Pdf.Text.FontRepository.Substitutions.Add(new CustomPdfFontSubstitution());

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    using (var converter = new Aspose.Pdf.Facades.PdfConverter())
    {
        // Bind PDF document
        converter.BindPdf(dataDir + "ConvertWithSubstitution.pdf");

        // Initialize the converting process
        converter.DoConvert();

        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Generate output file name with '_out' suffix
            var outputFileName = dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg";
            // Convert the page to image and save it
            converter.GetNextImage(outputFileName, System.Drawing.Imaging.ImageFormat.Jpeg);
        }
    }
}

private class CustomPdfFontSubstitution : Aspose.Pdf.Text.CustomFontSubstitutionBase
{
    public override bool TrySubstitute(
        Aspose.Pdf.Text.CustomFontSubstitutionBase.OriginalFontSpecification originalFontSpecification,
        out Aspose.Pdf.Text.Font substitutionFont)
    {
        if (originalFontSpecification.OriginalFontName == "Helvetica")
        {
            substitutionFont = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
            return true;
        }
        // Default substitution logic
        return base.TrySubstitute(originalFontSpecification, out substitutionFont);
    }
}
```

## Veja também

Aspose.PDF for .NET permite converter documentos PDF para vários formatos e também converter de outros formatos para PDF. Além disso, você pode verificar a qualidade da conversão do Aspose.PDF e visualizar os resultados online com o aplicativo de conversão Aspose.PDF. Aprenda na seção [Convertendo](/pdf/pt/net/converting/) para resolver suas tarefas.