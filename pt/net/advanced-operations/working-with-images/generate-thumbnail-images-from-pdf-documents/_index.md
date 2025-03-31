---
title: Gerar Imagens em Miniatura a partir de PDF
linktitle: Gerar Imagens em Miniatura
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /pt/net/generate-thumbnail-images-from-pdf-documents/
description: Esta seção descreve como gerar imagens em miniatura a partir de documentos PDF
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Generate Thumbnail Images from PDF",
    "alternativeHeadline": "Generate Thumbnails from PDF Documents Effortlessly",
    "abstract": "O novo recurso permite que os usuários gerem eficientemente imagens em miniatura diretamente de documentos PDF. Essa funcionalidade melhora a gestão de documentos ao transformar páginas PDF em formatos de imagem facilmente compartilháveis, agilizando fluxos de trabalho para desenvolvedores e usuários. Com suporte para vários formatos de imagem, esse recurso simplifica o processo de visualização do conteúdo PDF sem a necessidade de software externo como o Adobe Acrobat",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Generate Thumbnail Images, PDF documents, Aspose.PDF for .NET, Acrobat SDK, image formats, PDF Manipulation Library, JavaScript, interapplication communication, thumbnail images, JPEG conversion",
    "wordcount": "767",
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
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2024-11-26",
    "description": "Esta seção descreve como gerar imagens em miniatura a partir de documentos PDF"
}
</script>

{{% alert color="primary" %}}

O SDK do Adobe Acrobat é um conjunto de ferramentas que ajuda você a desenvolver software que interage com a tecnologia Acrobat. O SDK contém arquivos de cabeçalho, bibliotecas de tipos, utilitários simples, código de exemplo e documentação.

Usando o SDK do Acrobat, você pode desenvolver software que se integra ao Acrobat e ao Adobe Reader de várias maneiras:

- **JavaScript** — Escreva scripts, seja em um documento PDF individual ou externamente, para estender a funcionalidade do Acrobat ou do Adobe Reader.
- **Plug-ins** — Crie plug-ins que estão vinculados dinamicamente e estendem a funcionalidade do Acrobat ou do Adobe Reader.
- **Comunicação entre aplicações** — Escreva um processo de aplicação separado que usa comunicação entre aplicações (IAC) para controlar a funcionalidade do Acrobat. DDE e OLE são suportados no Microsoft® Windows®, e eventos Apple/AppleScript no Mac OS®. IAC não está disponível no UNIX®.

Aspose.PDF for .NET fornece muita da mesma funcionalidade, libertando você da dependência da Automação do Adobe Acrobat. Este artigo mostra como gerar imagens em miniatura a partir de documentos PDF usando primeiro o SDK do Acrobat e depois o Aspose.PDF.

{{% /alert %}}

## Desenvolvendo Aplicativo usando a API de Comunicação entre Aplicações do Acrobat

Pense na API do Acrobat como tendo duas camadas distintas que usam objetos de Comunicação entre Aplicações (IAC) do Acrobat:

- A camada da aplicação Acrobat (AV). A camada AV permite que você controle como o documento é visualizado. Por exemplo, a visualização de um objeto de documento reside na camada associada ao Acrobat.
- A camada de documento portátil (PD). A camada PD fornece acesso às informações dentro de um documento, como uma página. A partir da camada PD, você pode realizar manipulações básicas de documentos PDF, como excluir, mover ou substituir páginas, bem como alterar atributos de anotações. Você também pode imprimir páginas PDF, selecionar texto, acessar texto manipulado e criar ou excluir miniaturas.

Como nossa intenção é converter páginas PDF em imagens em miniatura, estamos nos concentrando mais na IAC. A API IAC contém objetos como PDDoc, PDPage, PDAnnot e outros, que permitem ao usuário lidar com a camada de documento portátil (PD). O seguinte exemplo de código escaneia uma pasta e converte páginas PDF em imagens em miniatura. Usando o SDK do Acrobat, também poderíamos ler os metadados do PDF e recuperar o número de páginas no documento.

### Abordagem do Acrobat

Para gerar as imagens em miniatura para cada documento, usamos o SDK do Adobe Acrobat 7.0 e o Microsoft .NET 2.0 Framework.

O [SDK do Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/) combinado com a versão completa do Adobe Acrobat expõe uma biblioteca COM de objetos (infelizmente, o Adobe Reader gratuito não expõe as interfaces COM) que podem ser usados para manipular e acessar informações PDF. Usando esses objetos COM via COM Interop, carregue o documento PDF, obtenha a primeira página e renderize essa página para a área de transferência. Em seguida, com o .NET Framework, copie isso para um bitmap, escale e combine a imagem e salve o resultado como um arquivo GIF ou PNG.

Uma vez que o Adobe Acrobat esteja instalado, use regedit.exe e procure na HKEY_CLASSES_ROOT pela entrada chamada AcroExch.PDDoc.

