---
title: Convertir PDF a Microsoft PowerPoint 
linktitle: Convertir PDF a PowerPoint
type: docs
weight: 30
url: /java/convert-pdf-to-powerpoint/
lastmod: "2021-11-19"
description: Aspose.PDF le permite convertir PDF a formato PowerPoint usando Java. Una forma hay una posibilidad de convertir PDF a PPTX con diapositivas como imágenes.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF para Java** le permite seguir el progreso de la conversión de PDF a PPTX. Tenemos una API llamada Aspose.Slides que ofrece la función de crear y manipular presentaciones PPT/PPTX. Esta API también proporciona la función de convertir archivos PPT/PPTX al formato PDF. En Aspose.PDF para Java, hemos introducido una función para transformar documentos PDF en formato PPTX. Durante esta conversión, las páginas individuales del archivo PDF se convierten en diapositivas separadas en el archivo PPTX.

Durante la conversión de PDF a PPTX, el texto se representa como Texto donde puede seleccionarlo/actualizarlo, en lugar de ser representado como una imagen.
 Por favor, tenga en cuenta que para convertir archivos PDF a formato PPTX, Aspose.PDF proporciona una clase llamada PptxSaveOptions. Un objeto de la clase [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) se pasa como un segundo argumento al método [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

Revise el siguiente fragmento de código para resolver sus tareas con la conversión de PDF a formato PowerPoint:

```java
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_Simple();
        convertPDFtoPPTX_SlideAsImages();
        convertPDFtoPPTX_ProgresDetails();
    }

    public static void convertPDFtoPPTX_Simple() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // Cargar documento PDF
        Document document = new Document(documentFileName);

        // Instanciar instancia de PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // Guardar la salida en formato PPTX
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```

## Convertir PDF a PPTX con Diapositivas como Imágenes

En caso de que necesites convertir un PDF buscable a PPTX como imágenes en lugar de texto seleccionable, Aspose.PDF proporciona tal característica a través de la clase [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions). Para lograr esto, establece la propiedad SlidesAsImages de la clase [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) a 'true' como se muestra en el siguiente ejemplo de código.

El siguiente fragmento de código muestra el proceso para convertir archivos PDF en formato PPTX con Diapositivas como Imágenes.

```java
public static void convertPDFtoPPTX_SlideAsImages() {
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
    String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

    // Cargar documento PDF
    Document document = new Document(documentFileName);
    // Instanciar la instancia de PptxSaveOptions
    PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();
    // Guardar la salida en formato PPTX
    pptxSaveOptions.setSlidesAsImages(true);

    document.save(pptxDocumentFileName, pptxSaveOptions);
    document.close();
}
```


## Mostrar Progreso En Consola con Aspose.PDF para Java se ve así:

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.PptxSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Convertir PDF a PPTX.
 */
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_ProgressDetails();
    }

    public static void convertPDFtoPPTX_ProgressDetails() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // Cargar documento PDF
        Document document = new Document(documentFileName);

        // Instanciar PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // Especificar Manejador de Progreso Personalizado
        pptx_save.setCustomProgressHandler(new ShowProgressOnConsole());

        // Guardar la salida en formato PPTX
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```


## Detalle del Progreso de Conversión a PPTX

Aspose.PDF para Java te permite rastrear el progreso de la conversión de PDF a PPTX. La clase [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) proporciona la propiedad [CustomProgressHandler](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlSaveOptions) que se puede especificar a un método personalizado para rastrear el progreso de la conversión como se muestra en el siguiente ejemplo de código.

```java
package com.aspose.pdf.examples;

import java.time.LocalDateTime;

import com.aspose.pdf.ProgressEventType;
import com.aspose.pdf.UnifiedSaveOptions.ConversionProgressEventHandler;
import com.aspose.pdf.UnifiedSaveOptions.ProgressEventHandlerInfo;

class ShowProgressOnConsole extends ConversionProgressEventHandler{

    @Override
    public void invoke(ProgressEventHandlerInfo eventInfo) {        
        switch (eventInfo.EventType) {
            case ProgressEventType.TotalProgress:
                System.out.println(
                        String.format("%s  - Progreso de conversión : %d %%.", LocalDateTime.now().toString(), eventInfo.Value));
                break;
            case ProgressEventType.ResultPageCreated:
                System.out.println(String.format("%s  - Página de resultado %s de %d layout creada.", LocalDateTime.now().toString(),
                        eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.ResultPageSaved:
                System.out.println(String.format("%s  - Página de resultado %d de %d exportada.", LocalDateTime.now(), eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.SourcePageAnalysed:
                System.out.println(String.format("%s  - Página fuente %d de %d analizada.", LocalDateTime.now(),  eventInfo.Value, eventInfo.MaxValue));
                break;
            default:
                break;
        }
    }
```


{{% alert color="success" %}}
**Intenta convertir PDF a PowerPoint en línea**

Aspose.PDF para Java te presenta una aplicación gratuita en línea ["PDF a PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF de PDF a PPTX con Aplicación Gratis](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}