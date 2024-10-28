---
title: Extrair Imagens de Arquivo PDF usando C++
linktitle: Extrair Imagens
type: docs
weight: 30
url: /cpp/extract-images-from-pdf-file/
description: Esta seção mostra como extrair imagens de um arquivo PDF usando a biblioteca C++.
lastmod: "2021-12-18"
---

Você pode usar o Aspose.PDF para C++ para extrair todas as imagens de seus documentos PDF em arquivos separados que podem ser reutilizados em outros programas.

As imagens são mantidas na coleção Imagens da coleção Recursos de cada página. Para extrair uma página específica, obtenha a imagem da coleção Imagens usando o índice específico da imagem.

O índice da imagem retorna um objeto [XImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image). Este objeto fornece um método Save que pode ser usado para salvar a imagem extraída.

O seguinte trecho de código mostra como extrair imagens de um arquivo PDF.

```cpp
void WorkingWithImages::ExtractImages()
{
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"ExtractImages.pdf");

    // Extrair uma imagem específica
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + u"output.jpg");

    // Salvar imagem de saída
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    // Salvar arquivo PDF atualizado
    document->Save(_dataDir + u"ExtractImages_out.pdf");
}
```