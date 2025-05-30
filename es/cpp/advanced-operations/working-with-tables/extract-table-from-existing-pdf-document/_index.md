---
title: Extraer Tabla de PDF
linktitle: Extraer Tabla
type: docs
weight: 20
url: /es/cpp/extract-table-from-existing-pdf-document/
description: Aspose.PDF para C++ hace posible llevar a cabo varias manipulaciones con las tablas contenidas en su documento pdf. Puede agregar y extraer una tabla en el documento PDF existente, renderizar la tabla en una nueva página, etc.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer Tabla de PDF

Puede parecer que es bastante difícil extraer cualquier dato de un documento PDF. Sin embargo, la biblioteca **Aspose.PDF para C++** le permite manejar esta tarea. Extraiga tablas de su archivo pdf con C++:

>Encabezado:

```cpp
#include <system/console.h>
#include <system/collections/stack.h>
#include <system/io/memory_stream.h>

#include <drawing/imaging/image_format.h>
#include <drawing/bitmap.h>
#include <drawing/graphics.h>
#include <drawing/solid_brush.h>
#include <drawing/drawing2d/matrix.h>
#include <drawing/drawing2d/graphics_path.h>
#include <drawing/drawing2d/smoothing_mode.h>
#include <system/console.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>

#include <Aspose.PDF.Cpp/Operator.h>
#include <Aspose.PDF.Cpp/OperatorCollection.h>

#include <Aspose.PDF.Cpp/DOM/Matrix.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextSegment.h>
#include <Aspose.PDF.Cpp/Text/TextSegmentCollection.h>

#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedRow.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedCell.h>
```

```cpp
using namespace System;
using namespace System::Collections::Generic;

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void Extract_Table()
{
    String _dataDir("C:\\Samples\\");
    // Cargar documento PDF de origen    
    auto document = MakeObject<Document>(_dataDir + u"the_worlds_cities_in_2018_data_booklet 7.pdf");
    for (auto page : document->get_Pages())
    {
        auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();
        absorber->Visit(page);
        for (auto table : absorber->get_TableList())
        {
            for (auto row : table->get_RowList())
            {
                for (auto cell : row->get_CellList())
                {
                    auto textfragment = MakeObject<TextFragment>();
                    auto textFragmentCollection = cell->get_TextFragments();
                    for (auto fragment : textFragmentCollection)
                    {
                        String txt;
                        for (auto seg : fragment->get_Segments())
                        {
                            txt += seg->get_Text();
                        }
                        Console::WriteLine(txt);
                    }
                }
            }
        }
    }
}
```

## Extraer el borde de la tabla como Imagen

El siguiente fragmento de código muestra los pasos para extraer el borde de la tabla como una Imagen de un documento PDF:

