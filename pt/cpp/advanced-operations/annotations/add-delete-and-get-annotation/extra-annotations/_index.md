---
title: Anotações Extras usando C++
linktitle: Anotações Extras
type: docs
weight: 60
url: /pt/cpp/extra-annotations/
description: Esta seção descreve como adicionar, obter e excluir tipos extras de anotações do seu documento PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Como adicionar Anotação de Acento em um arquivo PDF existente

Anotação de Acento é um símbolo que indica edição de texto. Anotação de Acento também é uma anotação de marcação, então a classe Caret deriva da classe Markup e também fornece funções para obter ou definir propriedades da Anotação de Acento e redefinir o fluxo da aparência da Anotação de Acento.

Passos com os quais criamos a anotação de acento:

1. Carregar o arquivo PDF - novo [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Crie uma nova [Anotação de Colchete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/) e defina os parâmetros do Colchete (novo Retângulo, título, Assunto, Flags, cor, largura, EstiloInicial e EstiloFinal). Esta anotação é usada para indicar a inserção de texto.
1. Crie uma nova [Anotação de Colchete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/) e defina os parâmetros do Colchete (novo Retângulo, título, Assunto, Flags, cor, largura, EstiloInicial e EstiloFinal). Esta anotação é usada para indicar a substituição de texto.
1. Crie uma nova [Anotação de Tachado](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.strike_out_annotation/) e defina os parâmetros (novo Retângulo, título, cor, novos PontosQuad e novos pontos, Assunto, EmRespostaPara, TipoResposta).
1. Depois podemos adicionar anotações à página.

O trecho de código a seguir mostra como adicionar uma Anotação de Colchete a um arquivo PDF:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MarkupAnnotations::AddCaretAnnotation() {
    String _dataDir("C:\\Samples\\");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    // Esta anotação é usada para indicar a inserção de texto
    auto caretAnnotation1 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(299.988, 713.664, 308.708, 720.769));
    caretAnnotation1->set_Title(u"Aspose User");
    caretAnnotation1->set_Subject(u"Texto inserido 1");
    caretAnnotation1->set_Flags(AnnotationFlags::Print);
    caretAnnotation1->set_Color(Color::get_Blue());

    // Esta anotação é usada para indicar a substituição de texto
    auto caretAnnotation2 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        new Rectangle(361.246, 727.908, 370.081, 735.107));

    caretAnnotation2->set_Title(u"Usuário Aspose");
    caretAnnotation2->set_Flags(AnnotationFlags::Print);
    caretAnnotation2->set_Subject(u"Texto inserido 2");
    caretAnnotation2->set_Color(Color::get_Blue());

    auto strikeOutAnnotation = MakeObject<StrikeOutAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(318.407, 727.826, 368.916, 740.098));

    strikeOutAnnotation->set_Color(Color::get_Blue());

    strikeOutAnnotation->set_QuadPoints(
        MakeArray<System::SharedPtr<Point>>({
            MakeObject<Point>(321.66, 739.416),
            MakeObject<Point>(365.664, 739.416),
            MakeObject<Point>(321.66, 728.508),
            MakeObject<Point>(365.664, 728.508) }));

    strikeOutAnnotation->set_Subject(u"Riscar");
    strikeOutAnnotation->set_InReplyTo(caretAnnotation2);
    strikeOutAnnotation->set_ReplyType(ReplyType::Group);

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation1);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation2);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(strikeOutAnnotation);

    document->Save(_dataDir + u"sample_caret.pdf");
}
```
### Obter Anotação de Caret

Por favor, tente usar o seguinte trecho de código para Obter Anotação de Caret no documento PDF

```cpp
void MarkupAnnotations::GetCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // Filtrar anotações usando AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // imprimir resultados
    for (auto ca : caretAnnotations) {
        Console::WriteLine(ca->get_Rect());
    }
}
```

### Excluir Anotação de Caret

O seguinte trecho de código mostra como Excluir Anotação de Caret de um arquivo PDF.

```cpp

void MarkupAnnotations::DeleteCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // Filtrar anotações usando AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // excluir anotação
    for (auto ca : caretAnnotations) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(ca);
    }
    document->Save(_dataDir + u"sample_caret_del.pdf");
}
```

## Como adicionar Anotação de Link

Uma [Anotação de Link](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) é um link de hipertexto que leva a um destino em outro lugar no documento ou a uma ação a ser executada.

Um Link é uma área retangular que pode ser colocada em qualquer lugar da página. Cada link tem uma ação PDF correspondente associada a ele. Esta ação é executada quando o usuário clica na área deste link.

O trecho de código a seguir mostra como adicionar uma Anotação de Link a um arquivo PDF usando um exemplo de número de telefone:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLinkAnnotation() {
    String _dataDir("C:\\Samples\\");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);

    // Criar objeto TextFragmentAbsorber para encontrar um número de telefone
    auto textFragmentAbsorber = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>("678-555-0103");

    // Aceitar o absorvedor apenas para a 1ª página
    page->Accept(textFragmentAbsorber);

    auto phoneNumberFragment = textFragmentAbsorber->get_TextFragments()->idx_get(1);

    // Criar Anotação de Link e definir a ação para chamar um número de telefone
    auto linkAnnotation = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, phoneNumberFragment->get_Rectangle());
    linkAnnotation->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("callto:678-555-0103"));

    // Adicionar anotação à página
    page->get_Annotations()->Add(linkAnnotation);
    document->Save(_dataDir + u"SimpleResume_mod.pdf");
}
```

