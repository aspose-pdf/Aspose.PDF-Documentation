---
title: Crear o Agregar Tabla en PDF 
linktitle: Crear o Agregar Tabla
type: docs
weight: 10
url: /cpp/add-table-in-existing-pdf-document/
description: Aspose.PDF para C++ es una biblioteca utilizada para crear, leer y editar tablas en PDF. Usando esta biblioteca, puedes paginar una tabla en la página PDF usando C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Creación de Tabla usando C++

Las tablas son importantes cuando se trabaja con documentos PDF. Ofrecen excelentes características para mostrar información de manera sistemática.

Las tablas en un documento PDF organizan datos en filas y columnas de manera sistemática. La API Aspose.PDF para C++ te permite agregar tablas a un documento PDF, y agregar filas y columnas a ellas en tus aplicaciones C++. La clase [Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table/) se utiliza para agregar una tabla al documento. Los siguientes pasos se pueden seguir para agregar una tabla a un documento PDF usando C++.

### Agregar Tabla en Documento PDF Existente

Para agregar una tabla a un archivo PDF existente con Aspose.PDF para C++, toma los siguientes pasos:

1. Cargar el archivo fuente.
1. Inicializar una tabla y establecer sus columnas y filas.
1. Configurar el ajuste de la tabla (hemos configurado los bordes).
1. Rellenar la tabla.
1. Añadir la tabla a una página.
1. Guardar el archivo.

Los siguientes fragmentos de código muestran cómo añadir texto en un archivo PDF existente.

>Encabezados

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
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderCornerStyle.h>
#include <Aspose.PDF.Cpp/Generator/ColumnAdjustment.h>
#include <Aspose.PDF.Cpp/Generator/ImageFileType.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/HtmlFragment.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
```

>Sample

```cpp
using namespace System;
using namespace Aspose::Pdf;

void AddingTableInExistingPDFDocument() {
    
    String _dataDir("C:\\Samples\\");
    
    // Cargar documento PDF de origen
    auto document = MakeObject<Document>(_dataDir + u"AddTable.pdf");
    
    // Inicializa una nueva instancia de la Tabla
    auto table = MakeObject<Table>();
    
    // Establecer el color del borde de la tabla como LightGray
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));
    // Establecer el borde para las celdas de la tabla
    table->set_DefaultCellBorder (MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));

    // Crear un bucle para agregar 10 filas
    for (int row_count = 1; row_count < 10; row_count++)
    {
        // Agregar fila a la tabla
        auto row = table->get_Rows()->Add();
        // Agregar celdas a la tabla
        row->get_Cells()->Add(String::Format(u"Columna ({0}, 1)", row_count));
        row->get_Cells()->Add(String::Format(u"Columna ({0}, 2)", row_count));
        row->get_Cells()->Add(String::Format(u"Columna ({0}, 3)", row_count));
    }

    // Agregar objeto tabla a la primera página del documento de entrada
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    
    // Guardar documento actualizado que contiene el objeto tabla
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

### ColSpan y RowSpan en Tablas

Aspose.PDF para C++ presenta una propiedad [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) para fusionar las columnas en una tabla y una propiedad [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) para fusionar las filas.

Usamos la propiedad [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) o [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) en el objeto [Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell) que crea la celda de la tabla. Después de aplicar las propiedades requeridas, la celda creada puede ser añadida a la tabla.

