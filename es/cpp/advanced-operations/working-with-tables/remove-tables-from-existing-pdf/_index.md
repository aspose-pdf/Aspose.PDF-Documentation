---
title: Eliminar Tablas de un PDF existente
linktitle: Eliminar Tablas
type: docs
weight: 50
url: /es/cpp/remove-tables-from-existing-pdf/
description: Esta sección describe cómo eliminar una Tabla de un documento PDF.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF para C++ le permite insertar y crear una Tabla dentro de un documento PDF mientras se genera desde cero o también puede agregar el objeto de la tabla en cualquier documento PDF existente. Pero puede tener un requisito para [Manipular Tablas en PDF existente](https://docs.aspose.com/pdf/cpp/manipulate-tables-in-existing-pdf/) donde puede actualizar el contenido de las celdas de la tabla existente. Además, puede encontrarse con un requisito para eliminar objetos de tabla de los documentos PDF existentes.

Para eliminar las tablas, necesitamos usar la clase [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) para obtener las tablas en el PDF existente y luego llamar al método 'Remove'.

## Eliminar Tabla de un documento PDF

Hemos añadido una nueva función, es decir. [Remove](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber#ace39006d8f44c9cb776ee26281a1cbb3) a la clase existente TableAbsorber para eliminar la tabla del documento PDF. Una vez que el absorbedor encuentra tablas en la página con éxito, se vuelve capaz de eliminarlas. Por favor, revise el siguiente fragmento de código que muestra cómo eliminar una tabla de un documento PDF:

>Headers:

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
```

>Samples:

```cpp
using namespace System;
using namespace Aspose::Pdf;

void RemoveTable() {

    String _dataDir("C:\\Samples\\");

    // Cargar documento PDF de origen
    auto document = MakeObject<Document>(_dataDir + u"Table_input.pdf");

    // Crear objeto TableAbsorber para encontrar tablas
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visitar la primera página con el absorbedor
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Obtener la primera tabla en la página
    auto table = absorber->get_TableList()->idx_get(0);

    // Eliminar la tabla
    absorber->Remove(table);

    // Guardar PDF
    document->Save(_dataDir + u"Table_out.pdf");
}
```
## Eliminar Múltiples Tablas de un Documento PDF

Algunas tareas estarán asociadas con trabajar con varias tablas en un documento pdf.
Y necesitarás eliminar varias tablas de él. Para eliminar múltiples tablas de un documento PDF, utiliza el siguiente fragmento de código:

```cpp
void RemoveMultipleTables() {

    String _dataDir("C:\\Samples\\");

    // Cargar documento PDF existente
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // Crear objeto TableAbsorber para encontrar tablas
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visitar primera página con el absorbente
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Obtener copia de la colección de tablas
    auto tables = absorber->get_TableList();


    // Recorrer la copia de la colección y eliminar tablas
    for(auto table : tables)
    absorber->Remove(table);

    // Guardar documento
    document->Save(_dataDir + u"Table2_out.pdf");
}
```

{{% alert color="primary" %}}

Ten en cuenta que eliminar o reemplazar una tabla cambia la colección TableList. Therefore, en caso de eliminar/reemplazar tablas en un bucle, la copia de la colección TableList es esencial.

{{% /alert %}}