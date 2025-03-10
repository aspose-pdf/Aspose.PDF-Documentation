---
title: Formatando Documento PDF usando C#
linktitle: Formatando Documento PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/formatting-pdf-document/
description: Crie e formate o Documento PDF com Aspose.PDF for .NET. Use o próximo trecho de código para resolver suas tarefas.
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
    "abstract": "Descubra o poderoso novo recurso de Aspose.PDF for .NET que permite aos usuários criar e formatar documentos PDF de forma contínua. Com controle abrangente sobre propriedades do documento, como configurações de exibição da janela, opções de incorporação de fontes e fatores de zoom personalizáveis, os desenvolvedores podem melhorar a experiência do usuário e manter a integridade do documento em diferentes plataformas. Otimize suas tarefas de manipulação de PDF com essa funcionalidade robusta que melhora significativamente a eficiência de suas aplicações .NET",
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
    "description": "Crie e formate o Documento PDF com Aspose.PDF for .NET. Use o próximo trecho de código para resolver suas tarefas."
}
</script>

## Formatando Documento PDF

### Obter Propriedades da Janela do Documento e Exibição da Página

Este tópico ajuda você a entender como obter propriedades da janela do documento, aplicativo visualizador e como as páginas são exibidas. Para definir essas propriedades:

Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Agora, você pode definir as propriedades do objeto Document, como

- CenterWindow – Centraliza a janela do documento na tela. Padrão: falso.
- Direction – Ordem de leitura. Isso determina como as páginas são dispostas quando exibidas lado a lado. Padrão: da esquerda para a direita.
- DisplayDocTitle – Exibe o título do documento na barra de título da janela do documento. Padrão: falso (o título é exibido).
- HideMenuBar – Oculta ou exibe a barra de menu da janela do documento. Padrão: falso (a barra de menu é exibida).
- HideToolBar – Oculta ou exibe a barra de ferramentas da janela do documento. Padrão: falso (a barra de ferramentas é exibida).
- HideWindowUI – Oculta ou exibe elementos da janela do documento, como barras de rolagem. Padrão: falso (os elementos da interface do usuário são exibidos).
- NonFullScreenPageMode – Como o documento é exibido quando não está em modo de página cheia.
- PageLayout – O layout da página.
- PageMode – Como o documento é exibido quando é aberto pela primeira vez. As opções são mostrar miniaturas, tela cheia, mostrar painel de anexos.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

O seguinte trecho de código mostra como obter as propriedades usando a classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

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

### Definir Propriedades da Janela do Documento e Exibição da Página

Este tópico explica como definir as propriedades da janela do documento, aplicativo visualizador e exibição da página. Para definir essas diferentes propriedades:

1. Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Defina as propriedades do objeto Document.
1. Salve o arquivo PDF atualizado usando o método Save.

As propriedades disponíveis são:

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

Cada uma é usada e descrita no código abaixo. O seguinte trecho de código mostra como definir as propriedades usando a classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

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

### Incorporando Fontes em um arquivo PDF existente

