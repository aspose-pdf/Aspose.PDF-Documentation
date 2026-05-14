---
title: Extraer archivos adjuntos de PDF
linktitle: Extraer archivos adjuntos
type: docs
weight: 50
url: /es/python-net/extract-attachment/
description: Aprenda cómo trabajar con archivos adjuntos PDF usando Python y Aspose.PDF.
lastmod: "2026-04-26"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Guía completa para administrar archivos adjuntos PDF en Python: agregar, extraer y procesar archivos incrustados"
Abstract: Los archivos adjuntos PDF se utilizan ampliamente para almacenar documentos de soporte, informes, imágenes y otros recursos directamente dentro de un archivo PDF. Este artículo ofrece una visión completa del manejo de archivos adjuntos PDF con Python usando Aspose.PDF. Explica cómo incrustar archivos externos en PDFs existentes, extraer adjuntos específicos o todos los adjuntos, inspeccionar metadatos como el tamaño del archivo y las marcas de tiempo, y recuperar archivos almacenados como anotaciones FileAttachment. Cada ejemplo muestra técnicas prácticas para automatizar flujos de trabajo de adjuntos, mejorar la portabilidad de documentos y simplificar la gestión de archivos. Ya sea construyendo sistemas de documentos empresariales o scripts de automatización personalizados, los desarrolladores pueden usar estos métodos para gestionar eficientemente los archivos incrustados dentro de documentos PDF.
---

## Extraer adjunto específico de PDF

Extraiga un archivo incrustado único de un documento PDF usando Python y Aspose.PDF. Busca un adjunto por nombre, recupera su contenido y lo guarda como un archivo separado. Esto es útil para acceder a documentos incrustados como informes, registros o archivos de apoyo almacenados dentro del PDF.

1. Definir función 'extract_single_attachment()'.
1. Abrir documento PDF.
1. Buscar adjunto.
1. Extraer contenido del adjunto.

```python
import aspose.pdf as ap

def extract_single_attachment(infile, attachment_name, outfile):
    with ap.Document(infile) as document:
        print(f"Extracting attachment: {attachment_name}")

        attachment_found = False
        for file_spec in document.embedded_files:
            if file_spec.name == attachment_name:
                with open(outfile, "wb") as f:
                    f.write(file_spec.contents.read())
                print("Attachment extracted successfully")
                attachment_found = True
                break

        if not attachment_found:
            raise ValueError(f"Attachment '{attachment_name}' not found in PDF")
```

## Mostrar metadatos del archivo adjunto

Esta función auxiliar imprime la información de metadatos de un objeto de especificación de archivo. Normalmente se usa al trabajar con archivos adjuntos incrustados en PDFs usando Aspose.PDF, lo que permite a los desarrolladores inspeccionar detalles como suma de verificación, fecha de creación, fecha de modificación y tamaño del archivo.

```python
def _print_file_params(params):
    """Helper to print file specification parameters."""
    if params:
        print(f"CheckSum: {params.check_sum}")
        print(f"Creation Date: {params.creation_date}")
        print(f"Modification Date: {params.mod_date}")
        print(f"Size: {params.size}")
```

## Extraer e inspeccionar todos los archivos adjuntos PDF

Este fragmento de código muestra cómo extraer todos los archivos incrustados de un documento PDF usando Python y Aspose.PDF. No solo guarda cada adjunto en una carpeta especificada, sino que también imprime metadatos detallados como el nombre del archivo, la descripción, el tipo MIME, la suma de verificación y las marcas de tiempo. Esto es útil para auditorías, exportaciones o el procesamiento de contenido incrustado en archivos PDF.

```python
from os import path
import aspose.pdf as ap

def extract_attachments(infile, output_dir):
    with ap.Document(infile) as document:
        print(f"Total files: {len(document.embedded_files)}")

        for file_spec in document.embedded_files:
            print(f"Name: {file_spec.name}")
            print(f"Description: {file_spec.description}")
            print(f"Mime Type: {file_spec.mime_type}")
            _print_file_params(file_spec.params)

            output_path = path.join(output_dir, file_spec.name)
            with open(output_path, "wb") as f:
                f.write(file_spec.contents.read())
```

## Extraer archivos de anotaciones de adjuntos PDF

Extraer un archivo incrustado de una anotación FileAttachment en un PDF usando Python y Aspose.PDF. Busca en la primera página la primera anotación de adjunto, recupera el archivo incrustado y lo guarda en un directorio de salida seleccionado. Esto es útil cuando los PDF contienen íconos de adjuntos de archivo clicables en lugar de colecciones estándar de archivos incrustados.

```python
from os import path
import aspose.pdf as ap
from aspose.pycore import cast

def extract_file_attachment_annotation(infile, output_dir):
    # Open PDF document
    with ap.Document(infile) as document:

        # Get first page
        page = document.pages[1]

        # Find first FileAttachment annotation
        file_attachment = next(
            (
                annot
                for annot in page.annotations
                if annot.annotation_type == ap.annotations.AnnotationType.FILE_ATTACHMENT
            ),
            None,
        )

        if file_attachment is None:
            print("No FileAttachment annotation found on the first page.")
            return

        # Cast to FileAttachmentAnnotation
        faa = cast(ap.annotations.FileAttachmentAnnotation, file_attachment)

        # Access embedded file
        file_spec = faa.file
        print(f"File name: {file_spec.name}")

        # Save embedded file to disk
        output_path = path.join(output_dir, f"extracted-{file_spec.name}")
        with open(output_path, "wb") as f:
            f.write(file_spec.contents.read())

        print(f"Extracted to: {output_path}")
```