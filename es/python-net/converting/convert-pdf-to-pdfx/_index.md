---
title: Convertir PDF a formatos PDF/x en Python
linktitle: Convertir PDF a formatos PDF/x
type: docs
weight: 120
url: /es/python-net/convert-pdf-to-pdf_x/
lastmod: "2025-09-27"
description: Este tema le muestra cómo convertir PDF a formatos PDF/x utilizando Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: Convertir PDF a PDF/A, PDF/E y PDF/X
Abstract: >
    Esta página muestra cómo convertir documentos PDF a estándares PDF/A, PDF/E y PDF/X con Aspose.PDF for Python via .NET. Incluye ejemplos para validación, archivado y preparación de archivos PDF para flujos de impresión y conformidad.
---

**PDF a formato PDF/x significa la capacidad de convertir PDF a formatos adicionales, a saber PDF/A, PDF/E y PDF/X.**

## Convertir PDF a PDF/A

**Aspose.PDF for Python** permite convertir un archivo PDF a un <abbr title="Portable Document Format / A">PDF/A</abbr> archivo PDF conforme. Antes de hacerlo, el archivo debe ser validado. Este tema explica cómo.

{{% alert color="primary" %}}

Por favor, tenga en cuenta que seguimos Adobe Preflight para validar la conformidad PDF/A. Todas las herramientas del mercado tienen su propia “representación” de la conformidad PDF/A. Por favor, consulte este artículo sobre herramientas de validación PDF/A para referencia. Elegimos productos de Adobe para verificar cómo Aspose.PDF produce archivos PDF porque Adobe está en el centro de todo lo relacionado con PDF.

{{% /alert %}}

Convierta el archivo usando el método Convert de la clase Document. Antes de convertir el PDF a un archivo compatible con PDF/A, valide el PDF usando el método Validate. El resultado de la validación se almacena en un archivo XML y luego este resultado también se pasa al método Convert. También puede especificar la acción para los elementos que no pueden convertirse usando la enumeración ConvertErrorAction.

{{% alert color="success" %}}
**Intenta convertir PDF a PDF/A en línea**

