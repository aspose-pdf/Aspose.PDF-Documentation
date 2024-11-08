---
title: Trabalhando com Cabeçalhos em PDF
type: docs
weight: 90
url: /pt/cpp/working-with-headings/
lastmod: "2021-11-11"
description: Crie numeração no cabeçalho do seu documento PDF com C++. Aspose.PDF para C++ mostra diferentes tipos de estilos de numeração.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aplicar Estilo de Numeração no Cabeçalho

Qualquer texto em um documento começa com um cabeçalho. Os cabeçalhos são uma parte integral do conteúdo, independentemente do estilo e tema.
Os cabeçalhos ajudam a chamar a atenção para o texto e ajudam os usuários a encontrar a informação de que precisam no documento, melhorando a legibilidade e a percepção visual. Usando estilos de cabeçalho, você também pode criar rapidamente um índice, alterar a estrutura do documento.
Então, vamos ver como trabalhar com cabeçalhos usando a biblioteca Aspose.PDF para C++.

[Aspose.PDF para C++](/pdf/pt/cpp/) oferece muitos estilos de numeração pré-definidos. Estas estilos de numeração pré-definidos são armazenados em uma enumeração, NumberingStyle. Os valores pré-definidos da enumeração NumberingStyle e suas descrições são fornecidos abaixo:

|**Tipos de Cabeçalho**|**Descrição**|
| :- | :- |
|NumeralsArabic|Tipo árabe, por exemplo, 1,1.1,...|
|NumeralsRomanUppercase|Tipo romano maiúsculo, por exemplo, I,I.II, ...|
|NumeralsRomanLowercase|Tipo romano minúsculo, por exemplo, i,i.ii, ...|
|LettersUppercase|Tipo inglês maiúsculo, por exemplo, A,A.B, ...|
|LettersLowercase|Tipo inglês minúsculo, por exemplo, a,a.b, ...|
A propriedade **Style** da classe **Aspose.PDF.Heading** é usada para definir os estilos de numeração dos cabeçalhos.

|**Figura: Estilos de numeração pré-definidos**|
| :- |
O código-fonte, para obter a saída mostrada na figura acima, é fornecido abaixo no exemplo.

```cpp
void WorkingWithHeadingsInPDF() {
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de entrada
    String outputFileName("ApplyNumberStyle_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>();

    document->get_PageInfo()->set_Width(612.0);
    document->get_PageInfo()->set_Height(792.0);
    document->get_PageInfo()->set_Margin(MakeObject<MarginInfo>());
    document->get_PageInfo()->get_Margin()->set_Left(72);
    document->get_PageInfo()->get_Margin()->set_Right(72);
    document->get_PageInfo()->get_Margin()->set_Top(72);
    document->get_PageInfo()->get_Margin()->set_Bottom(72);
            
    auto pdfPage = document->get_Pages()->Add();
    pdfPage->get_PageInfo()->set_Width(612.0);
    pdfPage->get_PageInfo()->set_Height(792.0);
    pdfPage->get_PageInfo()->set_Margin(MakeObject<MarginInfo>());
    pdfPage->get_PageInfo()->get_Margin()->set_Left(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Right(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Top(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Bottom(72);

    auto floatBox = MakeObject<FloatingBox>();
    floatBox->set_Margin(pdfPage->get_PageInfo()->get_Margin());

    pdfPage->get_Paragraphs()->Add(floatBox);

    auto textFragment = MakeObject<TextFragment>();
    auto segment = MakeObject<TextSegment>();

    auto heading = MakeObject<Heading>(1);
    heading->set_IsInList(true);
    heading->set_StartNumber(1);
    heading->set_Text(u"List 1");
    heading->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading);

    auto heading2 = MakeObject<Heading>(1);
    heading2->set_IsInList(true);
    heading2->set_StartNumber(13);
    heading2->set_Text(u"List 2");
    heading2->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading2->set_IsAutoSequence(true);;

    floatBox->get_Paragraphs()->Add(heading2);

    auto heading3 = MakeObject<Heading>(2);
    heading3->set_IsInList(true);
    heading3->set_StartNumber(1);
    heading3->set_Text(u"o valor, na data efetiva do plano, da propriedade a ser distribuída sob o plano em razão de cada permitido");
    heading3->set_Style(NumberingStyle::LettersLowercase);
    heading3->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading3); 

    // Salvar arquivo de saída concatenado
    document->Save(_dataDir + outputFileName);
}
```