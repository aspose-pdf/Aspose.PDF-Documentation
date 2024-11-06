---
title: Trabajando con Operadores usando C++
linktitle: Trabajando con Operadores
type: docs
weight: 170
url: es/cpp/operators/
description: Este tema explica cómo usar operadores con Aspose.PDF en C++. Las clases de operadores proporcionan grandes características para la manipulación de PDF.
lastmod: "2021-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introducción a los Operadores PDF y su Uso

Un operador es una palabra clave PDF que especifica alguna acción que se debe realizar, como pintar una forma gráfica en la página. Una palabra clave de operador se distingue de un objeto nombrado por la ausencia de un carácter de barra inicial (2Fh). Los operadores solo tienen sentido dentro del flujo de contenido.

Un flujo de contenido es un objeto de flujo PDF cuyos datos consisten en instrucciones que describen los elementos gráficos que se pintarán en una página. Se pueden encontrar más detalles sobre los operadores PDF en la [especificación PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Detalles de Implementación

Este tema explica cómo usar operadores con Aspose.PDF. El ejemplo seleccionado agrega una imagen a un archivo PDF para ilustrar el concepto. Para agregar una imagen en un archivo PDF, se necesitan diferentes operadores. Este ejemplo utiliza [GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save), [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix), [Do](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do) y [GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore).

- El operador **GSave** guarda el estado gráfico actual del PDF.
- El operador **ConcatenateMatrix** (concatenar matriz) se utiliza para definir cómo debe colocarse una imagen en la página del PDF.
- El operador **Do** dibuja la imagen en la página.
- El operador **GRestore** restaura el estado gráfico.

Para agregar una imagen en un archivo PDF:

1. Cree un objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) y abra el documento PDF de entrada.
1. Obtenga la página particular a la que se va a agregar la imagen.
1. Agregue la imagen a la colección de Recursos de la página.
1. Use los operadores para colocar la imagen en la página:
   - Primero, use el operador GSave para guardar el estado gráfico actual.
   - Luego use el operador ConcatenateMatrix para especificar dónde se colocará la imagen.
   - Use el operador Do para dibujar la imagen en la página.
1. Finalmente, use el operador GRestore para guardar el estado gráfico actualizado.

El siguiente fragmento de código muestra cómo usar los operadores de PDF.

```cpp
void ExampleUsingOperators()
{
    // Abre el documento
    String _dataDir("C:\\Samples\\");

    // Abre el documento
    auto document = MakeObject<Document>(_dataDir + u"PDFOperators.pdf");

    // Establecer coordenadas
    int lowerLeftX = 100;
    int lowerLeftY = 100;
    int upperRightX = 200;
    int upperRightY = 200;

    // Obtener la página donde se necesita agregar la imagen
    auto page = document->get_Pages()->idx_get(1);

    // Cargar imagen en el flujo
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"PDFOperators.jpg");
    // Agregar imagen a la colección de Imágenes de Recursos de Página
    page->get_Resources()->get_Images()->Add(imageStream);

    // Usando el operador GSave: este operador guarda el estado gráfico actual
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Crear objetos de Rectángulo y Matriz
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
    auto matrix = MakeObject<Matrix>(
        new double[] {
            rectangle->get_URX() - rectangle->get_LLX(), 0, 0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(),  rectangle->get_LLY() });
    // Usando el operador ConcatenateMatrix (concatenar matriz): define cómo se debe colocar la imagen
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());
    // Usando el operador Do: este operador dibuja la imagen
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    // Usando el operador GRestore: este operador restaura el estado gráfico
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());


    // Guardar documento actualizado
    document->Save(_dataDir + u"PDFOperators_out.pdf");
}
```
## Dibujar XForm en la Página usando Operadores

Este tema demuestra cómo usar los operadores GSave/GRestore, el operador ConcatenateMatrix para posicionar un xForm y el operador Do para dibujar un xForm en una página.

