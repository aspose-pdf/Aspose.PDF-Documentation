---
title: Adicionar Cabeçalho e Rodapé ao PDF
linktitle: Adicionar Cabeçalho e Rodapé ao PDF
type: docs
weight: 70
url: /cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF para C++ permite que você adicione cabeçalhos e rodapés ao seu arquivo PDF usando a classe TextStamp.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para C++** permite que você adicione cabeçalho e rodapé em seu arquivo PDF existente. Você pode adicionar imagens ou texto a um documento PDF. Além disso, tente adicionar diferentes cabeçalhos em um arquivo PDF com C++.

## Adicionando Texto no Cabeçalho do Arquivo PDF

Você pode usar a classe [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) para adicionar texto no cabeçalho de um arquivo PDF. TextStamp class fornece as propriedades necessárias para criar um carimbo baseado em texto, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar texto no cabeçalho, você precisa criar um objeto Document e um objeto TextStamp usando as propriedades necessárias. Depois disso, você pode chamar o método AddStamp da Page para adicionar o texto no cabeçalho do PDF.

Você precisa definir a propriedade TopMargin de forma que ajuste o texto na área do cabeçalho do seu PDF. Você também precisa definir HorizontalAlignment para Center e VerticalAlignment para Top.

O trecho de código a seguir mostra como adicionar texto no cabeçalho de um arquivo PDF com C++.

```cpp
void AddingTextInHeaderOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinHeader.pdf");
    String outputFileName("TextinHeader_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Criar cabeçalho
    auto textStamp = MakeObject<TextStamp>(u"Header Text");

    // Definir propriedades do carimbo
    textStamp->set_TopMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // Adicionar cabeçalho em todas as páginas
    for(auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // Salvar documento atualizado
    document->Save(_dataDir + outputFileName);
}
```
## Adicionando Texto no Rodapé do Arquivo PDF

Você pode usar a classe TextStamp para adicionar texto no rodapé de um arquivo PDF. A classe TextStamp fornece as propriedades necessárias para criar um carimbo baseado em texto, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar texto no rodapé, você precisa criar um objeto Document e um objeto TextStamp usando as propriedades necessárias. Após isso, você pode chamar o método AddStamp da Page para adicionar o texto no rodapé do PDF.

{{% alert color="primary" %}}

Você precisa definir a propriedade Bottom Margin de forma que ajuste o texto na área do rodapé do seu PDF. Você também precisa definir HorizontalAlignment para Center e VerticalAlignment para Bottom.

{{% /alert %}}

O snippet de código a seguir mostra como adicionar texto no rodapé de um arquivo PDF com C++.

```cpp
void AddingTextInFooterOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinFooter.pdf");
    String outputFileName("TextinFooter_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Criar rodapé
    auto textStamp = MakeObject<TextStamp>(u"Texto do Rodapé");

    // Definir propriedades do carimbo
    textStamp->set_BottomMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Bottom);

    // Adicionar rodapé em todas as páginas
    for (auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // Salvar documento atualizado
    document->Save(_dataDir + outputFileName);
}
```

## Adicionando Imagem no Cabeçalho do Arquivo PDF

Você pode usar a classe [ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) para adicionar imagem no cabeçalho de um arquivo PDF. A classe Image Stamp fornece as propriedades necessárias para criar um carimbo baseado em imagem, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar uma imagem no cabeçalho, você precisa criar um objeto Documento e um objeto Image Stamp usando as propriedades necessárias. Depois disso, você pode chamar o método AddStamp da Página para adicionar a imagem no cabeçalho do PDF.

O seguinte trecho de código mostra como adicionar uma imagem no cabeçalho de um arquivo PDF com C++.

```cpp
void AddingImageInHeaderOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinHeader.pdf");
    String outputFileName("ImageinHeader_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Criar cabeçalho
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // Definir propriedades do carimbo
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment (VerticalAlignment::Top);

    // Adicionar cabeçalho em todas as páginas
    for(auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // Salvar documento atualizado
    document->Save(_dataDir + outputFileName);
}
```

## Adicionando Imagem no Rodapé do Arquivo PDF

Você pode usar a classe Image Stamp para adicionar imagem no rodapé de um arquivo PDF. A classe Image Stamp fornece propriedades necessárias para criar um carimbo baseado em imagem, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar imagem no rodapé, você precisa criar um objeto Document e um objeto Image Stamp usando as propriedades requeridas. Depois disso, você pode chamar o método AddStamp da Página para adicionar a imagem no rodapé do PDF.