Aspose.PDF for Python le presenta una aplicación gratuita en línea ["PDF a PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a PDF/A con App gratuita](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

El método 'document.validate()' valida si un archivo PDF cumple con el estándar PDF/A-1B (una versión estandarizada por ISO de PDF diseñada para archivado a largo plazo). Los resultados de la validación se guardan en un archivo de registro.

1. Cargue el documento PDF usando 'ap.Document'.
1. Llame al método validate con el nivel de cumplimiento objetivo (ap.PdfFormat.PDF_A_1B).
1. Los resultados de la validación se escriben en el archivo de registro especificado.

```python
path_infile = path.join(self.data_dir, infile)
path_logfile = path.join(self.data_dir, "python", outfile)

document = ap.Document(path_infile)
document.validate(path_logfile, ap.PdfFormat.PDF_A_1B)
```

### Convertir PDF a PDF/A-1B

El siguiente fragmento de código muestra cómo convertir archivos PDF al formato PDF/A-1B:

1. Cargue el documento PDF usando 'ap.Document'.
1. Llame al método convert con los siguientes parámetros:
    - Ruta del archivo de registro - almacena los detalles del proceso de conversión y las verificaciones de cumplimiento.
    - Formato de destino - 'ap.PdfFormat.PDF_A_1B' (estándar de archivo).
    - Acción de error - 'ap.ConvertErrorAction.DELETE' — elimina automáticamente los elementos que impiden el cumplimiento.
1. Guarde el archivo convertido compatible con PDF/A en la ruta de salida.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

document = ap.Document(path_infile)
document.convert(
    self.data_dir + "pdf_pdfa.log",
    ap.PdfFormat.PDF_A_1B,
    ap.ConvertErrorAction.DELETE,
)
document.save(path_outfile)

print(infile + " converted into " + outfile)
```

### Convertir PDF a PDF 2.0 y PDF/A-4

Este ejemplo demuestra cómo convertir un documento PDF en formatos estandarizados más recientes: PDF 2.0 y PDF/A-4.
Ambas conversiones ayudan a garantizar el cumplimiento de las especificaciones modernas y los requisitos de archivo.

1. Cargue el documento de entrada usando ap.Document.
1. Realice la primera conversión a PDF 2.0 llamando a document.convert con:
    - Ruta del archivo de registro para los detalles de conversión.
    - Formato de destino - 'ap.PdfFormat.V_2_0'.
    - Acción de error - 'ap.ConvertErrorAction.DELETE' para eliminar elementos no conformes.
1. Realice una segunda conversión a PDF/A-4 usando el mismo método, asegurándose de que el archivo también cumpla con los estándares de archivo.
1. Guarda el documento resultante en la ruta de salida especificada.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
path_logfile = path_outfile.replace(".pdf", "_log.xml")

document = ap.Document(path_infile)
document.convert(path_logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)

document.convert(path_logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
document.save(path_outfile)

print(infile + " converted into " + outfile)
```

### Convertir PDF a PDF/A-3A con archivos incrustados

El siguiente fragmento de código demuestra cómo incrustar archivos externos en un PDF y luego convertir el PDF al formato PDF/A-3A, que admite archivos adjuntos y es adecuado para el archivado a largo plazo con contenido incrustado.

1. Cargue el PDF de entrada usando 'ap.Document'.
1. Cree un objeto 'FileSpecification' que apunte al archivo a incrustar (p. ej., "aspose-logo.jpg") con una descripción.
1. Agrega la especificación de archivo a la colección 'embedded_files' del PDF.
1. Convertir el documento a PDF/A-3A usando 'document.convert', especificando:
    - Ruta del archivo de registro.
    - Formato de destino - 'ap.PdfFormat.PDF_A_3A'.
    - Acción de error - 'ap.ConvertErrorAction.DELETE' para eliminar elementos no conformes.
1. Guarda el PDF convertido en la ruta de salida.
1. Imprime un mensaje de confirmación.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
path_logfile = path_outfile.replace(".pdf", "_log.xml")

document = ap.Document(path_infile)

fileSpecification = ap.FileSpecification(
    self.data_dir + "aspose-logo.jpg", "Large Image file"
)
document.embedded_files.add(fileSpecification)
document.convert(path_logfile, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

### Convertir PDF a PDF/A-1B con sustitución de fuentes

Esta función convierte un PDF al formato PDF/A-1B mientras maneja fuentes faltantes sustituyéndolas por otras disponibles. Esto garantiza que el PDF convertido mantenga la consistencia visual y cumpla con los estándares de archivo.

1. Cargue el PDF usando 'ap.Document'.
1. Convertir el PDF a PDF/A-1B usando 'document.convert', especificando:
    - Ruta del archivo de registro.
    - Formato de destino - 'ap.PdfFormat.PDF_A_1B'.
    - Acción de error - 'ap.ConvertErrorAction.DELETE' para eliminar elementos no conformes.
1. Guarda el PDF convertido en la ruta de salida.
1. Imprime un mensaje de confirmación.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
path_logfile = path_outfile.replace(".pdf", "_log.xml")

try:
    ap.text.FontRepository.find_font("AgencyFB")

except ap.FontNotFoundException:
    font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
    ap.text.FontRepository.Substitutions.append(font_substitution)

document = ap.Document(path_infile)
document.convert(path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

### Convertir PDF a PDF/A-1B con etiquetado automático

Esta función convierte un documento PDF al formato PDF/A-1B mientras etiqueta automáticamente el contenido para accesibilidad y consistencia estructural. El etiquetado automático mejora la usabilidad del documento para lectores de pantalla y garantiza una estructura semántica adecuada.

1. Cargue el PDF usando 'ap.Document'.
1. Crear 'PdfFormatConversionOptions' especificando:
    - Ruta del archivo de registro.
    - Formato de destino - 'ap.PdfFormat.PDF_A_1B'.
    - Acción de error - 'ap.ConvertErrorAction.DELETE' para eliminar elementos no conformes.
1. Configurar 'AutoTaggingSettings':
    - Habilitar 'enable_auto_tagging = True'.
    - Establezca 'heading_recognition_strategy = AUTO' para detectar automáticamente los encabezados.
1. Asigne la configuración de etiquetado automático a las opciones de conversión.
1. Convierta el PDF usando 'document.convert(options)'.
1. Guarda el PDF convertido en la ruta de salida.
1. Imprime un mensaje de confirmación.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
path_logfile = path_outfile.replace(".pdf", "_log.xml")

document = ap.Document(path_infile)
options = ap.PdfFormatConversionOptions(
    path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE
)

auto_tagging_settings = ap.AutoTaggingSettings()
auto_tagging_settings.enable_auto_tagging = True

auto_tagging_settings.heading_recognition_strategy = ap.HeadingRecognitionStrategy.AUTO

options.auto_tagging_settings = auto_tagging_settings
document.convert(options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Convertir PDF a PDF/E

Este fragmento valida si un documento PDF cumple con la norma PDF/E-1, que es una norma ISO diseñada para documentos de ingeniería y técnicos. Los resultados de la validación se guardan en un archivo de registro.

1. Cargue el documento PDF usando 'ap.Document'.
1. Llame al método validate, especificando:
    - Ruta del archivo de registro para almacenar los resultados de validación.
    - Formato objetivo - 'ap.PdfFormat.PDF_E_1'.
1. Los resultados de la validación se guardan en el archivo de registro para su revisión.

```python
path_infile = path.join(self.data_dir, infile)
path_logfile = path.join(self.data_dir, "python", outfile)

document = ap.Document(path_infile)
document.validate(path_logfile, ap.PdfFormat.PDF_E_1)
```

El siguiente ejemplo muestra cómo convertir un PDF al formato PDF/E-1, que es una norma ISO diseñada para la ingeniería y la documentación técnica. Este formato conserva la disposición precisa, los gráficos y los metadatos requeridos para los flujos de trabajo de ingeniería.

1. Cargue el PDF de origen usando 'ap.Document'.
1. Crear 'PdfFormatConversionOptions' especificando:
    - Ruta del archivo de registro para rastrear problemas de conversión.
    - Formato objetivo - 'ap.PdfFormat.PDF_E_1'.
    - Acción de error - 'ap.ConvertErrorAction.DELETE' para eliminar elementos no conformes.
1. Convierta el PDF usando 'document.convert(options)'.
1. Guarde el PDF convertido en la ruta de salida especificada.
1. Imprime un mensaje de confirmación.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
path_logfile = path_outfile.replace(".pdf", "_log.xml")

document = ap.Document(path_infile)
options = ap.PdfFormatConversionOptions(
    path_logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE
)

document.convert(options)

# Save PDF document
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Convertir PDF a PDF/X

El siguiente fragmento de código convierte un documento PDF al formato PDF/X-4, que es una norma ISO comúnmente utilizada en la industria de la impresión y la publicación. PDF/X-4 garantiza la precisión del color, mantiene la transparencia e incrusta perfiles ICC para una salida consistente en todos los dispositivos.

1. Cargue el PDF de origen usando 'ap.Document'.
1. Crear 'PdfFormatConversionOptions' especificando:
    - Ruta del archivo de registro.
    - Formato de destino - 'ap.PdfFormat.PDF_X_4'.
    - Acción de error - 'ap.ConvertErrorAction.DELETE' para eliminar elementos no conformes.
1. Proporcione el **archivo de perfil ICC** para la gestión del color a través de 'icc_profile_file_name'.
1. Especifique un **OutputIntent** con un identificador de condición (p.ej., "FOGRA39") para los requisitos de impresión.
1. Convierta el PDF usando 'document.convert()'.
1. Guarde el PDF convertido en la ruta de salida especificada.
1. Imprime un mensaje de confirmación.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
path_logfile = path_outfile.replace(".pdf", "_log.xml")

document = ap.Document(path_infile)
options = ap.PdfFormatConversionOptions(
    path_logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE
)

# Provide the name of the external ICC profile file (optional)
options.icc_profile_file_name = path.join(self.data_dir, "ISOcoated_v2_eci.icc")
# Provide an output condition identifier and other necessary OutputIntent properties (optional)
options.output_intent = ap.OutputIntent("FOGRA39")

document.convert(options)

# Save PDF document
document.save(path_outfile)
print(infile + " converted into " + outfile)
```
