---
title: Formatação de Texto em PDF usando C++
linktitle: Formatação de Texto em PDF
type: docs
weight: 30
url: pt/cpp/text-formatting-inside-pdf/
description: Esta página explica como formatar texto dentro do seu arquivo PDF. Há a adição de recuo de linha, adição de borda de texto, adição de texto sublinhado, adição de uma borda ao redor do texto adicionado, alinhamento de texto para conteúdos de caixa flutuante e etc.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Como adicionar Recuo de Linha ao PDF

Para adicionar recuo de linha ao PDF, Aspose.PDF para C++ usa a propriedade [SubsequentLinesIndent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a89b064ab1f39d56040625d7d98194ad3) na classe [TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options/) e também auxilia as coleções [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) e [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs).

Por favor, use o seguinte trecho de código para usar a propriedade:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLineIndent() {

    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de saída
    String outputFileName("SubsequentIndent_out.pdf");


    // Criar novo objeto de documento
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto text = MakeObject<TextFragment>("A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog.");

    // Inicializar TextFormattingOptions para o fragmento de texto e especificar o valor SubsequentLinesIndent

    text->get_TextState()->set_FormattingOptions(MakeObject<Aspose::Pdf::Text::TextFormattingOptions>());
    text->get_TextState()->get_FormattingOptions()->set_SubsequentLinesIndent(20);

    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line2");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line3");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line4");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line5");
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);

}
```

## Como adicionar borda ao texto

O trecho de código a seguir mostra como adicionar uma borda a um texto usando TextBuilder e configurando a propriedade DrawTextRectangleBorder de [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state)

```cpp
void AddTextBorder() {

    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de saída
    String outputFileName("PDFWithTextBorder_out.pdf");

    // Criar novo objeto de documento
    auto document = MakeObject<Document>();
    // Obter página específica
    auto page = document->get_Pages()->Add();

    // Criar fragmento de texto
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // Definir propriedades do texto
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Definir propriedade StrokingColor para desenhar borda ao redor do texto
    // retângulo
    textFragment->get_TextState()->set_StrokingColor(Color::get_DarkRed());
    // Definir valor da propriedade DrawTextRectangleBorder como true
    textFragment->get_TextState()->set_DrawTextRectangleBorder(true);
    auto tb = MakeObject<TextBuilder>(page);
    tb->AppendText(textFragment);
    // Salvar o documento
    document->Save(_dataDir + outputFileName);
}
```

## Como adicionar Texto Sublinhado

O seguinte trecho de código mostra como adicionar texto sublinhado ao criar um novo arquivo PDF.

```cpp
void AddUnderlineText() {
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de saída
    String outputFileName("AddUnderlineText_out.pdf");

    // Criar novo objeto de documento
    auto document = MakeObject<Document>();
    // Obter página específica
    auto page = document->get_Pages()->Add();

    // TextFragment com texto de exemplo
    auto fragment = MakeObject<TextFragment>("Texto com decoração de sublinhado");
    // Definir a fonte para TextFragment
    fragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    fragment->get_TextState()->set_FontSize(10);

    // Definir a formatação do texto como Sublinhado
    fragment->get_TextState()->set_Underline(true);

    // Especificar a posição onde TextFragment precisa ser colocado
    fragment->set_Position(MakeObject<Position>(10, 800));

    auto tb = MakeObject<TextBuilder>(page);
    // Anexar TextFragment ao arquivo PDF
    tb->AppendText(fragment);

    // Salvar documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

## Como adicionar borda ao redor do texto adicionado

Você tem controle sobre a aparência do texto que adiciona. O exemplo abaixo mostra como adicionar uma borda ao redor de um trecho de texto que você adicionou, desenhando um retângulo ao redor dele. Saiba mais sobre a classe [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor/).

```cpp
void AddBorderAroundAddedText() {

    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada
    String inputFileName("sample.pdf");

    // String para nome do arquivo de saída
    String outputFileName("AddingBorderAroundAddedText_out.pdf");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    editor->BindPdf(_dataDir + inputFileName);
    auto lineInfo = MakeObject<Aspose::Pdf::Facades::LineInfo>();

    lineInfo->set_LineWidth(2);
    lineInfo->set_VerticeCoordinate(MakeArray<float>({ 0, 0, 100, 100, 50, 100 }));
    lineInfo->set_Visibility(true);
    auto rect = MakeObject<System::Drawing::Rectangle>(0, 0, 0, 0);
    editor->CreatePolygon(lineInfo, 1, System::Drawing::Rectangle(0, 0, 0, 0), String::Empty);

    // Salvar documento PDF resultante.
    editor->Save(_dataDir + outputFileName);
}
```

## Como adicionar uma quebra de linha

Para adicionar texto com quebra de linha, por favor, use [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) com [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph).

O seguinte trecho de código mostra como adicionar uma quebra de linha em seu arquivo PDF:

```cpp
void AddNewLineFeed() {
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de saída
    String outputFileName("AddNewLineFeed_out.pdf");

    // Criar novo objeto de documento
    auto document = MakeObject<Document>();
    // Obter página específica
    auto page = document->get_Pages()->Add();

    // Inicializar novo TextFragment com texto contendo marcadores de nova linha necessários
    auto textFragment = MakeObject<TextFragment>("Applicant Name: \r\n Joe Smoe");

    // Definir propriedades do fragmento de texto, se necessário
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());

    // Criar objeto TextParagraph
    auto par = MakeObject<TextParagraph>();

    // Adicionar novo TextFragment ao parágrafo
    par->AppendLine(textFragment);

    // Definir posição do parágrafo
    par->set_Position(MakeObject<Position>(100, 600));

    // Criar objeto TextBuilder
    auto textBuilder = new TextBuilder(page);
    // Adicionar o TextParagraph usando TextBuilder
    textBuilder->AppendParagraph(par);

    // Salvar documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

## Como adicionar texto tachado

Você pode usar a classe [TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) para definir formatação de texto como Negrito, Itálico, Sublinhado, e também, a API forneceu as capacidades para marcar a formatação de texto como Tachado.

Por favor, tente usar o seguinte trecho de código para adicionar TextFragment com formatação Tachada.

```cpp
void AddStrikeOutText() {
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de saída
    String outputFileName("AddStrikeOutText_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>();
    // Obter página específica
    auto page = document->get_Pages()->Add();

    // Criar fragmento de texto
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // Definir propriedades do texto
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Definir propriedade de Tachado
    textFragment->get_TextState()->set_StrikeOut(true);
    // Marcar texto como Negrito
    textFragment->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Criar objeto TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);
    // Anexar o fragmento de texto à página PDF
    textBuilder->AppendText(textFragment);

    // Salvar documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

## Aplicar Sombreamento em Gradiente ao Texto

A Classe [Aspose.Pdf.Color](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color) foi ainda mais aprimorada com a introdução de uma nova propriedade de [PatternColorSpace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color#a8be6d8ab626d2ba6935a13a9c5b0de54), que pode ser usada para especificar cores de sombreamento para o texto. Esta nova propriedade adiciona diferentes Sombreamentos em Gradiente ao texto, por exemplo, Sombreamento Axial, Sombreamento Radial (Tipo 3), conforme mostrado no seguinte trecho de código:

```cpp
void ApplyGradientShading() {

    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de entrada
    String inputFileName("sample.pdf");

    // String para o nome do arquivo de saída
    String outputFileName("ApplyGradientShading_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>("always print correctly");

    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientAxialShading>(Color::get_Red(), Color::get_Blue()));

    // Criar nova cor com o espaço de cores do padrão
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);

}
```

>Para aplicar um Gradiente Radial, você pode definir a propriedade 'PatternColorSpace' igual a 'Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)' no trecho de código acima.

## Como alinhar texto ao conteúdo flutuante

Aspose.PDF suporta a definição de alinhamento de texto para conteúdos dentro de um elemento Floating Box. As propriedades de alinhamento da instância [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box) podem ser usadas para alcançar isso, como mostrado no exemplo de código a seguir.

```cpp
void ApplyGradientShadingRadial() {

    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada
    String inputFileName("sample.pdf");

    // String para nome do arquivo de saída
    String outputFileName("ApplyGradientShadingRadial_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>(u"always print correctly");
    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientRadialShading>(Color::get_Red(), Color::get_Blue()));

    // Criar nova cor com espaço de cor padrão
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);
}
```