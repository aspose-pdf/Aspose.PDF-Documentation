---
title: Obter e Definir Propriedades da Página
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
url: /pt/net/get-and-set-page-properties/
description: Aprenda como obter e definir propriedades de página para documentos PDF usando Aspose.PDF for .NET, permitindo formatação personalizada de documentos.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get and Set Page Properties",
    "alternativeHeadline": "Manage PDF Page Properties with Ease",
    "abstract": "O recurso Obter e Definir Propriedades da Página em Aspose.PDF for .NET capacita os desenvolvedores a acessar e manipular atributos de página PDF sem esforço. Essa funcionalidade permite que os usuários recuperem informações críticas, como contagens de páginas e propriedades específicas, como tipos de cor, caixas de mídia e caixas de corte, tudo com apenas algumas linhas de código. Melhore suas capacidades de gerenciamento de documentos PDF hoje aproveitando este recurso robusto para manipulação eficiente de PDF em aplicações .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1117",
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
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

Aspose.PDF for .NET permite que você leia e defina propriedades de páginas em um arquivo PDF em suas aplicações .NET. Esta seção mostra como obter o número de páginas em um arquivo PDF, obter informações sobre propriedades de página PDF, como cor, e definir propriedades de página. Os exemplos dados estão em C#, mas você pode usar qualquer linguagem .NET, como VB.NET, para alcançar o mesmo.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Obter Número de Páginas em um Arquivo PDF

Ao trabalhar com documentos, você frequentemente quer saber quantas páginas eles contêm. Com Aspose.PDF, isso não leva mais do que duas linhas de código.

Para obter o número de páginas em um arquivo PDF:

1. Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Em seguida, use a propriedade Count da coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) (do objeto Document) para obter o número total de páginas no documento.

O seguinte trecho de código mostra como obter o número de páginas de um arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetNumberOfPagesInAPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetNumberofPages.pdf"))
    {
        // Get page count
        System.Console.WriteLine("Page Count : {0}", document.Pages.Count);
    }
}
```

### Obter contagem de páginas sem salvar o documento

Às vezes, geramos os arquivos PDF dinamicamente e, durante a criação do arquivo PDF, podemos nos deparar com a necessidade (criando Índice, etc.) de obter a contagem de páginas do arquivo PDF sem salvar o arquivo no sistema ou stream. Portanto, para atender a essa necessidade, um método [ProcessParagraphs](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/processparagraphs) foi introduzido na classe Document. Por favor, dê uma olhada no seguinte trecho de código que mostra os passos para obter a contagem de páginas sem salvar o documento.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPageCountWithoutSavingTheDocument()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create loop instance
        for (var i = 0; i < 300; i++)
        {
            // Add TextFragment to paragraphs collection of page object
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Pages count test"));
        }
        // Process the paragraphs in PDF file to get accurate page count
        document.ProcessParagraphs();
        // Print number of pages in document
        Console.WriteLine("Number of pages in document = " + document.Pages.Count);
    }
}
```

## Obter Propriedades da Página

Cada página em um arquivo PDF possui um número de propriedades, como largura, altura, bleed-, crop- e trimbox. Aspose.PDF permite que você acesse essas propriedades.

### **Entendendo Propriedades da Página: a Diferença entre Artbox, BleedBox, CropBox, MediaBox, TrimBox e propriedade Rect**

- **Media box**: A media box é a maior caixa de página. Ela corresponde ao tamanho da página (por exemplo, A4, A5, Carta dos EUA, etc.) selecionado quando o documento foi impresso em PostScript ou PDF. Em outras palavras, a media box determina o tamanho físico da mídia na qual o documento PDF é exibido ou impresso.
- **Bleed box**: Se o documento tiver bleed, o PDF também terá uma bleed box. Bleed é a quantidade de cor (ou arte) que se estende além da borda de uma página. É usado para garantir que, quando o documento é impresso e cortado para o tamanho (“trimmed”), a tinta vá até a borda da página. Mesmo que a página seja mal cortada - cortada ligeiramente fora das marcas de corte - nenhuma borda branca aparecerá na página.
- **Trim box**: A trim box indica o tamanho final de um documento após impressão e corte.
- **Art box**: A art box é a caixa desenhada ao redor do conteúdo real das páginas em seus documentos. Esta caixa de página é usada ao importar documentos PDF em outras aplicações.
- **Crop box**: A crop box é o tamanho da “página” em que seu documento PDF é exibido no Adobe Acrobat. Na visualização normal, apenas o conteúdo da crop box é exibido no Adobe Acrobat.
  Para descrições detalhadas dessas propriedades, leia a especificação Adobe.Pdf, particularmente 10.10.1 Limites da Página.
- **Page.Rect**: a interseção (retângulo visível comum) da MediaBox e DropBox. A imagem abaixo ilustra essas propriedades.

Para mais detalhes, visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Acessando Propriedades da Página**

A classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) fornece todas as propriedades relacionadas a uma página PDF específica. Todas as páginas dos arquivos PDF estão contidas na coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

A partir daí, é possível acessar objetos Page individuais usando seu índice ou percorrer a coleção, usando um loop foreach, para obter todas as páginas. Uma vez que uma página individual é acessada, podemos obter suas propriedades. O seguinte trecho de código mostra como obter propriedades da página.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessingPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetProperties.pdf"))
    {
        // Get page collection
        var pageCollection = document.Pages;
        // Get particular page
        var pdfPage = pageCollection[1];
        // Get page properties
        System.Console.WriteLine("ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.ArtBox.Height, pdfPage.ArtBox.Width, pdfPage.ArtBox.LLX,
            pdfPage.ArtBox.LLY, pdfPage.ArtBox.URX, pdfPage.ArtBox.URY);
        System.Console.WriteLine("BleedBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.BleedBox.Height, pdfPage.BleedBox.Width, pdfPage.BleedBox.LLX,
            pdfPage.BleedBox.LLY, pdfPage.BleedBox.URX, pdfPage.BleedBox.URY);
        System.Console.WriteLine("CropBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.CropBox.Height, pdfPage.CropBox.Width, pdfPage.CropBox.LLX,
            pdfPage.CropBox.LLY, pdfPage.CropBox.URX, pdfPage.CropBox.URY);
        System.Console.WriteLine("MediaBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.MediaBox.Height, pdfPage.MediaBox.Width, pdfPage.MediaBox.LLX,
            pdfPage.MediaBox.LLY, pdfPage.MediaBox.URX, pdfPage.MediaBox.URY);
        System.Console.WriteLine("TrimBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.TrimBox.Height, pdfPage.TrimBox.Width, pdfPage.TrimBox.LLX,
            pdfPage.TrimBox.LLY, pdfPage.TrimBox.URX, pdfPage.TrimBox.URY);
        System.Console.WriteLine("Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.Rect.Height, pdfPage.Rect.Width, pdfPage.Rect.LLX, pdfPage.Rect.LLY,
            pdfPage.Rect.URX, pdfPage.Rect.URY);
        System.Console.WriteLine("Page Number : {0}", pdfPage.Number);
        System.Console.WriteLine("Rotate : {0}", pdfPage.Rotate);
    }
}
```

## Obter uma Página Particular do Arquivo PDF

Aspose.PDF permite que você [divida um PDF em páginas individuais](/pdf/net/split-pdf-document/) e as salve como arquivos PDF. Obter uma página especificada em um arquivo PDF e salvá-la como um novo PDF é uma operação muito semelhante: abra o documento de origem, acesse a página, crie um novo documento e adicione a página a este.

A coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) contém as páginas no arquivo PDF. Para obter uma página particular dessa coleção:

1. Especifique o índice da página usando a propriedade Pages.
1. Crie um novo objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Adicione o objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) ao novo objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Salve a saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

O seguinte trecho de código mostra como obter uma página particular de um arquivo PDF e salvá-la como um novo arquivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAParticularPageOfThePdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get particular page
        var pdfPage = document.Pages[2];
        // Save the page as PDF file
        using (var newDocument = new Aspose.Pdf.Document())
        {
            newDocument.Pages.Add(pdfPage);
            // Save PDF document
            newDocument.Save(dataDir + "GetParticularPage_out.pdf");
        }
    }
}
```

## Determinar a Cor da Página

A classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) fornece as propriedades relacionadas a uma página específica em um documento PDF, incluindo que tipo de cor - RGB, preto e branco, escala de cinza ou indefinido - a página usa.

Todas as páginas dos arquivos PDF estão contidas pela coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection). A propriedade ColorType especifica a cor dos elementos na página. Para obter ou determinar as informações de cor para uma página PDF específica, use a propriedade [ColorType](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/colortype) do objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

O seguinte trecho de código mostra como iterar através de páginas individuais de um arquivo PDF para obter informações de cor.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeterminePageColor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Iterate through all the page of PDF file
        for (var pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            // Get the color type information for particular PDF page
            Aspose.Pdf.ColorType pageColorType = document.Pages[pageCount].ColorType;
            switch (pageColorType)
            {
                case Aspose.Pdf.ColorType.BlackAndWhite:
                    Console.WriteLine("Page # -" + pageCount + " is Black and white..");
                    break;
                case Aspose.Pdf.ColorType.Grayscale:
                    Console.WriteLine("Page # -" + pageCount + " is Gray Scale...");
                    break;
                case Aspose.Pdf.ColorType.Rgb:
                    Console.WriteLine("Page # -" + pageCount + " is RGB..", pageCount);
                    break;
                case Aspose.Pdf.ColorType.Undefined:
                    Console.WriteLine("Page # -" + pageCount + " Color is undefined..");
                    break;
            }
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