Leitores de PDF suportam [um núcleo de 14 fontes](https://en.wikipedia.org/wiki/PDF#Text) para que os documentos possam ser exibidos da mesma forma, independentemente da plataforma em que o documento é exibido. Quando um PDF contém uma fonte que não é uma das 14 fontes principais, incorpore a fonte no arquivo PDF para evitar a substituição de fontes.

Aspose.PDF for .NET suporta a incorporação de fontes em arquivos PDF existentes. Você pode incorporar uma fonte completa ou um subconjunto da fonte. Para incorporar a fonte, abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Em seguida, use a classe [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/net/aspose.pdf.text) para incorporar a fonte no arquivo PDF. Para incorporar a fonte completa, use a propriedade IsEmbeded da classe Font; para usar um subconjunto da fonte, use a propriedade IsSubset.

{{% alert color="primary" %}}

Um subconjunto de fonte incorpora apenas os caracteres que são usados e é útil onde as fontes são usadas para frases curtas ou slogans, por exemplo, onde uma fonte corporativa é usada para um logotipo, mas não para o texto do corpo. Usar um subconjunto reduz o tamanho do arquivo do PDF de saída. No entanto, se uma fonte personalizada for usada para o texto do corpo, incorpore-a na íntegra.

{{% /alert %}}

O seguinte trecho de código mostra como incorporar uma fonte em um arquivo PDF.

### Incorporando Fontes Padrão Tipo 1

Alguns documentos PDF têm fontes de um conjunto especial de fontes da Adobe. Fontes desse conjunto são chamadas de “Fontes Padrão Tipo 1”. Este conjunto inclui 14 fontes e a incorporação desse tipo de fontes requer o uso de flags especiais, ou seja, [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts). A seguir está o trecho de código que pode ser usado para obter um documento com todas as fontes incorporadas, incluindo Fontes Padrão Tipo 1:

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

### Incorporando Fontes ao criar PDF

Se você precisar usar qualquer fonte além das 14 fontes principais suportadas pelo Adobe Reader, deve incorporar a descrição da fonte ao gerar o arquivo PDF. Se as informações da fonte não forem incorporadas, o Adobe Reader as obterá do sistema operacional se estiver instalado no sistema, ou construirá uma fonte substituta de acordo com o descritor da fonte no PDF.

>Por favor, note que a fonte incorporada deve estar instalada na máquina host, ou seja, no caso do seguinte código, a fonte ‘Univers Condensed’ está instalada no sistema.

Usamos a propriedade IsEmbedded da classe Font para incorporar as informações da fonte no arquivo PDF. Definir o valor dessa propriedade como ‘True’ incorporará o arquivo de fonte completo no PDF, sabendo que isso aumentará o tamanho do arquivo PDF. A seguir está o trecho de código que pode ser usado para incorporar as informações da fonte no PDF.

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

### Definir Nome da Fonte Padrão ao Salvar PDF

Quando um documento PDF contém fontes que não estão disponíveis no próprio documento e no dispositivo, a API substitui essas fontes pela fonte padrão. Quando a fonte está disponível (está instalada no dispositivo ou está incorporada no documento), o PDF de saída deve ter a mesma fonte (não deve ser substituída pela fonte padrão). O valor da fonte padrão deve conter o nome da fonte (não o caminho para os arquivos de fonte). Implementamos um recurso para definir o nome da fonte padrão ao salvar um documento como PDF. O seguinte trecho de código pode ser usado para definir a fonte padrão:

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

### Obter Todas as Fontes do Documento PDF

Caso você queira obter todas as fontes de um documento PDF, pode usar o método FontUtilities.GetAllFonts() fornecido na classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Por favor, verifique o seguinte trecho de código para obter todas as fontes de um documento PDF existente:

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

### Obter Avisos para Substituição de Fontes

Aspose.PDF for .NET fornece métodos para obter notificações sobre substituição de fontes para lidar com casos de substituição de fontes. Os trechos de código abaixo mostram como usar a funcionalidade correspondente.

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

O **OnFontSubstitution** método é conforme listado abaixo.

```csharp
private static void OnFontSubstitution(Aspose.Pdf.Text.Font oldFont, Aspose.Pdf.Text.Font newFont)
{
    // Handle the font substitution event here
    Console.WriteLine(string.Format("Font '{0}' was substituted with another font '{1}'",
        oldFont.FontName, newFont.FontName));
}
```

### Melhorar a Incorporação de Fontes usando FontSubsetStrategy

O recurso para incorporar as fontes como um subconjunto pode ser realizado usando a propriedade IsSubset, mas às vezes você deseja reduzir um conjunto de fontes totalmente incorporadas apenas para subconjuntos que são usados no documento. Aspose.Pdf.Document tem a propriedade FontUtilities que inclui o método SubsetFonts(FontSubsetStrategy subsetStrategy). No método SubsetFonts(), o parâmetro subsetStrategy ajuda a ajustar a estratégia de subconjunto. FontSubsetStrategy suporta duas variantes seguintes de subconjunto de fontes.

- SubsetAllFonts - Isso irá subdefinir todas as fontes usadas em um documento.
- SubsetEmbeddedFontsOnly - Isso irá subdefinir apenas aquelas fontes que estão totalmente incorporadas no documento.

O seguinte trecho de código mostra como definir FontSubsetStrategy:

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

### Obter-Definir Fator de Zoom do Arquivo PDF

Às vezes, você deseja determinar qual é o fator de zoom atual de um documento PDF. Com Aspose.Pdf, você pode descobrir o valor atual, bem como definir um.

A propriedade Destination da classe [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) permite que você obtenha o valor de zoom associado a um arquivo PDF. Da mesma forma, pode ser usada para definir o fator de zoom de um arquivo.

#### Definir Fator de Zoom

O seguinte trecho de código mostra como definir o fator de zoom de um arquivo PDF.

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

#### Obter Fator de Zoom

O seguinte trecho de código mostra como obter o fator de zoom de um arquivo PDF.

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

### Definindo Propriedades de Predefinição do Diálogo de Impressão

Aspose.PDF permite definir as propriedades de predefinição do diálogo de impressão de um documento PDF. Ele permite que você altere a propriedade DuplexMode para um documento PDF que é definido como simplex por padrão. Isso pode ser alcançado usando duas metodologias diferentes, conforme mostrado abaixo.

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

### Definindo Propriedades de Predefinição do Diálogo de Impressão usando Editor de Conteúdo PDF

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