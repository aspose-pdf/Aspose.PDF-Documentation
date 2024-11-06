---
title: Ejemplo de Hello World usando el lenguaje Python
linktitle: Ejemplo de Hello World
type: docs
weight: 20
url: es/python-cpp/hello-world-example/
description: Esta muestra demuestra cómo crear un documento PDF simple "Hello, World!" usando Aspose.PDF para Python
lastmod: "2023-07-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ejemplo de Hello World usando el lenguaje Python",
    "alternativeHeadline": "Aspose.PDF Python (via C++) ejemplo",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, Python, generación de documentos",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-cpp.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://https://www.youtube.com/@AsposePDF",
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
    "url": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta muestra demuestra cómo crear un documento PDF simple usando Aspose.PDF para Python.",
    "articleBody": "Un caso de uso simple puede ayudar a demostrar las características de un lenguaje de programación o software. Esto se hace generalmente con un ejemplo de 'Hello World'.\n\nAspose.PDF para Python vía C++ es una poderosa API de PDF que permite a los desarrolladores crear, manipular y convertir documentos PDF en sus aplicaciones Python. Soporta trabajar con varios formatos de archivo como PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX y formatos de archivo de imagen. En este artículo, le mostraremos cómo crear un documento PDF con el texto 'Hello World!' usando la API Aspose.PDF. Debe instalar Aspose.PDF para Python vía C++ en su entorno antes de ejecutar el siguiente ejemplo de código.\n1. Importe el módulo AsposePdfPython.\n2. Cree un nuevo objeto de documento PDF usando la función document_create.\n3. Obtenga la colección de páginas del documento usando la función document_get_pages.\n4. Agregue una nueva página a la colección de páginas usando la función page_collection_add_page.\n5. Obtenga la colección de párrafos de la página usando la función page_get_paragraphs.\n6. Cree un nuevo objeto de imagen usando la función image_create.\n7. Establezca el nombre del archivo del objeto de imagen en 'sample.jpg' usando la función image_set_file.\n8. Agregue el objeto de imagen a la colección de párrafos usando la función paragraphs_add_image.\n9. Guarde el documento en un archivo llamado 'document.pdf' usando la función document_save.\n10. Cierre el manejador del documento usando la función close_handle."
}
</script>


Un caso de uso simple puede ayudar a demostrar las características de un lenguaje de programación o software. Esto generalmente se hace con un ejemplo de "Hola Mundo".

Aspose.PDF para Python vía C++ es una potente API de PDF que permite a los desarrolladores crear, manipular y convertir documentos PDF en sus aplicaciones Python. Soporta trabajar con varios formatos de archivo como PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX y formatos de archivo de imagen. En este artículo, te mostraremos cómo crear un documento PDF con el texto "¡Hola Mundo!" usando la API de Aspose.PDF. Necesitas instalar Aspose.PDF para Python vía C++ en tu entorno antes de ejecutar el siguiente ejemplo de código.

1. Importa el módulo `AsposePdfPython`.
1. Crea un nuevo objeto de documento PDF usando la función `document_create`.
1. Obtén la colección de páginas del documento usando la función `document_get_pages`.
1. Añade una nueva página a la colección de páginas usando la función `page_collection_add_page`.

1. Obtener la colección de párrafos de la página usando la función `page_get_paragraphs`.
1. Crear un nuevo objeto de imagen usando la función `image_create`.
1. Establecer el nombre de archivo del objeto de imagen a "sample.jpg" usando la función `image_set_file`.
1. Agregar el objeto de imagen a la colección de párrafos usando la función `paragraphs_add_image`.
1. Guardar el documento en un archivo llamado "document.pdf" usando la función `document_save`.
1. Cerrar el manejador del documento usando la función `close_handle`.

El siguiente fragmento de código es un programa Hola Mundo que demuestra cómo funciona Aspose.PDF para Python a través de C++.

```python
from AsposePdfPython import *
 
doc = document_create()
pages = document_get_pages(doc)
page = page_collection_add_page(pages)
paragraphs = page_get_paragraphs(page)
image = image_create()
image_set_file(image,"sample.jpg")
paragraphs_add_image(paragraphs,image)
 
document_save(doc, "document.pdf")
close_handle(doc)
```