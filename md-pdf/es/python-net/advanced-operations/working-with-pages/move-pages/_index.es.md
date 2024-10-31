---
title: Mover páginas de PDF programáticamente a través de Python
linktitle: Mover páginas de PDF
type: docs
weight: 100
url: /python-net/move-pages/
description: Intente mover páginas a la ubicación deseada o al final de un archivo PDF usando Aspose.PDF para Python a través de .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Mover páginas de PDF programáticamente Python",
    "alternativeHeadline": "Cómo mover páginas de PDF con Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, mover página pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/move-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "Intente mover páginas a la ubicación deseada o al final de un archivo PDF usando Aspose.PDF para Python a través de .NET."
}
</script>


## Mover una Página de un Documento PDF a Otro

Este tema explica cómo mover una página de un documento PDF al final de otro documento usando Python.
Para mover una página debemos:

1. Crear un objeto de clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el archivo PDF de origen.
1. Crear un objeto de clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el archivo PDF de destino.
1. Obtener la página de la colección [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) la página al documento de destino.
1. Guardar el PDF de salida usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) la página en el documento de origen.

1. Guarde el PDF de origen usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

El siguiente fragmento de código le muestra cómo mover una página.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(src_file_name)
    dstDocument = ap.Document(dst_File_name)
    page = srcDocument.pages[2]
    dstDocument.pages.add(page)
    # Guardar archivo de salida
    dstDocument.save(dst_File_name_new)
    srcDocument.pages.delete(2)
    srcDocument.save(src_file_name_new)
```

## Mover un Conjunto de Páginas de un Documento PDF a Otro

1. Cree un objeto de clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el archivo PDF de origen.
2. Cree un objeto de clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el archivo PDF de destino.
3. Defina un array con los números de página a mover.
4. Ejecute un bucle a través del array:

1. Obtener página de la [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) página al documento de destino.
1. Guardar el PDF de salida usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) página en el documento fuente usando array.
1. Guardar el PDF fuente usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

El siguiente fragmento de código te muestra cómo insertar una página vacía al final de un archivo PDF.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)
    dstDocument = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = srcDocument.pages[page_index]
        dstDocument.pages.add(page)
    # Guardar archivos de salida
    dstDocument.save(output_pdf_1)
    srcDocument.pages.delete(pages)
    srcDocument.save(output_pdf_2)
```


## Moviendo una Página a una nueva ubicación en el Documento PDF actual

1. Cree un objeto de la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) con el archivo PDF de origen.
1. Obtenga la Página de la colección [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) página a la nueva ubicación (por ejemplo, al final).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) página en la ubicación anterior.
1. Guarde el PDF de salida usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Guardar archivo de salida
    srcDocument.save(output_pdf)