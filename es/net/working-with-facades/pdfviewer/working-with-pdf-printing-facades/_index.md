---
title: Trabajando con impresión de PDF - Fachadas
type: docs
weight: 10
url: /es/net/working-with-pdf-printing-facades/
description: Esta sección explica cómo imprimir archivos PDF con Aspose.PDF Facades usando la clase PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Imprimir archivo PDF en la impresora predeterminada usando configuraciones de impresora y página

Primero, el documento se convierte en imagen y luego se imprime en la impresora. Creamos una instancia de la clase [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) que le permite imprimir un archivo PDF en la impresora predeterminada, usando el método BindPdf para el documento y realizar ciertas configuraciones. En nuestro ejemplo, estamos usando formato A4, orientación vertical. En las printerSettings, primero indicamos el nombre de la impresora en la que estamos imprimiendo. De lo contrario, imprimirá en la impresora predeterminada. A continuación, anotamos el número de copias que necesitamos.

```csharp
 public static void PrintingPDFFile()
        {
            // Crear objeto PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Abrir archivo PDF de entrada
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Establecer atributos para la impresión
            viewer.AutoResize = true;         // Imprimir el archivo con tamaño ajustado
            viewer.AutoRotate = true;         // Imprimir el archivo con rotación ajustada
            viewer.PrintPageDialog = false;   // No mostrar el diálogo de número de página al imprimir

            // Crear objetos para configuraciones de impresora y de página y PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
            System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

            // Establecer nombre de la impresora
            ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

            // Establecer tamaño de página (si es necesario)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Establecer márgenes de página (si es necesario)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimir documento usando configuraciones de impresora y de página
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Cerrar el archivo PDF después de imprimir
            viewer.Close();
        }
```

En orden de mostrar un diálogo de impresión, intenta usar el siguiente fragmento de código:

```csharp
        public static void PrintingPDFDisplayPrintDialog()
        {
            // Crear objeto PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Abrir archivo PDF de entrada
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Establecer atributos para imprimir
            viewer.AutoResize = true;         // Imprimir el archivo con tamaño ajustado
            viewer.AutoRotate = true;         // Imprimir el archivo con rotación ajustada

            // Crear objetos para la impresora y configuraciones de página y PrintDocument

            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings
            {

                // Establecer PageSize (si es necesario)
                PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169),

                // Establecer PageMargins (si es necesario)
                Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0)
            };

            System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
            if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                // El código de impresión del documento va aquí
                // Imprimir documento usando la impresora y configuraciones de página
                System.Drawing.Printing.PrinterSettings ps = printDialog.PrinterSettings;
                viewer.PrintDocumentWithSettings(pgs, ps);
            }

            // Cerrar el archivo PDF después de imprimir
            viewer.Close();
        }
```

## Imprimir PDF en Impresora Virtual

Hay impresoras que imprimen en un archivo. Establecemos el nombre de la impresora virtual y, por analogía con el ejemplo anterior, realizamos la configuración.

```csharp
public static void PrintingPDFToSoftPrinter()
        {
            // Crear objeto PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Abrir archivo PDF de entrada
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Establecer atributos para la impresión
            viewer.AutoResize = true;         // Imprimir el archivo con tamaño ajustado
            viewer.AutoRotate = true;         // Imprimir el archivo con rotación ajustada
            viewer.PrintPageDialog = false;   // No producir el diálogo de número de página al imprimir

            viewer.PrintAsImage = false;

            // Crear objetos para configuración de impresora y página y PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Establecer nombre de la impresora
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // O establecer la impresora PDF
            //ps.PrinterName = "Adobe PDF";

            // Establecer tamaño de página (si es necesario)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Establecer márgenes de página (si es necesario)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimir documento usando la configuración de impresora y página
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Cerrar el archivo PDF después de imprimir
            viewer.Close();
        }
```

## Ocultando el Diálogo de Impresión

Aspose.PDF para .NET te permite ocultar el diálogo de impresión. Para esto, utiliza el método [PrintPageDialog](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/properties/printpagedialog).

