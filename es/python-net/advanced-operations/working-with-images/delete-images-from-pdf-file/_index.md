---
title: Eliminar imágenes de archivo PDF usando Python
linktitle: Eliminar imágenes
type: docs
weight: 20
url: /es/python-net/delete-images-from-pdf-file/
description: Esta sección explica cómo eliminar imágenes de un archivo PDF usando Aspose.PDF para Python mediante .NET.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Cómo eliminar imágenes de PDF usando Python
Abstract: El artículo discute las diversas razones para eliminar imágenes de archivos PDF, como proteger la privacidad, evitar el acceso no autorizado a información sensible, reducir el tamaño del archivo para facilitar su compartición y almacenamiento, y preparar el documento para compresión o extracción de texto. Presenta **Aspose.PDF for Python via .NET** como una herramienta para realizar esta tarea. El artículo proporciona instrucciones paso a paso y fragmentos de código para eliminar imágenes específicas o todas las imágenes de un archivo PDF usando Aspose.PDF. El proceso implica abrir un documento PDF existente, eliminar imágenes de forma individual o masiva, y guardar el archivo actualizado. El código Python proporcionado muestra cómo eliminar imágenes accediendo a los recursos del documento y modificando las páginas deseadas.
---

Hay muchas razones para eliminar todas o ciertas imágenes de los PDFs.
A veces un archivo PDF puede contener imágenes importantes que deben eliminarse para proteger la privacidad o evitar el acceso no autorizado a cierta información.

Eliminar imágenes no deseadas o redundantes puede ayudar a reducir el tamaño del archivo, facilitando su compartición o almacenamiento.
Si es necesario, puedes reducir el número de páginas eliminando todas las imágenes del documento.
Además, eliminar imágenes del documento ayudará a preparar el PDF para la compresión o la extracción de información textual.

**Aspose.PDF for Python via .NET** te ayudará con esta tarea.

## Eliminar imágenes de archivo PDF

Para eliminar una imagen de un archivo PDF:

1. Abrir documento PDF existente.
1. Eliminar una imagen concreta.
1. Guardar el archivo PDF actualizado.

El siguiente fragmento de código muestra cómo eliminar una imagen de un archivo PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    document.pages[1].resources.images.delete(1)
    document.save(path_outfile)
```
