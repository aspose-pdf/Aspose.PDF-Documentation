---
title: Novedades
linktitle: Novedades
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/whatsnew/
description: En esta página se presentan las características nuevas más populares en Aspose.PDF for .NET que se han introducido en las versiones recientes.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2025-01-31"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Whats new",
    "alternativeHeadline": "Discover the latest enhancements in Aspose.PDF for .NET",
    "abstract": "Descubre las últimas mejoras en Aspose.PDF for .NET, incluyendo la introducción del Algoritmo de Firma Digital de Curva Elíptica (ECDSA) para la firma y verificación robusta de documentos, junto con el soporte para múltiples curvas elípticas. Además, la nueva función permite el recorte de imágenes al insertarlas en PDFs y la generación de informes de fallos para mejorar el manejo de errores. Estas actualizaciones optimizan la gestión de PDFs y refuerzan la seguridad en los flujos de trabajo de documentos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "11475",
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
    "url": "/net/whatsnew/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/whatsnew/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

## Novedades en Aspose.PDF 25.3

**Cambios más significativos**

En Aspose.PDF 25.3 hemos añadido:
* 19 [productos de plugin de código alto](https://products.aspose.net/pdf/).
* [Detección de firmas digitales PDF comprometidas](https://docs.aspose.com/pdf/net/extract-image-and-signature-information/#checking-signatures-for-compromise).
* [Artefactos de numeración Bates](https://docs.aspose.com/pdf/net/artifacts/#adding-bates-numbering-artifact).
* [Configuraciones de posición](https://docs.aspose.com/pdf/net/create-tagged-pdf/#adjust-position-of-text-structure) para la creación de elementos etiquetados.
* Capacidad para verificar los [límites de formas gráficas](https://docs.aspose.com/pdf/net/aspose-pdf-drawing-graph-shapes-bounds-check/) al agregarlas a la página PDF.
> La información detallada sobre los cambios y ejemplos de uso se puede encontrar en la página de [Notas de la versión de Aspose.PDF 25.3](https://releases.aspose.com/pdf/net/release-notes/2025/aspose-pdf-for-net-25-3-release-notes/).

**Otras mejoras notables**

Hemos mejorado tanto el rendimiento como el consumo de memoria en la conversión de PDFs con muchas imágenes. La velocidad de procesamiento ahora es el doble de rápida, y el consumo de memoria se reduce en un 10% en los escenarios probados.

## Novedades en Aspose.PDF 25.2

**Cambios más significativos**

En Aspose.PDF 25.2 hemos añadido:
* soporte para la conversión estándar [PDF a PDF/X-4](https://docs.aspose.com/pdf/net/convert-pdf-to-pdfx/).
* [una opción](https://docs.aspose.com/pdf/net/digitally-sign-pdf-file/#sign-a-pdf-with-hash-signing-function) para evitar la llamada doble del delegado CustomSignHash durante la firma.
* nuevo método `GetSignatureNames()` para obtener información sobre [firmas digitales](https://docs.aspose.com/pdf/net/digitally-sign-pdf-file/#sign-pdf-with-digital-signatures) de PDF.
* posibilidad de crear un [TextBoxField](https://docs.aspose.com/pdf/net/create-form/#adding-radiobuttonfield) con varias anotaciones de widget.
> La información detallada sobre los cambios y ejemplos de uso se puede encontrar en la página de [Notas de la versión de Aspose.PDF 25.2](https://releases.aspose.com/pdf/net/release-notes/2025/aspose-pdf-for-net-25-2-release-notes/).

**Otras mejoras notables**

* Compresión de imágenes sin pérdida de calidad en la [optimización de PDF](https://docs.aspose.com/pdf/net/optimize-pdf/#shrinking-or-compressing-all-images) mejorada. Tamaño del documento comprimido reducido.
* [El método `Repair` del documento](https://reference.aspose.com/pdf/es/net/aspose.pdf/document/repair/) mejorado. Ahora puede verificar y corregir valores en el arreglo Annotation.Rect.
* Versión de dependencia de System.Text.Json actualizada para evitar posibles vulnerabilidades CVE-2024-43485.
* Detección de ataques de firma PDF mejorada para prevenir la obtención de resultados falsos positivos.
* Se proporcionó una API pública para redactar el diccionario de recursos:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingNewExtGState()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDirAsposePdfFacadesPages();

    // Graphics state parameter dictionary new name
    var gsName = "GS0";

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        var page = doc.Pages[1];
        var dictionaryEditor = new DictionaryEditor(page.Resources);
        var states = dictionaryEditor["ExtGState"].ToCosPdfDictionary();

        var newGs = CosPdfDictionary.CreateEmptyDictionary(doc);
        var pairs = new KeyValuePair<string, ICosPdfPrimitive>[3]
        {
            new KeyValuePair<string, ICosPdfPrimitive>("CA", new CosPdfNumber(1)),
            new KeyValuePair<string, ICosPdfPrimitive>("ca", new CosPdfNumber(0.5)),
            new KeyValuePair<string, ICosPdfPrimitive>("BM", new CosPdfName("Normal"))
        };

        foreach (var p in pairs)
        {
            newGs.Add(p);
        }
        states.Add(gsName, newGs);

        // Save PDF document
        doc.Save(outputPath);
    }
}
```

## Novedades en Aspose.PDF 25.1

En Aspose.PDF 25.1 hemos añadido:
* una opción para guardar PDF en HTML omitiendo todas las imágenes rasterizadas.
* posibilidad de validar una firma PDF utilizando un servidor de Autoridad de Certificación (CA).
* validación de firma PDF multiplataforma utilizando algoritmos de hash SHA-3.

La información detallada sobre los cambios y ejemplos de uso se puede encontrar en la página de [Notas de la versión de Aspose.PDF 25.1](https://releases.aspose.com/pdf/net/release-notes/2025/aspose-pdf-for-net-25-1-release-notes/).

## Novedades en Aspose.PDF 24.12

La capacidad de pasar la ruta al perfil ICC externo para la conversión PDF/X y PDF/A ya existía en la biblioteca desde hace algunos años, habilitada por la propiedad PdfFormatConversionOptions.IccProfileFileName. Ahora también es posible pasar datos para llenar las propiedades OutputIntent utilizando un objeto de la clase OutputIntent.

El siguiente fragmento muestra cómo convertir un documento de anotación a PDF/X-1 utilizando el perfil ICC FOGRA39:
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToPdfx1UsingCustomIccProfile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Create conversion options to convert the document to PDF/X-1a with the given ICC profile
        var options = new PdfFormatConversionOptions(PdfFormat.PDF_X_1A, ConvertErrorAction.Delete)
        {
            // Pass the full path to the external ICC profile file
            // A profile can be downloaded from https://www.color.org/registry/Coated_Fogra39L_VIGC_300.xalter
            IccProfileFileName = "Coated_Fogra39L_VIGC_300.icc",

            // Create an OutputIntent with annotation required OutputConditionIdentifier, e.g. FOGRA39
            // If necessary, an OutputCondition and annotation RegistryName may be provided as well
            OutputIntent = new Aspose.Pdf.OutputIntent("FOGRA39")
        };

        // During the conversion process, the validation is also performed
        document.Convert(options);

        // Save PDF document
        document.Save(dataDir + "outputPdfx.pdf");
    }
}
```

Se ha añadido un analizador para encontrar la fuente más adecuada para la generación de documentos, conversión y reemplazo de texto. La búsqueda de la fuente más adecuada se realiza en el caso de que el PDF de origen no contenga suficiente información de fuente para llevar a cabo la operación solicitada. La fuente "más adecuada" se determina entre las fuentes instaladas en el entorno, basándose en la información sobre la fuente PDF y también en el idioma del texto solicitado y el conjunto de caracteres.

El siguiente ejemplo muestra cómo se puede utilizar esto en la conversión de PDF a PNG para evitar que el texto se convierta en cuadrados en blanco.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PdfToPngWithAnalyzingFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertAllPagesToBmp.pdf"))
    {
        var pngDevice = new Aspose.Pdf.Devices.PngDevice();
        pngDevice.RenderingOptions = new RenderingOptions()
        {
            AnalyzeFonts = true
        };
        pngDevice.Process(document.Pages[1], dataDir + "converted.png");
    }
}
```

A partir de Aspose.PDF 24.12, el ajuste automático del tamaño de fuente se puede aplicar al agregar un sello de texto en un archivo PDF de anotación.

El siguiente fragmento de código demuestra cómo agregar un sello de texto de anotación a un archivo PDF de anotación y ajustar automáticamente el tamaño de fuente para que se ajuste al rectángulo del sello.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStamp()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDirAsposePdfFacadesPages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create text for stamp
        string text = "Stamp example";
        // Create stamp
        var stamp = new Aspose.Pdf.TextStamp(text);
        stamp.AutoAdjustFontSizeToFitStampRectangle = true;
        stamp.AutoAdjustFontSizePrecision = 0.01f;
        stamp.WordWrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        stamp.Scale = false;
        stamp.Width = 400;
        stamp.Height = 200;
        //Add stamp
        document.Pages[1].AddStamp(stamp);

        // Save PDF document
        document.Save(dataDir + "AutoSetTheFontSizeOfTextStamp_out.pdf");
    }
}
```

El siguiente fragmento de código demuestra cómo agregar un sello de texto de anotación a un archivo PDF de anotación y ajustar automáticamente el tamaño de fuente para que se ajuste al tamaño de la página.
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AutoSetTheFontSizeOfTextStampToFitPage()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDirAsposePdfFacadesPages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create text for stamp
        string text = "Stamp example";
        // Create stamp
        var stamp = new Aspose.Pdf.TextStamp(text);
        stamp.AutoAdjustFontSizeToFitStampRectangle = true;
        stamp.AutoAdjustFontSizePrecision = 0.01f;
        stamp.WordWrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        stamp.Scale = false;
        //Add stamp
        document.Pages[1].AddStamp(stamp);

        // Save PDF document
        document.Save(dataDir + "AutoSetTheFontSizeOfTextStampToFItPage_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 24.11

Se ha añadido un método de extensión `PageCollection` para actualizar el número de página y los artefactos de encabezado/pie de fecha al agregar o insertar nuevas páginas. Las configuraciones para el número de página y el formato de fecha deben almacenarse en el documento original de acuerdo con la especificación PDF, tal como lo implementa Adobe Acrobat.

El siguiente fragmento de código demuestra cómo actualizar la paginación en el documento:
```csharp
private static void UpdatePagination()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document that contains at least one page with pagination artifacts
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithPaginationArtifacts.pdf"))
    {
        // Update pages
        document.Pages.Insert(1, document.Pages[2]);
        document.Pages.Add();

        // Update pagination artifacts
        document.Pages.UpdatePagination();

        // Save PDF document
        document.Save(dataDir + "DocumentWithUpdatedPagination.pdf");
    }
}
```

Desde la versión 24.11, hemos añadido la capacidad de elegir un algoritmo de hash para Pkcs7Detached. El predeterminado es SHA-256. Para las firmas digitales ECDSA, el algoritmo de digestión predeterminado depende de la longitud de la clave.

ECDSA admite SHA-1, SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384 y SHA3-512. Los algoritmos SHA3-256, SHA3-384 y SHA3-512 son compatibles solo para .NET 8 y versiones más nuevas. Para obtener detalles sobre las plataformas compatibles con SHA-3, consulte la [documentación](https://learn.microsoft.com/en-us/dotnet/standard/security/cross-platform-cryptography#sha-3).

RSA admite SHA-1, SHA-256, SHA-384 y SHA-512.

DSA solo admite SHA-1. Tenga en cuenta que SHA-1 está obsoleto y no cumple con los estándares de seguridad actuales.

El siguiente fragmento de código demuestra la configuración del algoritmo de hash para Pkcs7Detached:
```csharp
private static void SignWithManualDigestHashAlgorithm(string cert, string pass)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 detached object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, pass, Aspose.Pdf.DigestHashAlgorithm.Sha512);
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}
```

Se ha añadido una nueva propiedad `FontEncodingStrategy` a la clase `HtmlSaveOptions`. La especificación PDF recomienda utilizar la tabla `ToUnicode` para extraer el contenido de texto de los PDFs. Sin embargo, utilizar la tabla CMap de la fuente puede producir mejores resultados para ciertos tipos de documentos. A partir de la versión 24.11, puede elegir qué tabla utilizar para la decodificación. Por defecto, se utiliza la tabla `ToUnicode`.

El siguiente ejemplo demuestra la nueva opción utilizando:
```csharp
private static void ConvertPdfToHtmlUsingCMap()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            // New option there
            FontEncodingStrategy = Aspose.Pdf.HtmlSaveOptions.FontEncodingRules.DecreaseToUnicodePriorityLevel
        };
        // Save HTML document
        document.Save(dataDir + "CmapFontHTML_out.html", options);
    }
}
```

## Novedades en Aspose.PDF 24.10

El Algoritmo de Firma Digital de Curva Elíptica (ECDSA) es un algoritmo criptográfico moderno conocido por proporcionar una fuerte seguridad con tamaños de clave más pequeños en comparación con los algoritmos tradicionales. Desde la versión 24.10, ha sido posible firmar documentos PDF utilizando ECDSA, así como verificar firmas ECDSA. Las siguientes curvas elípticas son compatibles para crear y verificar firmas digitales:
* P-256 (secp256r1).
* P-384 (secp384r1).
* P-521 (secp521r1).
* brainpoolP256r1.
* brainpoolP384r1.
* brainpoolP512r1.

El algoritmo de hash SHA-256 se utiliza para generar la firma. Las firmas ECDSA se pueden verificar utilizando los siguientes algoritmos de hash: SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384 y SHA3-512.

Puede utilizar su código habitual para firmar documentos con ECDSA y verificar firmas:
 
```cs
private static void Sign(string cert, string pass)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 detached object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, pass);
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}

private static void Verify()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign_out.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Get annotation list of signature names in the document
            var sigNames = signature.GetSignNames();

            // Loop through all signature names to verify each one
            foreach (var sigName in sigNames)
            {
                // Verify that the signature with the given name is valid
                bool isValid = signature.VerifySignature(sigName);
                Console.WriteLine("Signature '{0}' validation returns {1}", sigName, isValid);
            }
        }
    }
}
```

A veces, es necesario recortar una imagen antes de insertarla en un PDF. Hemos añadido una versión sobrecargada del método `AddImage()` para soportar la adición de imágenes recortadas:

```cs
private static void AddCroppedImageToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Open image stream
        using (Stream imgStream = File.OpenRead(Path.Combine(dataDir, "Images", "Sample-01.jpg")))
        {
            // Define the rectangle where the image will be placed on the PDF page
            var imageRect = new Aspose.Pdf.Rectangle(17.62, 65.25, 602.62, 767.25);

            // Crop the image to half its original width and height
            var w = imageRect.Width / 2;
            var h = imageRect.Height / 2;
            var bbox = new Aspose.Pdf.Rectangle(imageRect.LLX, imageRect.LLY, imageRect.LLX + w, imageRect.LLY + h);

            // Add page
            var page = document.Pages.Add();

            // Insert the cropped image onto the page, specifying the original position (imageRect)
            // and the cropping area (bbox)
            page.AddImage(imgStream, imageRect, bbox);
        }

        // Save PDF document
        document.Save(dataDir + "AddCroppedImageMender_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 24.9

Desde la versión 24.9, ha sido posible generar un informe de fallos cuando la biblioteca lanza una excepción. Un informe de fallos incluye información sobre el tipo de excepción, título de la aplicación, versión de Aspose.PDF, versión del sistema operativo, mensaje de error y traza de pila.

El siguiente fragmento de código demuestra un escenario común para generar un informe de fallos:

```cs
private static void GenerateCrashReportExample()
{
    try
    {
        // some code
        // ....

        // Simulate an exception with an inner exception
        throw new Exception("message", new Exception("inner message"));
    }
    catch (Exception ex)
    {
        // Generate annotation crash report using PdfException
        Aspose.Pdf.PdfException.GenerateCrashReport(new Aspose.Pdf.CrashReportOptions(ex));
    }
}
```

La extracción de elementos de capas de un documento PDF y su guardado en un nuevo flujo PDF están disponibles desde ahora. En los documentos PDF, las capas (también conocidas como Grupos de Contenido Opcionales o OCGs) se utilizan para diversos propósitos, principalmente para gestionar y controlar la visibilidad del contenido dentro del documento. Esta funcionalidad es particularmente útil en diseño, ingeniería y publicación. Por ejemplo: aspectos de planos, componentes de diagramas complejos, versiones de idioma del mismo contenido.

```cs
private static void ExtractPdfLayer()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var inputDocument = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = inputDocument.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + string.Format("Layer_{0}.pdf", layer.Id));
        }
    }
}
```

Se ha añadido la clase `GraphicalPdfComparer` para la comparación gráfica de documentos y páginas PDF. La comparación gráfica se ocupa de las imágenes de las páginas del documento. Devuelve el resultado como un objeto `ImagesDifference` o como un documento PDF que contiene imágenes fusionadas del original y las diferencias. La comparación gráfica es más útil para documentos que tienen diferencias menores en contenido de texto o gráfico.

El siguiente fragmento de código demuestra la comparación gráfica de dos documentos PDF y guarda una imagen con las diferencias en el documento PDF resultante:

```cs
private static void ComparePDFWithCompareDocumentsToPdfMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf"))
        {
            // Create comparer
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer()
            {
                Threshold = 3.0,
                Color = Aspose.Pdf.Color.Blue,
                Resolution = new Aspose.Pdf.Devices.Resolution(300)
            };
            // Compare and save result
            comparer.CompareDocumentsToPdf(document1, document2, dataDir + "compareDocumentsToPdf_out.pdf");
        }
    }
}
```

API implementada para integrar FileFormat.HEIC y Aspose.PDF. El HEIC (Codificación de Imágenes de Alta Eficiencia) es un formato de archivo de imagen moderno introducido por Apple con iOS 11 en 2017 como el formato de imagen predeterminado para iPhones y iPads.

Para convertir imágenes HEIC a PDF, el usuario debe agregar la referencia al paquete NuGet `FileFormat.HEIC` y utilizar el siguiente fragmento de código:

```cs
private static void ConvertHEICtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open HEIC file
    using (var fs = new FileStream(dataDir + "HEICtoPDF.heic", FileMode.Open))
    {
        var image = FileFormat.Heic.Decoder.HeicImage.Load(fs);
        var pixels = image.GetByteArray(FileFormat.Heic.Decoder.PixelFormat.Rgb24);
        var width = (int)image.Width;
        var height = (int)image.Height;

        // Open PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            var page = document.Pages.Add();
            var asposeImage = new Aspose.Pdf.Image();
            asposeImage.BitmapInfo = new Aspose.Pdf.BitmapInfo(pixels, width, height, Aspose.Pdf.BitmapInfo.PixelFormat.Rgb24);
            page.PageInfo.Height = height;
            page.PageInfo.Width = width;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Left = 0;

            page.Paragraphs.Add(asposeImage);

            // Save PDF document
            document.Save(dataDir + "HEICtoPDF_out.pdf");
        }
    }
}
```

## Novedades en Aspose.PDF 24.8

Conversión de documentos PDF al formato PDF/A-4

Desde la versión 24.8, ha sido posible convertir documentos PDF al PDF/A-4. La Parte 4 del estándar, basada en PDF 2.0, se publicó a finales de 2020.

El siguiente fragmento de código demuestra cómo convertir un documento al formato PDF/A-4 cuando el documento de entrada es una versión PDF anterior a 2.0.

```cs
private static void ConvertPdfToPdfA4()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToPDFA.pdf"))
    {
        // If the document version is less than PDF-2.0, it must be converted to PDF-2.0
        document.Convert(Stream.Null, Aspose.Pdf.PdfFormat.v_2_0, Aspose.Pdf.ConvertErrorAction.Delete);

        // Convert to the PDF/A-4 format
        document.Convert(dataDir + "PDFA4ConversionLog.xml", Aspose.Pdf.PdfFormat.PDF_A_4, Aspose.Pdf.ConvertErrorAction.Delete);

        // Save PDF document
        document.Save(dataDir + "PDFToPDFA4_out.pdf");
    }
}
```

Desde 24.8 introdujimos un método para aplanar contenido transparente en documentos PDF:

```cs
private static void FlattenTransparency()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithTransparentImage.pdf"))
    {
        // Flatten image transparency
        document.FlattenTransparency();
        // Save PDF document
        document.Save(dataDir + "PdfWithFlattenedImage.pdf");
    }
}
```

## Novedades en Aspose.PDF 24.7

Comparación de documentos PDF con Aspose.PDF for .NET

Desde 24.7 es posible comparar el contenido de documentos PDF con marcas de anotación y salida lado a lado:

El primer fragmento de código demuestra cómo comparar las primeras páginas de dos documentos PDF.

```cs
private static void ComparingSpecificPagesSideBySide()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1],
                dataDir + "ComparingSpecificPages_out.pdf", new Aspose.Pdf.Comparison.SideBySideComparisonOptions
            {
                AdditionalChangeMarks = true,
                ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
            });
        }
    }
}
```

El segundo fragmento de código amplía el alcance para comparar todo el contenido de dos documentos PDF.

```cs
private static void ComparingEntireDocumentsSideBySide()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(
                document1,
                document2,
                dataDir + "ComparingEntireDocuments_out.pdf",
                new Aspose.Pdf.Comparison.SideBySideComparisonOptions
                {
                    AdditionalChangeMarks = true,
                    ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
                });
        }
    }
}
```

Además, en esta versión se añadió el plugin Aspose.PDF Security para .NET:

Función de cifrado:

```cs
var input = "sample.pdf";
var output = "encrypted.pdf";

