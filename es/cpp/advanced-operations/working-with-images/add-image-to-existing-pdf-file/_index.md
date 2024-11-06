---
title: Add Image to PDF using C++
linktitle: Add Image
type: docs
weight: 10
url: es/cpp/add-image-to-existing-pdf-file/
description: Esta sección describe cómo agregar una imagen a un archivo PDF existente usando la biblioteca C++.
lastmod: "2021-12-18"
---

## Agregar Imagen en un Archivo PDF Existente

Cada página PDF contiene propiedades de Recursos y Contenidos. Los recursos pueden ser imágenes y formularios, por ejemplo, mientras que el contenido está representado por un conjunto de operadores PDF. Cada operador tiene su nombre y argumento. Este ejemplo utiliza operadores para agregar una imagen a un archivo PDF.

Para agregar una imagen a un archivo PDF existente:

- Cree un objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) y abra el documento PDF de entrada.
- Obtenga la página a la que desea agregar una imagen.
- Agregue la imagen a la colección de Recursos de la página.
- Use operadores para colocar la imagen en la página:
- Use el operador [GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) para guardar el estado gráfico actual.

- Use el [operador ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix#a40ca09b1fa45560d57a1fd042d3fbe96) para especificar dónde se colocará la imagen.
- Utilice el [operador Do](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do/) para dibujar la imagen en la página.
- Finalmente, use el [operador GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/) para guardar el estado gráfico actualizado.
- Guarde el archivo.
El siguiente fragmento de código muestra cómo agregar la imagen en un documento PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImages::AddImageToExistingPDF()
{
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"AddImage.pdf");

    // Establecer coordenadas
    int lowerLeftX = 50;
    int lowerLeftY = 750;
    int upperRightX = 100;
    int upperRightY = 800;

    // Obtener la página a la que desea agregar la imagen
    auto page = document->get_Pages()->idx_get(1);

    // Cargar imagen en el flujo
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"logo.png");

    // Agregar una imagen a la colección de Imágenes de los recursos de la página
    page->get_Resources()->get_Images()->Add(imageStream);

    // Usando el operador GSave: este operador guarda el estado gráfico actual
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // Crear objetos Rectangle y Matrix
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

    auto matrix = MakeObject<Matrix>(
        MakeArray<double>({
            rectangle->get_URX() - rectangle->get_LLX(),
            0,                  0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(), rectangle->get_LLY() }));

    // Usando el operador ConcatenateMatrix (concatenar matriz):
    // define cómo debe colocarse la imagen
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

    // Usando el operador Do: este operador dibuja la imagen
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));

    // Usando el operador GRestore: este operador restaura el estado gráfico
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Guardar el nuevo PDF
    document->Save(_dataDir + u"updated_document.pdf");

    // Cerrar flujo de imagen
    imageStream->Close();
}
```

## Agregar referencia de una sola imagen múltiples veces en un documento PDF

A veces tenemos el requisito de usar la misma imagen múltiples veces en un documento PDF. Agregar una nueva instancia aumenta el documento PDF resultante. El método [XImageCollection.Add(XImage)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image/) permite agregar referencia al mismo objeto PDF como imagen original que optimiza el tamaño del documento PDF.

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

## Colocar imagen en la página y preservar (controlar) la proporción

Si no conocemos las dimensiones de la imagen, existe la posibilidad de obtener una imagen distorsionada en la página. El siguiente ejemplo muestra una de las formas de evitar esto.

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

## Identificar si la imagen dentro del PDF es a color o en blanco y negro

Para reducir el tamaño de la imagen, necesitas comprimirla. Antes de poder determinar el tipo de compresión de una imagen, necesitas saber si es en color o en blanco y negro.

El tipo de compresión aplicado a la imagen depende del ColorSpace de la imagen original, es decir, si la imagen está en color (RGB) entonces usa la compresión JPEG2000, y si es en blanco y negro entonces usa la compresión JBIG2 / JBIG2000.

Un archivo PDF puede contener elementos como Texto, Imagen, Gráfico, Adjunto, Anotación, etc. y si el archivo PDF fuente contiene imágenes, podemos determinar el espacio de color de la imagen y aplicar la compresión adecuada para reducir el tamaño del archivo PDF.

El siguiente fragmento de código muestra los pasos para identificar si la imagen dentro del PDF es en color o en blanco y negro.

```cpp
void WorkingWithImages::CheckColors() {

    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>(_dataDir + u"test4.pdf");
    try {
        // iterar a través de todas las páginas del archivo PDF
        for (auto page : document->get_Pages()) {
            // crear instancia del absorbedor de colocación de imágenes
            auto abs = MakeObject<ImagePlacementAbsorber>();
            page->Accept(abs);

            for (auto ia : abs->get_ImagePlacements()) {
                /* Tipo de Color */
                auto colorType = ia->get_Image()->GetColorType();
                switch (colorType) {
                case ColorType::Grayscale:
                    Console::WriteLine(u"Imagen en escala de grises");
                    break;
                case ColorType::Rgb:
                    Console::WriteLine(u"Imagen en color");
                    break;
                }
            }
        }
    }
    catch (Exception ex) {
        Console::WriteLine(u"Error al leer el archivo = {0}", document->get_FileName());
    }
}
```
## Controlar la Calidad de la Imagen

Es posible controlar la calidad de una imagen que se está añadiendo a un archivo PDF. Utilice el método sobrecargado [Replace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection#a698b65051b073f0f4b84b1235889bd72) en la clase [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection).

El siguiente fragmento de código demuestra cómo convertir todas las imágenes del documento en JPEGs que usan un 80% de calidad para la compresión.

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