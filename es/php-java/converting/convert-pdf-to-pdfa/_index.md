---
title: Convertir PDF a formatos PDF/A 
linktitle: Convertir PDF a formatos PDF/A
type: docs
weight: 100
url: es/php-java/convert-pdf-to-pdfa/
lastmod: "2024-05-20"
description: Este tema muestra cómo Aspose.PDF permite convertir un archivo PDF a un archivo PDF conforme con PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF para PHP** te permite convertir un archivo PDF a un archivo PDF conforme con PDF/A. Antes de hacerlo, el archivo debe ser validado. Este artículo explica cómo.

Por favor, ten en cuenta que seguimos Adobe Preflight para validar la conformidad con PDF/A. Todas las herramientas en el mercado tienen su propia "representación" de conformidad con PDF/A. Por favor, consulta este artículo sobre [herramientas de validación de PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) como referencia. Elegimos los productos de Adobe para verificar cómo Aspose.PDF produce archivos PDF porque Adobe está en el centro de todo lo relacionado con PDF.

Antes de convertir el PDF a un archivo conforme con PDF/A, valida el PDF usando el método de validación.
 El resultado de la validación se almacena en un archivo XML y luego este resultado también se pasa al método de conversión. También puede especificar la acción para los elementos que no se pueden convertir utilizando la enumeración [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

## Conversión de PDF a PDF/A

El siguiente fragmento de código muestra cómo convertir archivos PDF a PDF compatibles con PDF/A-1b.

```php
// Crear un nuevo objeto de Documento y cargar el archivo PDF de entrada.
$document = new Document($inputFile);

// Convertir el documento al formato PDF/A-1a y especificar el archivo de registro y la acción de error.
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// Guardar el documento convertido en el archivo de salida.
$document->save($outputFile);
```

Para realizar solo la validación, use la siguiente línea de código:

```php
// Crear un nuevo objeto de Documento y cargar el archivo PDF de entrada.
$document = new Document($inputFile);

// Convertir el documento al formato PDF/A-1a y especificar el archivo de registro y la acción de error.
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// Validar PDF para PDF/A-1a
if ($document->validate("validation-result-A1A.xml", PdfFormat.PDF_A_1A))
{
    echo "Válido";
}
else
{
    echo "No válido";
}
```

{{% alert color="primary" %}}
**Intenta convertir PDF a PDF/A en línea**

Aspose.PDF para PHP te presenta la aplicación en línea gratuita ["PDF a PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF de PDF a PDF/A con Aplicación Gratuita](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}