var plugin = new Security();
var opt = new EncryptionOptions("123456789", "123", DocumentPrivilege.ForbidAll);
opt.AddInput(new FileDataSource(input));
opt.AddOutput(new FileDataSource(output));
plugin.Process(opt);
```

Función de descifrado:

```cs
var input = "encrypted.pdf";
var output = "decrypted.pdf";

var plugin = new Security();
var opt = new DecryptionOptions("123456789");
opt.AddInput(new FileDataSource(input));
opt.AddOutput(new FileDataSource(output));
plugin.Process(opt);
```

## Novedades en Aspose.PDF 24.6

Desde la versión 24.6, como parte de la edición de PDF etiquetados, se añadieron métodos en **Aspose.Pdf.LogicalStructure.Element**:

- Etiqueta (agregar etiquetas a operadores específicos como imágenes, texto y enlaces)
- InsertarHijo
- EliminarHijo
- LimpiarHijos

Además, en esta versión es posible crear un PDF accesible utilizando funciones de bajo nivel:

El siguiente fragmento de código trabaja con un documento PDF y su contenido etiquetado, utilizando una biblioteca Aspose.PDF para procesarlo.

```cs
private static void CreateAnAccessibleDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "tourguidev2_gb_tags.pdf"))
    {
        // Access tagged content
        Aspose.Pdf.Tagged.ITaggedContent content = document.TaggedContent;
        // Create annotation span element
        Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
        // Append span to root element
        content.RootElement.AppendChild(span);
        // Iterate over page contents
        foreach (var op in document.Pages[1].Contents)
        {
            var bdc = op as Aspose.Pdf.Operators.BDC;
            if (bdc != null)
            {
                span.Tag(bdc);
            }
        }
        // Save PDF document
        document.Save(dataDir + "AccessibleDocument_out.pdf");
    }
}
```

Desde 24.6, Aspose.PDF for .NET permite firmar PDF con X509Certificate2 en formato base64:

```cs
private static void SignWithBase64Certificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    var base64Str = "Certificate in base64 format";
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        var sign = new Aspose.Pdf.Forms.ExternalSignature(base64Str, false);// without Private Key
        sign.ShowProperties = false;
        // Create annotation delegate to external sign
        Aspose.Pdf.Forms.SignHash customSignHash = delegate (byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
        {
            // Simulated Server Part (This will probably just be sending data and receiving annotation response)
            var signerCert = new X509Certificate2(pfxFilePath, password, X509KeyStorageFlags.Exportable);// must have Private Key
            var rsaCSP = new RSACryptoServiceProvider();
            var xmlString = signerCert.PrivateKey.ToXmlString(true);
            rsaCSP.FromXmlString(xmlString);
            byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
            return signedData;
        };
        sign.CustomSignHash = customSignHash;
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "input.pdf");
        // Sign the file
        pdfSign.Sign(1, "second approval", "second_user@example.com", "Australia", false,
            new System.Drawing.Rectangle(200, 200, 200, 100),
            sign);
        // Save PDF document
        pdfSign.Save(dataDir + "SignWithBase64Certificate_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 24.5

Esta versión nos permite trabajar con capas PDF. Por ejemplo:

- bloquear una capa PDF
- extraer elementos de la capa PDF
- aplanar un PDF en capas
- fusionar todas las capas dentro del PDF en una

### Bloquear una capa PDF

Desde la versión 24.5, puedes abrir un PDF, bloquear una capa específica en la primera página y guardar el documento con los cambios. Se añadieron dos nuevos métodos y una propiedad:

Layer.Lock(); - Bloquea la capa.
Layer.Unlock(); - Desbloquea la capa.
Layer.Locked; - Propiedad que indica el estado de bloqueo de la capa.

```cs
private static void LockLayerInPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page and the first layer
        var page = document.Pages[1];
        var layer = page.Layers[0];

        // Lock the layer
        layer.Lock();

        // Save PDF document
        document.Save(dataDir + "LockLayerInPDF_out.pdf");
    }
}
```

### Extraer elementos de la capa PDF

La biblioteca Aspose.PDF for .NET permite extraer cada capa de la primera página y guardar cada capa en un archivo separado.

Para crear un nuevo PDF a partir de una capa, se puede utilizar el siguiente fragmento de código:

```cs
private static void ExtractPdfLayer()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var inputDocument = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = inputDocument.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + string.Format("Layer_{0}.pdf", layer.Id));
        }
    }
}
```

### Aplanar un PDF en capas

La biblioteca Aspose.PDF for .NET abre un PDF, itera a través de cada capa en la primera página y aplana cada capa, haciéndola permanente en la página.

```cs
private static void FlattenPdfLayers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Flatten each layer on the page
        foreach (var layer in page.Layers)
        {
            layer.Flatten(true);
        }

        // Save PDF document
        document.Save(dataDir + "FlattenedLayersPdf_out.pdf");
    }
}
```

El método 'Layer.Flatten(bool cleanupContentStream)' acepta el parámetro booleano que especifica si se deben eliminar los marcadores de grupo de contenido opcional del flujo de contenido. Establecer el parámetro cleanupContentStream en falso acelera el proceso de aplanamiento.

### Fusionar todas las capas dentro del PDF en una

La biblioteca Aspose.PDF for .NET permite fusionar todas las capas PDF o una capa específica en la primera página en una nueva capa y guardar el documento actualizado.

Se añadieron dos métodos para fusionar todas las capas en la página:

- void MergeLayers(string newLayerName);
- void MergeLayers(string newLayerName, string newOptionalContentGroupId); 

El segundo parámetro permite renombrar el marcador de grupo de contenido opcional. El valor predeterminado es "oc1" (/OC /oc1 BDC).

```cs
private static void MergePdfLayers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        page.MergeLayers("NewLayerName");
        // Or
        // page.MergeLayers("NewLayerName", "OC1");

        // Save PDF document
        document.Save(dataDir + "MergeLayersInPdf_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 24.4

Esta versión admite la aplicación de una máscara de recorte a imágenes:

```cs
private static void AddStencilMasksToImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddStencilMasksToImages.pdf"))
    {
        // Open the first mask image file
        using (var fs1 = new FileStream(dataDir + "mask1.jpg", FileMode.Open))
        {
            // Open the second mask image file
            using (var fs2 = new FileStream(dataDir + "mask2.png", FileMode.Open))
            {
                // Apply stencil mask to the first image on the first page
                document.Pages[1].Resources.Images[1].AddStencilMask(fs1);

                // Apply stencil mask to the second image on the first page
                document.Pages[1].Resources.Images[2].AddStencilMask(fs2);
            }
        }

        // Save PDF document
        document.Save(dataDir + "AddStencilMasksToImages_out.pdf");
    }
}
```

Desde 24.4 puedes seleccionar la fuente de papel elegida por el tamaño de página PDF en el cuadro de diálogo de impresión utilizando la API.

A partir de Aspose.PDF 24.4, esta preferencia se puede activar y desactivar utilizando la propiedad Document.PickTrayByPdfSize o la fachada PdfContentEditor:

```cs
private static void PickTrayByPdfSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello world!"));

        // Set the flag to choose annotation paper tray using the PDF page size
        document.PickTrayByPdfSize = true;

        // Save PDF document
        document.Save(dataDir + "PickTrayByPdfSize_out.pdf");
    }
}
```

```cs
private static void PickTrayByPdfSizeFacade()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create the PdfContentEditor facade
    using (var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        contentEditor.BindPdf(dataDir + "PrintDocument.pdf");

        // Set the flag to choose annotation paper tray using the PDF page size
        contentEditor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.PickTrayByPDFSize);

        // Save PDF document
        contentEditor.Save(dataDir + "PickTrayByPdfSizeFacade_out.pdf");
    }
}
```

Desde esta versión se añadió el plugin Aspose.PDF Signature para .NET:

- Ejemplo de creación de un nuevo campo y opciones:

```cs
// create Signature
var plugin = new Signature();
// create SignOptions object to set instructions
var opt = new SignOptions(inputPfxPath, inputPfxPassword);
// add input file path
opt.AddInput(new FileDataSource(inputPath));
// set output file path
opt.AddOutput(new FileDataSource(outputPath));
// set extra options
opt.Reason = "my Reason";
opt.Contact = "my Contact";
opt.Location = "my Location";
// perform the process
plugin.Process(opt);
```

- Ejemplo con un campo vacío existente

```cs
// create Signature
var plugin = new Signature();
// create SignOptions object to set instructions
var opt = new SignOptions(inputPfxPath, inputPfxPassword);
// add input file path with empty signature field
opt.AddInput(new FileDataSource(inputPath));
// set output file path
opt.AddOutput(new FileDataSource(outputPath));
// set name of existing signature field
opt.Name = "Signature1";
// perform the process
plugin.Process(opt);
```

## Novedades en Aspose.PDF 24.3

Desde esta versión se añadió el plugin PDF/A Converter para .NET:

```cs
var options = new PdfAConvertOptions
{
    PdfAVersion = PdfAStandardVersion.PDF_A_3B
};

