---
title: Agregar Sello de Texto e Imagen
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/add-text-and-image-stamp/
description: Esta sección explica cómo agregar un Sello de Texto e Imagen con Aspose.PDF Facades utilizando la clase PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text and Image Stamp",
    "alternativeHeadline": "Add Custom Text and Image Stamps in PDFs",
    "abstract": "Las funciones de Agregar Sello de Texto e Imagen en Aspose.PDF for .NET permiten a los usuarios aplicar sin problemas sellos de texto e imagen personalizados en todas o en páginas específicas de documentos PDF. Esta funcionalidad mejora la personalización del documento, permitiendo un control detallado sobre los atributos del sello, como posición, rotación y calidad, mejorando en última instancia la presentación y la marca de sus archivos PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1435",
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
    "url": "/net/add-text-and-image-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-and-image-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulte la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Agregar Sello de Texto en Todas las Páginas de un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp) permite agregar un sello de texto en todas las páginas de un archivo PDF. Para agregar un sello de texto, primero necesita crear objetos de las clases [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp) y [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). También necesita crear el sello de texto utilizando el método [BindLogo](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/stamp/methods/bindlogo) de la clase [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). Puede establecer otros atributos como origen, rotación, fondo, etc. utilizando el objeto [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp) también. Luego puede agregar el sello en el archivo PDF utilizando el método [AddStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp). Finalmente, guarde el archivo PDF de salida utilizando el método [Close](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp). El siguiente fragmento de código le muestra cómo agregar un sello de texto en todas las páginas de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));

        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnAllPages_out.pdf");
    }
}
```

## Agregar Sello de Texto en Páginas Particulares de un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp) permite agregar un sello de texto en páginas particulares de un archivo PDF. Para agregar un sello de texto, primero necesita crear objetos de las clases [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp) y [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). También necesita crear el sello de texto utilizando el método [BindLogo](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/stamp/methods/bindlogo) de la clase [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). Puede establecer otros atributos como origen, rotación, fondo, etc. utilizando el objeto [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp) también. Como desea agregar un sello de texto en páginas particulares del archivo PDF, también necesita establecer la propiedad [Pages](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/stamp/properties/pages) de la clase [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). Esta propiedad requiere un arreglo de enteros que contenga los números de las páginas en las que desea agregar el sello. Luego puede agregar el sello en el archivo PDF utilizando el método [AddStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp). Finalmente, guarde el archivo PDF de salida utilizando el método [Close](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp). El siguiente fragmento de código le muestra cómo agregar un sello de texto en páginas particulares de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));
        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnParticularPages_out.pdf");
    }
}
```

## Agregar Sello de Imagen en Todas las Páginas de un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp) permite agregar un sello de imagen en todas las páginas de un archivo PDF. Para agregar un sello de imagen, primero necesita crear objetos de las clases [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp) y [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). También necesita crear el sello de imagen utilizando el método [BindImage](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/stamp/methods/bindimage/index) de la clase [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). Puede establecer otros atributos como origen, rotación, fondo, etc. utilizando el objeto [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp) también. Luego puede agregar el sello en el archivo PDF utilizando el método [AddStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/page/methods/addstamp) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp). Finalmente, guarde el archivo PDF de salida utilizando el método [Close](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp). El siguiente fragmento de código le muestra cómo agregar un sello de imagen en todas las páginas de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnAllPages_out.pdf");
    }
}
```

### Controlar la calidad de la imagen al agregarla como sello

Al agregar una imagen como objeto de sello, también puede controlar la calidad de la imagen. Para cumplir con este requisito, se ha agregado la propiedad Quality para la clase [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). Indica la calidad de la imagen en porcentajes (los valores válidos son 0..100).

## Agregar Sello de Imagen en Páginas Particulares de un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp) permite agregar un sello de imagen en páginas particulares de un archivo PDF. Para agregar un sello de imagen, primero necesita crear objetos de las clases [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp) y [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). También necesita crear el sello de imagen utilizando el método [BindImage](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/stamp/methods/bindimage/index) de la clase [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). Puede establecer otros atributos como origen, rotación, fondo, etc. utilizando el objeto [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp) también. Como desea agregar un sello de imagen en páginas particulares del archivo PDF, también necesita establecer la propiedad [Pages](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/stamp/properties/pages) de la clase [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). Esta propiedad requiere un arreglo de enteros que contenga los números de las páginas en las que desea agregar el sello. Luego puede agregar el sello en el archivo PDF utilizando el método [AddStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/page/methods/addstamp) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp). Finalmente, guarde el archivo PDF de salida utilizando el método [Close](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp). El siguiente fragmento de código le muestra cómo agregar un sello de imagen en páginas particulares de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnParticularPages_out.pdf");
    }
}
```