### Obter Anotação de Link

Tente usar o seguinte trecho de código para Obter LinkAnnotation de um documento PDF.

```cpp
void GetLinkAnnotations() {

    String _dataDir("C:\\Samples\\");
    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // Filtrar anotações usando AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto linkAnnotations = annotationSelector->get_Selected();

    // imprimir resultados
    for (auto la : linkAnnotations) {

        auto l = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(la);

        // Imprimir o URL de cada Anotação de Link
        Console::WriteLine(u"URI: " + System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(l->get_Action())->get_URI());

        auto absorber = MakeObject<TextAbsorber>();
        absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
        absorber->get_TextSearchOptions()->set_Rectangle(l->get_Rect());
        page->Accept(absorber);

        String extractedText = absorber->get_Text();

        // Imprimir o texto associado ao hyperlink
        Console::WriteLine(extractedText);
    }
}
```

### Excluir Anotação de Link

O trecho de código a seguir mostra como excluir a anotação de link de um arquivo PDF. Para isso, precisamos encontrar e remover todas as anotações de link na 1ª página. Após isso, salvaremos o documento com a anotação removida.

```cpp
void DeleteLinkAnnotations()
{
    String _dataDir("C:\\Samples\\");
    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // Filtrar anotações usando AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto lineAnnotations = annotationSelector->get_Selected();

    // imprimir resultados
    for (auto la : lineAnnotations) {
        page->get_Annotations()->Delete(la);
    }

    // Salvar documento com anotação removida
    document->Save(_dataDir + u"SimpleResume_del.pdf");
}
```

## Redigir certa região da página com Anotação de Redação usando Aspose.PDF para C++

Aspose.PDF para C++ suporta o recurso de adicionar e também manipular Anotações em um arquivo PDF existente. Recentemente, alguns de nossos clientes solicitaram a necessidade de redigir (remover texto, imagem, etc., elementos de) uma certa região da página de um documento PDF. Para atender a essa necessidade, uma classe chamada RedactionAnnotation é fornecida, que pode ser usada para redigir certas regiões da página ou pode ser usada para manipular RedactionAnnotations existentes e redigi-las (ou seja, achatar a anotação e remover o texto sob ela).

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;


void RedactAnnotation::AddRedactionAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Criar instância de RedactionAnnotation para região específica da página
    auto annot = MakeObject<RedactionAnnotation>(page, MakeObject<Rectangle>(200, 500, 300, 600));
    annot->set_FillColor(Color::get_Green());
    annot->set_BorderColor(Color::get_Yellow());
    annot->set_Color(Color::get_Blue());

    // Texto a ser impresso na anotação de redação
    annot->set_OverlayText(u"REDACTED");
    annot->set_TextAlignment(HorizontalAlignment::Center);

    // Repetir texto de sobreposição na anotação de redação
    annot->set_Repeat(true);

    // Adicionar anotação à coleção de anotações da primeira página
    page->get_Annotations()->Add(annot);

    // Achatar a anotação e redigir o conteúdo da página (ou seja, remove texto e imagem
    // Sob a anotação redigida)
    annot->Redact();
    document->Save(_dataDir + u"RedactPage_out.pdf");
}
```

## Abordagem de Facades

Aspose.PDF.Facades suporta a classe [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/), que fornece o recurso para manipular Anotações existentes dentro de um arquivo PDF.

Esta classe contém um método chamado [RedactArea(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a35ebd333b63b6df2c0c299c7331e3c63) que fornece a capacidade de remover certas regiões da página.

```cpp
void RedactAnnotation::AddRedactionAnnotationViaFacades() {

    String _dataDir("C:\\Samples\\");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();

    editor->BindPdf(_dataDir + u"sample.pdf");

    // Redigir certa região da página
    editor->RedactArea(1, MakeObject<Rectangle>(100, 100, 20, 70), System::Drawing::Color::get_White());
    editor->BindPdf(_dataDir + u"sample.pdf");
    editor->Save(_dataDir + u"FacadesApproach_out.pdf");
}
```