// Add the source file
options.AddInput(new FileDataSource("path_to_your_pdf_file.pdf")); // replace with your actual file path

// Add the path to save the converted file
options.AddOutput(new FileDataSource("path_to_the_converted_file.pdf"));

// Create the plugin instance
var plugin = new PdfAConverter();

// Run the conversion
plugin.Process(options);
```

- Implementar una búsqueda a través de una lista de frases en un TextFragmentAbsorber:

```cs
private static void SearchMultipleRegex()
{
    // Create resular expressions
    var regexes = new Regex[]
    {
        new Regex(@"(?s)document\s+(?:(?:no\(?s?\)?\.?)|(?:number(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|and)*)", RegexOptions.IgnoreCase),
        new Regex(@"[\s\r\n]+Tract[\s\r\n]+of:? ", RegexOptions.IgnoreCase),
        new Regex(@"vested[\s\r\n]+in", RegexOptions.IgnoreCase),
        new Regex("Vested in:", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+(?:nos?|numbers?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
        new Regex(@"file.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
    };

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchRegularExpressionAll.pdf"))
    {
        // Create TextAbsorber object to find all instances of the input search phrase
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber(regexes, new Aspose.Pdf.Text.TextSearchOptions(true));
        document.Pages.Accept(absorber);
        // Get result
        var result = absorber.RegexResults;
    }
}
```

Desde 24.3 es posible agregar un campo de firma vacío en cada página del archivo PDF/A.

```cs
private static void AddEmptySignatureFieldOnEveryPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    var fieldName = "signature_1234";

    using (var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf"))
    {
        // The new suggested code, using SignatureField object
        var signatureField = new Aspose.Pdf.Forms.SignatureField(document.Pages[1], new Aspose.Pdf.Rectangle(10, 10, 100, 100));

        // Add the default appearance for the signature field
        signatureField.DefaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance("Helv", 12, System.Drawing.Color.Black);
        var newAddedField = document.Form.Add(signatureField, fieldName, 1);

        // Find annotation associated with the field
        Aspose.Pdf.Annotations.Annotation addedAnnotation = null;
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[1].Annotations)
        {
            if (annotation.FullName == fieldName)
            {
                addedAnnotation = annotation;
                break;
            }
        }

        // Add the annotation to every page except of initial
        if (addedAnnotation != null)
        {
            for (int p = 2; p <= document.Pages.Count; p++)
            {
                document.Pages[p].Annotations.Add(addedAnnotation);
            }
        }

        // Save PDF document
        document.Save(dataDir + "outputPdfaWithSignatureFields.pdf");
    }
}
```

## Novedades en Aspose.PDF 24.2

Desde 24.2 es posible obtener los datos vectoriales de un archivo PDF.

Se implementó GraphicsAbsorber para obtener datos vectoriales de documentos:

```cs
private static void UsingGraphicsAbsorber()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open the document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Step 5: Display information about the extracted elements
            foreach (var element in graphicsAbsorber.Elements)
            {
                Console.WriteLine($"Page Number: {element.SourcePage.Number}");
                Console.WriteLine($"Position: ({element.Position.X}, {element.Position.Y})");
                Console.WriteLine($"Number of Operators: {element.Operators.Count}");
            }
        }
    }
}
```

## Novedades en Aspose.PDF 24.1

Desde la versión 24.1 es posible importar anotaciones en formato FDF a PDF:

```cs
private static void ImportFDFByForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "input.pdf"))
    {
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }
        // Save PDF document
        form.Save(dataDir + "ImportDataFromPdf_Form_out.pdf");
    }
}
```

Además, admite el acceso al Diccionario de Página o al Catálogo de Documento.

Aquí hay ejemplos de código para DictionaryEditor:

- Agregar nuevos valores

```cs
/private static void AddNewKeysToPdfPageDicrionary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // example of key's names
    string KEY_NAME = "name";
    string KEY_STRING = "str";
    string KEY_BOOL = "bool";
    string KEY_NUMBER = "number";

    // Open the document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);

        dictionaryEditor.Add(KEY_NAME, new Aspose.Pdf.DataEditor.CosPdfName("name data"));
        dictionaryEditor.Add(KEY_STRING, new Aspose.Pdf.DataEditor.CosPdfString("string data"));
        dictionaryEditor.Add(KEY_BOOL, new Aspose.Pdf.DataEditor.CosPdfBoolean(true));
        dictionaryEditor.Add(KEY_NUMBER, new Aspose.Pdf.DataEditor.CosPdfNumber(11.2));

        // Save PDF document
        document.Save(dataDir + "PageDictionaryEditor_out.pdf");
    }
}
```

- Agregar y establecer valores en el diccionario

```cs
private static void ModifyKeysInPdfPageDicrionary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    string KEY_NAME = "name";

    // Open the document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new Aspose.Pdf.DataEditor.CosPdfName("Old data"));
        // Modify existing value
        dictionaryEditor[KEY_NAME] = new Aspose.Pdf.DataEditor.CosPdfName("New data");

        // Save PDF document
        document.Save(dataDir + "PageDictionaryEditorEdit_out.pdf");
    }
}
```

- Obtener valor del diccionario

```cs
private static void GetValuesFromPdfPageDicrionary()
{
    string KEY_NAME = "name";

    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);
        dictionaryEditor[KEY_NAME] = new Aspose.Pdf.DataEditor.CosPdfName("name");
        var value = dictionaryEditor[KEY_NAME];
        // or 
        Aspose.Pdf.DataEditor.ICosPdfPrimitive primitive;
        dictionaryEditor.TryGetValue(KEY_NAME, out primitive);
    }
}
```

- Eliminar valor del diccionario

```cs
private static void RemoveFromPdfPageDicrionary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    string KEY_NAME = "name";
    string EXPECTED_NAME = "name data";

    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var dictionaryEditor = new Aspose.Pdf.DataEditor.DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new Aspose.Pdf.DataEditor.CosPdfName(EXPECTED_NAME));
        dictionaryEditor.Remove(KEY_NAME);

        // Save PDF document
        document.Save(dataDir + "PageDictionaryEditorRemove_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 23.12

Se puede encontrar el formulario y el texto se puede reemplazar utilizando el siguiente fragmento de código:

```cs
private static void ReplaceTextInPdfForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextBox.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        foreach (var form in forms)
        {
            // Check if the form is of type "Typewriter" and subtype "Form"
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                // Create a TextFragmentAbsorber to find text fragments
                var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
                absorber.Visit(form);

                // Clear the text in each fragment
                foreach (var fragment in absorber.TextFragments)
                {
                    fragment.Text = "";
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```            

O, el formulario se puede eliminar por completo:

```cs
private static void DeleteSpecifiedForm1()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        for (int i = forms.Count; i > 0; i--)
        {
            if (forms[i].IT == "Typewriter" && forms[i].Subtype == "Form")
            {
                forms.Delete(forms[i].Name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```            

Otra variante de eliminar el formulario:

```cs
private static void DeleteSpecifiedForm2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        foreach (var form in forms)
        {
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                var name = forms.GetFormName(form);
                forms.Delete(name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
``` 

- Todos los formularios se pueden eliminar utilizando el siguiente fragmento de código:

```cs
private static void RemoveAllForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Clear all forms
        forms.Clear();

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```

- Implementar conversión de PDF a Markdown:

```cs
private static void ConvertPDFtoMarkup()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "demo.pdf"))
    {
        // Create an instance of MarkdownSaveOptions to configure the Markdown export settings
        var saveOptions = new MarkdownSaveOptions()
        {
            // Set to false to prevent the use of HTML <img> tags for images in the Markdown output
            UseImageHtmlTag = false
        };
        
        // Specify the directory name where resources (like images) will be stored
        saveOptions.ResourcesDirectoryName = "images";

        // Save PDF document in Markdown format to the specified output file path using the defined save options
        document.Save(dataDir + "PDFtoMarkup_out.md", saveOptions);
    }
}
```

- Implementar conversión de OFD a PDF:

```cs
private static void ConvertOFDToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    // Convert options
    var options = new Aspose.Pdf.OfdLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertOFDToPDF.ofd", options))
    {
        // Save PDF document
        document.Save(dataDir + "ConvertOFDToPDF_out.pdf");
    }
}
```

Desde esta versión se añadió el plugin Merger:

```cs
private static void PdfMergeUsingPlugin()
{
    string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Create annotation new instance of Merger
    using (var merger = new Aspose.Pdf.Plugins.Merger())
    {
        // Create MergeOptions
        var opt = new Aspose.Pdf.Plugins.MergeOptions();
        opt.AddInput(new Aspose.Pdf.Plugins.FileDataSource(dataDir + "Concat1.pdf"));
        opt.AddInput(new Aspose.Pdf.Plugins.FileDataSource(dataDir + "Concat2.pdf"));
        opt.AddOutput(new Aspose.Pdf.Plugins.FileDataSource(dataDir + "ConcatenatePdfFiles_out.pdf"));

        // Process the PDF merging
        merger.Process(opt);
    }
}
```

Además, desde esta versión se añadió el plugin ChatGPT:

```cs
private static async void InvokeChatGptPlugin()
{
    using (var plugin = new Aspose.Pdf.Plugins.PdfChatGpt())
    {
        var options = new Aspose.Pdf.Plugins.PdfChatGptRequestOptions();
        options.AddOutput(new Aspose.Pdf.Plugins.FileDataSource("PdfChatGPT_output.pdf")); // Add the output file path.
        options.ApiKey = "Your API key."; // You need to provide the key to access the API.
        options.MaxTokens = 1000; // The maximum number of tokens to generate in the chat completion.

        // Add the request messages.
        options.Messages.Add(new Aspose.Pdf.Plugins.Message
        {
            Content = "You are annotation helpful assistant.",
            Role = Aspose.Pdf.Plugins.Role.System
        });
        options.Messages.Add(new Aspose.Pdf.Plugins.Message
        {
            Content = "What is the biggest pizza diameter ever made?",
            Role = Aspose.Pdf.Plugins.Role.User
        });

        // Process the request.
        var result = await plugin.ProcessAsync(options);

        var fileResultPath = result.ResultCollection[0].Data;

        // The ChatGPT API chat completion object.
        var chatCompletionObject = result.ResultCollection[1].Data as Aspose.Pdf.Plugins.ChatCompletion;
    }
}
```

## Novedades en Aspose.PDF 23.11

Desde esta versión es posible eliminar texto oculto de un archivo PDF:

```cs
private static void RemoveHiddenText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "HiddenText.pdf"))
    {
        // Use TextFragmentAbsorber with no parameters to get all text
        var textAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        // This option can be used to prevent other text fragments from moving after hidden text replacement
        textAbsorber.TextReplaceOptions = new Aspose.Pdf.Text.TextReplaceOptions(Aspose.Pdf.Text.TextReplaceOptions.ReplaceAdjustment.None);

        document.Pages.Accept(textAbsorber);

        // Remove hidden text
        foreach (var fragment in textAbsorber.TextFragments)
        {
            if (fragment.TextState.Invisible)
            {
                fragment.Text = "";
            }
        }

        // Save PDF document
        document.Save(dataDir + "HiddenText_out.pdf");
    }
}
```

Desde 23.11 admite la interrupción de hilos:

```cs
private static void InterruptExample()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    using (var monitor = new Aspose.Pdf.Multithreading.InterruptMonitor())
    {
        // An class that can produce long-drawn-out work
        RowSpanWorker worker = new RowSpanWorker(dataDir + "RowSpanWorker_out.pdf", monitor);

        var thread = new System.Threading.Thread(new System.Threading.ThreadStart(worker.Work));
        thread.Start();

        // The timeout should be less than the time required for full document save (without interruption)
        System.Threading.Thread.Sleep(500);

        // Interrupt the process
        monitor.Interrupt();

        // Wait for interruption...
        thread.Join();
    }
}

private class RowSpanWorker
{
    private readonly string outputPath;
    private readonly Aspose.Pdf.Multithreading.InterruptMonitor monitor;

    public RowSpanWorker(string outputPath, Aspose.Pdf.Multithreading.InterruptMonitor monitor)
    {
        this.outputPath = outputPath;
        this.monitor = monitor;
    }

    public void Work()
    {
        // This is some large text, used Lorem Ipsum in 10000 characters to cause suspension in processing
        string text = RunExamples.GetLoremIpsumString(10000);

        // Open PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            Aspose.Pdf.Multithreading.InterruptMonitor.ThreadLocalInstance = this.monitor;
            var page = document.Pages.Add();

            var table = new Aspose.Pdf.Table
            {
                DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F)
            };

            var row0 = table.Rows.Add();

            // Add annotation cell that spans for two rows and contains annotation long-long text
            var cell00 = row0.Cells.Add(text);
            cell00.RowSpan = 2;
            cell00.IsWordWrapped = true;
            row0.Cells.Add("Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum ");
            row0.Cells.Add("Dolor Dolor Dolor Dolor Dolor Dolor ");

            var row1 = table.Rows.Add();
            row1.Cells.Add("IpsumDolor Dolor Dolor Dolor Dolor ");
            row1.Cells.Add("DolorDolor Dolor Dolor Dolor Dolor ");

            page.Paragraphs.Add(table);

            try
            {
                // Save PDF document
                document.Save(this.outputPath);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}
```

## Novedades en Aspose.PDF 23.10

La actualización actual presenta tres versiones de eliminación de etiquetas de PDFs etiquetados.

- Eliminar algún elemento nodo de un documentElement (elemento raíz del árbol):

```cs
private static void RemoveStructElement()
{
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StructureElementsTree.pdf"))
    {
        // Access to root element(s)
        var structure = document.LogicalStructure;
        var documentElement = structure.Children[0];
        var structElement = documentElement.Children.Count > 1 ? documentElement.Children[1] as Aspose.Pdf.Structure.StructElement : null;

        if (documentElement.Children.Remove(structElement))
        {
            // Element removed. Save PDF document.
            document.Save(dataDir + "StructureElementsRemoved.pdf");
        }

        // You can also delete the structElement itself
        //if (structElement != null)
        //{
        //    structElement.Remove();
        //    document.Save(outputPdfPath);
        //}
    }
}
```

- Eliminar todas las etiquetas de elementos marcados del documento, pero mantener los elementos de estructura:

```cs
private static void RemoveMarkedElementsTags()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TH.pdf"))
    {
        // Access to root element(s)
        var structure = document.LogicalStructure;
        var root = structure.Children[0];
        var queue = new Queue<Aspose.Pdf.Structure.Element>();
        queue.Enqueue(root);

        while (queue.TryDequeue(out var element))
        {
            foreach (var child in element.Children)
            {
                queue.Enqueue(child);
            }

            if (element is Aspose.Pdf.Structure.TextElement || element is Aspose.Pdf.Structure.FigureElement)
            {
                element.Remove();
            }
        }

        // Save PDF document
        document.Save(dataDir + "MarkedElementsTagsRemoved.pdf");
    }
}
```

- Eliminar etiquetas por completo:

```cs
private static void RemoveTags()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TH.pdf"))
    {
        // Access to root element(s)
        var structure = document.LogicalStructure;
        var documentElement = structure.Children[0];
        documentElement.Remove();

        // Save PDF document
        document.Save(dataDir + "TagsRemoved.pdf");
    }
}
```

Desde 23.10 se implementó una nueva función para medir la altura de los caracteres. Utilice el siguiente código para medir la altura de un carácter.

```cs
private static void DisplayCharacterHeight()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextFragmentAbsorber to get information about state of document text
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);

        // Get height of 'A' character being displayed with font of first text fragment
        var textState = absorber.TextFragments[1].TextState;
        var height = textState.MeasureHeight('A');
        Console.WriteLine("The height of 'A' character displayed with {0} font size of {1} is {2:N3}", textState.Font.FontName, textState.FontSize,height);
    }
}
```

Tenga en cuenta que la medición se basa en la fuente incrustada en el documento. Si falta información para una dimensión, este método devuelve 0.

Además, esta versión proporciona la firma de un PDF utilizando un HASH firmado:

```cs
private static void SignPdfUsingSignedHash(string certP12, string pfxPassword)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        sign.BindPdf(dataDir + "input.pdf");
        var pkcs7 = new Aspose.Pdf.Forms.PKCS7(certP12, pfxPassword);

        // Create a delegate to external sign
        pkcs7.CustomSignHash = delegate (byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
        {
            X509Certificate2 signerCert = new X509Certificate2(certP12, pfxPassword, X509KeyStorageFlags.Exportable);
            RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
            var xmlString = signerCert.PrivateKey.ToXmlString(true);    //not supported on core 2.0
            rsaCSP.FromXmlString(xmlString);                            //not supported on core 2.0

            byte[] signedData = rsaCSP.SignHash(signableHash, CryptoConfig.MapNameToOID("SHA1"));
            return signedData;
        };

        // Sign PDF file
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);

        // Save PDF document
        sign.Save(dataDir + "SignWithCertificate_out.pdf");
    }

    // Verify
    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        sign.BindPdf(dataDir + "SignWithCertificate_out.pdf");

        if (!sign.VerifySignature("Signature1"))
        {
            throw new Exception("Not verified");
        }
    }
}
```

Una nueva función más es la Escala de Página de los Ajustes del Cuadro de Diálogo de Impresión:

```cs
private static void SetPrintScaling()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        // Disable print scaling
        document.PrintScaling = PrintScaling.None;

        // Save PDF document
        document.Save(dataDir + "SetPrintScaling_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 23.9

Desde 23.9 se admite la eliminación de una anotación secundaria de un campo rellenable.

```cs
private static void RemoveChildAnnotationFromFillableField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FieldWithChildAnnots.pdf"))
    {
        // Get field with child annotations
        var field = (Aspose.Pdf.Forms.Field)document.Form["1 Vehicle Identification Number"];
        // Get first child annotation
        var annotation = field[1];
        // Remove the annotation
        document.Pages[annotation.PageIndex].Annotations.Remove(annotation);

        // Save PDF document
        document.Save(dataDir + "RemoveChildAnnotation_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 23.8

Desde 23.8 se admite la detección de Actualizaciones Incrementales.

Se ha añadido la función para detectar Actualizaciones Incrementales en un documento PDF. Esta función devuelve 'true' si un documento se guardó con actualizaciones incrementales; de lo contrario, devuelve 'false'.

```cs
private static bool HasIncrementalUpdate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithIncrementalUpdate.pdf"))
    {
        // New method
        bool hasIncrementalUpdate = document.HasIncrementalUpdate();

        Console.WriteLine("Document {0} incremental update check returns: {1}", document.FileName, hasIncrementalUpdate);
        return hasIncrementalUpdate;
    }
}
```

Además, 23.8 admite formas de trabajar con campos de casilla de verificación anidados. Muchos formularios PDF rellenables tienen campos de casilla de verificación que actúan como grupos de radio:

- Crear campo de casilla de verificación de múltiples valores:

```cs
private static void CreateMultivalueCheckboxField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        var checkbox = new Aspose.Pdf.Forms.CheckboxField(page, new Aspose.Pdf.Rectangle(50, 50, 70, 70));

        // Set the first checkbox group option value
        checkbox.ExportValue = "option 1";

        // Add new option right under existing ones
        checkbox.AddOption("option 2");

        // Add new option at the given rectangle
        checkbox.AddOption("option 3", new Aspose.Pdf.Rectangle(100, 100, 120, 120));

        document.Form.Add(checkbox);

        // Select the added checkbox
        checkbox.Value = "option 2";

        // Save PDF document
        document.Save(dataDir + "MultivalueCheckboxField.pdf");
    }
}
```

- Obtener y establecer el valor de una casilla de verificación de múltiples valores:

```cs
private static void GetAndSetValueOfMultivalueCheckboxField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MultivalueCheckboxField.pdf"))
    {
        var form = document.Form;
        var checkbox = form.Fields[0] as Aspose.Pdf.Forms.CheckboxField;

        // Allowed values may be retrieved from the AllowedStates collection
        // Set the checkbox value using Value property
        checkbox.Value = checkbox.AllowedStates[0];
        var checkboxValue = checkbox.Value; // the previously set value, e.g. "option 1"

        // The value should be any element of AllowedStates
        checkbox.Value = "option 2";
        checkboxValue = checkbox.Value; // option 2

        // Uncheck boxes by either setting Value to "Off" or setting Checked to false
        checkbox.Value = "Off";
        // or, alternately:
        // checkbox.Checked = false;
        checkboxValue = checkbox.Value; // Off
    }
}
```

## Novedades en Aspose.PDF 23.7

Desde Aspose.PDF 23.7 se admite la extracción de formas:

```cs
private static void CopyShape()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

    // Open PDF document
    using (var sourceDocument = new Aspose.Pdf.Document(dataDir + "test.pdf"))
    {
        // Create PDF document
        using (var destDocument = new Aspose.Pdf.Document())
        {
            // Absorb vector graphics from the source document
            var graphicAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber();
            graphicAbsorber.Visit(sourceDocument.Pages[1]);

            // Copy the graphics into the destination document specified page and area
            var area = new Aspose.Pdf.Rectangle(90, 250, 300, 400);
            destDocument.Pages[1].AddGraphics(graphicAbsorber.Elements, area);

            // Save PDF document
            destDocument.Save(dataDir + "CopyShape_out.pdf");
        }
    }
}
```

También se admite la capacidad de detectar desbordamiento al agregar texto:

```cs
private static void FitTextIntoRectangle()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document()) 
    {
        // Generate text to add: "Lorem Ipsum" text of 1000 characters
        var paragraphContent = RunExamples.GetLoremIpsumString(1000);
        // Create a text fragment with the desired text
        var fragment = new Aspose.Pdf.Text.TextFragment(paragraphContent);
        // Declare the rectangle to fit text into
        var rectangle = new Aspose.Pdf.Rectangle(100, 600, 500, 700, false);
        
        // Check whether the text fits into the rectangle
        var isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);

        // Iteratively decrease font size until text fits the rectangle
        while (!isFitRectangle)
        {
            fragment.TextState.FontSize -= 0.5f;
            isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);
        }

        // Create a paragraph from the text fragment in the specified rectangle. Now you may be sure it fits.
        var paragraph = new Aspose.Pdf.Text.TextParagraph();
        paragraph.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
        paragraph.FormattingOptions.WrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;
        paragraph.Rectangle = rectangle;
        paragraph.AppendLine(fragment);

        // Create a text builder to place the paragraph on the document page
        var builder = new Aspose.Pdf.Text.TextBuilder(document.Pages.Add());
        builder.AppendParagraph(paragraph);

        // Save PDF document
        document.Save(dataDir + "FitTextIntoRectangle_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 23.6

Desde Aspose.PDF 23.6 se admite la adición de los siguientes plugins:

- Aspose PdfConverter Html a PDF 
- Aspose PdfOrganizer API de Redimensionar
- Aspose PdfOrganizer API de Comprimir

Actualizar el Aspose.PdfForm 
- agregar la función ‘Exportar "Valores de campos en el documento a archivo CSV"
- agregar la capacidad de establecer propiedades para campos separados

También se admite la capacidad de establecer el título de la página HTML, Epub:

```cs
private static void SetHtmlTitle()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            ExplicitListOfSavedPages = new[] { 1 },
            SplitIntoPages = false,
            FixedLayout = true,
            CompressSvgGraphicsIfAny = false,
            SaveTransparentTexts = true,
            SaveShadowedTextsAsTransparentTexts = true,
            FontSavingMode = Aspose.Pdf.HtmlSaveOptions.FontSavingModes.AlwaysSaveAsWOFF,
            RasterImagesSavingMode = Aspose.Pdf.HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground,
            PartsEmbeddingMode = Aspose.Pdf.HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml,
            // New property
            Title = "Title for page"
        };

        // Save HTML document
        document.Save(dataDir + "SetHtmlTitle_out.html", options);
    }
}
```

## Novedades en Aspose.PDF 23.5

Desde 23.5 se admite la opción FontSize de RedactionAnnotation. Utilice el siguiente fragmento de código para resolver esta tarea:

```cs
private static void AddRedactionAnnotationFontSize() 
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf")) 
    {
        // Create RedactionAnnotation instance for specific page region
        var annot = new Aspose.Pdf.Annotations.RedactionAnnotation(document.Pages[1],
            new Aspose.Pdf.Rectangle(367, 756.919982910156, 420, 823.919982910156));
        annot.FillColor = Aspose.Pdf.Color.Black;

        annot.BorderColor = Aspose.Pdf.Color.Yellow;
        annot.Color = Aspose.Pdf.Color.Blue;
        // Text to be printed on redact annotation
        annot.OverlayText = "(Unknown)";
        annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        // Repat Overlay text over redact Annotation
        annot.Repeat = false;

        // New property
        annot.FontSize = 20;

        // Add annotation to annotations collection of first page
        document.Pages[1].Annotations.Add(annot);
        // Flattens annotation and redacts page contents (i.e. removes text and image under redacted annotation)
        annot.Redact();
        // Save PDF document
        document.Save(dataDir + "AddRedactionAnnotationFontSize_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 23.4

Aspose.PDF anunció el lanzamiento del SDK .NET 7.

## Novedades en Aspose.PDF 23.3.1

Desde Aspose.PDF 23.3 se admite la adición de los siguientes plugins:

- Aspose.PdfForm
- Aspose.PdfConverter PDF a HTML
- Aspose.PdfConverter PDF a XLSX
- Aspose.PdfOrganizer Rotar
- Aspose.PdfExtrator para Imágenes

## Novedades en Aspose.PDF 23.3

La versión 23.3 introdujo soporte para mantener las proporciones y la resolución de la imagen al insertarla en la página. Se pueden utilizar dos métodos para resolver este problema:

```cs
private static void InsertImageWithNativeResolutionAsTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        var table = new Aspose.Pdf.Table
        {
            ColumnWidths = "600"
        };

        for (var j = 0; j < 2; j++)
        {
            var row = table.Rows.Add();
            var cell = row.Cells.Add();
            cell.Paragraphs.Add(new Aspose.Pdf.Image()
            {
                IsApplyResolution = true,
                File = dataDir + "Image1.jpg"
            });
        }

        page.Paragraphs.Add(table);

        // Save PDF document
        document.Save(dataDir + "ImageWithNativeResolutionAsTable_out.pdf");
    }
}
```

Y el segundo enfoque:

```cs
private static void InsertImageWithNativeResolutionAsParagraph()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();

        for (var j = 0; j < 2; j++)
        {
            page.Paragraphs.Add(new Aspose.Pdf.Image()
            {
                IsApplyResolution = true,
                File = dataDir + "Image1.jpg"
            });
        }

        // Save PDF document
        document.Save(dataDir + "ImageWithNativeResolutionAsParagraph_out.pdf");
    }
}
```

La imagen se colocará en un tamaño escalado y resolución nativa. Puede establecer propiedades FixedWidth o FixedHeight en combinación con IsApplyResolution.

## Novedades en Aspose.PDF 23.1.1

Desde Aspose.PDF 23.1.1 se admite la adición de los siguientes plugins:

- Plugin Aspose.PdfOrganizer
- Plugin Aspose.PdfExtractor

## Novedades en Aspose.PDF 23.1

Desde la versión 23.1 se admite la creación de anotaciones de marcas de impresora.

Las marcas de impresora son símbolos gráficos o texto añadidos a una página para ayudar al personal de producción a identificar componentes de un trabajo de múltiples placas y mantener una salida consistente durante la producción. Ejemplos comúnmente utilizados en la industria de la impresión incluyen:

- Objetivos de registro para alinear placas
- Rampas grises y barras de color para medir colores y densidades de tinta
- Marcas de corte que muestran dónde se debe recortar el medio de salida

Mostraremos el ejemplo de la opción con barras de color para medir colores y densidades de tinta. Hay una clase abstracta básica PrinterMarkAnnotation y de ella la clase hija ColorBarAnnotation - que ya implementa estas franjas. Vamos a revisar el ejemplo:

```cs
private static void AddPrinterMarkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        page.TrimBox = new Aspose.Pdf.Rectangle(20, 20, 580, 820);

        var rectBlack = new Aspose.Pdf.Rectangle(100, 300, 300, 320);
        var rectCyan = new Aspose.Pdf.Rectangle(200, 600, 260, 690);
        var rectMagenta = new Aspose.Pdf.Rectangle(10, 650, 140, 670);

        var colorBarBlack = new Aspose.Pdf.Annotations.ColorBarAnnotation(page, rectBlack);
        var colorBarCyan = new Aspose.Pdf.Annotations.ColorBarAnnotation(page, rectCyan,
            Aspose.Pdf.Annotations.ColorsOfCMYK.Cyan);
        var colorBarMagenta = new Aspose.Pdf.Annotations.ColorBarAnnotation(page, rectMagenta);
        colorBarMagenta.ColorOfCMYK = Aspose.Pdf.Annotations.ColorsOfCMYK.Magenta;
        var colorBarYellow = new Aspose.Pdf.Annotations.ColorBarAnnotation(page,
            new Aspose.Pdf.Rectangle(400, 250, 450, 700), Aspose.Pdf.Annotations.ColorsOfCMYK.Yellow);

        page.Annotations.Add(colorBarBlack);
        page.Annotations.Add(colorBarCyan);
        page.Annotations.Add(colorBarMagenta);
        page.Annotations.Add(colorBarYellow);

        // Save PDF document
        document.Save(dataDir + "PrinterMarkAnnotation_out.pdf");
    }
}
```
También se admite la extracción de imágenes vectoriales. Intente utilizar el siguiente código para detectar y extraer gráficos vectoriales:

```cs
private static void SavePdfVectorGraphicToSvg()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Graphs();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "test.pdf"))
    {
        // Attempt to save the vector graphics into a specified SVG file
        document.Pages[1].TrySaveVectorGraphics(dataDir + "PdfVectorGraphicToSvg.svg");
    }
}
```

## Novedades en Aspose.PDF 22.12

Desde esta versión se admite la conversión de PDF a imagen DICOM.

```cs
private static void PdfToDicom()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PagesToImages.pdf"))
    {
        var dicom = new Aspose.Pdf.Devices.DicomDevice();
        FileStream outStream = new FileStream(dataDir + "PdfToDicom_out.dcm", FileMode.Create, FileAccess.ReadWrite);
        dicom.Process(document.Pages[1], outStream);
    }
}
```    

## Novedades en Aspose.PDF 22.09

Desde 22.09 se admite la adición de propiedades para modificar el orden de las rúbricas del sujeto (E=, CN=, O=, OU=, ) en la firma.

```cs
private static void SignPdfWithModifiedOrderOfSubjectRubrics(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var fileSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        fileSign.BindPdf(dataDir + "DigitallySign.pdf");

        var rect = new System.Drawing.Rectangle(100, 100, 400, 100);
        var signature = new Aspose.Pdf.Forms.PKCS7Detached(pfxFilePath, password);

        // Set signature custom appearance
        signature.CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance()
        {
            UseDigitalSubjectFormat = true,
            DigitalSubjectFormat = new Aspose.Pdf.Forms.SubjectNameElements[] { Aspose.Pdf.Forms.SubjectNameElements.CN, Aspose.Pdf.Forms.SubjectNameElements.O }
            //or
            //DigitalSubjectFormat = new Aspose.Pdf.Forms.SubjectNameElements[] { Aspose.Pdf.Forms.SubjectNameElements.OU, Aspose.Pdf.Forms.SubjectNameElements.S, Aspose.Pdf.Forms.SubjectNameElements.C }
        };

        // Sign PDF file
        fileSign.Sign(1, true, rect, signature);
        // Save PDF document
        fileSign.Save(dataDir + "SignPdfWithModifiedOrderOfSubjectRubrics_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 22.6

Desde 22.5 se admite la extracción de texto SubScript y SuperScript de PDF.

Si el documento PDF contiene texto SubScript y SuperScript como H2O, entonces la extracción del texto del PDF también debe extraer su información de formato (en el texto plano extraído).
Si el PDF contiene texto en cursiva, también debe incluirse en el contenido extraído.

```cs
private static void ExtractTextSuperscript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextWithSubscriptsSuperscripts.pdf"))
    {
        // Use TextFragmentAbsorber with no parameters to get all text
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);

        // Iterate through text fragments to find superscript text
        foreach (var textFragment in absorber.TextFragments) 
        {
            if (textFragment.TextState.Superscript)
            {
                Console.WriteLine(String.Format("Text {0} at {1} is superscript!", textFragment.Text, textFragment.Position));
            }
        }
    }
}
```

## Novedades en Aspose.PDF 22.4

Esta versión incluye información para Aspose.PDF for .NET:

- PDF a ODS: Reconocer texto en subíndice y superíndice;

**ejemplo**

```cs
private static void ConvertPdfToOds()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSaveOptions object
        var saveOptions = new Aspose.Pdf.ExcelSaveOptions
        {
            // Specify the desired table file format
            Format = Aspose.Pdf.ExcelSaveOptions.ExcelFormat.ODS
        };

        // Save the file in ODS format
        document.Save(dataDir + "PDFToODS_out.ods", saveOptions);
    }
}
```

- PDF a XMLSpreadSheet2003: Reconocer texto en subíndice y superíndice;

- PDF a Excel: Reconocer texto en subíndice y superíndice;

- Eliminar firmas UR al guardar el documento;

- Eliminar la bandera de Sospechosos en MarkInfo al guardar el documento;

- Eliminar información al guardar el documento.

## Novedades en Aspose.PDF 22.3

Esta versión incluye las siguientes actualizaciones:

- Soporte para AFRelationship;

- Validación de encabezado PDF;

- Eliminar el subfiltro adbe.x509.rsa_sha1 al guardar el documento;

- Formatear campo como número y formato de fecha;

- Prohibir el uso de cifrado RC4 en FDF 2.0.

## Novedades en Aspose.PDF 22.2

Desde la versión 22.2 es posible firmar un documento utilizando PdfFileSignature con LTV, y con la capacidad de cambiar el hash de SHA1 a SHA256.

```csharp
private static void SignPdfWithSha256(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var fileSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        fileSign.BindPdf(dataDir + "DigitallySign.pdf");

        var rect = new System.Drawing.Rectangle(300, 100, 1, 1);
        var signature = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password)
        {
            UseLtv = true,
            TimestampSettings = new Aspose.Pdf.TimestampSettings("http://freetsa.org/tsr", string.Empty, Aspose.Pdf.DigestHashAlgorithm.Sha256)
        };

        // Sign PDF file
        fileSign.Sign(1, false, rect, signature);
        // Save PDF document
        fileSign.Save(dataDir + "SignPdfWithSha256_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 22.1

Ahora, Aspose.PDF for .NET admite la carga de documentos de uno de los formatos de documento más populares, el Formato de Documento Portátil (PDF) versión 2.0.

## Novedades en Aspose.PDF 21.11

### Permitir caracteres no latinos en la contraseña

```csharp
private static void EncriptPdfNonlatinPassCharacters()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "input.pdf");
        // Encrypt file using 256-bit encryption
        bool isSuccessful = fileSecurity.EncryptFile("æøå", "æøå", Aspose.Pdf.Facades.DocumentPrivilege.Print,
            Aspose.Pdf.Facades.KeySize.x256, Aspose.Pdf.Facades.Algorithm.AES);
        Console.WriteLine(isSuccessful);
        // Save PDF document
        fileSecurity.Save(dataDir + "PdfNonlatinPassEncrypted_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 21.10

### ¿Cómo detectar texto oculto?

Utilice TextState.Invisible para obtener información sobre la invisibilidad del texto fuera de la configuración del modo de renderizado.

Utilizamos el siguiente código para las pruebas:

```csharp
private static void DisplayTextInvisibility()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithHiddenText.pdf"))
    {
        Console.WriteLine(document.FileName);

        // Use TextFragmentAbsorber with no parameters to get all text
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        absorber.Visit(document.Pages[1]);
        var textFragmentCollection = absorber.TextFragments;

        // Iterate through text fragments to find hidden text
        for (int i = 1; i <= textFragmentCollection.Count; i++)
        {
            var fragment = textFragmentCollection[i];
            Console.WriteLine("Fragment {0} at {1}", i, fragment.Rectangle.ToString());
            Console.WriteLine("Text: {0}", fragment.Text);
            Console.WriteLine("RenderingMode: {0}", fragment.TextState.RenderingMode.ToString());
            Console.WriteLine("Invisibility: {0}", fragment.TextState.Invisible);
            Console.WriteLine("---");
        }
    }
}
```

### ¿Cómo obtener información sobre el número de capas en un documento PDF?

```csharp
private static void GetPdfLayers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithLayers.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;
        // Save each layer to the output path
        foreach (var layer in layers)
        {
            Console.WriteLine("Document {0} contains a layer named: {1} ", document.FileName, layer.Name);
        }
    }
}
```

## Novedades en Aspose.PDF 21.9

Personalizar el color de fondo para la apariencia de la firma y el color de fuente de las etiquetas en el área de firma con Aspose.PDF for .NET.

```csharp
private static void SignPdfWithCustomColorsInAppearance(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "DigitallySign.pdf");
        var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
        // Create PKCS#7 object for sign
        var pkcs = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);

        // Set signature custom appearance
        pkcs.CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance()
        {
            // Set colors
            ForegroundColor = Aspose.Pdf.Color.DarkGreen,
            BackgroundColor = Aspose.Pdf.Color.LightSeaGreen,
        };
        // Sign PDF file
        pdfFileSignature.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "SignPdfWithCustomColorsInAppearance_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 21.8

