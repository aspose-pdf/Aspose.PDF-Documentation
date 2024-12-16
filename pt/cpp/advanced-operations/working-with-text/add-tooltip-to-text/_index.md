---
title: PDF Tooltip usando C++
linktitle: PDF Tooltip
type: docs
weight: 20
url: /pt/cpp/pdf-tooltip/
description: Aprenda a adicionar tooltip ao fragmento de texto em PDF usando C++ e Aspose.PDF
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Tooltip ao Texto Pesquisado adicionando Botão Invisível

Este artigo demonstra como adicionar tooltip ao texto em um documento PDF existente em C++. O Aspose.PDF suporta a criação de tooltips adicionando um botão invisível sobre o texto pesquisado do arquivo PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void AddTooltipToSearchedText() {

    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de saída
    String outputFileName("Tooltip_out.pdf");

    // Criar documento de exemplo com texto
    auto document = MakeObject<Document>();
    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Mova o cursor do mouse aqui para exibir um tooltip"));

    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(MakeObject<TextFragment>("Mova o cursor do mouse aqui para exibir um tooltip muito longo"));

    document->Save(outputFileName);

    // Abrir documento com texto
    auto document = MakeObject<Document>(outputFileName);
    // Criar objeto TextAbsorber para encontrar todas as frases que correspondem à expressão regular
    auto absorber = MakeObject<TextFragmentAbsorber>("Mova o cursor do mouse aqui para exibir um tooltip");
    // Aceitar o absorber para as páginas do documento
    document->get_Pages()->Accept(absorber);

    // Obter os fragmentos de texto extraídos
    auto textFragments = absorber->get_TextFragments();

    // Percorrer os fragmentos
    for(auto fragment : textFragments)
    {
        // Criar botão invisível na posição do fragmento de texto
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // O valor de AlternateName será exibido como tooltip por uma aplicação de visualização
        field->set_AlternateName (u"Tooltip para texto.");
        // Adicionar campo de botão ao documento
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // A seguir será um exemplo de tooltip muito longo
    absorber = MakeObject<TextFragmentAbsorber>("Mova o cursor do mouse aqui para exibir um tooltip muito longo");
    document->get_Pages()->Accept(absorber);
    textFragments = absorber->get_TextFragments();

    for(auto fragment : textFragments)
    {
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // Definir texto muito longo
        field->set_AlternateName(String("Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
            sed do eiusmod tempor incididunt ut labore et dolore magna\
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
            ullamco laboris nisi ut aliquip ex ea commodo consequat.\
            Duis aute irure dolor in reprehenderit in voluptate velit\
            esse cillum dolore eu fugiat nulla pariatur. Excepteur sint\
            occaecat cupidatat non proident, sunt in culpa qui officia\
            deserunt mollit anim id est laborum."));
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // Salvar documento
    document->Save(outputFileName);

}
```

## Criar um Bloco de Texto Oculto e Mostrá-lo ao Passar o Mouse

Aspose.PDF para C++ implementa uma função de ações ocultas, com a qual você pode mostrar/ocultar um campo de texto (ou qualquer outro tipo de anotação) ao entrar/sair do mouse sobre algum botão invisível. Para fazer isso, use a classe Aspose.Pdf.Annotations.HideAction para atribuir uma ação de ocultar/mostrar ao bloco de texto. Use o seguinte trecho de código para mostrar/ocultar o bloco de texto na entrada/saída do mouse.

Também observe que as ações de PDF nos documentos funcionam bem em seus respectivos leitores (como o Adobe Reader), mas não oferecem garantias para outros leitores de PDF (como plug-ins de navegador). Fizemos uma breve investigação e descobrimos:

- Todas as implementações da ação de ocultar em documentos PDF funcionam bem no Internet Explorer v.11.0.
- Todas as implementações da ação de ocultar também funcionam no Opera v.12.14, mas notamos algum atraso de resposta na primeira abertura do documento.

- Somente a implementação usando o construtor HideAction aceitando o nome do campo funciona se o Google Chrome v.61.0 navegar pelo documento; Por favor, use os construtores correspondentes se a navegação no Google Chrome for significativa:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```cpp
void CreateHiddenTextBlock() {

    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de saída
    String outputFileName("TextBlock_HideShow_MouseOverOut_out.pdf");

    // Criar documento de exemplo com texto
    auto document = MakeObject<Document>();

    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Mova o cursor do mouse aqui para exibir o texto flutuante"));
    document->Save(outputFileName);

    // Abrir documento com texto
    auto document = MakeObject<Document>(outputFileName);

    // Criar objeto TextAbsorber para encontrar todas as frases correspondentes à expressão regular
    auto absorber = MakeObject<TextFragmentAbsorber>("Mova o cursor do mouse aqui para exibir o texto flutuante");
    // Aceitar o absorvedor para as páginas do documento
    document->get_Pages()->Accept(absorber);
    // Obter o primeiro fragmento de texto extraído
    auto textFragments = absorber->get_TextFragments();
    auto fragment = textFragments->idx_get(1);

    // Criar campo de texto oculto para texto flutuante no retângulo especificado da página
    auto floatingField = MakeObject<Aspose::Pdf::Forms::TextBoxField>(fragment->get_Page(), MakeObject<Rectangle>(100, 700, 220, 740));
    // Definir texto a ser exibido como valor do campo
    floatingField->set_Value(u"Este é o \"campo de texto flutuante\".");
    // Recomendamos tornar o campo 'somente leitura' para este cenário
    floatingField->set_ReadOnly(true);
    // Definir flag 'oculto' para tornar o campo invisível na abertura do documento
    floatingField->set_Flags(floatingField->get_Flags() | Aspose::Pdf::Annotations::AnnotationFlags::Hidden);

    // Definir um nome de campo único não é necessário, mas permitido
    floatingField->set_PartialName (u"FloatingField_1");

    // Definir características de aparência do campo não é necessário, mas melhora
    floatingField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>("Helv", 10, Color::get_Blue()));
    floatingField->get_Characteristics()->set_Background (System::Drawing::Color::get_LightBlue());
    floatingField->get_Characteristics()->set_Border (System::Drawing::Color::get_DarkBlue());
    floatingField->set_Border(MakeObject<Aspose::Pdf::Annotations::Border>(floatingField));
    floatingField->get_Border()->set_Width (1);
    floatingField->set_Multiline (true);

    // Adicionar campo de texto ao documento
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(floatingField));

    // Criar botão invisível na posição do fragmento de texto
    auto buttonField = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
    // Criar nova ação de ocultar para o campo (anotação) especificado e flag de invisibilidade.
    // (Você também pode referir-se ao campo flutuante pelo nome se o especificou acima.)
    // Adicionar ações na entrada/saída do mouse no campo do botão invisível
    buttonField->get_Actions()->set_OnEnter(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField, false));
    buttonField->get_Actions()->set_OnExit(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField));

    // Adicionar campo de botão ao documento
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(buttonField));

    // Salvar documento
    document->Save(outputFileName);
}
```