El siguiente fragmento de código te muestra cómo ocultar el diálogo de impresión.

```csharp
public static void PrintingPDFHidePrintDialog()
        {
            // Crear objeto PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Abrir archivo PDF de entrada
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Establecer atributos para la impresión
            viewer.AutoResize = true;         // Imprimir el archivo con tamaño ajustado
            viewer.AutoRotate = true;         // Imprimir el archivo con rotación ajustada

            viewer.PrintPageDialog = false;   // No producir el diálogo de número de página al imprimir

            // Crear objetos para la impresora y la configuración de página y PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Establecer nombre de impresora XPS/PDF
            ps.PrinterName = "OneNote for Windows 10";

            // Establecer PageSize (si es necesario)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Establecer PageMargins (si es necesario)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimir documento usando la configuración de impresora y página
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Cerrar el archivo PDF después de imprimir
            viewer.Close();
        }
```

## Imprimir PDF en Color a Archivo XPS en Escala de Grises

Un documento PDF en color puede ser impreso en una impresora XPS como escala de grises, usando [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). Para lograrlo, necesitas usar la propiedad PdfViewer.PrintAsGrayscale y configurarla en *true*. El siguiente fragmento de código demuestra la implementación de la propiedad PdfViewer.PrintAsGrayscale.

```csharp
public static void PrintingPDFasGrayscale()
        {
            // Crear objeto PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Abrir archivo PDF de entrada
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Establecer atributos para la impresión
            viewer.AutoResize = true;         // Imprimir el archivo con tamaño ajustado
            viewer.AutoRotate = true;         // Imprimir el archivo con rotación ajustada

            viewer.PrintPageDialog = false;   // No mostrar el diálogo de número de página al imprimir
            viewer.PrintAsGrayscale = false;

            // Crear objetos para la impresora y configuración de página y PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Establecer nombre de impresora XPS/PDF
            ps.PrinterName = "OneNote for Windows 10";

            // Establecer tamaño de página (si es necesario)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Establecer márgenes de página (si es necesario)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimir documento usando la impresora y configuración de página
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Cerrar el archivo PDF después de imprimir
            viewer.Close();
        }
```

## Conversión de PDF a PostScript

La clase [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) proporciona la capacidad de imprimir documentos PDF y, con la ayuda de esta clase, también podemos convertir archivos PDF al formato PostScript. Para convertir un archivo PDF a PostScript, primero instale cualquier impresora PS y simplemente imprima en un archivo con la ayuda de PdfViewer.

El siguiente fragmento de código le muestra cómo imprimir y convertir un PDF al formato PostScript.

```csharp
public static void PrintingPDFToPostScript()
        {
            // Crear objeto PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Abrir archivo PDF de entrada
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Establecer atributos para la impresión
            viewer.AutoResize = true;         // Imprimir el archivo con tamaño ajustado
            viewer.AutoRotate = true;         // Imprimir el archivo con rotación ajustada
            viewer.PrintPageDialog = false;   // No producir el diálogo de número de página al imprimir

            viewer.PrintAsImage = false;

            // Crear objetos para la configuración de la impresora y página y PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Establecer el nombre de la impresora XPS/PDF
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Establecer el nombre del archivo de salida y el atributo PrintToFile
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // Establecer el tamaño de la página (si es necesario)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Establecer los márgenes de la página (si es necesario)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimir documento usando la configuración de impresora y página
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Cerrar el archivo PDF después de imprimir
            viewer.Close();
        }
```

## Comprobando el Estado del Trabajo de Impresión

Un archivo PDF puede ser impreso en una impresora física así como en el Microsoft XPS Document Writer, sin mostrar un cuadro de diálogo de impresión, usando la clase [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). Al imprimir archivos PDF grandes, el proceso puede tardar mucho tiempo, por lo que el usuario podría no estar seguro de si el proceso de impresión se completó o encontró un problema. Para determinar el estado de un trabajo de impresión, use la propiedad PrintStatus. El siguiente fragmento de código le muestra cómo imprimir el archivo PDF en un archivo XPS y obtener el estado de la impresión.

