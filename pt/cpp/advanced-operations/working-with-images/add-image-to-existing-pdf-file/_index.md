---
title: Adicionar Imagem a PDF usando C++
linktitle: Adicionar Imagem
type: docs
weight: 10
url: /pt/cpp/add-image-to-existing-pdf-file/
description: Esta seção descreve como adicionar imagem a um arquivo PDF existente usando a biblioteca C++.
lastmod: "2021-12-18"
---

## Adicionar Imagem em um Arquivo PDF Existente

Cada página PDF contém propriedades de Recursos e Conteúdos. Recursos podem ser imagens e formulários, por exemplo, enquanto o conteúdo é representado por um conjunto de operadores PDF. Cada operador tem seu nome e argumento. Este exemplo usa operadores para adicionar uma imagem a um arquivo PDF.

Para adicionar uma imagem a um arquivo PDF existente:

- Crie um objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) e abra o documento PDF de entrada.
- Obtenha a página na qual você deseja adicionar uma imagem.
- Adicione a imagem à coleção de Recursos da página.
- Use operadores para colocar a imagem na página:
- Use o [operador GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save/) para salvar o estado gráfico atual.

- Use o [operador ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix#a40ca09b1fa45560d57a1fd042d3fbe96) para especificar onde a imagem deve ser colocada.
- Use o [operador Do](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do/) para desenhar a imagem na página.
- Finalmente, use o [operador GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore/) para salvar o estado gráfico atualizado.
- Salve o arquivo.
O trecho de código a seguir mostra como adicionar a imagem em um documento PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImages::AddImageToExistingPDF()
{
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"AddImage.pdf");

    // Definir coordenadas
    int lowerLeftX = 50;
    int lowerLeftY = 750;
    int upperRightX = 100;
    int upperRightY = 800;

    // Obter a página na qual você deseja adicionar a imagem
    auto page = document->get_Pages()->idx_get(1);

    // Carregar imagem no stream
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"logo.png");

    // Adicionar uma imagem à coleção de Imagens dos recursos da página
    page->get_Resources()->get_Images()->Add(imageStream);

    // Usando o operador GSave: este operador salva o estado gráfico atual
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // Criar objetos Rectangle e Matrix
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

    auto matrix = MakeObject<Matrix>(
        MakeArray<double>({
            rectangle->get_URX() - rectangle->get_LLX(),
            0,                  0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(), rectangle->get_LLY() }));

    // Usando o operador ConcatenateMatrix (concatenar matriz):
    // define como a imagem deve ser posicionada
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

    // Usando o operador Do: este operador desenha a imagem
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));

    // Usando o operador GRestore: este operador restaura o estado gráfico
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Salvar o novo PDF
    document->Save(_dataDir + u"updated_document.pdf");

    // Fechar o stream de imagem
    imageStream->Close();
}
```

## Adicionar Referência de uma única Imagem várias vezes em um Documento PDF

Às vezes temos a necessidade de usar a mesma imagem várias vezes em um documento PDF. Adicionar uma nova instância aumenta o documento PDF resultante. O método [XImageCollection.Add(XImage)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image/) permite adicionar referência ao mesmo objeto PDF como imagem original, otimizando o tamanho do Documento PDF.

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

## Colocar imagem na página e preservar (controlar) a proporção

Se não conhecermos as dimensões da imagem, há todas as chances de obter uma imagem distorcida na página. O exemplo a seguir mostra uma das maneiras de evitar isso.

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

## Identificar se a imagem dentro do PDF é Colorida ou Preto e Branco

Para reduzir o tamanho da imagem, você precisa comprimi-la. Antes de poder determinar o tipo de compressão de uma imagem, você precisa saber se ela é colorida ou em preto e branco.

O tipo de compressão aplicado à imagem depende do Espaço de Cor da imagem original, ou seja, se a imagem estiver em cores (RGB), use a compressão JPEG2000, e se for em preto e branco, use a compressão JBIG2 / JBIG2000.

Um arquivo PDF pode conter elementos como Texto, Imagem, Gráfico, Anexo, Anotação, etc., e se o arquivo PDF de origem contiver imagens, podemos determinar o espaço de cor da imagem e aplicar a compressão apropriada para reduzir o tamanho do arquivo PDF.

O trecho de código a seguir mostra as etapas para identificar se a imagem dentro do PDF é colorida ou em preto e branco.

```cpp
void WorkingWithImages::CheckColors() {

    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>(_dataDir + u"test4.pdf");
    try {
        // iterar por todas as páginas do arquivo PDF
        for (auto page : document->get_Pages()) {
            // criar instância de Image Placement Absorber
            auto abs = MakeObject<ImagePlacementAbsorber>();
            page->Accept(abs);

            for (auto ia : abs->get_ImagePlacements()) {
                /* Tipo de Cor */
                auto colorType = ia->get_Image()->GetColorType();
                switch (colorType) {
                case ColorType::Grayscale:
                    Console::WriteLine(u"Imagem em Escala de Cinza");
                    break;
                case ColorType::Rgb:
                    Console::WriteLine(u"Imagem Colorida");
                    break;
                }
            }
        }
    }
    catch (Exception ex) {
        Console::WriteLine(u"Erro ao ler o arquivo = {0}", document->get_FileName());
    }
}
```
## Controlar a Qualidade da Imagem

É possível controlar a qualidade de uma imagem que está sendo adicionada a um arquivo PDF. Use o método sobrecarregado [Replace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection#a698b65051b073f0f4b84b1235889bd72) na classe [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection).

O trecho de código a seguir demonstra como converter todas as imagens do documento em JPEGs que usam 80% de qualidade para compressão.

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