```cpp
void ExtractTableBorderAsImage()
{
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"input.pdf");
    auto graphicsState = MakeObject<System::Collections::Generic::Stack<System::SmartPtr<object>>>();

    auto bitmap = MakeObject<System::Drawing::Bitmap>(
        (int)document->get_Pages()->idx_get(1)->get_PageInfo()->get_Width(),
        (int)document->get_Pages()->idx_get(1)->get_PageInfo()->get_Height());
    auto graphicsPath = MakeObject<System::Drawing::Drawing2D::GraphicsPath>();
    // El valor de la matriz ctm predeterminada es 1,0,0,1,0,0
    auto lastCTM = MakeObject<System::Drawing::Drawing2D::Matrix>(1, 0, 0, -1, 0, 0);
    // El sistema de coordenadas de System.Drawing se basa en la parte superior izquierda, mientras que el sistema de coordenadas pdf se basa en la parte inferior izquierda, por lo que debemos aplicar la matriz de inversión
    auto inversionMatrix = MakeObject<System::Drawing::Drawing2D::Matrix>(
        1, 0, 0, -1, 0,
        (float)document->get_Pages()->idx_get(1)->get_PageInfo()->get_Height());

    auto lastPoint = MakeObject< System::Drawing::PointF>(0, 0);
    System::Drawing::Color fillColor = System::Drawing::Color::FromArgb(0, 0, 0);
    System::Drawing::Color strokeColor = System::Drawing::Color::FromArgb(0, 0, 0);

    auto gr = System::Drawing::Graphics::FromImage(bitmap);
    gr->set_SmoothingMode(System::Drawing::Drawing2D::SmoothingMode::HighQuality);
    graphicsState->Push(MakeObject<System::Drawing::Drawing2D::Matrix>(1, 0, 0, 1, 0, 0));

    // Procesar todos los comandos de contenido
    for (auto op : document->get_Pages()->idx_get(1)->get_Contents())
    {
        auto opSaveState = System::DynamicCast<Aspose::Pdf::Operators::GSave>(op);
        auto opRestoreState = System::DynamicCast<Aspose::Pdf::Operators::GRestore>(op);
        auto opCtm = System::DynamicCast<Aspose::Pdf::Operators::ConcatenateMatrix>(op);
        auto opMoveTo = System::DynamicCast<Aspose::Pdf::Operators::MoveTo>(op);
        auto opLineTo = System::DynamicCast<Aspose::Pdf::Operators::LineTo>(op);
        auto opRe = System::DynamicCast<Aspose::Pdf::Operators::Re>(op);
        auto opEndPath = System::DynamicCast<Aspose::Pdf::Operators::EndPath>(op);
        auto opStroke = System::DynamicCast< Aspose::Pdf::Operators::Stroke>(op);
        auto opFill = System::DynamicCast<Aspose::Pdf::Operators::Fill>(op);
        auto opEOFill = System::DynamicCast< Aspose::Pdf::Operators::EOFill>(op);
        auto opRGBFillColor = System::DynamicCast<Aspose::Pdf::Operators::SetRGBColor>(op);
        auto opRGBStrokeColor = System::DynamicCast<Aspose::Pdf::Operators::SetRGBColorStroke>(op);

        if (opSaveState != nullptr)
        {
            // Guardar el estado anterior y empujar el estado actual a la cima de la pila
            graphicsState->Push(System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Clone());
            lastCTM = System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek());
        }
        else if (opRestoreState != nullptr)
        {
            // Descartar el estado actual y restaurar el anterior
            graphicsState->Pop();
            lastCTM = System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek());
        }
        else if (opCtm != nullptr)
        {
            auto cm = MakeObject<System::Drawing::Drawing2D::Matrix>(
                (float)opCtm->get_Matrix()->get_A(),
                (float)opCtm->get_Matrix()->get_B(),
                (float)opCtm->get_Matrix()->get_C(),
                (float)opCtm->get_Matrix()->get_D(),
                (float)opCtm->get_Matrix()->get_E(),
                (float)opCtm->get_Matrix()->get_F());

            // Multiplicar la matriz actual con la matriz de estado
            System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Multiply(cm);
            lastCTM = System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek());
        }
        else if (opMoveTo != nullptr)
        {
            lastPoint = MakeObject<System::Drawing::PointF>((float)opMoveTo->get_X(), (float)opMoveTo->get_Y());
        }
        else if (opLineTo != nullptr)
        {
            auto linePoint = MakeObject<System::Drawing::PointF>((float)opLineTo->get_X(), (float)opLineTo->get_Y());
            graphicsPath->AddLine(
                linePoint->get_X(), 
                linePoint->get_Y(), 
                lastPoint->get_X(), 
                lastPoint->get_Y());

            lastPoint = linePoint;
        }
        else if (opRe != nullptr)
        {
            auto re = MakeObject<System::Drawing::RectangleF>(
                (float)opRe->get_X(), 
                (float)opRe->get_Y(), 
                (float)opRe->get_Width(), 
                (float)opRe->get_Height());
            graphicsPath->AddRectangle(*re);
        }
        else if (opEndPath != nullptr)
        {
            graphicsPath = MakeObject<System::Drawing::Drawing2D::GraphicsPath>();
        }
        else if (opRGBFillColor != nullptr)
        {
            fillColor = opRGBFillColor->getColor();
        }
        else if (opRGBStrokeColor != nullptr)
        {
            strokeColor = opRGBStrokeColor->getColor();
        }
        else if (opStroke != nullptr)
        {
            graphicsPath->Transform(lastCTM);
            graphicsPath->Transform(inversionMatrix);
            gr->DrawPath(MakeObject<System::Drawing::Pen>(strokeColor), graphicsPath);
            graphicsPath = MakeObject<System::Drawing::Drawing2D::GraphicsPath>();
        }
        else if (opFill != nullptr)
        {
            graphicsPath->set_FillMode(System::Drawing::Drawing2D::FillMode::Winding);
            graphicsPath->Transform(lastCTM);
            graphicsPath->Transform(inversionMatrix);
            gr->FillPath(MakeObject<System::Drawing::SolidBrush>(fillColor), graphicsPath);
            graphicsPath = MakeObject<System::Drawing::Drawing2D::GraphicsPath>();
        }
        else if (opEOFill != nullptr)
        {
            graphicsPath->set_FillMode(System::Drawing::Drawing2D::FillMode::Alternate);
            graphicsPath->Transform(lastCTM);
            graphicsPath->Transform(inversionMatrix);
            gr->FillPath(MakeObject<System::Drawing::SolidBrush>(fillColor), graphicsPath);
            graphicsPath = MakeObject<System::Drawing::Drawing2D::GraphicsPath>();
        }
    }

    bitmap->Save(_dataDir + u"ExtractBorder_out.png", System::Drawing::Imaging::ImageFormat::get_Png());
}
```