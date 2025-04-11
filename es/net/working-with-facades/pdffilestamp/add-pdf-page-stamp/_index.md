---
title: Agregar Sello de Página PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/add-pdf-page-stamp/
description: Descubre cómo agregar sellos a las páginas PDF en .NET, incluyendo texto e imágenes, para marcas de agua o branding utilizando Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Page Stamp",
    "alternativeHeadline": "Enhance PDFs with Custom Stamps and Page Numbers",
    "abstract": "Presentamos la función de Sello de Página PDF que permite a los usuarios agregar sellos personalizados en todas o en páginas específicas de un documento PDF utilizando la clase PdfFileStamp. Esta funcionalidad mejora la personalización del documento al habilitar varios atributos como rotación, fondo y estilos de numeración personalizados para los sellos de página, haciendo que tus archivos PDF sean no solo únicos, sino también profesionalmente pulidos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1309",
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
    "url": "/net/add-pdf-page-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pdf-page-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Agregar Sello de Página PDF en Todas las Páginas de un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp) te permite agregar un sello de página PDF en todas las páginas de un archivo PDF. Para agregar un sello de página PDF, primero necesitas crear objetos de las clases [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp) y [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). También necesitas crear el sello de página PDF utilizando el método [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp) de la clase [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). Puedes establecer otros atributos como origen, rotación, fondo, etc. utilizando el objeto [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp) también. Luego puedes agregar el sello en el archivo PDF utilizando el método [AddStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp). Finalmente, guarda el archivo PDF de salida utilizando el método [Close](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp). El siguiente fragmento de código te muestra cómo agregar un sello de página PDF en todas las páginas de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "AddPageStampOnAllPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnAllPages_out.pdf");
    }
}
```

## Agregar Sello de Página PDF en Páginas Particulares de un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp) te permite agregar un sello de página PDF en páginas particulares de un archivo PDF. Para agregar un sello de página PDF, primero necesitas crear objetos de las clases [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp) y [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). También necesitas crear el sello de página PDF utilizando el método [BindPdf](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.facade/bindpdf/methods/3) de la clase [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). Puedes establecer otros atributos como origen, rotación, fondo, etc. utilizando el objeto [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp) también. Como deseas agregar un sello de página PDF en páginas particulares del archivo PDF, también necesitas establecer la propiedad [Pages](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/stamp/properties/pages) de la clase [Stamp](https://reference.aspose.com/pdf/es/net/aspose.pdf/stamp). Esta propiedad requiere un arreglo de enteros que contenga los números de las páginas en las que deseas agregar el sello. Luego puedes agregar el sello en el archivo PDF utilizando el método [AddStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp). Finalmente, guarda el archivo PDF de salida utilizando el método [Close](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp). El siguiente fragmento de código te muestra cómo agregar un sello de página PDF en páginas particulares de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnCertainPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "PageStampOnCertainPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;
        stamp.Pages = new[] { 1, 3 };  // Apply stamp to specific pages (1 and 3)

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnCertainPages_out.pdf");
    }
}
```

## Agregar Número de Página en un Archivo PDF

La clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp) te permite agregar números de página en un archivo PDF. Para agregar números de página, primero necesitas crear un objeto de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp). Si deseas mostrar el número de página como “Página X de N” donde X es el número de la página actual y N es el número total de páginas en el archivo PDF, entonces primero necesitas obtener el conteo de páginas utilizando la propiedad [NumberOfpages](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) de la clase [PdfFileInfo](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileinfo). Para obtener el número de la página actual, puedes usar el signo **#** en tu texto donde desees. Puedes formatear el texto del número de página utilizando la clase [FormattedText](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formattedtext). Si deseas comenzar la numeración de páginas desde un número específico, entonces puedes establecer la propiedad [StartingNumber](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber). Una vez que estés listo para agregar el número de página en el archivo, necesitas llamar al método [AddPageNumber](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp). Finalmente, guarda el archivo PDF de salida utilizando el método [Close](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/facade/methods/close) de la clase [PdfFileStamp](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffilestamp). El siguiente fragmento de código te muestra cómo agregar un número de página en un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;
        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```

### Estilo de Numeración Personalizado

La clase PdfFileStamp ofrece la función de agregar información del Número de Página como objeto de sello dentro del documento PDF. Antes de esta versión, la clase solo admitía el estilo de numeración de páginas 1,2,3,4. Sin embargo, ha habido una solicitud de algunos clientes para utilizar un estilo de numeración personalizado al colocar el sello de número de página dentro del documento PDF. Para cumplir con este requisito, se ha introducido la propiedad [NumberingStyle](https://reference.aspose.com/pdf/es/net/aspose.pdf/numberingstyle), que acepta los valores de la enumeración [NumberingStyle](https://reference.aspose.com/pdf/es/net/aspose.pdf/numberingstyle). A continuación se especifican los valores ofrecidos en esta enumeración.

- LetrasMinúsculas.
- LetrasMayúsculas.
- NúmerosÁrabes.
- NúmerosRomanosMinúsculas.
- NúmerosRomanosMayúsculas.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCustomPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Specify numbering style as Numerals Roman UpperCase
        fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;

        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddCustomPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```