---
title: Definir Tamanho da Imagem usando C++
linktitle: Definir Tamanho da Imagem
type: docs
weight: 80
url: /pt/cpp/set-image-size/
description: Esta seção descreve como definir o tamanho da imagem em um arquivo PDF usando a biblioteca C++.
lastmod: "2021-12-18"
---

É possível definir o tamanho de uma imagem que está sendo adicionada a um arquivo PDF. Para definir o tamanho, você pode usar as propriedades [FixWidth](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#a08f2f92b184632385eab19fb96c6d40e) e [FixHeight](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image#aed67b52e058b97df6931c214d7092dfa) da [Classe Aspose.Pdf.Image](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image).

O seguinte trecho de código demonstra como definir o tamanho de uma imagem:

```cpp
void WorkingWithImages::ExampleSetImageSize()
{
    String _dataDir("C:\\Samples\\");
    // Instanciar objeto Document
    auto document = MakeObject<Document>();
    // adicionar página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->Add();
    // Criar uma instância de imagem
    auto img = MakeObject<Image>();
    // Definir Largura e Altura da Imagem em Pontos
    img->set_FixWidth(100);
    img->set_FixHeight(100);
    // Definir tipo de imagem como SVG
    img->set_FileType(Aspose::Pdf::ImageFileType::Unknown);
    // Caminho para o arquivo fonte
    img->set_File(_dataDir + u"aspose-logo.jpg");
    page->get_Paragraphs()->Add(img);
    // Definir propriedades da página
    page->get_PageInfo()->set_Width(800);
    page->get_PageInfo()->set_Height(800);
    // salvar arquivo PDF resultante
    document->Save(_dataDir + u"SetImageSize_out.pdf");
}
```