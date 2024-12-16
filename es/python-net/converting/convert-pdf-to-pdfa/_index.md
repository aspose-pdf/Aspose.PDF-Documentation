---
title: Convertir formatos PDF a PDF/A en Python
linktitle: Convertir formatos PDF a PDF/A
type: docs
weight: 100
url: /es/python-net/convert-pdf-to-pdfa/
lastmod: "2022-12-23"
description: Este tema muestra cómo Aspose.PDF para Python permite convertir un archivo PDF a un archivo PDF compatible con PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF para Python** te permite convertir un archivo PDF a un archivo PDF compatible con <abbr title="Formato de Documento Portátil / A">PDF/A</abbr>. Antes de hacerlo, el archivo debe ser validado. Este tema explica cómo.

{{% alert color="primary" %}}

Por favor, ten en cuenta que seguimos Adobe Preflight para validar la conformidad con PDF/A. Todas las herramientas en el mercado tienen su propia “representación” de la conformidad con PDF/A. Por favor, consulta este artículo sobre herramientas de validación de PDF/A como referencia. Elegimos los productos de Adobe para verificar cómo Aspose.PDF produce archivos PDF porque Adobe está en el centro de todo lo relacionado con PDF.

{{% /alert %}}

Convierte el archivo usando el método Convert de la clase Document.
 Antes de convertir el PDF a un archivo compatible con PDF/A, valida el PDF usando el método Validate. El resultado de la validación se almacena en un archivo XML y luego este resultado también se pasa al método Convert. También puedes especificar la acción para los elementos que no se pueden convertir usando la enumeración ConvertErrorAction.

{{% alert color="success" %}}
**Intenta convertir PDF a PDF/A en línea**

Aspose.PDF para Python te presenta la aplicación en línea gratuita ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Aspose.PDF Conversión de PDF a PDF/A con Aplicación Gratuita](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Convertir archivo PDF a PDF/A-1b

El siguiente fragmento de código muestra cómo convertir archivos PDF a PDF/A-1b compatible.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pdfa.pdf"
    output_log = DIR_OUTPUT + "convert_pdf_to_pdfa.log"
    # Abrir documento PDF
    document = ap.Document(input_pdf)
    # Convertir a documento compatible con PDF/A
    document.convert(output_log, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    # Guardar documento de salida
    document.save(output_pdf)
```