### ¿Cómo cambiar el color del texto en la firma digital?

En la versión 21.8, la propiedad ForegroundColor permite cambiar el color del texto en la firma digital.

```csharp
private static void SignPdfWithForegroundColorInAppearance(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Instantiate PdfFileSignature object
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "DigitallySign.pdf");
        var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
        // Create PKCS#7 object for sign
        var pkcs = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);

        // Set signature custom appearance
        pkcs.CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance()
        {
            // Set text color
            ForegroundColor = Aspose.Pdf.Color.Green
        };
        // Sign PDF file
        pdfSign.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfSign.Save(dataDir + "SignPdfWithForegroundInAppearance_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 21.7

### Creación de PDF basada en XML y XLS con parámetros

Para agregar parámetros XSL, necesitamos crear nuestra propia [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) y establecerla como propiedad en [XslFoLoadOptions](https://reference.aspose.com/pdf/es/net/aspose.pdf/xslfoloadoptions). El siguiente fragmento muestra cómo utilizar esta clase con los archivos de muestra descritos anteriormente.

```csharp
private static void ConvertXslfoToPdfWithArgumentList()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create convert options
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "XSLFOToPdfInput.xslt");

    // Example of using XsltArgumentList
    options.XsltArgumentList = new XsltArgumentList();
    options.XsltArgumentList.AddParam("isBoldName", "", "yes");

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "XSLFOToPdfInput.xml", options))
    {
        // Save PDF document
        document.Save(dataDir + "XslfoToPdfWithArgumentList_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 21.6

Con Aspose.PDF for .NET puedes ocultar imágenes utilizando ImagePlacementAbsorber del documento:

```csharp
private static void HideImageInPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImagePlacement.pdf"))
    {
        // Create ImagePlacementAbsorber instance
        var absorber = new Aspose.Pdf.ImagePlacementAbsorber();
        // Load the images of the first page
        document.Pages[1].Accept(absorber);

        // Iterate through each image placement on the first page
        foreach (var imagePlacement in absorber.ImagePlacements)
        {
            // Hide image
            imagePlacement.Hide();
        }

        // Save PDF document
        document.Save(dataDir + "HideImageInPdf_out.pdf");
    }
}
```

## Novedades en Aspose.PDF 21.5

### ¿Cómo extraer el nombre completo de la fuente de su descripción/recurso en PDF?

Puedes obtener una fuente completa con el prefijo con la propiedad BaseFont para la clase Font.

```csharp
private static void DisplayFontFullNames()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "BreakfastMenu.pdf"))
    {
        // Get document fonts
        var fonts = document.FontUtilities.GetAllFonts();

        // Iterate through the fonts
        foreach (var font in fonts)
        {
            // Show font names
            Console.WriteLine($"font name : {font.FontName} BaseFont name : {font.BaseFont}");
        }
    }
}
```

## Novedades en Aspose.PDF 21.4

### Agregar API para fusionar imágenes

Aspose.PDF 21.4 te permite combinar imágenes. Sigue el siguiente fragmento de código:

```csharp
private static void MergeAsJpeg()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    List<Stream> inputImagesStreams = new List<Stream>();
    using (FileStream firstImageStream = new FileStream(dataDir + "aspose.jpg", FileMode.Open))
    {
        inputImagesStreams.Add(firstImageStream);
        using (FileStream secondImageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            inputImagesStreams.Add(secondImageStream);

            // Invoke PdfConverter.MergeImages to perform merge
            using (Stream inputStream = Aspose.Pdf.Facades.PdfConverter.MergeImages(inputImagesStreams,
                  Aspose.Pdf.Drawing.ImageFormat.Jpeg, Aspose.Pdf.Facades.ImageMergeMode.Vertical, 1, 1))
            {
                using (FileStream outputStream = new FileStream(dataDir + "Merge_out.jpg", FileMode.Create))
                {
                    byte[] buffer = new byte[32768];
                    int read;
                    while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                    {
                        outputStream.Write(buffer, 0, read);
                    }
                }
            }
        }
    }
}
```

También puedes fusionar tus imágenes en formato Tiff:

```csharp
private static void MergeAsTiff()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    List<Stream> inputImagesStreams = new List<Stream>();
    using (FileStream firstImageStream = new FileStream(dataDir + "aspose.jpg", FileMode.Open))
    {
        inputImagesStreams.Add(firstImageStream);
        using (FileStream secondImageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            inputImagesStreams.Add(secondImageStream);

            // Invoke PdfConverter.MergeImagesAsTiff to perform merge
            using (Stream inputStream = Aspose.Pdf.Facades.PdfConverter.MergeImagesAsTiff(inputImagesStreams))
            {
                using (FileStream outputStream = new FileStream(dataDir + "Merge_out.tiff", FileMode.Create))
                {
                    byte[] buffer = new byte[32768];
                    int read;
                    while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                    {
                        outputStream.Write(buffer, 0, read);
                    }
                }
            }
        }
    }
}
```

## Novedades en Aspose.PDF 21.3

### Exposición pública de la propiedad para detectar la Protección de Información de Azure

Con el siguiente fragmento de código, deberías poder acceder a la carga útil cifrada de tus archivos PDF, protegidos con la Protección de Información de Azure:

```csharp
private static void AzureInformationProtection()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetAlltheAttachments.pdf"))
    {
        if (document.EmbeddedFiles[1].AFRelationship == Aspose.Pdf.AFRelationship.EncryptedPayload)
        {
            if (document.EmbeddedFiles[1].EncryptedPayload != null)
            {
                // document.EmbeddedFiles[1].EncryptedPayload.Type == "EncryptedPayload"
                // document.EmbeddedFiles[1].EncryptedPayload.Subtype == "MicrosoftIRMServices"
                // document.EmbeddedFiles[1].EncryptedPayload.Version == "2"
            }
        }
    }
}
```

## Novedades en Aspose.PDF 21.1

### Agregar soporte para recuperar el color de fondo de TextFragment

En esta versión de Aspose.PDF, se hizo disponible la función para recuperar el color de fondo. Debes especificar searchOptions.SearchForTextRelatedGraphics = true; en las opciones del objeto TextFragmentAbsorber.

Por favor, considera el siguiente código:

```csharp
private static void DisplayPdfTextBackgroundColor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfWithTextBackgroundColor.pdf"))
    {
        // Use TextFragmentAbsorber with no parameters to get all text
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();

        var searchOptions = new Aspose.Pdf.Text.TextSearchOptions(false);
        // Setting this option into the 'true' is necessary 
        searchOptions.SearchForTextRelatedGraphics = true;
        textFragmentAbsorber.TextSearchOptions = searchOptions;

        // Accept the absorber for all the pages
        document.Pages.Accept(textFragmentAbsorber);
        
        // Loop through the fragments
        foreach (var textFragment in textFragmentAbsorber.TextFragments)
        {
            Console.WriteLine("Text: '{0}'", textFragment.Text);
            Console.WriteLine("BackgroundColor: '{0}'", textFragment.TextState.BackgroundColor);
            Console.WriteLine("ForegroundColor: '{0}'", textFragment.TextState.ForegroundColor);
            Console.WriteLine("Segment BackgroundColor: '{0}'", textFragment.Segments[1].TextState.BackgroundColor);
        }
    }
}
```

### Después de la conversión a HTML, la fuente está completamente incrustada en la salida

Además, en Aspose.PDF 21.1, después de convertir PDF a HTML, se hicieron disponibles fuentes incrustadas en un documento HTML de salida. Esto es posible con la nueva opción booleana de guardado HtmlSaveParameter.SaveFullFont.

Aquí está el fragmento de código:

```csharp
private static void PdfToHtmlWithFullFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToHTML.pdf"))
    {
        // Instantiate HTML SaveOptions object
        var options = new Aspose.Pdf.HtmlSaveOptions
        {
            RasterImagesSavingMode = Aspose.Pdf.HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground,
            PartsEmbeddingMode = Aspose.Pdf.HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml,
            LettersPositioningMethod = Aspose.Pdf.HtmlSaveOptions.LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss,
            FontSavingMode = Aspose.Pdf.HtmlSaveOptions.FontSavingModes.AlwaysSaveAsTTF,
            SaveTransparentTexts = true,
            // New option
            SaveFullFont = true
        };
        // Save HTML document
        document.Save(dataDir + "PdfToHtmlWithFullFont_out.html", options);
    }
}
```