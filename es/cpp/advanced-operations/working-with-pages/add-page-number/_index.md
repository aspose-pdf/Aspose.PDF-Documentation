---
title: Añadir Número de Página a PDF con C++
linktitle: Añadir Número de Página
type: docs
weight: 100
url: es/cpp/add-page-number/
description: Aspose.PDF para C++ te permite añadir un Sello de Número de Página a tu archivo PDF usando la clase PageNumber Stamp.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cómo Añadir Números de Página a un PDF Existente

Todos los documentos deben tener números de página. El número de página facilita al lector localizar diferentes partes del documento.
**Aspose.PDF para C++** te permite añadir números de página con PageNumberStamp.

Los siguientes pasos y código de ejemplo ilustran cómo añadir etiquetas de numeración de páginas a un documento PDF existente usando el elemento de página [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) para añadir automáticamente números de página a un PDF.

Pasos para Añadir Números de Página a un Documento PDF Existente:

Para añadir un sello de número de página, necesitas crear un objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) y un objeto [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) usando las propiedades requeridas.

Después de eso, puede llamar al método [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) de la [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) para agregar el sello en el PDF.

También puede establecer los atributos de fuente del sello del número de página.

El siguiente fragmento de código le muestra cómo agregar números de página en un archivo PDF.

```cpp
void AddPageNumberToPDF() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("PageNumberStamp.pdf");
    String outputFileName("PageNumberStamp_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Crear sello de número de página
    auto pageNumberStamp = MakeObject<PageNumberStamp>();
    //// Si el sello es de fondo
    //pageNumberStamp.Background = false;
    //pageNumberStamp.Format = "Página # de " + pdfDocument.Pages.Count;
    //pageNumberStamp.BottomMargin = 10;
    //pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
    //pageNumberStamp.StartingNumber = 1;

    //// Establecer propiedades de texto
    //pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
    //pageNumberStamp.TextState.FontSize = 14.0F;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
    //pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

    // Agregar sello a una página en particular
    document->get_Pages()->idx_get(1)->AddStamp(pageNumberStamp);

    // Guardar documento de salida
    document->Save(_dataDir+ outputFileName);
}
```

## Ejemplo en Vivo

[Añadir números de página a PDF](https://products.aspose.app/pdf/page-number) es una aplicación web gratuita en línea que le permite investigar cómo funciona la funcionalidad de agregar números de página.

[![Cómo añadir número de página en pdf usando C++](page_number.png)](https://products.aspose.app/pdf/page-number)

## Añadir/Quitar numeración Bates

**La numeración Bates** (también conocida como estampado Bates) se utiliza en los campos legal, médico y empresarial para colocar números identificativos y/o marcas de fecha/hora en imágenes y documentos a medida que se escanean o procesan, por ejemplo, durante la etapa de descubrimiento de preparativos para un juicio o identificación de recibos de negocio. Este proceso proporciona identificación, protección y numeración consecutiva automática de las imágenes o documentos.

Aspose.PDF tiene soporte limitado para la Numeración Bates por ahora. Esta funcionalidad se actualizará de acuerdo con las solicitudes de los clientes.

### Cómo quitar la numeración Bates

```cpp
void WorkingWithPages::RemoveBatesNubmering()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("BatesNumbering.pdf");
    String outputFileName("BatesNumbering_out.pdf");
    String customSubtype("BatesN");
    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    for (auto page : document->get_Pages())
    {
        auto coll = page->get_Artifacts();
        for (auto batesNum : coll)
        {
        if (batesNum->get_CustomSubtype() == customSubtype)
            page->get_Artifacts()->Delete(batesNum);
        }
    }

    // Guardar documento de salida
    document->Save(_dataDir + outputFileName);
}
```