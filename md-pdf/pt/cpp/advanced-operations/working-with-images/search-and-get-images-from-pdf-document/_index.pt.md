---
title: Pesquisar e Obter Imagens de Documento PDF usando C++
linktitle: Pesquisar e Obter Imagens
type: docs
weight: 60
url: /cpp/search-and-get-images-from-pdf-document/
description: Esta seção explica como pesquisar e obter imagens de um documento PDF com a biblioteca Aspose.PDF.
lastmod: "2021-12-18"
---

O ImagePlacementAbsorber permite que você pesquise entre imagens em todas as páginas de um documento PDF.

Para pesquisar imagens em um documento inteiro:

1. Chame o método [Accept](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#ae71a2782e747936e3c14b7ded5c6dc3f) da coleção [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection). O método Accept leva um objeto [ImagePlacementAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_placement_absorber/) como parâmetro. Isso retorna uma coleção de objetos ImagePlacement.
1. Percorra os objetos ImagePlacements e obtenha suas propriedades (Imagem, dimensões, resolução e assim por diante).

O trecho de código a seguir mostra como pesquisar um documento por todas as suas imagens.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetImagesFromPDFDocument() {

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"SearchAndGetImages.pdf");

    // Criar objeto ImagePlacementAbsorber para realizar a busca de colocação de imagem
    auto abs = MakeObject<ImagePlacementAbsorber>();

    // Aceitar o absorvedor para todas as páginas
    document->get_Pages()->Accept(abs);

    // Percorrer todos os ImagePlacements, obter imagem e Propriedades de ImagePlacement
    for(auto imagePlacement : abs->get_ImagePlacements())
    {
        // Obter a imagem usando o objeto ImagePlacement
        auto image = imagePlacement->get_Image();

        // Exibir propriedades de colocação de imagem para todas as colocações
        Console::WriteLine(u"largura da imagem: {0}", imagePlacement->get_Rectangle()->get_Width());
        Console::WriteLine(u"altura da imagem:{0}", imagePlacement->get_Rectangle()->get_Height());
        Console::WriteLine(u"imagem LLX:{0}", imagePlacement->get_Rectangle()->get_LLX());
        Console::WriteLine(u"imagem LLY:{0}", imagePlacement->get_Rectangle()->get_LLY());
        Console::WriteLine(u"resolução horizontal da imagem:{0}", imagePlacement->get_Resolution()->get_X());
        Console::WriteLine(u"resolução vertical da imagem:{0}", imagePlacement->get_Resolution()->get_Y());
    }
}
```