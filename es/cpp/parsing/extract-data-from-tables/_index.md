---
title: Extraer Datos de Tabla en PDF 
linktitle: Extraer Datos de Tabla
type: docs
weight: 40
url: es/cpp/extract-data-from-table-in-pdf/
description: Aprende cómo extraer datos tabulares de PDF usando Aspose.PDF para C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer Tablas de PDF programáticamente

Dado que PDF es el formato más común para intercambiar documentos, consideremos un documento con varios conjuntos de datos que necesitan análisis. En este artículo, describiremos la extracción de tablas de PDF.

**Aspose.PDF para C++** proporciona a los desarrolladores las herramientas que necesitan para extraer datos de tablas en documentos PDF.

Este ejemplo demuestra el uso de la clase [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) para recuperar datos tabulares de tablas en un archivo PDF.

El siguiente ejemplo muestra la extracción de tablas de todas las páginas:

```cpp
void ExtractTable() {
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // Cadena para el nombre del archivo
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    // Escanear páginas
    for (auto page : document->get_Pages()) {
        absorber->Visit(page);
        for (auto table : absorber->get_TableList()) {
        std::cout << "Table" << std::endl;
        // Iterar a través de la lista de filas
        for (auto row : table->get_RowList()) {
            // Iterar a través de la lista de celdas
            for (auto cell : row->get_CellList()) {
                String sb;
                for (auto fragment : cell->get_TextFragments()) {
                sb += fragment->get_Text();
                }
                std::cout << sb << "|";
            }
            std::cout << std::endl;
        }
        }
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extraer tabla en área específica de la página PDF

Cada tabla absorbida tiene la propiedad [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/) que describe la posición de la tabla en la página.

Por lo tanto, si necesitas extraer tablas ubicadas en una región específica, debes trabajar con coordenadas específicas.

El siguiente ejemplo muestra cómo extraer una tabla marcada con Anotación Cuadrada:

```cpp
void ExtractMarkedTable()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para el nombre de la ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para el nombre del archivo
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    auto page = document->get_Pages()->idx_get(1);
    auto sqa = MakeObject<Aspose::Pdf::Annotations::SquareAnnotation>(page, Rectangle::get_Trivial());
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(sqa);


    auto list = annotationSelector->get_Selected();
    if (list->get_Count() == 0) {
        std::cerr << "Tablas marcadas no encontradas.." << std::endl;
        return;
    }

    auto squareAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::SquareAnnotation>(list->idx_get(1));

    absorber->Visit(page);

    for (auto table : absorber->get_TableList())
    {
        auto isInRegion =
        (squareAnnotation->get_Rect()->get_LLX() < table->get_Rectangle()->get_LLX()) &&
        (squareAnnotation->get_Rect()->get_LLY() < table->get_Rectangle()->get_LLY()) &&
        (squareAnnotation->get_Rect()->get_URX() > table->get_Rectangle()->get_URX()) &&
        (squareAnnotation->get_Rect()->get_URY() > table->get_Rectangle()->get_URY());

        if (isInRegion)
        {
        for (auto row : table->get_RowList()) {
            // Iterar a través de la lista de celdas
            for (auto cell : row->get_CellList()) {
                String sb;
                for (auto fragment : cell->get_TextFragments()) {
                sb += fragment->get_Text();
                }
                std::cout << sb << "|";
            }
            std::cout << std::endl;
        }
        }
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extraer Datos de Tabla de un PDF y almacenarlos en un archivo CSV

El siguiente ejemplo muestra cómo extraer una tabla y almacenarla como un archivo CSV. Para ver cómo convertir un PDF a una hoja de cálculo de Excel, por favor consulta el artículo [Convertir PDF a Excel](/pdf/cpp/convert-pdf-to-excel/).

```cpp
void ExtractTableSaveCSV()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // Cadena para el nombre del archivo
    String infilename("sample-table.pdf");
    String outfilename("PDFToXLS_out.csv");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de opción de guardado en Excel
    auto excelSave = MakeObject<ExcelSaveOptions>();
    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::CSV);

    // Guardar la salida en formato XLS
    document->Save(_dataDir + outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```