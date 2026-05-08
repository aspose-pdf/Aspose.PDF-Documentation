---
title: Convertir PDF a PDF/A, PDF/E y PDF/X en Python
linktitle: Convertir PDF a PDF/A, PDF/E y PDF/X
type: docs
weight: 120
url: /es/python-net/convert-pdf-to-pdf_x/
lastmod: "2026-04-14"
description: Aprenda cómo convertir archivos PDF a PDF/A, PDF/E y PDF/X en Python con Aspose.PDF for Python via .NET para flujos de trabajo de archivado, accesibilidad e impresión.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a formatos PDF/x
Abstract: El artículo ofrece una guía completa sobre cómo convertir PDF a formatos PDF/A, PDF/E y PDF/X utilizando Aspose.PDF for Python.
---

**PDF a formato PDF/x significa la capacidad de convertir PDF a formatos adicionales, a saber PDF/A, PDF/E y PDF/X.**

## Convertir PDF a PDF/A

**Aspose.PDF for Python** permite convertir un archivo PDF a un <abbr title="Portable Document Format / A">PDF/A</abbr> Archivo PDF conforme. Antes de hacerlo, el archivo debe ser validado. Este tema explica cómo.

{{% alert color="primary" %}}

Tenga en cuenta que seguimos Adobe Preflight para validar la conformidad PDF/A. Todas las herramientas del mercado tienen su propia “representación” de la conformidad PDF/A. Por favor, consulte este artículo sobre herramientas de validación PDF/A como referencia. Elegimos productos de Adobe para verificar cómo Aspose.PDF produce archivos PDF porque Adobe está en el centro de todo lo relacionado con PDF.

{{% /alert %}}

Convierta el archivo usando el método Convert de la clase Document. Antes de convertir el PDF a un archivo compatible con PDF/A, valide el PDF usando el método Validate. El resultado de la validación se almacena en un archivo XML y luego ese resultado también se pasa al método Convert. También puede especificar la acción para los elementos que no pueden convertirse usando la enumeración ConvertErrorAction.

{{% alert color="success" %}}
**Intenta convertir PDF a PDF/A en línea**

