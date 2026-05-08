---
title: Convertir PDF/A y PDF/UA a PDF en Python
linktitle: Convertir PDF/A y PDF/UA a PDF
type: docs
weight: 120
url: /es/python-net/convert-pdf_x-to-pdf/
lastmod: "2026-04-14"
description: Aprenda cómo eliminar el cumplimiento de PDF/A y PDF/UA de archivos PDF en Python con Aspose.PDF for Python via .NET y guardarlos como documentos PDF estándar.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir PDF/A y PDF/UA a PDF estándar en Python
Abstract: Este artículo explica cómo eliminar el cumplimiento de PDF/A y PDF/UA de documentos PDF basados en estándares mediante Aspose.PDF for Python via .NET. Cubre escenarios en los que puede necesitar un PDF estándar en lugar de un archivo de archivo o con restricciones de accesibilidad, y muestra cómo guardar el resultado después de eliminar los metadatos y restricciones de cumplimiento.
---

Utilice esta página cuando necesite convertir un PDF basado en estándares, como PDF/A o PDF/UA, de nuevo a un documento PDF normal para edición, procesamiento o redistribución posteriores.

Los PDFs que cumplen con los estándares son útiles para flujos de trabajo de archivo, impresión y accesibilidad, pero en algunos casos puede que necesite eliminar ese cumplimiento antes de integrar el archivo en otros sistemas o canalizaciones. Aspose.PDF for Python via .NET le permite hacerlo programáticamente y luego guardar el resultado como un archivo PDF estándar.

## Convertir PDF/A a PDF

Este ejemplo elimina los metadatos y restricciones de cumplimiento de PDF/A de un PDF para que el documento pueda guardarse nuevamente como un archivo PDF normal.

1. Cargue el documento PDF usando 'ap.Document'.
1. Llame a 'remove_pdfa_compliance()' para eliminar todas las configuraciones y metadatos de cumplimiento relacionados con PDF/A.
1. Guarde el PDF resultante en la ruta de salida.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdfa_compliance()
    document.save(outfile)
```

## Eliminando cumplimiento PDF/UA

Este ejemplo demuestra cómo eliminar el cumplimiento relacionado con PDF/UA para que el documento pueda guardarse como un PDF estándar para flujos de trabajo que no son específicos de accesibilidad.

1. Cargue el documento PDF usando 'ap.Document()'.
1. Llame a 'document.remove_pdfa_compliance()' para eliminar cualquier restricción o configuración de cumplimiento PDF/A.
1. Guarde el PDF modificado en 'path_outfile'.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFUA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdf_ua_compliance()
    document.save(outfile)
```

## Cuándo usar este flujo de trabajo

- Elimine la configuración de cumplimiento antes de enviar un documento a una cadena de herramientas que no requiera restricciones de PDF/A o PDF/UA.
- Simplifique el procesamiento de documentos posterior cuando los metadatos de archivo o de accesibilidad ya no sean necesarios.
- Normaliza los PDFs de entrada antes de exportarlos a otros formatos.

## Conversiones relacionadas

- [Convertir PDF a PDF/A, PDF/E y PDF/X](/pdf/es/python-net/convert-pdf-to-pdf_x/) si necesitas el flujo de trabajo opuesto y deseas crear PDFs compatibles con estándares.
- [Convertir PDF a Word](/pdf/es/python-net/convert-pdf-to-word/) para una salida de documento editable después de eliminar las restricciones de cumplimiento.
- [Convertir PDF a HTML](/pdf/es/python-net/convert-pdf-to-html/) para una salida compatible con navegadores a partir de archivos PDF estándar.
