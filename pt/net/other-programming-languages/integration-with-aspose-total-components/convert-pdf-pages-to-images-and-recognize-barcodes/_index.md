---
title: Converter Páginas de PDF em Imagens e Reconhecer Códigos de Barras
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF Pages to Images and Recognize Barcodes",
    "alternativeHeadline": "Convert PDF Pages to Images with Barcode Recognition in C#",
    "abstract": "O novo recurso permite a conversão sem costura de páginas de PDF em vários formatos de imagem, facilitando a identificação de códigos de barras incorporados usando Aspose.Barcode para .NET. Essa funcionalidade simplifica o processamento de documentos, permitindo que os usuários transformem o conteúdo do PDF em imagens e reconheçam com precisão os códigos de barras para um manuseio eficiente de dados.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "858",
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
    "url": "/net/convert-pdf-pages-to-images-and-recognize-barcodes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-pages-to-images-and-recognize-barcodes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

{{% alert color="primary" %}}

Documentos PDF geralmente compreendem texto, imagens, tabelas, anexos, gráficos, anotações e outros objetos. Alguns de nossos clientes precisam incorporar códigos de barras em documentos e, em seguida, identificar códigos de barras no arquivo PDF. O seguinte artigo explica como transformar as páginas em um arquivo PDF em imagens e identificar códigos de barras nas imagens com Aspose.Barcode para .NET.

{{% /alert %}}

## Convertendo Páginas em Imagens e Reconhecendo Códigos de Barras

{{% alert color="primary" %}}

Aspose.PDF for .NET é um produto muito poderoso para gerenciar documentos PDF. Ele facilita a conversão de páginas em documentos PDF em imagens. Aspose.BarCode para .NET é um produto igualmente poderoso para gerar e reconhecer códigos de barras.

A classe PdfConverter sob o namespace Aspose.Pdf.Facades suporta a conversão de páginas PDF em vários formatos de imagem. O PngDevice sob o namespace Aspose.Pdf.Devices suporta a conversão de páginas PDF em arquivos PNG. Qualquer uma dessas classes pode ser usada para transformar páginas de um arquivo PDF em imagens.

Quando as páginas foram convertidas para um formato de imagem, podemos usar Aspose.BarCode para .NET para identificar códigos de barras dentro delas. Os exemplos de código abaixo mostram como converter páginas usando PdfConverter ou PngDevice.

{{% /alert %}}

### Usando Aspose.Pdf.Facades

{{% alert color="primary" %}}

A classe PdfConverter contém um método chamado GetNextImage que gera uma imagem da página PDF atual. Para especificar o formato da imagem de saída, este método aceita um argumento da enumeração System.Drawing.Imaging.ImageFormat.

Aspose.Barcode contém um namespace, BarCodeRecognition, que contém a classe BarCodeReader. A classe BarCodeReader permite que você leia, determine e identifique códigos de barras a partir de arquivos de imagem.

Para os propósitos deste exemplo, primeiro converta uma página em um arquivo PDF em uma imagem com Aspose.Pdf.Facades.PdfConverter. Em seguida, use a classe Aspose.BarCodeRecognition.BarCodeReader para reconhecer o código de barras na imagem.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodesConverter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create a PdfConverter object
    var converter = new Aspose.Pdf.Facades.PdfConverter();

    // Bind PDF document
    converter.BindPdf(dataDir + "IdentifyBarcodes.pdf");

    // Specify the start page to be processed
    converter.StartPage = 1;

    // Specify the end page for processing
    converter.EndPage = 1;

    // Create a Resolution object to specify the resolution of resultant image
    converter.Resolution = new Aspose.Pdf.Devices.Resolution(300);

    // Initialize the convertion process
    converter.DoConvert();

    // Create a MemoryStream object to hold the resultant image
    using (var imageStream = new MemoryStream())
    {
        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Save the image in the given image Format
            converter.GetNextImage(imageStream, System.Drawing.Imaging.ImageFormat.Png);

            // Set the stream position to the beginning of the stream
            imageStream.Position = 0;

            // Instantiate a BarCodeReader object
            var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

            // String txtResult.Text = "";
            while (barcodeReader.Read())
            {
                // Get the barcode text from the barcode image
                var code = barcodeReader.GetCodeText();

                // Write the barcode text to Console output
                Console.WriteLine("BARCODE : " + code);
            }

            // Close the BarCodeReader object to release the image file
            barcodeReader.Close();
        }

        // Close the PdfConverter instance and release the resources
        converter.Close();
    }
}
```

{{% alert color="primary" %}}

Nos trechos de código acima, a imagem de saída é salva em um objeto MemoryStream. A imagem também pode ser salva no disco. Para fazer isso, substitua o objeto MemoryStream por um objeto string que representa o caminho do arquivo para o método GetNextImage da classe PdfConverter.

{{% /alert %}}

#### Usando a Classe PngDevice

No Aspose.Pdf.Devices, está o PngDevice. Esta classe permite que você converta páginas em documentos PDF em imagens PNG.

Para os propósitos deste exemplo, carregue o arquivo PDF de origem nas páginas do Documento] cument's pages into PNG images. Quando as imagens forem criadas, use a classe BarCodeReader sob o Aspose.BarCodeRecognition para identificar e ler códigos de barras nas imagens.

{{% alert color="primary" %}}

Os exemplos de código dados aqui percorrem as páginas do documento PDF e tentam identificar códigos de barras em cada página.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "IdentifyBarcodes.pdf"))
    {
        // Traverse through the individual pages of the PDF file
        for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            using (var imageStream = new MemoryStream())
            {
                // Create a Resolution object
                var resolution = new Aspose.Pdf.Devices.Resolution(300);

                // Instantiate a PngDevice object while passing a Resolution object as an argument to its constructor
                var pngDevice = new Aspose.Pdf.Devices.PngDevice(resolution);

                // Convert a particular page and save the image to stream
                pngDevice.Process(document.Pages[pageCount], imageStream);

                // Set the stream position to the beginning of Stream
                imageStream.Position = 0;

                // Instantiate a BarCodeReader object
                var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

                // String txtResult.Text = "";
                while (barcodeReader.Read())
                {
                    // Get the barcode text from the barcode image
                    var code = barcodeReader.GetCodeText();

                    // Write the barcode text to Console output
                    Console.WriteLine("BARCODE : " + code);
                }

                // Close the BarCodeReader object to release the image file
                barcodeReader.Close();
            }
        }
    }
}
```

{{% alert color="primary" %}}

Para mais informações sobre os tópicos abordados neste artigo, vá para:

- Converter Páginas de PDF em Diferentes Formatos de Imagem (Facades)
- Converter todas as páginas PDF em Imagens PNG
- [Ler Códigos de Barras](https://docs.aspose.com/barcode/net/barcode-recognition/)

{{% /alert %}}