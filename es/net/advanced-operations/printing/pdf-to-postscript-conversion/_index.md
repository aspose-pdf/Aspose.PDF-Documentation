---
title: Conversión de PDF a PostScript
linktitle: Conversión de PDF a PostScript
type: docs
weight: 30
url: /es/net/pdf-to-postscript-conversion/
keywords: "pdf to postscript c#"
description: Tenemos una solución para la conversión de PDF a PostScript. Utiliza para esta tarea la impresión y la clase PdfViewer.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Conversión de PDF a PostScript",
    "alternativeHeadline": "Convertir PDF a PostScript",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, pdf to postscript",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación Aspose.PDF",
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
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/pdf-to-postscript-conversion/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-to-postscript-conversion/"
    },
    "dateModified": "2022-02-04",
    "description": "Tenemos una solución para la conversión de PDF a PostScript. Utiliza para esta tarea la impresión y la clase PdfViewer."
}
</script>
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## **PDF a Postscript en C#**

La clase PdfViewer proporciona la capacidad de imprimir documentos PDF y con la ayuda de esta clase, también podemos convertir archivos PDF a formato PostScript. Para convertir un archivo PDF en PostScript, primero instale cualquier impresora PS y simplemente imprima el archivo con la ayuda de PdfViewer. Puede seguir las instrucciones especificadas por la Universidad de Hawaii sobre cómo instalar una impresora PS. El siguiente fragmento de código le muestra cómo imprimir y convertir un PDF a formato PostScript.

```csharp
public static void PrintToPostscriptFile()
{
    // La ruta al directorio de documentos.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    Aspose.Pdf.Facades.PdfViewer viewer = new Aspose.Pdf.Facades.PdfViewer();
    viewer.BindPdf(_dataDir + "input.pdf");
    // Configurar PrinterSettings y PageSettings
    System.Drawing.Printing.PrinterSettings printerSettings = new System.Drawing.Printing.PrinterSettings();
    printerSettings.Copies = 1;
    // Configurar la impresora PS, se puede encontrar este controlador en la lista de controladores de impresora preinstalados en Windows
    printerSettings.PrinterName = "HP LaserJet 2300 Series PS";
    // Configurar el nombre del archivo de salida y el atributo PrintToFile
    printerSettings.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
    printerSettings.PrintToFile = true;
    // Desactivar el diálogo de impresión de página
    viewer.PrintPageDialog = false;
    // Pasar el objeto de configuración de impresora al método
    viewer.PrintDocumentWithSettings(printerSettings);
    viewer.Close();
}
```
## Verificación del Estado de un Trabajo de Impresión

Un archivo PDF puede ser impreso en una impresora física así como en el Microsoft XPS Document Writer, sin mostrar un diálogo de impresión, utilizando la clase PdfViewer. Cuando se imprimen archivos PDF grandes, el proceso puede tomar mucho tiempo, por lo que el usuario podría no estar seguro de si el proceso de impresión se completó o encontró un problema. Para determinar el estado de un trabajo de impresión, utilice la propiedad PrintStatus. El siguiente fragmento de código muestra cómo imprimir el archivo PDF en un archivo XPS y obtener el estado de la impresión.

```csharp
public static void VerificarEstadoDelTrabajoDeImpresion()
{
    // Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
    // La ruta al directorio de documentos.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Instanciar el objeto PdfViewer
    PdfViewer viewer = new PdfViewer();

    // Vincular el archivo PDF fuente
    viewer.BindPdf(_dataDir + "input.pdf");
    viewer.AutoResize = true;

    // Ocultar el diálogo de impresión
    viewer.PrintPageDialog = false;

    // Crear objeto de configuración de impresora
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // Especificar el nombre de la impresora
    ps.PrinterName = "Microsoft XPS Document Writer";

    // Nombre resultante de la impresión
    ps.PrintFileName = "ResultantPrintout.xps";

    // Imprimir la salida a archivo
    ps.PrintToFile = true;
    ps.FromPage = 1;
    ps.ToPage = 2;
    ps.PrintRange = System.Drawing.Printing.PrintRange.SomePages;

    // Especificar el tamaño de página de la impresión
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
    ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Imprimir el documento con los ajustes especificados arriba
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Verificar el estado de la impresión
    if (viewer.PrintStatus != null)
    {
        // Se lanzó una excepción
        if (viewer.PrintStatus is Exception ex)
        {
            // Obtener el mensaje de la excepción
            Console.WriteLine(ex.Message);
        }
    }
    else
    {
        // No se encontraron errores. El trabajo de impresión se ha completado con éxito
        Console.WriteLine("impresión completada sin ningún problema..");
    }
}
```
## Obtener/Establecer el nombre del propietario del trabajo de impresión