```csharp
public static void CheckingPrintJobStatus()
        {
            // Crear objeto PdfViewer
            PdfViewer viewer = new PdfViewer();

            // Abrir archivo PDF de entrada
            viewer.BindPdf(_dataDir + "sample1.pdf");

            // Establecer atributos para la impresión
            viewer.AutoResize = true;         // Imprimir el archivo con tamaño ajustado
            viewer.AutoRotate = true;         // Imprimir el archivo con rotación ajustada
            viewer.PrintPageDialog = false;   // No producir el cuadro de diálogo de número de página al imprimir

            viewer.PrintAsImage = false;

            // Crear objetos para configuraciones de impresora y de página y PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Establecer nombre de la impresora XPS/PDF
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Establecer nombre del archivo de salida y atributo PrintToFile
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // Establecer tamaño de página (si es necesario)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Establecer márgenes de página (si es necesario)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Imprimir documento usando configuraciones de impresora y de página
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Comprobar el estado de la impresión
            if (viewer.PrintStatus != null && viewer.PrintStatus is Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            else
            {
                // No se encontraron errores. El trabajo de impresión se ha completado exitosamente
                Console.WriteLine("Impresión completada sin ningún problema..");
            }

            // Cerrar el archivo PDF después de la impresión
            viewer.Close();
        }

        struct PrintingJobSettings
        {
            public int ToPage { get; set; }
            public int FromPage { get; set; }
            public string OutputFile { get; set; }
            public System.Drawing.Printing.Duplex Mode { get; set; }
        }
```

## Imprimiendo páginas en modo Simplex y Duplex

En un trabajo de impresión específico, las páginas de un documento PDF pueden imprimirse en modo Duplex o en modo Simplex, pero no se pueden imprimir algunas páginas como simplex y otras como duplex dentro de un solo trabajo de impresión. Sin embargo, para cumplir con el requisito, se pueden utilizar diferentes rangos de páginas y el objeto PrintingJobSettings. El siguiente fragmento de código muestra cómo imprimir algunas páginas de un archivo PDF en modo Simplex y algunas páginas en modo Duplex.

```csharp
 public static void PrintingPagesInSimplexAndDuplexMode()
        {
            int printingJobIndex = 0;
            string inPdf = _dataDir + "sample-8page.pdf";
            string output = _dataDir;
            IList<PrintingJobSettings> printingJobs = new List<PrintingJobSettings>();

            PrintingJobSettings printingJob1 = new PrintingJobSettings
            {
                FromPage = 1,
                ToPage = 3,
                OutputFile = output + "sample_1_3.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob1);

            PrintingJobSettings printingJob2 = new PrintingJobSettings
            {
                FromPage = 4,
                ToPage = 6,
                OutputFile = output + "sample_4_6.xps",
                Mode = Duplex.Simplex
            };

            printingJobs.Add(printingJob2);

            PrintingJobSettings printingJob3 = new PrintingJobSettings
            {
                FromPage = 7,
                ToPage = 7,
                OutputFile = output + "sample_7.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob3);

            PdfViewer viewer = new PdfViewer();

            viewer.BindPdf(inPdf);
            viewer.AutoResize = true;
            viewer.AutoRotate = true;
            viewer.PrintPageDialog = false;

            PrinterSettings ps = new PrinterSettings();
            PageSettings pgs = new PageSettings();

            ps.PrinterName = "Microsoft XPS Document Writer";
            ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
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
                    ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
                    ps.FromPage = printingJobs[printingJobIndex].FromPage;
                    ps.ToPage = printingJobs[printingJobIndex].ToPage;
                    ps.Duplex = printingJobs[printingJobIndex].Mode;
                    viewer.PrintDocumentWithSettings(pgs, ps);
                }
            };

            viewer.PrintDocumentWithSettings(pgs, ps);
        }
```