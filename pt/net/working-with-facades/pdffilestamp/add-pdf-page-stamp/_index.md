---
title: Adicionar Carimbo de Página PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/add-pdf-page-stamp/
description: Descubra como adicionar carimbos às páginas PDF em .NET, incluindo texto e imagens, para marca d'água ou branding usando Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Page Stamp",
    "alternativeHeadline": "Enhance PDFs with Custom Stamps and Page Numbers",
    "abstract": "Apresentando o recurso de Carimbo de Página PDF que permite aos usuários adicionar facilmente carimbos personalizados em todas ou em páginas específicas de um documento PDF usando a classe PdfFileStamp. Essa funcionalidade melhora a personalização do documento, permitindo vários atributos como rotação, fundo e estilos de numeração personalizados para carimbos de página, tornando seus arquivos PDF não apenas únicos, mas também profissionalmente polidos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1309",
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
    "url": "/net/add-pdf-page-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pdf-page-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Adicionar Carimbo de Página PDF em Todas as Páginas de um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) permite que você adicione um carimbo de página PDF em todas as páginas de um arquivo PDF. Para adicionar um carimbo de página PDF, você primeiro precisa criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) e [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você também precisa criar o carimbo de página PDF usando o método [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você pode definir outros atributos como origem, rotação, fundo etc. usando o objeto [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) também. Em seguida, você pode adicionar o carimbo no arquivo PDF usando o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). O seguinte trecho de código mostra como adicionar um carimbo de página PDF em todas as páginas de um arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "AddPageStampOnAllPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnAllPages_out.pdf");
    }
}
```

## Adicionar Carimbo de Página PDF em Páginas Específicas de um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) permite que você adicione um carimbo de página PDF em páginas específicas de um arquivo PDF. Para adicionar um carimbo de página PDF, você primeiro precisa criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) e [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você também precisa criar o carimbo de página PDF usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você pode definir outros atributos como origem, rotação, fundo etc. usando o objeto [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) também. Como você deseja adicionar um carimbo de página PDF em páginas específicas do arquivo PDF, você também precisa definir a propriedade [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Esta propriedade requer um array de inteiros contendo os números das páginas nas quais você deseja adicionar o carimbo. Em seguida, você pode adicionar o carimbo no arquivo PDF usando o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). O seguinte trecho de código mostra como adicionar um carimbo de página PDF em páginas específicas de um arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnCertainPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "PageStampOnCertainPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;
        stamp.Pages = new[] { 1, 3 };  // Apply stamp to specific pages (1 and 3)

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnCertainPages_out.pdf");
    }
}
```

## Adicionar Número de Página em um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) permite que você adicione números de página em um arquivo PDF. Para adicionar números de página, você primeiro precisa criar um objeto da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Se você deseja mostrar o número da página como “Página X de N”, onde X é o número da página atual e N é o número total de páginas no arquivo PDF, então você primeiro precisa obter a contagem de páginas usando a propriedade [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) da classe [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). Para obter o número da página atual, você pode usar o sinal **#** em seu texto onde quiser. Você pode formatar o texto do número da página usando a classe [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Se você deseja iniciar a numeração das páginas a partir de um número específico, então você pode definir a propriedade [StartingNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber). Uma vez que você esteja pronto para adicionar o número da página no arquivo, você precisa chamar o método [AddPageNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). O seguinte trecho de código mostra como adicionar um número de página em um arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;
        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```

### Estilo de Numeração Personalizado

A classe PdfFileStamp oferece o recurso de adicionar informações de Número de Página como objeto de carimbo dentro do documento PDF. Antes desta versão, a classe suportava apenas o estilo de numeração 1,2,3,4. No entanto, houve uma demanda de alguns clientes para usar um estilo de numeração personalizado ao colocar o carimbo de número de página dentro do documento PDF. Para atender a essa demanda, a propriedade [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle) foi introduzida, que aceita os valores da enumeração [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle). Especificados abaixo estão os valores oferecidos nesta enumeração.

- LetrasMinúsculas.
- LetrasMaiúsculas.
- NúmerosÁrabes.
- NúmerosRomanosMinúsculos.
- NúmerosRomanosMaiúsculos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCustomPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Specify numbering style as Numerals Roman UpperCase
        fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;

        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddCustomPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```