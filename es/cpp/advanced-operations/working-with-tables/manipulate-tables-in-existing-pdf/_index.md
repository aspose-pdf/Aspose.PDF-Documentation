---
title: Manipular Tablas en un PDF existente
linktitle: Manipular Tablas
type: docs
weight: 40
url: /es/cpp/manipulate-tables-in-existing-pdf/
description: Esta sección cubre varios métodos para la modificación de tablas utilizando Aspose.PDF para C++
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Manipular tablas en un PDF existente

Aspose.PDF para C++ le permite trabajar rápida y eficientemente con tablas, a saber, crearlas desde cero o añadirlas a documentos PDF existentes.

También obtiene la capacidad de integrar la tabla con la base de datos (DOM) para crear tablas dinámicas basadas en el contenido de la base de datos.

La clase [Aspose.PDF.Text.TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) le permite buscar y analizar tablas simples que ya existen en una página de un documento PDF. El siguiente fragmento de código muestra los pasos para actualizar el contenido en una celda específica en una tabla.

>Encabezados:

```cpp
#include <system/date_time.h>
#include <system/io/file.h>
#include <system/console.h>
#include <data/data_table.h>
#include <data/data_column_collection.h>
#include <system/type_info.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedRow.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedCell.h>
```

>Samples:

```cpp
using namespace System;
using namespace Aspose::Pdf;

#include "Table-Manipulate.h"

void ManipulateTables() {

    String _dataDir("C:\\Samples\\");

    // Cargar archivo PDF existente
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Crear objeto TableAbsorber para encontrar tablas
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visitar la primera página con el absorber
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Obtener acceso a la primera tabla en la página, su primera celda y fragmentos de texto en ella
    auto fragment = absorber->get_TableList()->idx_get(0)->get_RowList()->idx_get(0)->get_CellList()->idx_get(0)->get_TextFragments()->idx_get(1);

    // Cambiar el texto del primer fragmento de texto en la celda
    fragment->set_Text(u"hola mundo");
    document->Save(_dataDir + u"ManipulateTable_out.pdf");
}
```

## Reemplazar una tabla antigua con una nueva en el documento PDF

En caso de que necesites encontrar una tabla en particular y reemplazarla por la deseada, puedes usar el método Replace() de la Clase [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) para hacerlo.

El siguiente ejemplo demuestra la funcionalidad para reemplazar la tabla dentro del documento PDF:

```cpp
void ReplaceOldTable() {
    String _dataDir("C:\\Samples\\");

    // Cargar archivo PDF existente
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // Crear objeto TableAbsorber para encontrar tablas
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visitar la primera página con el absorbedor
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Obtener la primera tabla en la página
    auto table = absorber->get_TableList()->idx_get(0);

    // Crear nueva tabla
    auto newTable = MakeObject<Table>();
    newTable->set_ColumnWidths(u"100 100 100");
    newTable->set_DefaultCellBorder (MakeObject<BorderInfo>(BorderSide::All, 1.0F));

    auto row = newTable->get_Rows()->Add();
    row->get_Cells()->Add(u"Col 1");
    row->get_Cells()->Add(u"Col 2");
    row->get_Cells()->Add(u"Col 3");

    // Reemplazar la tabla con la nueva
    absorber->Replace(document->get_Pages()->idx_get(1), table, newTable);

    // Guardar documento
    document->Save(_dataDir + u"TableReplaced_out.pdf");
}
```