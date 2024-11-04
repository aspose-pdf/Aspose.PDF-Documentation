---
title: Rotacionar Páginas de PDF Usando C++
linktitle: Rotacionar Páginas de PDF
type: docs
weight: 50
url: /cpp/rotate-pages/
description: Este tópico descreve como rotacionar a orientação da página em um arquivo PDF existente programaticamente com C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Este tópico descreve como atualizar ou alterar a orientação das páginas em um arquivo PDF existente programaticamente com C++.

## Alterar Orientação da Página

Aspose.PDF para C++ permite alterar a orientação da página de paisagem para retrato e vice-versa. Para alterar a orientação da página, defina o MediaBox da página usando o seguinte trecho de código. Você também pode alterar a orientação da página definindo o ângulo de rotação usando o método Rotate().

```cpp
void ChangePageOrientation() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {

        auto r = page->get_MediaBox();
        double newHeight = r->get_Width();
        double newWidth = r->get_Height();
        double newLLX = r->get_LLX();

        // Precisamos mover a página para cima para compensar a mudança de tamanho da página
        // (a borda inferior da página é 0,0 e a informação geralmente é colocada a partir do
        // topo da página. É por isso que movemos a borda inferior para cima na diferença entre
        // a altura antiga e a nova.

        double newLLY = r->get_LLY() + (r->get_Height() - newHeight);
        page->set_MediaBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
        // Às vezes, também precisamos definir o CropBox (se foi definido no arquivo original)
        page->set_CropBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

        // Definindo ângulo de rotação da página
        page->set_Rotate(Rotation::on90);
    }

    // Salvar arquivo de saída
    document->Save(_dataDir + outputFileName);
}
```

## Ajustando o Conteúdo da Página para a Nova Orientação da Página

Por favor, note que ao usar o trecho de código acima, parte do conteúdo do documento pode ser cortado porque a altura da página é reduzida. Para evitar isso, aumente a largura proporcionalmente e mantenha a altura intacta. Exemplo de cálculos:

```cpp
void FittingPageContentToNewPageOrientation()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {
        auto r = page->get_MediaBox();
        // Nova altura a mesma
        double newHeight = r->get_Height();
        // Nova largura é expandida proporcionalmente para tornar a orientação paisagem
        // (assumimos que a orientação anterior é retrato)
        double newWidth = r->get_Height() * r->get_Height() / r->get_Width();

        // ...

    }
}
```

Além da abordagem acima, considere usar o facade PdfPageEditor, que pode aplicar zoom ao conteúdo das páginas.

```cpp
void ZoomPageContent()
{

    String _dataDir("C:\\Samples\\");
    String inputFileName("ZoomToPageContents.pdf");
    String outputFileName("ZoomToPageContents_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Obter a região retangular da primeira página do PDF
    auto rect = document->get_Pages()->idx_get(1)->get_Rect();

    // Instanciar instância de PdfPageEditor
    auto ppe = MakeObject<Aspose::Pdf::Facades::PdfPageEditor>();
    // Vincular PDF de origem
    ppe->BindPdf(_dataDir + inputFileName);
    // Definir coeficiente de zoom
    ppe->set_Zoom ((float)(rect->get_Width() / rect->get_Height()));
    // Atualizar tamanho da página
    ppe->set_PageSize(MakeObject<PageSize>((float)rect->get_Height(), (float)rect->get_Width()));

    // Salvar arquivo de saída
    document->Save(_dataDir + outputFileName);
}
```