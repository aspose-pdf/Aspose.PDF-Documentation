---
title: Get Resolution and Dimensions of Embedded Images using C++
linktitle: Get Resolution and Dimensions
type: docs
weight: 40
url: /cpp/get-resolution-and-dimensions-of-embedded-images/
description: Этот раздел показывает детали получения разрешения и размеров встроенных изображений
lastmod: "2021-12-18"
---

Эта тема объясняет, как использовать классы операторов в пространстве имен Aspose.PDF, которые предоставляют возможность получать информацию о разрешении и размерах изображений без необходимости их извлечения.

Существует несколько способов достижения этого. В этой статье объясняется, как использовать `arraylist` и [классы размещения изображений](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement).

1. Сначала загрузите исходный PDF файл (с изображениями).
1. Затем создайте объект ArrayList, чтобы удерживать имена любых изображений в документе.
1. Получите изображения, используя свойство Page.Resources.Images.
1. Создайте объект стека, чтобы удерживать графическое состояние изображения и использовать его для отслеживания различных состояний изображений.
1. Создайте объект ConcatenateMatrix, который определяет текущее преобразование. Он также поддерживает масштабирование, вращение и наклон любого содержимого. Он объединяет новую матрицу с предыдущей. Пожалуйста, обратите внимание, что мы не можем определить преобразование с нуля, а можем только изменить существующее преобразование.
1. Поскольку мы можем изменять матрицу с помощью ConcatenateMatrix, нам может понадобиться вернуться к исходному состоянию изображения. Используйте [оператор GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) и [оператор GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/). Эти операторы образуют пару, поэтому их следует вызывать вместе. Например, если вы выполняете некоторые графические работы с сложными преобразованиями и в конечном итоге возвращаете преобразования в начальное состояние, подход будет следующим:

Следующий фрагмент кода показывает, как получить размеры и разрешение изображения без извлечения изображения из PDF-документа.

```cpp
void WorkingWithImages::GetResolutionAndDimensionsOfEmbeddedImages()
{
    String _dataDir("C:\\Samples\\");
    // Загрузите исходный PDF файл
    auto document = MakeObject<Document>(_dataDir + u"ImageInformation.pdf");

    // Определите разрешение по умолчанию для изображения
    int defaultResolution = 72;
    auto graphicsState = MakeObject<System::Collections::Generic::Stack<System::SmartPtr<object>>>();
    // Определите объект списка массивов, который будет содержать имена изображений
    auto imageNames = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->get_Names();

    // Вставьте объект в стек
    graphicsState->Push(System::DynamicCast<object>(MakeObject<System::Drawing::Drawing2D::Matrix>(1, 0, 0, 1, 0, 0)));

    // Получите все операторы на первой странице документа
    for (auto op : document->get_Pages()->idx_get(1)->get_Contents())
    {
        // Используйте операторы GSave/GRestore, чтобы вернуть преобразования к ранее установленным
        auto opSaveState = System::DynamicCast<Aspose::Pdf::Operators::GSave>(op);
        auto opRestoreState = System::DynamicCast<Aspose::Pdf::Operators::GRestore>(op);

        // Создайте объект ConcatenateMatrix, так как он определяет текущую матрицу преобразования.
        auto opCtm = System::DynamicCast<Aspose::Pdf::Operators::ConcatenateMatrix>(op);

        // Создайте оператор Do, который рисует объекты из ресурсов. Он рисует объекты форм и изображения
        auto opDo = System::DynamicCast<Aspose::Pdf::Operators::Do>(op);

        if (opSaveState != nullptr)
        {
            // Сохраните предыдущее состояние и поместите текущее состояние наверх стека
            graphicsState->Push(System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Clone());
        }
        else if (opRestoreState != nullptr)
        {
            // Удалите текущее состояние и восстановите предыдущее
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

            // Умножьте текущую матрицу на матрицу состояния
            System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek())->Multiply(cm);
            continue;
        }
        else if (opDo != nullptr)
        {
            // В случае, если это оператор рисования изображения
            if (imageNames->Contains(opDo->get_Name()))
            {
                auto lastCTM = System::DynamicCast<System::Drawing::Drawing2D::Matrix>(graphicsState->Peek());
                // Создайте объект XImage для хранения изображений первой страницы pdf
                auto image = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(opDo->get_Name());

                // Получите размеры изображения
                double scaledWidth = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(0), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(1), 2));
                double scaledHeight = Math::Sqrt(Math::Pow(lastCTM->get_Elements()->idx_get(2), 2) + Math::Pow(lastCTM->get_Elements()->idx_get(3), 2));
                // Получите информацию о высоте и ширине изображения
                double originalWidth = image->get_Width();
                double originalHeight = image->get_Height();

                // Вычислите разрешение на основе вышеуказанной информации
                double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                double resVertical = originalHeight * defaultResolution / scaledHeight;

                // Отобразите информацию о размере и разрешении каждого изображения
                Console::Write(_dataDir);
                Console::Write(u" image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                    opDo->get_Name(), scaledWidth, scaledHeight, resHorizontal, resVertical);
            }
        }
    }
}
```