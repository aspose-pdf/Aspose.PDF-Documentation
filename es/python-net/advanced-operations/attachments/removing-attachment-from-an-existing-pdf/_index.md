---
title: Eliminar archivos adjuntos de PDF en Python
linktitle: Eliminar adjunto de un PDF existente
type: docs
weight: 30
url: /es/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF puede eliminar adjuntos de sus documentos PDF. Utilice Python PDF API para eliminar adjuntos en archivos PDF usando Aspose.PDF for Python via .NET library.
lastmod: "2026-04-26"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo eliminar adjuntos de PDF con Python
Abstract: Este artículo discute cómo eliminar adjuntos de archivos PDF usando Aspose.PDF for Python. Los adjuntos en un documento PDF se almacenan dentro de la colección `EmbeddedFiles` del objeto `Document`. Para eliminar todos los adjuntos de un PDF, puede invocar el método `delete()` en la colección `EmbeddedFiles` y luego guardar el documento actualizado usando el método `save()` del objeto `Document`. Se proporciona un fragmento de código para demostrar este proceso, mostrando los pasos de abrir un documento, eliminar sus adjuntos y guardar el archivo modificado.
---

Aspose.PDF for Python puede eliminar adjuntos de archivos PDF. Los adjuntos de un documento PDF se encuentran en el objeto Document. [Archivos incrustados](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) colección.

Este flujo de trabajo es útil cuando necesita limpiar archivos incrustados obsoletos, reducir el tamaño del paquete o preparar un PDF para redistribución sin los materiales fuente adjuntos.

Para eliminar todos los archivos adjuntos asociados a un archivo PDF:

1. Llame al [Archivos incrustados](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) colección\u0027s [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) método.
1. Guarde el archivo actualizado usando el [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) del objeto [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

El siguiente fragmento de código muestra cómo eliminar archivos adjuntos de un documento PDF.

```python

import aspose.pdf as ap

def remove_attachment(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete()
        document.save(outfile)
```

## Eliminar un archivo adjunto específico por nombre

Si necesitas eliminar solo un archivo adjunto y mantener los demás, usa el [delete_by_key()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/delete_by_key/) método y pasa el nombre del adjunto.

Para eliminar un adjunto específico:

1. Abre el archivo PDF fuente.
1. Llamada `document.embedded_files.delete_by_key(attachment_name)`.
1. Guarda el archivo PDF actualizado.

El siguiente fragmento de código elimina un adjunto por su nombre.

```python

import aspose.pdf as ap

def remove_attachment(infile, attachment_name, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete_by_key(attachment_name)
        document.save(outfile)
```

## Temas relacionados con archivos adjuntos

- [Trabajar con archivos adjuntos PDF en Python](/pdf/es/python-net/attachments/)
- [Agregar archivos adjuntos a PDF en Python](/pdf/es/python-net/add-attachment-to-pdf-document/)
- [Crear y gestionar portafolios PDF en Python](/pdf/es/python-net/portfolio/)