Você precisa definir a propriedade [BottomMargin](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.stamp#aeab91949cf3eb473018b31a74fed7173) de forma que ajuste a imagem na área do rodapé do seu PDF. Você também precisa definir [HorizontalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#aefec9c0bf30ee5e6fb2640e69aed6cd9) para `Center` e [VerticalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ad4956d03096fc515eaa34319a6bf636a) para `Bottom`.

O seguinte trecho de código mostra como adicionar imagem no rodapé de um arquivo PDF com C++.

```cpp
void AddingImageInFooterOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinFooter.pdf");
    String outputFileName("ImageinFooter_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Criar cabeçalho
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // Definir propriedades do carimbo
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // Adicionar cabeçalho em todas as páginas
    for (auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // Salvar documento atualizado
    document->Save(_dataDir + outputFileName);
}
```

## Adicionando cabeçalhos diferentes em um arquivo PDF

Sabemos que podemos adicionar TextStamp na seção Cabeçalho/Rodapé do documento usando as propriedades TopMargin ou Bottom Margin, mas às vezes podemos ter a necessidade de adicionar múltiplos cabeçalhos/rodapés em um único documento PDF. **Aspose.PDF for C++** explica como fazer isso.

Para cumprir este requisito, criaremos objetos TextStamp individuais (o número de objetos depende do número de Cabeçalhos/Rodapés necessários) e os adicionaremos ao documento PDF. Podemos também especificar diferentes informações de formatação para cada objeto de carimbo. No exemplo a seguir, criamos um objeto Document e três objetos TextStamp e, em seguida, usamos o método [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) da Página para adicionar o texto na seção de cabeçalho do PDF. O trecho de código a seguir mostra como adicionar uma imagem no rodapé de um arquivo PDF com Aspose.PDF para C++.

```cpp
void AddingDifferentHeadersInOnePDFFile()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("multiheader.pdf");
    String outputFileName("multiheader_out.pdf");

    // Abra o documento fonte
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Crie três carimbos
    auto stamp1 = MakeObject<TextStamp>("Header 1");
    auto stamp2 = MakeObject<TextStamp>("Header 2");
    auto stamp3 = MakeObject<TextStamp>("Header 3");

    // Defina o alinhamento do carimbo (colocar carimbo no topo da página, centralizado horizontalmente)
    stamp1->set_VerticalAlignment(VerticalAlignment::Top);
    stamp1->set_HorizontalAlignment(HorizontalAlignment::Center);
    // Especificar o estilo da fonte como Negrito
    stamp1->get_TextState()->set_FontStyle(FontStyles::Bold);
    // Definir a cor do texto em primeiro plano como vermelho
    stamp1->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Especificar o tamanho da fonte como 14
    stamp1->get_TextState()->set_FontSize(14);

    // Agora precisamos definir o alinhamento vertical do segundo objeto carimbo como Top
    stamp2->set_VerticalAlignment(VerticalAlignment::Top);
    // Definir informações de alinhamento horizontal para o carimbo como Centralizado
    stamp2->set_HorizontalAlignment (HorizontalAlignment::Center);
    // Definir o fator de zoom para o objeto carimbo
    stamp2->set_Zoom(10);

    // Definir a formatação do terceiro objeto carimbo
    // Especificar as informações de alinhamento vertical para o objeto carimbo como TOP
    stamp3->set_VerticalAlignment(VerticalAlignment::Top);
    // Definir informações de alinhamento horizontal para o objeto carimbo como Centralizado
    stamp3->set_HorizontalAlignment(HorizontalAlignment::Center);
    // Definir o ângulo de rotação para o objeto carimbo
    stamp3->set_RotateAngle(35);
    // Definir rosa como cor de fundo para o carimbo
    stamp3->get_TextState()->set_BackgroundColor(Color::get_Pink());
    // Alterar as informações da fonte para Verdana
    stamp3->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));

    // O primeiro carimbo é adicionado na primeira página;
    document->get_Pages()->idx_get(1)->AddStamp(stamp1);
    // O segundo carimbo é adicionado na segunda página;
    document->get_Pages()->idx_get(2)->AddStamp(stamp2);
    // O terceiro carimbo é adicionado na terceira página.
    document->get_Pages()->idx_get(3)->AddStamp(stamp3);

    // Salvar documento atualizado
    document->Save(_dataDir + outputFileName);
}
```