**O registro mostrando a entrada AcroExch.PDDDoc**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GenerateThumbnailImagesFromPDF()
{
    // Acrobat objects
    Acrobat.CAcroPDDoc pdfDoc;
    Acrobat.CAcroPDPage pdfPage;
    Acrobat.CAcroRect pdfRect;
    Acrobat.CAcroPoint pdfPoint;

    AppSettingsReader appSettings = new AppSettingsReader();
    string pdfInputPath = appSettings.GetValue("pdfInputPath", typeof(string)).ToString();
    string pngOutputPath = appSettings.GetValue("pngOutputPath", typeof(string)).ToString();
    string templatePortraitFile = Application.StartupPath + @"\pdftemplate_portrait.gif";
    string templateLandscapeFile = Application.StartupPath + @"\pdftemplate_landscape.gif";

    // Get list of files to process from the input path
    string[] files = Directory.GetFiles(pdfInputPath, "*.pdf");

    for (int n = 0; n < files.Length; n++)
    {
        string inputFile = files[n];
        string outputFile = Path.Combine(pngOutputPath, Path.GetFileNameWithoutExtension(inputFile) + ".png");

        // Create PDF document
        pdfDoc = (Acrobat.CAcroPDDoc)Microsoft.VisualBasic.Interaction.CreateObject("AcroExch.PDDoc", "");

        if (pdfDoc.Open(inputFile) == 0)
        {
            throw new FileNotFoundException($"Unable to open PDF file: {inputFile}");
        }

        int pageCount = pdfDoc.GetNumPages();
        pdfPage = (Acrobat.CAcroPDPage)pdfDoc.AcquirePage(0);
        pdfPoint = (Acrobat.CAcroPoint)pdfPage.GetSize();

        pdfRect = (Acrobat.CAcroRect)Microsoft.VisualBasic.Interaction.CreateObject("AcroExch.Rect", "");
        pdfRect.Left = 0;
        pdfRect.right = pdfPoint.x;
        pdfRect.Top = 0;
        pdfRect.bottom = pdfPoint.y;

        pdfPage.CopyToClipboard(pdfRect, 0, 0, 100);
        IDataObject clipboardData = Clipboard.GetDataObject();

        if (clipboardData.GetDataPresent(DataFormats.Bitmap))
        {
            Bitmap pdfBitmap = (Bitmap)clipboardData.GetData(DataFormats.Bitmap);

            int thumbnailWidth = 45;
            int thumbnailHeight = 59;
            string templateFile = pdfPoint.x < pdfPoint.y ? templatePortraitFile : templateLandscapeFile;

            if (pdfPoint.x > pdfPoint.y)
            {
                // Swap width and height for landscape orientation
                (thumbnailWidth, thumbnailHeight) = (thumbnailHeight, thumbnailWidth);
            }

            Bitmap templateBitmap = new Bitmap(templateFile);
            Image pdfImage = pdfBitmap.GetThumbnailImage(thumbnailWidth, thumbnailHeight, null, IntPtr.Zero);

            Bitmap thumbnailBitmap = new Bitmap(thumbnailWidth + 7, thumbnailHeight + 7, System.Drawing.Imaging.PixelFormat.Format32bppArgb);

            templateBitmap.MakeTransparent();

            using (Graphics thumbnailGraphics = Graphics.FromImage(thumbnailBitmap))
            {
                thumbnailGraphics.DrawImage(pdfImage, 2, 2, thumbnailWidth, thumbnailHeight);
                thumbnailGraphics.DrawImage(templateBitmap, 0, 0);
                thumbnailBitmap.Save(outputFile, System.Drawing.Imaging.ImageFormat.Png);
            }

            Console.WriteLine("Generated thumbnail: {0}", outputFile);

            pdfDoc.Close();
            Marshal.ReleaseComObject(pdfPage);
            Marshal.ReleaseComObject(pdfRect);
            Marshal.ReleaseComObject(pdfDoc);
        }
    }
}
```

## Abordagem Aspose.PDF for .NET

Aspose.PDF for .NET fornece suporte extenso para lidar com documentos PDF. Também suporta a capacidade de converter as páginas de documentos PDF para uma variedade de formatos de imagem. A funcionalidade descrita acima pode ser facilmente alcançada usando Aspose.PDF for .NET.

Aspose.PDF tem benefícios distintos:

- Você não precisa ter o Adobe Acrobat instalado em seu sistema para trabalhar com arquivos PDF.
- Usar Aspose.PDF for .NET é simples e fácil de entender em comparação com a Automação do Acrobat.

Se precisarmos converter páginas PDF em JPEGs, o namespace [Aspose.PDF.Devices](https://reference.aspose.com/pdf/pt/net/aspose.pdf.devices) fornece uma classe chamada [JpegDevice](https://reference.aspose.com/pdf/pt/net/aspose.pdf.devices/jpegdevice) para renderizar páginas PDF em imagens JPEG. Por favor, dê uma olhada no seguinte trecho de código.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GenerateThumbnailImagesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Retrieve names of all the PDF files in a particular directory
    string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

    // Iterate through all the files entries in array
    for (int counter = 0; counter < fileEntries.Length; counter++)
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(fileEntries[counter]))
        {
            for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
            {
                using (FileStream imageStream = new FileStream(dataDir + @"\Thumbanils" + counter.ToString() + "_" + pageCount + ".jpg", FileMode.Create))
                {
                    var resolution = new Aspose.Pdf.Devices.Resolution(300);
                    var jpegDevice = new Aspose.Pdf.Devices.JpegDevice(45, 59, resolution, 100);
                    // Convert a particular page and save the image to stream
                    jpegDevice.Process(document.Pages[pageCount], imageStream);
                }
            }
        }
    }
}
```

{{% alert color="primary" %}}

- Agradecimentos ao CodeProject por [Gerar Imagem em Miniatura a partir de documento PDF](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents).
- Agradecimentos ao Acrobat pela [referência do SDK do Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html).

{{% /alert %}}

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