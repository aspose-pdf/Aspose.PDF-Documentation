---
title: Convertir PDF a Microsoft PowerPoint 
linktitle: Convertir PDF a PowerPoint
type: docs
weight: 30
url: /php-java/convert-pdf-to-powerpoint/
lastmod: "2024-05-20"
description: Aspose.PDF te permite convertir PDF a formato PowerPoint usando PHP. Una forma es convertir PDF a PPTX con Diapositivas como Imágenes.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF para PHP** te permite seguir el progreso de la conversión de PDF a PPTX.
Tenemos una API llamada Aspose.Slides que ofrece la función de crear así como manipular presentaciones PPT/PPTX. Esta API también proporciona la función de convertir archivos PPT/PPTX a formato PDF. En Aspose.PDF para PHP, hemos introducido una función para transformar documentos PDF en formato PPTX. Durante esta conversión, las páginas individuales del archivo PDF se convierten en diapositivas separadas en el archivo PPTX.

Durante la conversión de PDF a PPTX, el texto se representa como Texto donde puedes seleccionarlo/actualizarlo, en lugar de ser representado como una imagen.
 Tenga en cuenta que para convertir archivos PDF a formato PPTX, Aspose.PDF proporciona una clase llamada PptxSaveOptions. Un objeto de la clase [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) se pasa como segundo argumento al método [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

Revise el siguiente fragmento de código para resolver sus tareas con la conversión de PDF a formato PowerPoint:

```php
// Cargar el documento PDF de entrada
$document = new Document($inputFile);

// Crear una instancia de PptxSaveOptions
$saveOption = new PptxSaveOptions();

// Guardar el documento PDF como un archivo PPTX
$document->save($outputFile, $saveOption);
```

## Convertir PDF a PPTX con Diapositivas como Imágenes

En caso de que necesite convertir un PDF buscable a PPTX como imágenes en lugar de texto seleccionable, Aspose.PDF proporciona tal característica a través de la clase [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions). Para lograr esto, establezca la propiedad SlidesAsImages de la clase [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) a 'true' como se muestra en el siguiente ejemplo de código.

El siguiente fragmento de código muestra el proceso para convertir archivos PDF en formato PPTX con las diapositivas como imágenes.

```php
// Cargar el documento PDF de entrada
$document = new Document($inputFile);

// Crear una instancia de PptxSaveOptions
$saveOption = new PptxSaveOptions();
$saveOption->setSlidesAsImages(true);

// Guardar el documento PDF como un archivo PPTX
$document->save($outputFile, $saveOption);

    public static void ConvertPDFtoPPTX_SlideAsImages() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX_out.pptx").toString();

        // Cargar documento PDF
        Document doc = new Document(pdfDocumentFileName);
        // Instanciar la instancia de PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();
        // Guardar la salida en formato PPTX
        pptx_save.setSlidesAsImages(true);

        doc.save(pptxDocumentFileName, pptx_save);
    }
```

{{% alert color="success" %}}
**Intenta convertir PDF a PowerPoint en línea**

Aspose.PDF para PHP te presenta la aplicación gratuita en línea ["PDF a PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF de PDF a PPTX con Aplicación Gratis](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}