El código a continuación envuelve los contenidos existentes de un archivo PDF con el par de operadores GSave/GRestore. Este enfoque ayuda a obtener el estado gráfico inicial al final de los contenidos existentes. Sin este enfoque, podrían permanecer transformaciones no deseadas al final de la cadena de operadores existente.

```cpp
void DrawXFormOnPageUsingOperators() {
    // Abrir documento
    String _dataDir("C:\\Samples\\");

    String imageFile(_dataDir + u"aspose-logo.jpg");
    String inFile(_dataDir + u"DrawXFormOnPage.pdf");
    String outFile(_dataDir + u"blank-sample2_out.pdf");

    auto document = MakeObject<Document>(inFile);
    auto pageContents = document->get_Pages()->idx_get(1)->get_Contents();

    // La muestra demuestra
    // Uso de operadores GSave/GRestore
    // Uso del operador ConcatenateMatrix para posicionar xForm
    // Uso del operador Do para dibujar xForm en la página

    // Envolver contenidos existentes con el par de operadores GSave/GRestore
    // esto es para obtener el estado gráfico inicial al final de los contenidos existentes
    // de lo contrario, podrían permanecer algunas transformaciones no deseadas al final de la cadena de operadores existente
    pageContents->Insert(1, MakeObject<Aspose::Pdf::Operators::GSave>());
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Agregar operador de guardar estado gráfico para limpiar adecuadamente el estado gráfico después de nuevos comandos
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // Crear xForm

    auto form = XForm::CreateNewForm(document->get_Pages()->idx_get(1), document);
    document->get_Pages()->idx_get(1)->get_Resources()->get_Forms()->Add(form);
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Definir ancho y alto de la imagen
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(200, 0, 0, 200, 0, 0));
    // Cargar imagen en el flujo
    auto imageStream = System::IO::File::OpenRead(imageFile);
    // Agregar imagen a la colección de Imágenes de los Recursos de XForm
    form->get_Resources()->get_Images()->Add(imageStream);
    auto ximage = form->get_Resources()->get_Images()->idx_get(form->get_Resources()->get_Images()->get_Count());
    // Usando el operador Do: este operador dibuja la imagen
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // ----------------------------------------------------

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Colocar formulario en las coordenadas x=100 y=500
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 500));
    // Dibujar formulario con el operador Do
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Colocar formulario en las coordenadas x=100 y=300
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 300));
    // Dibujar formulario con el operador Do
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Restaurar estado gráfico con GRestore después de GSave
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
    document->Save(outFile);
}
```

## Eliminar Objetos Gráficos usando Clases de Operadores

Las clases de operadores proporcionan grandes características para la manipulación de PDF. Cuando un archivo PDF contiene gráficos que no se pueden eliminar utilizando el método [DeleteImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor#af7d23ef932737bf606f008ad5ec48380) de la clase [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor), se pueden usar las clases de operadores para eliminarlos.

El siguiente fragmento de código muestra cómo eliminar gráficos. Tenga en cuenta que si el archivo PDF contiene etiquetas de texto para los gráficos, podrían persistir en el archivo PDF, utilizando este enfoque. Por lo tanto, busque los operadores gráficos para un método alternativo para eliminar dichas imágenes.

```cpp
void RemoveGraphicsObjects() {
    // Abrir documento
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"RemoveGraphicsObjects.pdf");

    auto page = document->get_Pages()->idx_get(2);
    auto oc = page->get_Contents();

    // Operadores de pintura de ruta usados
    auto operators = MakeArray<System::SmartPtr<Operator>>({
            MakeObject<Aspose::Pdf::Operators::Stroke>(),
            MakeObject<Aspose::Pdf::Operators::ClosePathStroke>(),
            MakeObject<Aspose::Pdf::Operators::Fill>()
    });

    oc->Delete(operators);
    document->Save(_dataDir + u"No_Graphics_out.pdf");
}
```