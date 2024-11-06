---
title: Anotações Adesivas em PDF usando C++
linktitle: Anotação Adesiva
type: docs
weight: 50
url: pt/cpp/sticky-annotations/
description: Este tópico sobre anotações adesivas, como exemplo mostramos a Anotação de Marca d'água no texto. É usado para representar gráficos na página. Verifique o trecho de código para resolver esta tarefa.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Anotação de Marca d'água

Uma anotação de marca d'água deve ser usada para representar gráficos que devem ser impressos em um tamanho e posição fixos em uma página, independentemente das dimensões da página impressa.

Você pode adicionar Texto de Marca d'água usando [WatermarkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.watermark_annotation/) em uma posição específica da página PDF. A opacidade da Marca d'água também pode ser controlada usando a propriedade de opacidade.

Por favor, verifique o seguinte trecho de código para adicionar WatermarkAnnotation.

```cpp
 using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void ExampleWatermarkAnnotation::AddWaterMarkAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Criar Anotação
    auto wa = MakeObject<WatermarkAnnotation>(page, MakeObject<Rectangle>(100, 500, 400, 600));

    // Adicionar anotação à coleção de Anotações da Página
    page->get_Annotations()->Add(wa);

    // Criar TextState para configurações de Fonte
    auto ts = MakeObject<TextState>();

    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Times New Roman"));
    ts->set_FontSize(32);

    // Definir nível de opacidade do Texto da Anotação
    wa->set_Opacity(0.5);

    // Adicionar Texto à Anotação
    wa->SetTextAndState(MakeArray<String>({ u"Aspose.PDF", u"Watermark", u"Demo" }), ts);

    // Salvar o Documento
    document->Save(_dataDir + u"sample_watermark.pdf");
}
```

## Obter Anotação de Marca d'Água

Por favor, tente usar o seguinte trecho de código para obter a anotação de marca d'água do documento PDF.

```cpp
void ExampleWatermarkAnnotation::GetWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Filtrar anotações usando AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // imprimir resultados
    for (auto wa : watermarkAnnotations) {
        Console::WriteLine(wa->get_Rect());
    }
}
```

## Excluir Anotação de Marca d'Água

Por favor, tente usar o seguinte trecho de código para excluir a anotação de marca d'água do documento PDF.

```cpp
void ExampleWatermarkAnnotation::DeleteWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Filtrar anotações usando AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // excluir anotações
    for (auto wa : watermarkAnnotations) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_watermark_del.pdf");
}
```