---
title: Rotar Páginas de PDF Usando Python a través de C++
linktitle: Rotar Páginas de PDF
type: docs
weight: 20
url: /es/python-cpp/rotate-pages/
description: Este tema describe cómo rotar la orientación de la página en un archivo PDF existente de manera programática con Python a través de C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

A veces, las páginas de PDF pueden tener una orientación incorrecta debido a problemas de escaneo o creación. Rotar las páginas asegura que se muestren en la orientación correcta para facilitar la lectura y visualización.
Rotar las páginas de PDF ayuda a mantener una experiencia de visualización consistente en diferentes dispositivos y plataformas.

Rotar páginas de PDF puede facilitar tareas de edición como agregar anotaciones, comentarios o firmas. Al rotar las páginas a la orientación deseada, puede hacer que los procesos de edición y revisión sean más eficientes.

Además, al imprimir documentos PDF, es importante asegurarse de que las páginas estén orientadas correctamente para evitar problemas de desalineación o recorte.
 Rotar las páginas según sea necesario antes de imprimir ayuda a optimizar la salida de impresión y asegura que el contenido se muestre como se pretende.  
Rotar las páginas de PDF es una función útil que ayuda a mejorar la legibilidad, consistencia y presentación de documentos en diversos contextos y propósitos.

Este tema describe cómo actualizar o cambiar la orientación de las páginas en un archivo PDF existente de manera programática con Python.

## Cambiar la Orientación de la Página

Aspose.PDF para Python vía C++ soporta grandes características como cambiar la orientación de la página

1. Crear un objeto de documento a partir del archivo de entrada
1. Obtener la colección de páginas del documento usando 'apCore.document_get_pages'
1. Obtener la primera página de la colección de páginas con 'apCore.page_collection_get_page'
1. Rotar la página 90 grados en sentido horario usando 'apCore.page_set_rotate'
1. Guardar el documento modificado en el archivo de salida con el método 'document.save'

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Creando un camino al directorio que contiene los archivos de muestra
    dataDir = os.path.join(os.getcwd(), "samples")

    # Creando caminos a los archivos de entrada y salida
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "rotated_document.pdf")

    # Creando un objeto de documento cargando el archivo de entrada
    doc = apCore.document_create_from_file(inputFile)

    # Obteniendo la colección de páginas en el documento
    pages = apCore.document_get_pages(doc)

    # Obteniendo la primera página de la colección
    page = apCore.page_collection_get_page(pages, 1)

    # Rotando la página 90 grados en sentido horario
    apCore.page_set_rotate(page, apCore.Rotation(apCore.on90))

    # Guardando el documento modificado en el archivo de salida
    apCore.document_save(doc, output_file)

    # Cerrando el manejador del documento para liberar recursos
    apCore.close_handle(doc)
```