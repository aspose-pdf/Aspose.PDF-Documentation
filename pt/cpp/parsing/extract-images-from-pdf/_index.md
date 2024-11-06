---
title: Extrair Imagens de PDF 
linktitle: Extrair Imagens de PDF
type: docs
weight: 20
url: pt/cpp/extract-images-from-the-pdf-file/
description: Como extrair uma parte da imagem de um PDF usando Aspose.PDF para C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Além disso, uma tarefa demandada ao trabalhar com documentos PDF é extrair imagens de um arquivo PDF. Por exemplo, você recebeu um email em PDF com muitas imagens ótimas que gostaria de extrair como arquivos separados.

A biblioteca Aspose.PDF permite que você extraia imagens do PDF com o seguinte trecho de código:

```cpp
void ExtractImage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para nome do arquivo
    String infilename("sample-image.pdf");
    String outfilename("extracted_image.jpeg");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Extrair uma imagem específica
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Salvar imagem de saída
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    std::clog << __func__ << ": Finish" << std::endl;
}
```