Recientemente recibimos un requisito para obtener/establecer el nombre del propietario del trabajo de impresión (el usuario actual que presionó el botón de impresión en la página web). Esta información es requerida al imprimir el archivo PDF. Para lograr este requisito, puedes usar la propiedad llamada PrinterJobName:

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
// Vincular archivo PDF fuente
viewer.BindPdf(dataDir + "input.pdf");
// Especificar el nombre del trabajo de impresión
viewer.PrinterJobName = GetCurrentUserCredentials();
```

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static string GetCurrentUserCredentials()
{
    // La implementación depende del tipo de aplicación en ejecución (ASP.NET, Windows forms, etc.)
    string userCredentials = string.Empty;
    return userCredentials;
}
```
## Uso de la Suplantación

Otro enfoque para obtener el nombre del propietario del trabajo de impresión es usar la suplantación (ejecutando rutinas de impresión en el contexto de otro usuario) o el usuario puede cambiar el nombre del propietario directamente utilizando la rutina SetJob.

Tenga en cuenta que no es posible establecer el valor del propietario utilizando la API de impresión de Aspose.PDF por consideraciones de seguridad. La propiedad PrinterJobName puede usarse para establecer el valor de la columna de nombre del documento en la aplicación de impresión del spooler. El fragmento de código compartido anteriormente solo muestra cómo el usuario puede unir el nombre de usuario en la columna de nombre del documento (por ejemplo, utilizando la sintaxis UserName\documentName). Pero la configuración de las columnas del propietario se puede implementar de las siguientes maneras directamente por el usuario:

1) Suplantación. Como el valor de la columna del propietario contiene el valor del usuario que ejecuta el código de impresión, hay una forma de invocar la API de impresión de Aspose.PDF dentro del contexto de otro usuario. Por ejemplo, eche un vistazo a la solución descrita aquí. Usando esta clase el usuario puede alcanzar un objetivo:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
viewer.BindPdf( dataDir + "input.pdf");
viewer.PrintPageDialog = false;
// No produce el diálogo de número de página al imprimir
using (new Impersonator("OwnerUserName", "SomeDomain", "OwnerUserNamePassword"))
{
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    ps.PrinterName = "Microsoft XPS Document Writer";
    viewer.PrintDocumentWithSettings(ps); // OwnerUserName es un valor de la columna Owner en la app spooler
    viewer.Close();
}
```
2) Uso de la API Spooler y la rutina SetJob

El siguiente fragmento de código muestra cómo imprimir algunas páginas de un archivo PDF en modo Simplex y algunas páginas en modo Duplex.

```csharp
struct PrintingJobSettings
{
    public int ToPage { get; set; }
    public int FromPage { get; set; }
    public string OutputFile { get; set; }
    public System.Drawing.Printing.Duplex Mode { get; set; }
}
```

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

int printingJobIndex = 0;
string inPdf = dataDir + "input.pdf";
string output = dataDir;
IList<PrintingJobSettings> printingJobs = new List<PrintingJobSettings>();

PrintingJobSettings printingJob1 = new PrintingJobSettings();
printingJob1.FromPage = 1;
printingJob1.ToPage = 3;
printingJob1.OutputFile = output + "35925_1_3.xps";
printingJob1.Mode = Duplex.Default;

printingJobs.Add(printingJob1);

PrintingJobSettings printingJob2 = new PrintingJobSettings();
printingJob2.FromPage = 4;
printingJob2.ToPage = 6;
printingJob2.OutputFile = output + "35925_4_6.xps";
printingJob2.Mode = Duplex.Simplex;

printingJobs.Add(printingJob2);

PrintingJobSettings printingJob3 = new PrintingJobSettings();
printingJob3.FromPage = 7;
printingJob3.ToPage = 7;
printingJob3.OutputFile = output + "35925_7.xps";
printingJob3.Mode = Duplex.Default;

printingJobs.Add(printingJob3);

PdfViewer viewer = new PdfViewer();

viewer.BindPdf(inPdf);
viewer.AutoResize = true; 
viewer.AutoRotate = true;
viewer.PrintPageDialog = false;

PrinterSettings ps = new PrinterSettings();
PageSettings pgs = new PageSettings();

ps.PrinterName = "Microsoft XPS Document Writer";
ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
ps.PrintToFile = true;
ps.FromPage = printingJobs[printingJobIndex].FromPage;
ps.ToPage = printingJobs[printingJobIndex].ToPage;
ps.Duplex = printingJobs[printingJobIndex].Mode;
ps.PrintRange = PrintRange.SomePages;

pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);
viewer.EndPrint += (sender, args) =>
{
    if (++printingJobIndex < printingJobs.Count)
    {
        ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
        ps.FromPage = printingJobs[printingJobIndex].FromPage;
        ps.ToPage = printingJobs[printingJobIndex].ToPage;
        ps.Duplex = printingJobs[printingJobIndex].Mode;
        viewer.PrintDocumentWithSettings(pgs, ps);
    }
};

viewer.PrintDocumentWithSettings(pgs, ps);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
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
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
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
    "applicationCategory": "Biblioteca de Manipulación de PDF para .NET",
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
```

