---
title: Rotacionar Texto Dentro do PDF usando C++
linktitle: Rotacionar Texto Dentro do PDF
type: docs
weight: 50
url: /pt/cpp/rotate-text-inside-pdf/
description: Aprenda diferentes maneiras de rotacionar texto em PDF. Aspose.PDF permite que você rotacione o texto em qualquer ângulo, rotacione fragmentos de texto ou um parágrafo inteiro.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Rotacionar Texto Dentro do PDF usando Propriedade de Rotação

Usando a propriedade Rotation da classe [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/), você pode rotacionar o texto em vários ângulos. A rotação de texto pode ser usada em diferentes cenários de geração de documentos. Você pode especificar o ângulo de rotação em graus para rotacionar o texto conforme sua necessidade. Por favor, verifique os diferentes cenários a seguir, nos quais você pode implementar a rotação de texto.

## Implementar Rotação usando TextFragment e TextBuilder

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ImplementRotationUsingTextFragmentAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // Inicializar objeto de documento
    auto document = MakeObject<Document>();
    // Obter página específica
    auto page = document->get_Pages()->Add();
    // Criar fragmento de texto
    auto textFragment1 = MakeObject<TextFragment>("main text");
    textFragment1->set_Position(MakeObject<Position>(100, 600));

    // Definir propriedades do texto
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Criar fragmento de texto rotacionado
    auto textFragment2 = MakeObject<TextFragment>("rotated text");
    textFragment2->set_Position(MakeObject<Position>(200, 600));
    // Definir propriedades do texto
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment2->get_TextState()->set_Rotation(45);

    // Criar fragmento de texto rotacionado
    auto textFragment3 = MakeObject<TextFragment>("rotated text");
    textFragment3->set_Position(MakeObject<Position>(300, 600));

    // Definir propriedades do texto
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment3->get_TextState()->set_Rotation(90);

    // criar objeto TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Anexar o fragmento de texto à página do PDF
    textBuilder->AppendText(textFragment1);
    textBuilder->AppendText(textFragment2);
    textBuilder->AppendText(textFragment3);

    // Salvar documento
    document->Save(_dataDir + u"TextFragmentTests_Rotated1_out.pdf");
}
```

## Implementar Rotação usando TextParagraph e TextBuilder (Fragmentos Rotacionados)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    String _dataDir("C:\\Samples\\");

    // Inicializar objeto documento
    auto document = MakeObject<Document>();
    // Obter página específica
    auto page = document->get_Pages()->Add();
    auto paragraph = MakeObject<TextParagraph>();
    paragraph->set_Position(MakeObject<Position>(200, 600));

    // Criar fragmento de texto
    auto textFragment1 = MakeObject<TextFragment>("texto rotacionado");
    // Definir propriedades do texto
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // Definir rotação
    textFragment1->get_TextState()->set_Rotation(45);

    // Criar fragmento de texto
    auto textFragment2 = MakeObject<TextFragment>("texto principal");
    // Definir propriedades do texto
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Criar fragmento de texto
    auto textFragment3 = MakeObject<TextFragment>("outro texto rotacionado");
    // Definir propriedades do texto
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // Definir rotação
    textFragment3->get_TextState()->set_Rotation(-45);

    // Adicionar os fragmentos de texto ao parágrafo
    paragraph->AppendLine(textFragment1);
    paragraph->AppendLine(textFragment2);
    paragraph->AppendLine(textFragment3);
    // Criar objeto TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Adicionar o parágrafo de texto à página PDF
    textBuilder->AppendParagraph(paragraph);
    // Salvar documento
    document->Save(_dataDir + u"TextFragmentTests_Rotated2_out.pdf");

}
```

## Implementar Rotação usando TextFragment e Page.Paragraphs

```cpp
void ImplementRotationUsingTextFragmentAndPageParagraphs() {

    String _dataDir("C:\\Samples\\");

    // Inicializar objeto do documento
    auto document = MakeObject<Document>();
    // Obter página específica
    auto page = document->get_Pages()->Add();
    // Criar fragmento de texto
    auto textFragment1 = MakeObject<TextFragment>("texto principal");
    // Definir propriedades do texto
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Criar fragmento de texto
    auto textFragment2 = MakeObject<TextFragment>("texto rotacionado");

    // Definir propriedades do texto
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Definir rotação
    textFragment2->get_TextState()->set_Rotation(315);

    // Criar fragmento de texto
    auto textFragment3 = MakeObject<TextFragment>("texto rotacionado");
    // Definir propriedades do texto
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // Definir rotação
    textFragment3->get_TextState()->set_Rotation(270);
    page->get_Paragraphs()->Add(textFragment1);
    page->get_Paragraphs()->Add(textFragment2);
    page->get_Paragraphs()->Add(textFragment3);

    // Salvar documento
    document->Save(_dataDir + u"TextFragmentTests_Rotated3_out.pdf");
}
```

## Implementar Rotação usando TextParagraph e TextBuilder (Parágrafo Inteiro Rotacionado)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // Inicializar objeto do documento
    auto document = MakeObject<Document>();
    // Obter página específica
    auto page = document->get_Pages()->Add();
    for (int i = 0; i < 4; i++) {
        auto paragraph = MakeObject<TextParagraph>();
        paragraph->set_Position(MakeObject<Position>(200, 600));
        // Especificar rotação
        paragraph->set_Rotation(i * 90 + 45);
        // Criar fragmento de texto
        auto textFragment1 = MakeObject<TextFragment>("Texto do Parágrafo");
        // Criar fragmento de texto
        textFragment1->get_TextState()->set_FontSize(12);
        textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment1->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment1->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // Criar fragmento de texto
        auto textFragment2 = MakeObject<TextFragment>("Segunda linha de texto");
        // Definir propriedades do texto
        textFragment2->get_TextState()->set_FontSize(12);
        textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment2->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment2->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // Criar fragmento de texto
        auto textFragment3 = MakeObject<TextFragment>("E um pouco mais de texto...");
        // Definir propriedades do texto
        textFragment3->get_TextState()->set_FontSize(12);
        textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment3->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment3->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment3->get_TextState()->set_Underline(true);

        paragraph->AppendLine(textFragment1);
        paragraph->AppendLine(textFragment2);
        paragraph->AppendLine(textFragment3);
        // Criar objeto TextBuilder
        auto textBuilder = MakeObject<TextBuilder>(page);
        // Anexar o fragmento de texto à página PDF
        textBuilder->AppendParagraph(paragraph);
    }
    // Salvar documento
    document->Save(_dataDir + u"TextFragmentTests_Rotated4_out.pdf");
}
```