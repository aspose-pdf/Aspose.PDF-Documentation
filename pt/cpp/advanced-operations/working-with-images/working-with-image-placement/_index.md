---
title: Trabalhando com Colocação de Imagem usando C++
linktitle: Trabalhando com Colocação de Imagem
type: docs
weight: 50
url: pt/cpp/working-with-image-placement/
description: Esta seção descreve as funcionalidades de trabalhar com colocação de imagem em um arquivo PDF usando a biblioteca C++.
lastmod: "2021-12-18"
---

**Aspose.PDF for C++** suporta o [ImagePlacement](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber) e [ImagePlacementCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_collection) que fornecem capacidade semelhante às classes descritas acima para obter a resolução e posição de uma imagem em um documento PDF.

- ImagePlacementAbsorber realiza a busca de uso de imagem como a coleção de objetos ImagePlacement.
- ImagePlacement fornece os membros Resolution e Rectangle que retornam os valores reais de colocação da imagem.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithImagePlacement() {

    String _dataDir("C:\\Samples\\");

    // Carregar o documento PDF de origem
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"ImagePlacement.pdf");

    auto abs = MakeObject<ImagePlacementAbsorber>();

    // Carregar o conteúdo da primeira página
    document->get_Pages()->idx_get(1)->Accept(abs);
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // Obter propriedades da imagem
        Console::WriteLine(u"largura da imagem: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"altura da imagem:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"LLX da imagem:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"LLY da imagem:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"resolução horizontal da imagem:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"resolução vertical da imagem:{0}", imagePlacement->get_Resolution()->get_Y());

        // Recuperar imagem com dimensões visíveis
        auto imageStream = MakeObject<System::IO::MemoryStream>();

        // Recuperar imagem dos recursos
        imagePlacement->get_Image()->Save(imageStream, System::Drawing::Imaging::ImageFormat::get_Png());
        auto resourceImage = System::DynamicCast< System::Drawing::Bitmap>(System::Drawing::Bitmap::FromStream(imageStream));

        // Criar bitmap com dimensões reais
        auto scaledImage = MakeObject<System::Drawing::Bitmap>(resourceImage, (int)imagePlacement->get_Rectangle()->get_Width(), (int)imagePlacement->get_Rectangle()->get_Height());
        // ...

    }

}
```