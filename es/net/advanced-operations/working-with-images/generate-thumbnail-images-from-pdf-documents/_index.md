---
title: Generar Imágenes en Miniatura a partir de PDF
linktitle: Generar Imágenes en Miniatura
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /es/net/generate-thumbnail-images-from-pdf-documents/
description: Esta sección describe cómo generar imágenes en miniatura a partir de documentos PDF
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Generate Thumbnail Images from PDF",
    "alternativeHeadline": "Generate Thumbnails from PDF Documents Effortlessly",
    "abstract": "La nueva función permite a los usuarios generar imágenes en miniatura de manera eficiente directamente desde documentos PDF. Esta funcionalidad mejora la gestión de documentos al transformar las páginas PDF en formatos de imagen fácilmente compartibles, optimizando los flujos de trabajo tanto para desarrolladores como para usuarios. Con soporte para varios formatos de imagen, esta función simplifica el proceso de visualización del contenido PDF sin necesidad de software externo como Adobe Acrobat",
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
    "description": "Esta sección describe cómo generar imágenes en miniatura a partir de documentos PDF"
}
</script>

{{% alert color="primary" %}}

El SDK de Adobe Acrobat es un conjunto de herramientas que te ayuda a desarrollar software que interactúa con la tecnología de Acrobat. El SDK contiene archivos de encabezado, bibliotecas de tipos, utilidades simples, código de ejemplo y documentación.

Usando el SDK de Acrobat, puedes desarrollar software que se integre con Acrobat y Adobe Reader de varias maneras:

- **JavaScript** — Escribe scripts, ya sea en un documento PDF individual o externamente, para extender la funcionalidad de Acrobat o Adobe Reader.
- **Complementos** — Crea complementos que están vinculados dinámicamente y extienden la funcionalidad de Acrobat o Adobe Reader.
- **Comunicación entre aplicaciones** — Escribe un proceso de aplicación separado que utiliza la comunicación entre aplicaciones (IAC) para controlar la funcionalidad de Acrobat. DDE y OLE son compatibles en Microsoft® Windows®, y eventos de Apple/AppleScript en Mac OS®. IAC no está disponible en UNIX®.

Aspose.PDF for .NET proporciona mucha de la misma funcionalidad, liberándote de la dependencia de la Automatización de Adobe Acrobat. Este artículo muestra cómo generar imágenes en miniatura a partir de documentos PDF utilizando primero el SDK de Acrobat y luego Aspose.PDF.

{{% /alert %}}

## Desarrollo de Aplicaciones utilizando la API de Comunicación entre Aplicaciones de Acrobat

Piensa en la API de Acrobat como si tuviera dos capas distintas que utilizan objetos de Comunicación entre Aplicaciones de Acrobat (IAC):

- La capa de aplicación de Acrobat (AV). La capa AV te permite controlar cómo se visualiza el documento. Por ejemplo, la vista de un objeto de documento reside en la capa asociada con Acrobat.
- La capa de documento portátil (PD). La capa PD proporciona acceso a la información dentro de un documento, como una página. Desde la capa PD puedes realizar manipulaciones básicas de documentos PDF, como eliminar, mover o reemplazar páginas, así como cambiar atributos de anotación. También puedes imprimir páginas PDF, seleccionar texto, acceder al texto manipulado y crear o eliminar miniaturas.

Dado que nuestra intención es convertir páginas PDF en imágenes en miniatura, nos estamos enfocando más en IAC. La API de IAC contiene objetos como PDDoc, PDPage, PDAnnot y otros, que permiten al usuario tratar con la capa de documento portátil (PD). El siguiente ejemplo de código escanea una carpeta y convierte páginas PDF en imágenes en miniatura. Usando el SDK de Acrobat, también podríamos leer los metadatos del PDF y recuperar el número de páginas en el documento.

### Enfoque de Acrobat

Para generar las imágenes en miniatura para cada documento, hemos utilizado el SDK de Adobe Acrobat 7.0 y el Framework Microsoft .NET 2.0.

El [SDK de Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/) combinado con la versión completa de Adobe Acrobat expone una biblioteca COM de objetos (lamentablemente, el Adobe Reader gratuito no expone las interfaces COM) que se pueden utilizar para manipular y acceder a la información PDF. Usando estos objetos COM a través de COM Interop, carga el documento PDF, obtiene la primera página y renderiza esa página en el portapapeles. Luego, con el Framework .NET, copia esto a un bitmap, escala y combina la imagen y guarda el resultado como un archivo GIF o PNG.

Una vez que Adobe Acrobat está instalado, usa regedit.exe y busca en HKEY_CLASSES_ROOT la entrada llamada AcroExch.PDDoc.

**El registro mostrando la entrada AcroExch.PDDDoc**

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

## Enfoque de Aspose.PDF for .NET

Aspose.PDF for .NET proporciona un amplio soporte para tratar con documentos PDF. También admite la capacidad de convertir las páginas de documentos PDF a una variedad de formatos de imagen. La funcionalidad descrita anteriormente se puede lograr fácilmente utilizando Aspose.PDF for .NET.

Aspose.PDF tiene beneficios distintos:

- No necesitas tener Adobe Acrobat instalado en tu sistema para trabajar con archivos PDF.
- Usar Aspose.PDF for .NET es simple y fácil de entender en comparación con la Automatización de Acrobat.

Si necesitamos convertir páginas PDF en JPEGs, el espacio de nombres [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) proporciona una clase llamada [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) para renderizar páginas PDF en imágenes JPEG. Por favor, echa un vistazo al siguiente fragmento de código.

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

- Gracias a CodeProject por [Generar Imagen en Miniatura a partir de documento PDF](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents).
- Gracias a Acrobat por la [referencia del SDK de Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html).

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