Aspose.PDF for Python le presenta una aplicación en línea ["PDF a PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión PDF a PDF/A con App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

El método 'document.validate()' valida si un archivo PDF cumple con el estándar PDF/A-1B (una versión estandarizada por ISO de PDF diseñada para el archivo a largo plazo). Los resultados de la validación se guardan en un archivo de registro.

### Convertir PDF a PDF/A-1B

El siguiente fragmento de código muestra cómo convertir archivos PDF a formato PDF/A-1B:

1. Cargue el documento PDF usando 'ap.Document'.
1. Llame al método convert con los siguientes parámetros:
    - Ruta del archivo de registro - almacena los detalles del proceso de conversión y de las comprobaciones de cumplimiento.
    - Formato de destino - 'ap.PdfFormat.PDF_A_1B' (estándar de archivado).
    - Acción de error - 'ap.ConvertErrorAction.DELETE' — elimina automáticamente los elementos que impiden el cumplimiento.
1. Guarde el archivo convertido compatible con PDF/A en la ruta de salida.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA(infile, outfile):
    """Convert PDF to PDF/A-1B format."""

    document = ap.Document(infile)
    document.convert(
        outfile.replace(".pdf", "-log.xml"),
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

### Convertir PDF a PDF 2.0 y PDF/A-4

Este ejemplo muestra cómo convertir un documento PDF a formatos estandarizados más recientes: PDF 2.0 y PDF/A-4.
Ambas conversiones ayudan a garantizar el cumplimiento de las especificaciones modernas y los requisitos de archivo.

1. Cargue el documento de entrada usando ap.Document.
1. Realice la primera conversión a PDF 2.0 llamando a document.convert con:
    - Ruta del archivo de registro para los detalles de conversión.
    - Formato de destino - 'ap.PdfFormat.V_2_0'.
    - Acción de error - 'ap.ConvertErrorAction.DELETE' para eliminar elementos no conformes.
1. Realice una segunda conversión a PDF/A-4 usando el mismo método, asegurándose de que el archivo también cumpla con los estándares de archivado.
1. Guarde el documento resultante en la ruta de salida especificada.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA4(infile, outfile):
    logfile = outfile.replace(".pdf", "_log.xml")

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)
    document.convert(logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### Convertir PDF a PDF/A-3A con archivos incrustados

El siguiente fragmento de código muestra cómo incrustar archivos externos en un PDF y luego convertir el PDF al formato PDF/A-3A, que admite archivos adjuntos y es adecuado para el archivado a largo plazo con contenido incrustado.

1. Cargue el PDF de entrada usando 'ap.Document'.
1. Cree un objeto 'FileSpecification' que apunte al archivo a incrustar (p. ej., "aspose-logo.jpg") con una descripción.
1. Agrega la especificación de archivo a la colección 'embedded_files' del PDF.
1. Convertir el documento a PDF/A-3A usando 'document.convert', especificando:
    - Ruta del archivo de registro.
    - Formato de destino - 'ap.PdfFormat.PDF_A_3A'.
    - Acción de error - 'ap.ConvertErrorAction.DELETE' para eliminar elementos no conformes.
1. Guarde el PDF convertido en la ruta de salida.
1. Imprime un mensaje de confirmación.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_attachment(infile, attachement_file, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    document = ap.Document(infile)

    fileSpecification = ap.FileSpecification(attachement_file, "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(
        logfile, ap.PdfFormat.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE
    )
    document.save(outfile)
```

### Convertir PDF a PDF/A-1B con sustitución de fuentes

Esta función convierte un PDF al formato PDF/A-1B mientras maneja fuentes faltantes sustituyéndolas por las disponibles. Esto garantiza que el PDF convertido permanezca visualmente consistente y cumpla con los estándares de archivado.

1. Cargue el PDF usando 'ap.Document'.
1. Convertir el PDF a PDF/A-1B usando 'document.convert', especificando:
    - Ruta del archivo de registro.
    - Formato de destino - 'ap.PdfFormat.PDF_A_1B'.
    - Acción de error - 'ap.ConvertErrorAction.DELETE' para eliminar elementos no conformes.
1. Guarde el PDF convertido en la ruta de salida.
1. Imprime un mensaje de confirmación.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_replace_missing_fonts(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### Convertir PDF a PDF/A-1B con etiquetado automático

Esta función convierte un documento PDF al formato PDF/A-1B mientras etiqueta automáticamente el contenido para accesibilidad y consistencia estructural. El etiquetado automático mejora la usabilidad del documento para los lectores de pantalla y garantiza una estructura semántica adecuada.

1. Cargue el PDF usando 'ap.Document'.
1. Crear 'PdfFormatConversionOptions' especificando:
    - Ruta del archivo de registro.
    - Formato de destino - 'ap.PdfFormat.PDF_A_1B'.
    - Acción de error - 'ap.ConvertErrorAction.DELETE' para eliminar elementos no conformes.
1. Configura 'AutoTaggingSettings':
    - Habilitar 'enable_auto_tagging = True'.
    - Establezca 'heading_recognition_strategy = AUTO' para detectar automáticamente los encabezados.
1. Asignar la configuración de autoetiquetado a las opciones de conversión.
1. Convierta el PDF usando 'document.convert(options)'.
1. Guarde el PDF convertido en la ruta de salida.
1. Imprime un mensaje de confirmación.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_automatic_tagging(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE
    )

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = (
        ap.HeadingRecognitionStrategy.AUTO
    )

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Convertir PDF a PDF/E

Este fragmento de código muestra cómo convertir un documento PDF al formato PDF/E-1, que es un estándar ISO adaptado para la ingeniería y la documentación técnica. Este formato preserva el diseño preciso, los gráficos y los metadatos necesarios para los flujos de trabajo de ingeniería.

1. Cargue el PDF de origen usando 'ap.Document'.
1. Crear 'PdfFormatConversionOptions' especificando:
    - Ruta del archivo de registro para rastrear problemas de conversión.
    - Formato de destino - 'ap.PdfFormat.PDF_E_1'.
    - Acción de error - 'ap.ConvertErrorAction.DELETE' para eliminar elementos no conformes.
1. Convierta el PDF usando 'document.convert(options)'.
1. Guarda el PDF convertido en la ruta de salida especificada.
1. Imprime un mensaje de confirmación.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_E(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE
    )

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Convertir PDF a PDF/X

El siguiente fragmento de código convierte un documento PDF al formato PDF/X-4, que es una norma ISO utilizada comúnmente en la industria de impresión y publicación. PDF/X-4 garantiza la precisión del color, mantiene la transparencia e incrusta perfiles ICC para una salida constante en diferentes dispositivos.

1. Cargue el PDF de origen usando 'ap.Document'.
1. Crear 'PdfFormatConversionOptions' especificando:
    - Ruta del archivo de registro.
    - Formato de destino - 'ap.PdfFormat.PDF_X_4'.
    - Acción de error - 'ap.ConvertErrorAction.DELETE' para eliminar elementos no conformes.
1. Proporcione el **archivo de perfil ICC** para la gestión del color a través de 'icc_profile_file_name'.
1. Especifique un **OutputIntent** con un identificador de condición (p.ej., "FOGRA39") para los requisitos de impresión.
1. Convierta el PDF usando 'document.convert()'.
1. Guarda el PDF convertido en la ruta de salida especificada.
1. Imprime un mensaje de confirmación.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_X(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE
    )

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(
        path.dirname(infile), "ISOcoated_v2_eci.icc"
    )
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Conversiones relacionadas

- [Convertir PDF a Word](/pdf/es/python-net/convert-pdf-to-word/) para flujos de trabajo de contenido editable después de la validación de estándares.
- [Convertir PDF a HTML](/pdf/es/python-net/convert-pdf-to-html/) cuando tu salida objetivo está lista para la web en lugar de PDF basado en estándares.
