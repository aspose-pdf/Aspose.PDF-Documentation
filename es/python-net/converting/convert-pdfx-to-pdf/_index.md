---
title: Convertir PDF/A y PDF/UA a PDF en Python
linktitle: Convertir PDF/A y PDF/UA a PDF
type: docs
weight: 120
url: /es/python-net/convert-pdf_x-to-pdf/
lastmod: "2026-04-14"
description: Aprenda cómo eliminar el cumplimiento de PDF/A y PDF/UA de los archivos PDF en Python con Aspose.PDF for Python via .NET y guardarlos como documentos PDF estándar.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: Cómo convertir PDF/A y PDF/UA a PDF estándar en Python
Abstract: Este artículo explica cómo eliminar el cumplimiento de PDF/A y PDF/UA de los documentos PDF basados en estándares utilizando Aspose.PDF for Python via .NET. Cubre escenarios en los que puede necesitar un PDF estándar en lugar de un archivo archivístico o con restricciones de accesibilidad, y muestra cómo guardar el resultado después de eliminar los metadatos y restricciones de cumplimiento.
---

Utilice esta página cuando necesite convertir un PDF basado en estándares, como PDF/A o PDF/UA, de nuevo a un documento PDF regular para su edición, procesamiento o redistribución posterior.

Los PDFs compatibles con normas son útiles para flujos de trabajo de archivo, impresión y accesibilidad, pero en algunos casos puede ser necesario eliminar esa conformidad antes de integrar el archivo en otros sistemas o canalizaciones. Aspose.PDF for Python via .NET le permite hacerlo programáticamente y luego guardar el resultado como un archivo PDF estándar.

## Convertir PDF/A a PDF

Este ejemplo elimina los metadatos y restricciones de conformidad PDF/A de un PDF para que el documento pueda guardarse nuevamente como un archivo PDF normal.

1. Cargue el documento PDF usando 'ap.Document'.
1. Llame a ’remove_pdfa_compliance()’ para eliminar todas las configuraciones de conformidad y metadatos relacionados con PDF/A.
1. Guarde el PDF resultante en la ruta de salida.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Eliminando la conformidad PDF/UA

Este ejemplo muestra cómo eliminar la conformidad relacionada con PDF/UA para que el documento pueda guardarse como un PDF estándar para flujos de trabajo que no requieren accesibilidad.

1. Cargue el documento PDF usando 'ap.Document()'.
1. Llame a 'document.remove_pdfa_compliance()' para eliminar cualquier restricción o configuración de cumplimiento de PDF/A.
1. Guarde el PDF modificado en 'path_outfile'.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Cuándo usar este flujo de trabajo

- Elimine configuraciones de cumplimiento antes de enviar un documento a una cadena de herramientas que no requiera restricciones de PDF/A o PDF/UA.
- Simplifique el procesamiento de documentos posteriores cuando ya no se necesiten los metadatos de archivado o accesibilidad.
- Normalice los PDFs de entrada antes de exportarlos a otros formatos.

## Conversiones relacionadas

- [Convertir PDF a PDF/A, PDF/E y PDF/X](/pdf/es/python-net/convert-pdf-to-pdf_x/) si necesitas el flujo de trabajo inverso y deseas crear PDFs compatibles con los estándares.
- [Convertir PDF a Word](/pdf/es/python-net/convert-pdf-to-word/) para la salida de documentos editables después de eliminar las restricciones de cumplimiento.
- [Convertir PDF a HTML](/pdf/es/python-net/convert-pdf-to-html/) para una salida compatible con navegadores a partir de archivos PDF estándar.
