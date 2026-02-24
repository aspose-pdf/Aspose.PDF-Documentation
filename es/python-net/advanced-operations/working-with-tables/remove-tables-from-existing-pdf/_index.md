---
title: Eliminar tablas de un PDF existente
linktitle: Eliminar tablas
type: docs
weight: 50
url: /es/python-net/removing-tables/
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo eliminar tablas de un PDF usando Python
Abstract: Este artículo discute la funcionalidad de Aspose.PDF para Python a través de .NET, centrándose específicamente en la manipulación de tablas dentro de documentos PDF. La biblioteca permite a los usuarios insertar o crear tablas tanto en archivos PDF nuevos como existentes, así como manipular o eliminar tablas de PDFs existentes. El artículo presenta la clase `TableAbsorber`, que es crucial para identificar e interactuar con tablas en un PDF. Se ha añadido un nuevo método, `remove()`, para habilitar la eliminación de tablas. El documento proporciona dos fragmentos de código uno que muestra cómo eliminar una sola tabla de un PDF, y otro que ilustra la eliminación de múltiples tablas. Estos ejemplos destacan la aplicación práctica de la clase `TableAbsorber` para lograr la eliminación de tablas de documentos PDF.
---

## Eliminar tabla de un documento PDF

Aspose.PDF para Python le permite eliminar una tabla de un PDF. Abre un PDF existente, detecta la primera tabla en la primera página con TableAbsorber, elimina esa tabla usando el [remove_one_table](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods). Después, guarde el PDF actualizado en un nuevo archivo.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(path_outfile)
```

## Eliminar todas las tablas de un documento PDF

Con nuestra biblioteca, puede eliminar todas las tablas de una página específica en un PDF. El código abre un PDF existente, detecta todas las tablas en la segunda página con TableAbsorber, recorre las tablas detectadas, elimina cada una y luego guarda el PDF modificado en un nuevo archivo. Es útil cuando necesita eliminar en bloque tablas de una página mientras mantiene el resto del contenido del PDF intacto.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit second page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(path_outfile)
```


