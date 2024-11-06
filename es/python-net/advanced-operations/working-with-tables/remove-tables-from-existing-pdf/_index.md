---
title: Eliminar tablas de un PDF existente
linktitle: Eliminar Tablas
type: docs
weight: 50
url: es/python-net/remove-tables-from-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Eliminar tablas de un PDF existente",
    "alternativeHeadline": "Cómo eliminar tablas de un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, eliminar tabla, borrar tablas",
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
    "url": "/python-net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


{{% alert color="primary" %}}

Aspose.PDF para Python a través de .NET ofrece la capacidad de insertar/crear una tabla dentro de un documento PDF mientras se genera desde cero o también puede agregar el objeto de tabla en cualquier documento PDF existente. Sin embargo, puede tener un requisito de [Manipular tablas en PDF existente](https://docs.aspose.com/pdf/python-net/manipulate-tables-in-existing-pdf/) donde puede actualizar los contenidos en las celdas de tablas existentes. Sin embargo, puede encontrarse con un requisito para eliminar objetos de tabla de un documento PDF existente.

{{% /alert %}}

Para eliminar las tablas, necesitamos usar la clase [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) para obtener las tablas en un PDF existente y luego llamar a [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods).

## Eliminar tabla del documento PDF

Hemos añadido una nueva función, es decir,
 [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) a la clase existente [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) para eliminar la tabla del documento PDF. Una vez que el absorbedor encuentra tablas en la página con éxito, se vuelve capaz de eliminarlas. Por favor, revise el siguiente fragmento de código que muestra cómo eliminar una tabla de un documento PDF:

```python

    import aspose.pdf as ap

    # Cargar documento PDF existente
    pdf_document = ap.Document(input_file)
    # Crear objeto TableAbsorber para encontrar tablas
    absorber = ap.text.TableAbsorber()
    # Visitar la primera página con el absorbedor
    absorber.visit(pdf_document.pages[1])
    # Obtener la primera tabla en la página
    table = absorber.table_list[0]
    # Eliminar la tabla
    absorber.remove(table)
    # Guardar PDF
    pdf_document.save(output_file)
```

## Eliminar Múltiples Tablas de un Documento PDF

A veces, un documento PDF puede contener más de una tabla y puede surgir la necesidad de eliminar múltiples tablas de él. Para eliminar múltiples tablas de un documento PDF, utilice el siguiente fragmento de código:

```python

    import aspose.pdf as ap

    # Cargar documento PDF existente
    pdf_document = ap.Document(input_file)
    # Crear objeto TableAbsorber para encontrar tablas
    absorber = ap.text.TableAbsorber()
    # Visitar la segunda página con el absorbedor
    absorber.visit(pdf_document.pages[1])
    # Obtener copia de la colección de tablas
    tables = absorber.table_list
    # Recorrer la copia de la colección y eliminar tablas
    for table in tables:
        absorber.remove(table)
    # Guardar documento
    pdf_document.save(output_file)