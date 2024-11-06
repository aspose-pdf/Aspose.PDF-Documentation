---
title: Добавить изображение в PDF с использованием C++
linktitle: Добавить изображение
type: docs
weight: 10
url: ru/cpp/add-image-to-existing-pdf-file/
description: Этот раздел описывает, как добавить изображение в существующий PDF файл с использованием библиотеки C++.
lastmod: "2021-12-18"
---

## Добавить изображение в существующий PDF файл

Каждая страница PDF содержит свойства Ресурсы и Содержимое. Ресурсы могут быть, например, изображениями и формами, в то время как содержимое представлено набором операторов PDF. Каждый оператор имеет свое имя и аргумент. В этом примере используются операторы для добавления изображения в PDF файл.

Чтобы добавить изображение в существующий PDF файл:

- Создайте объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) и откройте входной PDF документ.
- Получите страницу, на которую вы хотите добавить изображение.
- Добавьте изображение в коллекцию Ресурсов страницы.
- Используйте операторы, чтобы разместить изображение на странице:
- Используйте оператор [GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/), чтобы сохранить текущее графическое состояние.

- Используйте оператор [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix#a40ca09b1fa45560d57a1fd042d3fbe96), чтобы указать, где должно быть размещено изображение.
- Используйте [оператор Do](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do/), чтобы нарисовать изображение на странице.
- Наконец, используйте [оператор GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/), чтобы сохранить обновленное графическое состояние.
- Сохраните файл. Следующий фрагмент кода показывает, как добавить изображение в PDF-документ.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImages::AddImageToExistingPDF()
{
    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + u"AddImage.pdf");

    // Установить координаты
    int lowerLeftX = 50;
    int lowerLeftY = 750;
    int upperRightX = 100;
    int upperRightY = 800;

    // Получить страницу, на которую нужно добавить изображение
    auto page = document->get_Pages()->idx_get(1);

    // Загрузить изображение в поток
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"logo.png");

    // Добавить изображение в коллекцию изображений ресурсов страницы
    page->get_Resources()->get_Images()->Add(imageStream);

    // Использование оператора GSave: этот оператор сохраняет текущее состояние графики
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // Создать объекты Rectangle и Matrix
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

    auto matrix = MakeObject<Matrix>(
        MakeArray<double>({
            rectangle->get_URX() - rectangle->get_LLX(),
            0,                  0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(), rectangle->get_LLY() }));

    // Использование оператора ConcatenateMatrix (конкатенация матрицы):
    // определяет, как изображение должно быть размещено
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

    // Использование оператора Do: этот оператор рисует изображение
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));

    // Использование оператора GRestore: этот оператор восстанавливает состояние графики
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Сохранить новый PDF
    document->Save(_dataDir + u"updated_document.pdf");

    // Закрыть поток изображения
    imageStream->Close();
}
```

## Добавление ссылки на одно изображение несколько раз в PDF-документ

Иногда возникает необходимость использовать одно и то же изображение несколько раз в PDF-документе. Добавление новой копии увеличивает размер результирующего PDF-документа. Метод [XImageCollection.Add(XImage)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image/) позволяет добавить ссылку на тот же объект PDF, что и оригинальное изображение, что оптимизирует размер PDF-документа.

```cpp
void WorkingWithImages::AddReferenceOfaSingleImageMultipleTimes() {

    String _dataDir("C:\\Samples\\");
    auto imageRectangle = MakeObject<Rectangle>(0, 0, 30, 15);

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    document->get_Pages()->Add();
    document->get_Pages()->Add();

    auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.png");

    SharedPtr<Aspose::Pdf::XImage> image;

    for (auto page : document->get_Pages()) {
        auto annotation = MakeObject<Aspose::Pdf::Annotations::WatermarkAnnotation>(page, page->get_Rect());
        auto form = annotation->get_Appearance()->idx_get(u"N");
        form->set_BBox(page->get_Rect());
        String name;
        if (image != nullptr) {
            name = form->get_Resources()->get_Images()->Add(imageStream);
            image = form->get_Resources()->get_Images()->idx_get(name);
        }
        else {
            form->get_Resources()->get_Images()->AddWithName(image);
        }
        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
        form->get_Contents()->Add(
            MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(
                MakeObject<Matrix>(imageRectangle->get_Width(), 0, 0, imageRectangle->get_Height(), 0, 0)));

        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(name));
        form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
        page->get_Annotations()->Add(annotation, false);
        imageRectangle = MakeObject<Rectangle>(0, 0, imageRectangle->get_Width() * 1.01, imageRectangle->get_Height() * 1.01);
    }
    document->Save(_dataDir + u"AddReferenceOfaSingleImageMultipleTimes_out.pdf");
}
```

## Разместить изображение на странице и сохранить (контролировать) соотношение сторон

Если мы не знаем размеры изображения, есть большая вероятность получить искаженное изображение на странице. Следующий пример показывает один из способов избежать этого.

```cpp
void WorkingWithImages::AddingImageAndPreserveAspectRatioIntoPDF() {

    String _dataDir("C:\\Samples\\");

    auto bitmap = System::Drawing::Image::FromFile(_dataDir + u"3410492.jpg");

    int width;
    int height;

    width = bitmap->get_Width();
    height = bitmap->get_Height();

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    int scaledWidth = 400;
    int scaledHeight = scaledWidth * height / width;

    page->AddImage(_dataDir + u"3410492.jpg", new Rectangle(10, 10, scaledWidth, scaledHeight));
    document->Save(_dataDir + u"sample_image.pdf");
}
```

## Определить, является ли изображение внутри PDF цветным или черно-белым

Для уменьшения размера изображения необходимо его сжать. Before you can determine the type of compression of an image, you need to know whether it is color or black and white.

Тип сжатия, применяемый к изображению, зависит от ColorSpace оригинального изображения, т.е. если изображение цветное (RGB), то используйте сжатие JPEG2000, а если оно черно-белое, то используйте сжатие JBIG2 / JBIG2000.

PDF файл может содержать такие элементы, как текст, изображение, график, вложение, аннотация и т. д., и если исходный PDF файл содержит изображения, мы можем определить цветовое пространство изображения и применить соответствующее сжатие для изображения, чтобы уменьшить размер PDF файла.

Следующий фрагмент кода показывает шаги для определения, является ли изображение внутри PDF цветным или черно-белым.

```cpp
void WorkingWithImages::CheckColors() {

    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>(_dataDir + u"test4.pdf");
    try {
        // iterate through all pages of PDF file
        for (auto page : document->get_Pages()) {
            // create Image Placement Absorber instance
            auto abs = MakeObject<ImagePlacementAbsorber>();
            page->Accept(abs);

            for (auto ia : abs->get_ImagePlacements()) {
                /* ColorType */
                auto colorType = ia->get_Image()->GetColorType();
                switch (colorType) {
                case ColorType::Grayscale:
                    Console::WriteLine(u"Grayscale Image");
                    break;
                case ColorType::Rgb:
                    Console::WriteLine(u"Colored Image");
                    break;
                }
            }
        }
    }
    catch (Exception ex) {
        Console::WriteLine(u"Error reading file = {0}", document->get_FileName());
    }
}
```
## Контроль качества изображения

Можно контролировать качество изображения, которое добавляется в PDF файл. Используйте перегруженный метод [Replace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection#a698b65051b073f0f4b84b1235889bd72) в классе [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection).

Следующий фрагмент кода демонстрирует, как преобразовать все изображения документа в JPEG с использованием 80% качества для сжатия.

```cpp
void WorkingWithImages::ControlImageQuality() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample_with_images.pdf");

    for (auto page : document->get_Pages())
    {
        int idx = 1;
        for (auto image : page->get_Resources()->get_Images())
        {
            auto imageStream = MakeObject<System::IO::MemoryStream>();
            image->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Jpeg());
            page->get_Resources()->get_Images()->Replace(idx, imageStream, 80);
            idx = idx + 1;
        }
    }

    document->Save(_dataDir + u"sample_with_images_out.pdf");
}
```