```cpp
void AddTable_RowColSpan()
{
    String _dataDir("C:\\Samples\\");

    // Cargar documento PDF de origen
    auto document = MakeObject<Document>();
    document->get_Pages()->Add();

    // Inicializa una nueva instancia de la Tabla
    auto table = MakeObject<Table>();
    // Establecer el color del borde de la tabla como LightGray
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Color::get_Black()));
        // Establecer el borde para las celdas de la tabla
    table->set_DefaultCellBorder(
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, .5f, 
            Color::get_Black()));
    

    // Añadir 1ª fila a la tabla
    auto row1 = table->get_Rows()->Add();
    for (int cellCount = 1; cellCount < 5; cellCount++)
    {
        // Añadir celdas a la tabla
        row1->get_Cells()->Add(String::Format(u"Test 1 {0}", cellCount));
    }

    // Añadir 2ª fila a la tabla
    auto row2 = table->get_Rows()->Add();
    row2->get_Cells()->Add(u"Test 2 1");
    auto cell = row2->get_Cells()->Add(u"Test 2 2");
    cell->set_ColSpan(2);
    row2->get_Cells()->Add(u"Test 2 4");

    // Añadir 3ª fila a la tabla
    auto row3 = table->get_Rows()->Add();
    row3->get_Cells()->Add(u"Test 3 1");
    row3->get_Cells()->Add(u"Test 3 2");
    row3->get_Cells()->Add(u"Test 3 3");
    row3->get_Cells()->Add(u"Test 3 4");

    // Añadir 4ª fila a la tabla
    auto row4 = table->get_Rows()->Add();
    row4->get_Cells()->Add(u"Test 4 1");
    cell = row4->get_Cells()->Add(u"Test 4 2");
    cell->set_RowSpan (2);
    row4->get_Cells()->Add(u"Test 4 3");
    row4->get_Cells()->Add(u"Test 4 4");


    // Añadir 5ª fila a la tabla
    auto row5 = table->get_Rows()->Add();
    row5->get_Cells()->Add(u"Test 5 1");
    row5->get_Cells()->Add(u"Test 5 3");
    row5->get_Cells()->Add(u"Test 5 4");

    // Añadir objeto de tabla a la primera página del documento de entrada
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);

    // Guardar documento actualizado que contiene el objeto de tabla
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

El resultado del código de ejecución a continuación es la tabla representada en la siguiente imagen:

![Demostración de ColSpan y RowSpan](colspan_rowspan.png)

## Trabajando con Bordes, Márgenes y Relleno

Tenga en cuenta que también admite la función de establecer el borde, los márgenes y el relleno de las celdas para las tablas. Primero, comprendamos el concepto de bordes, márgenes y relleno, que se presenta en el diagrama a continuación:

![Bordes, márgenes y relleno](set-border-style-margins-and-padding-of-table_1.png)

Revise el dibujo en detalle. Muestra que los bordes de la tabla, filas y celdas se superponen. Usando Aspose.PDF para C++, la tabla puede tener márgenes y las celdas pueden tener sangría. Para establecer los márgenes de las celdas, debemos establecer el relleno de las celdas.

## Bordes

Para establecer los bordes de los objetos de [Tabla](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.row), [Fila](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.row) y [Celda](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell), use las propiedades Table.Border, Row.Border y Cell.Border. Los bordes de las celdas también pueden establecerse utilizando la propiedad DefaultCellBorder de la clase [Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) o Row. Todas las propiedades relacionadas con los bordes discutidas anteriormente se asignan a una instancia de la clase Row, que se crea llamando a su constructor. La clase Row tiene muchas sobrecargas que toman casi todos los parámetros necesarios para personalizar el borde.

## Márgenes o Relleno

El relleno de las celdas puede gestionarse utilizando la propiedad [DefaultCellPadding](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#ac64196de6dfed7550c3278892ed9dbe0) de la clase Table. Todas las propiedades relacionadas con el relleno se asignan a una instancia de la clase [MarginInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.margin_info/) que toma información sobre los parámetros `Left`, `Right`, `Top` y `Bottom` para crear márgenes personalizados.

![Margin and Border in PDF Table](margin-border.png)

```cpp
void AddTable_MergingPadding() {

    String _dataDir("C:\\Samples\\");

    // Instntiate the Document object by calling its empty constructor
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Instantiate a table object
    auto tab1 = MakeObject<Table>();
    // Add the table in paragraphs collection of the desired section
    page->get_Paragraphs()->Add(tab1);
    // Set with column widths of the table
    tab1->set_ColumnWidths (u"50 50 50");
    // Set default cell border using BorderInfo object
    tab1->set_DefaultCellBorder (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 0.1F));
    // Set table border using another customized BorderInfo object
    tab1->set_Border (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 1.0F));

    // Create MarginInfo object and set its left, bottom, right and top margins
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top (5.0f);
    margin->set_Left (5.0f);
    margin->set_Right (5.0f);
    margin->set_Bottom (5.0f);

    // Set the default cell padding to the MarginInfo object
    tab1->set_DefaultCellPadding (margin);
    // Create rows in the table and then cells in the rows
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add();

    auto mytext = MakeObject<Aspose::Pdf::Text::TextFragment>(u"col3 with large text string");
        
    row1->get_Cells()->idx_get(2)->get_Paragraphs()->Add(mytext);
    row1->get_Cells()->idx_get(2)->set_IsWordWrapped(false);
    

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // Save the Pdf
    document->Save(_dataDir + u"MarginsOrPadding_out.pdf");
}
```
Para crear una tabla con esquinas redondeadas, use la clase [BorderInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info) valor [RoundedBorderRadius](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info#a6a2bed69dd034fba9ce439dcbe1fd3de) y establezca el estilo de las esquinas de la tabla como redondeadas.

```cpp
void AddTable_RoundedBorderRadius()
{
    // La ruta al directorio de documentos.
    String _dataDir("C:\\Samples\\");

    auto tab1 = MakeObject<Aspose::Pdf::Table>();

    auto graph = MakeObject<GraphInfo>();
    graph->set_Color(Color::get_Red());
    // Crear un objeto BorderInfo en blanco
    auto bInfo = MakeObject<BorderInfo>(BorderSide::All, graph);

    // Establecer el borde como un borde redondeado donde el radio del redondeo es 15
    bInfo->set_RoundedBorderRadius(15);
    // Establecer el estilo de las esquinas de la tabla como redondeado.
    tab1->set_CornerStyle (Aspose::Pdf::BorderCornerStyle::Round);
    // Establecer la información del borde de la tabla
    tab1->set_Border(bInfo);
}
```

### Propiedad AutoFitToWindow en la enumeración ColumnAdjustmentType

```cpp
void AddTable_AutoFitToWindow() {
    
    // La ruta al directorio de documentos.
    String _dataDir("C:\\Samples\\");

    // Instanciar el objeto Pdf llamando a su constructor vacío
    auto document = MakeObject<Document>();

    // Crear la sección en el objeto Pdf
    auto sec1 = document->get_Pages()->Add();

    // Instanciar un objeto tabla
    auto tab1 = MakeObject<Aspose::Pdf::Table>();
    // Agregar la tabla en la colección de párrafos de la sección deseada
    sec1->get_Paragraphs()->Add(tab1);

    // Establecer los anchos de columna de la tabla
    tab1->set_ColumnWidths (u"50 50 50");
    tab1->set_ColumnAdjustment (ColumnAdjustment::AutoFitToWindow);

    // Establecer el borde de celda predeterminado usando el objeto BorderInfo
    tab1->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 0.1F));

    // Establecer el borde de la tabla usando otro objeto BorderInfo personalizado
    tab1->set_Border (MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 1.0F));

    // Crear objeto MarginInfo y establecer sus márgenes izquierdo, inferior, derecho y superior
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top(5.0f);
    margin->set_Left(5.0f);
    margin->set_Right(5.0f);
    margin->set_Bottom(5.0f);

    // Establecer el relleno de celda predeterminado al objeto MarginInfo
    tab1->set_DefaultCellPadding(margin);

    // Crear filas en la tabla y luego celdas en las filas
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // Guardar el documento actualizado que contiene el objeto tabla
    document->Save(_dataDir + u"AutoFitToWindow_out.pdf");
}
```

### Obtener el Ancho de la Tabla

Hay tareas en las que necesitas obtener dinámicamente el ancho de la tabla. La clase [Aspose.PDF.Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) tiene un método [GetWidth] para este propósito (https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#a3361cc8d4af87eec2e3da616c474ac1c). Por ejemplo, no has establecido explícitamente el ancho de las columnas de la tabla, y no has configurado [ColumnAdjustment] (https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#afc01382935026dd569c96d77d09dc3a4) en AutoFitToContent. En este caso, puedes obtener el siguiente ancho de la tabla.

```cpp
void GetTableWidth() {
    // Crear un nuevo documento
    auto document = MakeObject<Document>();
    
    // Agregar página en el documento
    auto page = document->get_Pages()->Add();

    // Inicializar nueva tabla
    auto table = MakeObject<Table>();
    table->set_ColumnAdjustment(ColumnAdjustment::AutoFitToContent);
    
    // Agregar fila en la tabla
    auto row = table->get_Rows()->Add();

    // Agregar celda en la tabla
    auto cell = row->get_Cells()->Add(u"Texto de Celda 1");
    cell = row->get_Cells()->Add(u"Texto de Celda 2");
    // Obtener el ancho de la tabla
    Console::WriteLine(table->GetWidth());
}
```

## Agregar Imagen SVG a la Celda de la Tabla

Aspose.PDF para C++ te permite agregar celdas de tabla a un archivo PDF. Cuando creas una tabla, puedes agregar texto o imágenes a las celdas. Además, la API también ofrece una función para convertir archivos SVG a PDF. Usando una combinación de estas funciones, es posible cargar una imagen SVG y añadirla a una celda de la tabla.

El siguiente fragmento de código muestra los pasos para crear una tabla e insertar una imagen SVG en una celda de la tabla.

```cpp
void InsertSVGObject() 
{
    String _dataDir("C:\\Samples\\");

    // Instanciar objeto Documento
    auto document = MakeObject<Document>();
    // Crear una instancia de imagen
    auto img = MakeObject<Aspose::Pdf::Image>();

    // Establecer el tipo de imagen como SVG
    img->set_FileType(Aspose::Pdf::ImageFileType::Svg);
    // Ruta para el archivo fuente
    img->set_File (_dataDir + u"SVGToPDF.svg");
    // Establecer ancho para la instancia de imagen
    img->set_FixWidth (50);
    // Establecer altura para la instancia de imagen
    img->set_FixHeight(50);
    // Crear instancia de tabla
    auto table = MakeObject<Aspose::Pdf::Table>();
    // Establecer ancho para las celdas de la tabla
    table->set_ColumnWidths (u"100 100");
    // Crear objeto fila y añadirlo a la instancia de tabla
    auto row = table->get_Rows()->Add();
    // Crear objeto celda y añadirlo a la instancia de fila
    auto cell = row->get_Cells()->Add();
    // Añadir fragmento de texto a la colección de párrafos del objeto celda
    cell->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"First cell"));
    // Añadir otra celda al objeto fila
    cell = row->get_Cells()->Add();
    // Añadir imagen SVG a la colección de párrafos de la instancia de celda recientemente añadida
    cell->get_Paragraphs()->Add(img);
    // Crear objeto página y añadirlo a la colección de páginas de la instancia de documento
    auto page = document->get_Pages()->Add();
    // Añadir tabla a la colección de párrafos del objeto página
    page->get_Paragraphs()->Add(table);    
    // Guardar archivo PDF
    document->Save(_dataDir + u"AddSVGObject_out.pdf");
}
```

## Usando Etiquetas HTML dentro de una Tabla

Para algunas tareas, necesitarás importar el contenido de la base de datos con algunas etiquetas HTML y luego importar el contenido en un objeto Tabla. Al importar contenido, las etiquetas HTML deben mostrarse dentro del documento PDF.

En el siguiente fragmento de código, puedes establecer el color del borde de la tabla, establecer el borde para las celdas de la tabla. Después, crearás un bucle para agregar 10 filas. Agrega el objeto tabla a la primera página del documento de entrada y guarda el documento actualizado.

```cpp
void AddHTMLFragmentToTableCell() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");    
    // Inicializa una nueva instancia de la Tabla
    auto table = MakeObject<Table>();
    // Establece el color del borde de la tabla como LightGray
    table->set_Border(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // establece el borde para las celdas de la tabla
    table->set_DefaultCellBorder(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // crea un bucle para agregar 10 filas       
    for (int row_count = 1; row_count < 10; row_count++) {
        SmartPtr<Cell> cell;
        // agrega fila a la tabla
        auto row = table->get_Rows()->Add();
        // agrega celdas de la tabla
        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Columna <strong>({0}, 1)</strong>", row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Columna <span style='color:red'>({0}, 2)</span>",row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Columna <span style='text-decoration: underline'>([0}, 3)</span>", row_count)));
    }
    // Agrega el objeto tabla a la primera página del documento de entrada
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    // Guarda el documento actualizado que contiene el objeto tabla
    document->Save(_dataDir + u"AddHTMLObject_out.pdf");
}
```

## Insertar un salto de página entre filas de la tabla

Normalmente, al crear una tabla dentro de un PDF, la tabla fluye a las páginas siguientes cuando alcanza el margen inferior de la tabla. Pero podemos tener un requisito para forzar la inserción de un salto de página cuando se agregan un cierto número de filas a la tabla. El siguiente fragmento de código muestra los pasos para insertar un salto de página mientras se agregan 10 filas a una tabla.

El siguiente fragmento de código muestra los pasos para insertar un salto de página cuando se agregan 10 filas a la tabla.

```cpp
void InsertPageBreak() {
    String _dataDir("C:\\Samples\\");

    // Instanciar una instancia de Document
    auto document = MakeObject<Document>();
    
    // Agregar página a la colección de páginas del archivo PDF
    auto page = document->get_Pages()->Add();

    // Crear una instancia de tabla
    auto tab = MakeObject<Table>();

    // Establecer el estilo de borde para la tabla
    tab->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // Establecer el estilo de borde predeterminado para la tabla con el color de borde como rojo
    tab->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // Especificar el ancho de las columnas de la tabla
    tab->set_ColumnWidths(u"100 100");

    // Crear un bucle para agregar 200 filas a la tabla
    for (int counter = 0; counter <= 200; counter++) {
        auto row = MakeObject<Row>();
        tab->get_Rows()->Add(row);
        auto cell1 = MakeObject<Cell>();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 0", counter)));
        row->get_Cells()->Add(cell1);

        auto cell2 = new Cell();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Cell {0}, 1", counter)));
        row->get_Cells()->Add(cell2);
        // Cuando se agregan 10 filas, renderizar nueva fila en nueva página
        if (counter % 10 == 0 && counter != 0)
            row->set_IsInNewPage(true);
    }
    // Agregar la tabla a la colección de párrafos del archivo PDF
    page->get_Paragraphs()->Add(tab);

    // Guardar el documento PDF
    document->Save(_dataDir + u"InsertPageBreak_out.pdf");
}
```

## Renderizar una Tabla en una Nueva Página

Por defecto, los párrafos se añaden a la colección de Párrafos de un objeto Page. Sin embargo, es posible renderizar una tabla en una nueva página en lugar de directamente después del objeto de nivel de párrafo previamente añadido en la página.

### Ejemplo: Cómo Renderizar una Tabla en una Nueva Página usando C++

Para renderizar una tabla en una nueva página, use la propiedad [IsInNewPage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph#a614946048d22afb9dce4cd42346c7561) en la clase [BaseParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph).
El siguiente fragmento de código muestra cómo.

```cpp
void RenderTableOnNewPage()
{
    auto document = MakeObject<Document>();
    auto pageInfo = document->get_PageInfo();
    auto marginInfo = pageInfo->get_Margin();

    marginInfo->set_Left (37);
    marginInfo->set_Right (37);
    marginInfo->set_Top (37);
    marginInfo->set_Bottom (37);

    pageInfo->set_IsLandscape(true);

    auto table = MakeObject<Aspose::Pdf::Table>();
    table->set_ColumnWidths(u"50 100");
    // Página añadida.
    auto curPage = document->get_Pages()->Add();
    for (int i = 1; i <= 120; i++)
    {
        auto row = table->get_Rows()->Add();
        row->set_FixedRowHeight(15);
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Content 1"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"HHHHH"));
    }
    auto paragraphs = curPage->get_Paragraphs();
    paragraphs->Add(table);

    //-------------------------------------

    auto document = MakeObject<Document>();
    auto table1 = MakeObject<Aspose::Pdf::Table>();
    table1->set_ColumnWidths(u"100 100");

    String _dataDir("C:\\Samples\\");

    for (int i = 1; i <= 10; i++)
    {
        auto row = table1->get_Rows()->Add();
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAAAAAA"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAGGGGGG"));
    }
    
    table1->set_IsInNewPage (true);
    // Quiero mantener la tabla 1 en la siguiente página por favor...
    paragraphs->Add(table1);
    
    document->Save(_dataDir + u"IsNewPageProperty_Test_out.pdf");
}
```