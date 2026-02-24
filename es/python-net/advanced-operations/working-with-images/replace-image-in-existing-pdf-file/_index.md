---
title: Reemplazar imagen en archivo PDF existente usando Python
linktitle: Reemplazar imagen
type: docs
weight: 70
url: /es/python-net/replace-image-in-existing-pdf-file/
description: Esta sección describe cómo reemplazar una imagen en un archivo PDF existente usando una biblioteca de Python.
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: Reemplazar una imagen en PDF
Abstract: La documentación de Aspose.PDF para Python via .NET proporciona una guía completa sobre cómo reemplazar imágenes dentro de archivos PDF existentes. Esta funcionalidad es esencial para tareas como actualizar logotipos, gráficos u otros elementos visuales en un documento PDF sin alterar su contenido textual.
---

## Reemplazar una imagen en PDF

¿Cómo reemplazar una imagen existente en una página PDF con una nueva imagen? Implementa esto usando Aspose.PDF para Python via .NET.

1. Importar los módulos necesarios (aspose.pdf, os.path, FileIO).
1. Definir rutas para:
- PDF de entrada (infile)
- Nuevo archivo de imagen (image_file)
- PDF de salida (outfile)
1. Cargar el documento PDF usando 'apdf.Document(path_infile)'.
1. Abrir el nuevo archivo de imagen en modo de lectura binaria.
1. Reemplazar la primera imagen en la primera página:
- 'document.pages[1].resources.images.replace(1, image_stream)'
1. Guardar el PDF actualizado en 'path_outfile'.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    with FileIO(path_image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(path_outfile)
```

## Reemplazar imagen específica

Este ejemplo muestra cómo reemplazar una imagen específica en una página PDF localizándola mediante la detección de ubicación de la imagen.

1. Cargar el PDF usando 'apdf.Document()'.
1. Crear un 'ImagePlacementAbsorber' para recopilar todas las ubicaciones de imágenes en la página.
1. Aceptar el absorbente en la primera página ('document.pages[1].accept(absorber)').
1. Verificar si existen ubicaciones de imágenes en la página.
1. Seleccionar la primera ubicación de imagen (absorber.image_placements[1]) y reemplazarla.
1. Guardar el PDF modificado en 'path_outfile'.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, outfile)

    document = apdf.Document(path_infile)

    # Create ImagePlacementAbsorber to find image placements
    absorber = apdf.ImagePlacementAbsorber()

    # Accept the absorber for the first page
    document.pages[1].accept(absorber)

    # Replace the first image placement found
    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(path_image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(path_outfile)
```
