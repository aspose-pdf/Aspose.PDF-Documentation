---
title: Extrair Imagens usando PdfExtractor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/extract-images/
description: Esta seção explica como extrair Imagens com Aspose.PDF Facades usando a Classe PdfExtractor.
lastmod: "2021-07-15"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images using PdfExtractor",
    "alternativeHeadline": "Extract Images from PDF with PdfExtractor Class",
    "abstract": "O recurso PdfExtractor do Aspose.PDF permite que os usuários extraiam imagens de documentos PDF de forma eficiente, oferecendo várias opções, como extrair imagens de todo o documento, páginas específicas ou intervalos especificados. Ele suporta salvar imagens diretamente em arquivos ou fluxos de memória, aumentando a flexibilidade para desenvolvedores que trabalham com ativos PDF. Essa funcionalidade poderosa permite controle preciso sobre os modos de extração de imagens, facilitando o manuseio de diferentes tipos de conteúdo PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1789",
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
    "url": "/net/extract-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Extrair Imagens de Todo o PDF para Arquivos (Facades)

A classe [PdfExtractor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor) permite que você extraia imagens de um arquivo PDF. Primeiro, você precisa criar um objeto da classe [PdfExtractor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/facade/methods/bindpdf/index). Depois disso, chame o método [ExtractImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/methods/extractimage) para extrair todas as imagens para a memória. Uma vez que as imagens sejam extraídas, você pode obter essas imagens com a ajuda dos métodos [HasNextImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) e [GetNextImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Você precisa percorrer todas as imagens extraídas usando um loop while. Para salvar as imagens no disco, você pode chamar a sobrecarga do método [GetNextImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) que aceita o caminho do arquivo como argumento. O seguinte trecho de código mostra como extrair imagens de todo o PDF para arquivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract all the images
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
    }
}
```

## Extrair Imagens de Todo o PDF para Fluxos (Facades)

A classe [PdfExtractor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor) permite que você extraia imagens de um arquivo PDF para fluxos. Primeiro, você precisa criar um objeto da classe [PdfExtractor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/facade/methods/bindpdf/index). Depois disso, chame o método [ExtractImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/methods/extractimage) para extrair todas as imagens para a memória. Uma vez que as imagens sejam extraídas, você pode obter essas imagens com a ajuda dos métodos [HasNextImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) e [GetNextImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Você precisa percorrer todas as imagens extraídas usando um loop while. Para salvar as imagens em um fluxo, você pode chamar a sobrecarga do método [GetNextImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) que aceita Stream como argumento. O seguinte trecho de código mostra como extrair imagens de todo o PDF para fluxos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDFStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract images
        extractor.ExtractImage();
        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## Extrair Imagens de uma Página Particular de um PDF (Facades)

Você pode extrair imagens de uma página particular de um arquivo PDF. Para fazer isso, você precisa definir as propriedades [StartPage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/properties/startpage) e [EndPage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/properties/endpage) para a página específica da qual deseja extrair imagens. Primeiro, você precisa criar um objeto da classe [PdfExtractor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/facade/methods/bindpdf/index). Em segundo lugar, você deve definir as propriedades [StartPage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/properties/startpage) e [EndPage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/properties/endpage). Depois disso, chame o método [ExtractImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/methods/extractimage) para extrair todas as imagens para a memória. Uma vez que as imagens sejam extraídas, você pode obter essas imagens com a ajuda dos métodos [HasNextImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) e [GetNextImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Você precisa percorrer todas as imagens extraídas usando um loop while. Você pode salvar as imagens no disco ou em um fluxo. Você só precisa chamar a sobrecarga apropriada do método [GetNextImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). O seguinte trecho de código mostra como extrair imagens de uma página particular de PDF para fluxos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesParticularPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();
        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## Extrair Imagens de um Intervalo de Páginas de um PDF (Facades)

Você pode extrair imagens de um intervalo de páginas de um arquivo PDF. Para fazer isso, você precisa definir as propriedades [StartPage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/properties/startpage) e [EndPage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/properties/endpage) para o intervalo de páginas do qual deseja extrair imagens. Primeiro, você precisa criar um objeto da classe [PdfExtractor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/facade/methods/bindpdf/index). Em segundo lugar, você deve definir as propriedades [StartPage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/properties/startpage) e [EndPage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/properties/endpage). Depois disso, chame o método [ExtractImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/methods/extractimage) para extrair todas as imagens para a memória. Uma vez que as imagens sejam extraídas, você pode obter essas imagens com a ajuda dos métodos [HasNextImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) e [GetNextImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Você precisa percorrer todas as imagens extraídas usando um loop while. Você pode salvar as imagens no disco ou em um fluxo. Você só precisa chamar a sobrecarga apropriada do método [GetNextImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). O seguinte trecho de código mostra como extrair imagens de um intervalo de páginas de PDF para fluxos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesRangePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open input PDF
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();

        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new
            FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## Extrair Imagens usando Modo de Extração de Imagem (Facades)

A classe [PdfExtractor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor) permite que você extraia imagens de um arquivo PDF. Aspose.PDF suporta dois modos de extração; o primeiro é ActuallyUsedImage, que extrai as imagens realmente usadas no documento PDF. O segundo modo é [DefinedInResources](https://reference.aspose.com/pdf/pt/net/aspose.pdf/extractimagemode), que extrai as imagens definidas nos recursos do documento PDF (modo de extração padrão). Primeiro, você precisa criar um objeto da classe [PdfExtractor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/facade/methods/bindpdf/index). Depois disso, especifique o modo de extração de imagem usando a propriedade [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode). Em seguida, chame o método [ExtractImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/methods/extractimage) para extrair todas as imagens para a memória, dependendo do modo que você especificou. Uma vez que as imagens sejam extraídas, você pode obter essas imagens com a ajuda dos métodos [HasNextImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) e [GetNextImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Você precisa percorrer todas as imagens extraídas usando um loop while. Para salvar as imagens no disco, você pode chamar a sobrecarga do método [GetNextImage](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) que aceita o caminho do arquivo como argumento.

O seguinte trecho de código mostra como extrair imagens de um arquivo PDF usando a opção ExtractImageMode.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesImageExtractionMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Specify Image Extraction Mode
        //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
        extractor.ExtractImageMode = Aspose.Pdf.ExtractImageMode.DefinedInResources;

        // Extract Images based on Image Extraction Mode
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
        }
    }
}
```

Para verificar se o PDF contém Texto ou Imagens, use o próximo trecho de código:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckIfPdfContainsTextOrImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Instantiate a memoryStream object to hold the extracted text from Document
    MemoryStream ms = new MemoryStream();
    // Instantiate PdfExtractor object
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "FilledForm.pdf");
        // Extract text from the input PDF document
        extractor.ExtractText();
        // Save the extracted text to a text file
        extractor.GetText(ms);
        // Check if the MemoryStream length is greater than or equal to 1

        bool containsText = ms.Length >= 1;

        // Extract images from the input PDF document
        extractor.ExtractImage();

        // Calling HasNextImage method in while loop. When images will finish, loop will exit
        bool containsImage = extractor.HasNextImage();

        // Now find out whether this PDF is text only or image only

        if (containsText && !containsImage)
        {
            Console.WriteLine("PDF contains text only");
        }
        else if (!containsText && containsImage)
        {
            Console.WriteLine("PDF contains image only");
        }
        else if (containsText && containsImage)
        {
            Console.WriteLine("PDF contains both text and image");
        }
        else if (!containsText && !containsImage)
        {
            Console.WriteLine("PDF contains neither text or nor image");
        }
    }
}
```