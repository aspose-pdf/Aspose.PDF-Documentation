---
title: Establecer Tamaño de PDF usando Python a través de C++
linktitle: Establecer Tamaño de PDF
type: docs
weight: 30
url: /python-cpp/get-and-set-page-properties/
description: Esta sección muestra cómo obtener o establecer propiedades de página de PDF como el tamaño del documento usando Python a través de C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Establecer Tamaño de archivo PDF

Aspose.PDF para Python a través de C++ te permite leer y establecer propiedades de páginas en un archivo PDF en tus aplicaciones Python.

El siguiente fragmento de código abre un archivo PDF, cambia el tamaño de la primera página ajustando el **Cuadro de Recorte** (el cuadro de recorte es el tamaño de "página" en el que se muestra tu documento PDF en Adobe Acrobat), y guarda el documento modificado en un nuevo archivo.

1. Crea un objeto de documento a partir del archivo de entrada
1. Obtén la colección de páginas del documento usando [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/)

1. Obtenga la primera página de la colección de páginas con [page_collection_get_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_get_page/)
1. Obtenga el rectángulo del cuadro de recorte de la página usando [page_get_rectangle](https://reference.aspose.com/pdf/python-cpp/core/page_get_rectangle/)
1. Calcule las nuevas coordenadas para el cuadro de recorte
1. Actualice las coordenadas del cuadro de recorte con los nuevos valores
1. Guarde el documento modificado en el archivo de salida con el método 'document.save'

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Obtenga el directorio de trabajo actual y cree la ruta al directorio "samples"
    dataDir = os.path.join(os.getcwd(), "samples")

    # Cree las rutas de los archivos de entrada y salida
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "resized_document.pdf")

    # Cree un objeto de documento desde el archivo de entrada
    doc = apCore.document_create_from_file(inputFile)

    # Obtenga la colección de páginas del documento
    pages = apCore.document_get_pages(doc)

    # Obtenga la primera página de la colección de páginas
    page = apCore.page_collection_get_page(pages, 1)

    # Obtenga el rectángulo del cuadro de recorte de la página
    crop_box = apCore.page_get_rectangle(page)

    # Calcule las nuevas coordenadas para el cuadro de recorte
    LLX = apCore.rectangle_get_LLX(crop_box) + 10
    LLY = apCore.rectangle_get_LLY(crop_box) + 10
    URX = apCore.rectangle_get_URX(crop_box) - 10
    URY = apCore.rectangle_get_URY(crop_box) - 10

    # Actualice las coordenadas del cuadro de recorte con los nuevos valores
    apCore.rectangle_set_LLX(crop_box, LLX)
    apCore.rectangle_set_LLY(crop_box, LLY)
    apCore.rectangle_set_URX(crop_box, URX)
    apCore.rectangle_set_URY(crop_box, URY)

    # Guarde el documento modificado en el archivo de salida
    apCore.document_save(doc, output_file)

    # Cierre el manejador del documento
    apCore.close_handle(doc)
```