---
title: Anotação de Texto em PDF
Texttitle: Anotação de Texto
type: docs
weight: 10
url: /cpp/text-annotation/
description: Aspose.PDF para C++ permite que você Adicione, Obtenha e Exclua Anotações de Texto do seu documento PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Como adicionar Anotação de Texto em um arquivo PDF existente

Uma Anotação de Texto é uma anotação anexada a um local específico em um documento PDF. Quando fechada, a anotação é exibida como um ícone; quando aberta, ela deve exibir uma janela pop-up contendo o texto da nota na fonte e tamanho escolhidos pelo leitor.

Anotações são contidas pela coleção [Annotations](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) de uma Página específica. Essa coleção contém as anotações apenas para essa página individual; cada página tem sua própria coleção de Anotações.

Para adicionar uma anotação a uma página específica, adicione-a à coleção de Anotações dessa página com o método [Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_collection#a1f7bf6c38fe2f97904a3575f5241d6c9).

1. Primeiro, crie uma anotação que você deseja adicionar ao PDF.
1. Em seguida, abra o PDF de entrada.
1. Adicione a anotação à coleção de Annotations do objeto [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).

O trecho de código a seguir mostra como adicionar uma anotação em uma página PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTextAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);
    auto rect = MakeObject<Rectangle>(200, 750, 400, 790);
    auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::TextAnnotation>(page, rect);

    textAnnotation->set_Title(u"Usuário Aspose");
    textAnnotation->set_Subject(u"Assunto de Exemplo");
    textAnnotation->set_State(Aspose::Pdf::Annotations::AnnotationState::Accepted);
    textAnnotation->set_Contents(u"Conteúdo de exemplo para a anotação");
    textAnnotation->set_Open(true);
    textAnnotation->set_Icon(Aspose::Pdf::Annotations::TextIcon::Circle);

    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textAnnotation);
    border->set_Width(5);
    border->set_Dash(MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textAnnotation->set_Border(border);
    textAnnotation->set_Rect(rect);

    page->get_Annotations()->Add(textAnnotation);
    document->Save(_dataDir + u"sample_textannot.pdf");
}
```

## Obter Anotação de Texto

Por favor, tente usar o seguinte trecho de código para Obter Anotação de Texto em documento PDF:

```cpp
void GetTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // Filtrar anotações usando AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // imprimir resultados
    for (auto fa : textAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

## Excluir Anotação de Texto do arquivo PDF

O seguinte trecho de código mostra como Excluir Anotação de Texto de um arquivo PDF.

```cpp
void DeleteTextAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // Filtrar anotações usando AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // excluir anotações
    for (auto fa : textAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_textannot_del.pdf");
}
```

## Como adicionar (ou Criar) nova Anotação de Texto Livre

Uma anotação de texto livre exibe texto diretamente na página. No trecho a seguir, adicionamos uma anotação de texto livre acima da primeira ocorrência da string.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void FreeTextAnnotations::AddFreeTextAnnotationDemo()
{
    String _dataDir("C:\\Samples\\");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto defaultAppearance = MakeObject<DefaultAppearance>();
    defaultAppearance->set_FontName(u"Helvetica");
    defaultAppearance->set_FontSize(12);
    defaultAppearance->set_TextColor(System::Drawing::Color::get_Blue());

    auto freeTextAnnotation = MakeObject<FreeTextAnnotation>(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

    freeTextAnnotation->set_RichText(u"Free Text Demo");
    page->get_Annotations()->Add(freeTextAnnotation);
    document->Save(_dataDir + u"sample_freetext.pdf");
}
```

## Obter Anotação de Texto Livre

Por favor, tente usar o seguinte trecho de código para Obter Anotação de Texto no documento PDF:

```cpp
void FreeTextAnnotations::GetFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Filtrar anotações usando AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // imprimir resultados
    for (auto fa : freeTextAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

### Tornar Anotação de Texto Livre Invisível

Às vezes, é necessário criar uma marca d'água que não seja visível no documento ao visualizá-lo, mas que deva ser visível quando o documento for impresso. Use flags de anotação para este propósito. O trecho de código a seguir mostra como.

```cpp
void FreeTextAnnotations::MakeFreeTextAnnotationInvisble() {

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto doc = MakeObject<Document>(_dataDir + u"input.pdf");

    auto annotation = new FreeTextAnnotation(doc->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(50, 600, 250, 650),
        MakeObject<DefaultAppearance>(u"Helvetica", 16,
            System::Drawing::Color::get_Red()));
    annotation->set_Contents(u"ABCDEFG");
    annotation->get_Characteristics()->set_Border(System::Drawing::Color::get_Red());
    annotation->set_Flags (AnnotationFlags::Print | AnnotationFlags::NoView);
    doc->get_Pages()->idx_get(1)->get_Annotations()->Add(annotation);

    // Salvar arquivo de saída
    doc->Save(_dataDir + u"InvisibleAnnotation_out.pdf");
}
```

## Deletar Anotação FreeText

O trecho de código a seguir mostra como deletar a anotação FreeText de um arquivo PDF.

```cpp
void FreeTextAnnotations::DeleteFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");

    // Filtrar anotações usando AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // deletar anotações
    for (auto fa : freeTextAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_freetext_del.pdf");
}
```