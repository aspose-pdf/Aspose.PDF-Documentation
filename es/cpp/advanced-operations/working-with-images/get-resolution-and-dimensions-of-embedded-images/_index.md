---
title: Obtener Resolución y Dimensiones de Imágenes Incrustadas usando C++
linktitle: Obtener Resolución y Dimensiones
type: docs
weight: 40
url: /es/cpp/get-resolution-and-dimensions-of-embedded-images/
description: Esta sección muestra detalles sobre cómo obtener la resolución y dimensiones de Imágenes Incrustadas
lastmod: "2021-12-18"
---

Este tema explica cómo utilizar las clases de operador en el espacio de nombres Aspose.PDF, que proporcionan la capacidad de obtener información de resolución y dimensión sobre imágenes sin tener que extraerlas.

Hay diferentes maneras de lograr esto. Este artículo explica cómo usar un `arraylist` y [clases de colocación de imágenes](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement).

1. Primero, cargue el archivo PDF fuente (con imágenes).
1. Luego, cree un objeto ArrayList para contener los nombres de cualquier imagen en el documento.
1. Obtenga las imágenes usando la propiedad Page.Resources.Images.
1. Cree un objeto stack para contener el estado gráfico de la imagen y úselo para realizar un seguimiento de diferentes estados de imagen.
1. Crea un objeto ConcatenateMatrix que define la transformación actual. También admite escalar, rotar e inclinar cualquier contenido. Concatena la nueva matriz con la anterior. Tenga en cuenta que no podemos definir la transformación desde cero, sino solo modificar la transformación existente.
1. Dado que podemos modificar la matriz con ConcatenateMatrix, también podemos necesitar volver al estado original de la imagen. Use [operador GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) y [operador GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/). Estos operadores están emparejados, por lo que deben ser llamados juntos. Por ejemplo, si realiza algún trabajo gráfico con transformaciones complejas y finalmente regresa las transformaciones al estado inicial, el enfoque será algo como esto:

El siguiente fragmento de código le muestra cómo obtener las dimensiones y la resolución de una imagen sin extraer la imagen del documento PDF.

```cpp
void WorkingWithImages::GetResolutionAndDimensionsOfEmbeddedImages()
{
    String _dataDir("C:\\Samples\\");
    // Cargar el archivo PDF fuente
    auto document = MakeObject<Document>(_dataDir + u"ImageInformation.pdf");

    // Definir la resolución predeterminada para la imagen
    int defaultResolution = 72;
    auto graphicsState = MakeObject<System::Collections::Generic::Stack<System::SmartPtr<object>>>();
    // Definir objeto de lista de arreglos que contendrá los nombres de las imágenes
    auto imageNames = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->get_Names();

    // Insertar un objeto en la pila
    graphicsState->Push(System::DynamicCast<object>(MakeObject<System::Drawing::Drawing2D::Matrix>(1, 0, 0, 1, 0, 0)));

    // Obtener todos los operadores en la primera página del documento
    for (auto op : document->get_Pages()->idx_get(1)->get_Contents())
    {
        // Usar operadores GSave/GRestore para revertir las transformaciones a las previamente establecidas
        auto opSaveState = System::DynamicCast<Aspose::Pdf::Operators::GSave>(op);
        auto opRestoreState = System::DynamicCast<Aspose::Pdf::Operators::GRestore>(op);

        // Instanciar objeto ConcatenateMatrix ya que define la matriz de transformación actual.
        auto opCtm = System::DynamicCast<Aspose::Pdf::Operators::ConcatenateMatrix>(op);

        // Crear operador Do que dibuja objetos de recursos. Dibuja objetos Form e Image
        auto opDo = System::DynamicCast<Aspose::Pdf::Operators::Do>(op);

        if (opSaveState != nullptr)
        {
            // Guardar el estado anterior y empujar el estado actual a la cima de la pila
            graphicsState->Push(System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Clone());
        }
        else if (opRestoreState != nullptr)
        {
            // Desechar el estado actual y restaurar el anterior
            graphicsState->Pop();
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
            continue;
        }
        else if (opDo != nullptr)
        {
            // En caso de que este sea un operador de dibujo de imagen
            if (imageNames->Contains(opDo->get_Name()))
            {
                auto lastCTM = System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek());
                // Crear objeto XImage para contener imágenes de la primera página del pdf
                auto image = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(opDo->get_Name());

                // Obtener dimensiones de la imagen
                double scaledWidth = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(0), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(1), 2));
                double scaledHeight = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(2), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(3), 2));
                // Obtener información de altura y ancho de la imagen
                double originalWidth = image->get_Width();
                double originalHeight = image->get_Height();

                // Calcular la resolución basada en la información anterior
                double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                double resVertical = originalHeight * defaultResolution / scaledHeight;

                // Mostrar información de dimensiones y resolución de cada imagen
                Console::Write(_dataDir);
                Console::Write(u" imagen {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                    opDo->get_Name(), scaledWidth, scaledHeight, resHorizontal, resVertical);
            }
        }
    }
}
```