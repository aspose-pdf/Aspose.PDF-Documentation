---
title: Convert PDF Pages to Images and Recognize Barcodes
type: docs
weight: 10
url: /net/convert-pdf-pages-to-images-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF Pages to Images and Recognize Barcodes",
    "alternativeHeadline": "Convert PDF Pages to Images with Barcode Recognition in C#",
    "abstract": "The new feature enables seamless conversion of PDF pages into various image formats, facilitating the identification of embedded barcodes using Aspose.Barcode for .NET. This functionality streamlines document processing by allowing users to transform PDF content into images and accurately recognize barcodes for efficient data handling",
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
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

{{% alert color="primary" %}}

PDF documents usually comprise text, images, tables, attachments, graphs, annotations and other objects. Some of our customers need to embed barcodes in documents and then identify barcodes in the PDF file. The following article explains how to transform the pages in a PDF file to images and identifying barcodes in the images with Aspose.Barcode for .NET.

{{% /alert %}}

### Converting Pages to Images and Recognizing Barcodes

{{% alert color="primary" %}}

Aspose.PDF for .NET is very powerful product for managing PDF documents. It makes it easy to convert pages in PDF documents to images. Aspose.BarCode for .NET is an equally powerful product for generating and recognizing barcodes.

The class PdfConverter under the Aspose.Pdf.Facades namespace supports converting PDF pages to various image formats. The PngDevice under the Aspose.Pdf.Devices namespace supports converting PDF pages to PNG files. Either of these classes can be used to transform pages of PDF file into images.

When the pages have been converted to an image format, we can use Aspose.BarCode for .NET to identify barcodes inside them. The code samples below show how to convert pages using either  PdfConverter or PngDevice.

{{% /alert %}}

#### Using Aspose.Pdf.Facades

{{% alert color="primary" %}}

The PdfConverter class contains a method named GetNextImage which generates the an image from the current PDF page. To specify the output image format, this method accepts an argument from the System.Drawing.Imaging.ImageFormat enumeration.

Aspose.Barcode contains a namespace, BarCodeRecognition, which contains the BarCodeReader class. The BarCodeReader class lets you read, determine, and identify barcodes from image files.

For the purposes of this example, first convert a page in a PDF file into an image with Aspose.Pdf.Facades.PdfConverter. Then use the Aspose.BarCodeRecognition.BarCodeReader class to recognize the barcode in the image.


{{% /alert %}}

##### Programming Samples

```csharp
// Create a PdfConverter object
var converter = new Aspose.Pdf.Facades.PdfConverter();

// Bind the input PDF file
converter.BindPdf("Source.pdf");

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
```

{{% alert color="primary" %}}

In above code snippets the output image is saved to a MemoryStream object. The image can also be saved to disk. To do so, replace the MemorStream object with a string object that represents the file path to the PdfConverter class' GetNextImage method.

{{% /alert %}}

{anchor:devices]
#### Using the PngDevice Class
In the Aspose.Pdf.Devices, is the PngDevice. This class lets you convert pages in PDF documents to PNG images.

For the purpose of this example, load the source PDF file into the Document] cument's pages into PNG images. When the images have been created, use the BarCodeReader class under the Aspose.BarCodeRecognition to identify and read barcodes in the images.

{{% alert color="primary" %}}

The code samples given here traverses through the pages of the PDF document and tries to identify barcodes on each page.

{{% /alert %}}
##### Programming Samples

```csharp
private static void IdentifyBarcodes()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open the PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "IdentifyBarcodes.pdf"))
    {
        // Traverse through the individual pages of the PDF file
        for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            using (var imageStream = new System.IO.MemoryStream())
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

For further information on topics covered in this article go to:

- Convert PDF Pages to Different Image Formats (Facades)
- Convert all PDF pages to PNG Images
- [Read Barcodes](https://docs.aspose.com/barcode/net/barcode-recognition/)


{{% /alert %}}
