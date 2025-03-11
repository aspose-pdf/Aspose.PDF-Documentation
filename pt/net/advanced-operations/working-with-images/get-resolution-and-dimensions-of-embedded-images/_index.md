---
title: Obter Resolução e Dimensões de Imagens
linktitle: Obter Resolução e Dimensões
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /pt/net/get-resolution-and-dimensions-of-embedded-images/
description: Aprenda como recuperar a resolução e as dimensões de imagens incorporadas em um PDF no .NET usando Aspose.PDF.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Resolution and Dimensions of Images",
    "alternativeHeadline": "Extract Image Resolution and Dimensions Efficiently",
    "abstract": "Descubra como obter de forma eficiente a resolução e as dimensões de imagens incorporadas em documentos PDF usando a biblioteca Aspose.PDF. Este recurso permite que os desenvolvedores acessem propriedades de imagem diretamente sem extração, simplificando o processo de manipulação de imagens em arquivos PDF, enquanto melhora a funcionalidade e o controle sobre os dados da imagem.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Get Resolution, Dimensions of Images, Embedded Images, Aspose.PDF.Drawing, ArrayList, Image Placement Classes, ConcatenateMatrix, XImage, PDF Manipulation Library, Image Resolution Computation",
    "wordcount": "827",
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
    "url": "/net/get-resolution-and-dimensions-of-embedded-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-resolution-and-dimensions-of-embedded-images/"
    },
    "dateModified": "2024-11-26",
    "description": "Esta seção mostra detalhes sobre como obter a resolução e as dimensões de Imagens Incorporadas."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

Este tópico explica como usar as classes de operador no namespace Aspose.PDF, que fornecem a capacidade de obter informações de resolução e dimensão sobre imagens sem precisar extraí-las.

Existem diferentes maneiras de alcançar isso. Este artigo explica como usar um `arraylist` e [classes de colocação de imagem](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement).

1. Primeiro, carregue o arquivo PDF de origem (com imagens).
1. Em seguida, crie um objeto ArrayList para armazenar os nomes de quaisquer imagens no documento.
1. Obtenha as imagens usando a propriedade Page.Resources.Images.
1. Crie um objeto de pilha para armazenar o estado gráfico da imagem e use-o para acompanhar diferentes estados da imagem.
1. Crie um objeto ConcatenateMatrix que define a transformação atual. Ele também suporta escalonamento, rotação e distorção de qualquer conteúdo. Ele concatena a nova matriz com a anterior. Observe que não podemos definir a transformação do zero, mas apenas modificar a transformação existente.
1. Como podemos modificar a matriz com ConcatenateMatrix, também pode ser necessário reverter ao estado original da imagem. Use os operadores GSave e GRestore. Esses operadores são emparelhados, portanto, devem ser chamados juntos. Por exemplo, se você fizer algum trabalho gráfico com transformações complexas e finalmente retornar as transformações ao estado inicial, a abordagem será algo assim:

```csharp
// Draw some text
GSave

ConcatenateMatrix  // rotate contents after the operator

// Some graphics work

ConcatenateMatrix // scale (with previous rotation) contents after the operator

// Some other graphics work

GRestore

// Draw some text
```

Como resultado, o texto é desenhado em forma regular, mas algumas transformações são realizadas entre os operadores de texto. Para exibir a imagem ou desenhar objetos de forma e imagens, precisamos usar o operador Do.

Também temos uma classe chamada XImage que fornece duas propriedades, Width e Height, que podem ser usadas para obter as dimensões da imagem.

1. Realize alguns cálculos para computar a resolução da imagem.
1. Exiba as informações em um Prompt de Comando junto com o nome da imagem.

O seguinte trecho de código mostra como obter as dimensões e a resolução de uma imagem sem extrair a imagem do documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageInformationFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageInformation.pdf"))
    {
        // Define the default resolution for image
        int defaultResolution = 72;
        var graphicsState = new Stack();

        // Define list which will hold image names
        var imageNames = new List<string>(document.Pages[1].Resources.Images.Names);

        // Insert an object to stack
        graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

        // Get all the operators on first page of document
        foreach (var op in document.Pages[1].Contents)
        {
            // Use GSave/GRestore operators to revert the transformations back to previously set
            var opSaveState = op as Aspose.Pdf.Operators.GSave;
            var opRestoreState = op as Aspose.Pdf.Operators.GRestore;
            var opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
            var opDo = op as Aspose.Pdf.Operators.Do;

            if (opSaveState != null)
            {
                // Save previous state and push current state to the top of the stack
                graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
            }
            else if (opRestoreState != null)
            {
                // Throw away current state and restore previous one
                graphicsState.Pop();
            }
            else if (opCtm != null)
            {
                var cm = new System.Drawing.Drawing2D.Matrix(
                   (float)opCtm.Matrix.A,
                   (float)opCtm.Matrix.B,
                   (float)opCtm.Matrix.C,
                   (float)opCtm.Matrix.D,
                   (float)opCtm.Matrix.E,
                   (float)opCtm.Matrix.F);

                // Multiply current matrix with the state matrix
                ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

                continue;
            }
            else if (opDo != null)
            {
                // In case this is an image drawing operator
                if (imageNames.Contains(opDo.Name))
                {
                    var lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
                    // Create XImage object to hold images of first pdf page
                    var image = document.Pages[1].Resources.Images[opDo.Name];

                    // Get image dimensions
                    double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
                    double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
                    // Get Height and Width information of image
                    double originalWidth = image.Width;
                    double originalHeight = image.Height;

                    // Compute resolution based on above information
                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    // Display Dimension and Resolution information of each image
                    Console.Out.WriteLine(
                            string.Format(dataDir + "image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                                         opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                         resVertical));
                }
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