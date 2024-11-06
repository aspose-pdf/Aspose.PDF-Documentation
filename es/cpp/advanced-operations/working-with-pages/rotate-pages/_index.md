---
title: Rotar Páginas de PDF Usando C++
linktitle: Rotar Páginas de PDF
type: docs
weight: 50
url: es/cpp/rotate-pages/
description: Este tema describe cómo rotar la orientación de la página en un archivo PDF existente de manera programática con C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Este tema describe cómo actualizar o cambiar la orientación de las páginas en un archivo PDF existente de manera programática con C++.

## Cambiar Orientación de Página

Aspose.PDF para C++ te permite cambiar la orientación de la página de horizontal a vertical y viceversa. Para cambiar la orientación de la página, establece el MediaBox de la página usando el siguiente fragmento de código. También puedes cambiar la orientación de la página estableciendo el ángulo de rotación usando el método Rotate().

```cpp
void ChangePageOrientation() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {

        auto r = page->get_MediaBox();
        double newHeight = r->get_Width();
        double newWidth = r->get_Height();
        double newLLX = r->get_LLX();

        // Debemos mover la página hacia arriba para compensar el cambio de tamaño de la página
        // (el borde inferior de la página es 0,0 y la información generalmente se coloca desde la
        // parte superior de la página. Por eso movemos el borde inferior hacia arriba en la diferencia entre
        // la altura antigua y la nueva.

        double newLLY = r->get_LLY() + (r->get_Height() - newHeight);
        page->set_MediaBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
        // A veces también necesitamos establecer el CropBox (si estaba establecido en el archivo original)
        page->set_CropBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

        // Estableciendo el ángulo de rotación de la página
        page->set_Rotate(Rotation::on90);
    }

    // Guardar archivo de salida
    document->Save(_dataDir + outputFileName);
}
```

## Ajustar el Contenido de la Página a la Nueva Orientación de la Página

Tenga en cuenta que al usar el fragmento de código anterior, parte del contenido del documento podría cortarse porque la altura de la página se reduce. Para evitar esto, aumente el ancho proporcionalmente y deje la altura intacta. Ejemplo de cálculos:

```cpp
void FittingPageContentToNewPageOrientation()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {
        auto r = page->get_MediaBox();
        // New height the same
        double newHeight = r->get_Height();
        // New width is expanded proportionally to make orientation landscape
        // (we assume that previous orientation is portrait)
        double newWidth = r->get_Height() * r->get_Height() / r->get_Width();

        // ...

    }
}
```

Además del enfoque anterior, considere usar la fachada PdfPageEditor, que puede aplicar zoom al contenido de la página.

```cpp
void ZoomPageContent()
{

    String _dataDir("C:\\Samples\\");
    String inputFileName("ZoomToPageContents.pdf");
    String outputFileName("ZoomToPageContents_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Obtener región rectangular de la primera página del PDF
    auto rect = document->get_Pages()->idx_get(1)->get_Rect();

    // Instanciar instancia de PdfPageEditor
    auto ppe = MakeObject<Aspose::Pdf::Facades::PdfPageEditor>();
    // Vincular PDF de origen
    ppe->BindPdf(_dataDir + inputFileName);
    // Establecer coeficiente de zoom
    ppe->set_Zoom ((float)(rect->get_Width() / rect->get_Height()));
    // Actualizar tamaño de página
    ppe->set_PageSize(MakeObject<PageSize>((float)rect->get_Height(), (float)rect->get_Width()));

    // Guardar archivo de salida
    document->Save(_dataDir + outputFileName);
}
```