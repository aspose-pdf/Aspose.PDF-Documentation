---
title: Pesquisar e Obter Texto das Páginas do Documento PDF
linktitle: Pesquisar e Obter Texto
type: docs
weight: 60
url: /pt/cpp/search-and-get-text-from-pdf/
description: Este artigo explica como usar várias ferramentas para pesquisar e obter texto de documentos PDF. Podemos pesquisar com expressões regulares em páginas específicas ou em todo o documento.
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Pesquisar e Obter Texto de Todas as Páginas do Documento PDF

A classe [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) permite que você encontre texto, correspondendo a uma frase específica, de todas as páginas de um documento PDF. Para pesquisar texto em todo o documento, você precisa chamar o método Accept da coleção [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). O método 'Accept' aceita um objeto TextFragmentAbsorber como parâmetro, que retorna uma coleção de objetos TextFragment.

O trecho de código a seguir mostra como pesquisar texto em todas as páginas.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetTextFromAllThePagesOfPDFDocument() {
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // Criar objeto TextAbsorber para encontrar todas as instâncias da frase de pesquisa de entrada
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("documento");

    // Aceitar o absorvedor para todas as páginas
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Obter os fragmentos de texto extraídos na coleção
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Percorrer os fragmentos
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"Texto :- {0}", textFragment->get_Text());
        Console::WriteLine(u"Posição :- {0}", textFragment->get_Position());
        Console::WriteLine(u"XIndent :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"YIndent :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"Fonte - Nome :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"Fonte - É Acessível :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"Fonte - Está Incorporada - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"Fonte - É Subconjunto :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"Tamanho da Fonte :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"Cor do Primeiro Plano :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```

## Search and Get Text from all pages using Regular Expression

TextFragmentAbsorber ajuda você a procurar e recuperar texto, de todas as páginas, com base em uma expressão regular. Primeiro, você precisa passar uma expressão regular para o construtor [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) como a frase. Depois disso, você deve definir a propriedade [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/) do objeto TextFragmentAbsorber. Esta propriedade requer um objeto TextSearchOptions e você precisa passar true como um parâmetro para seu construtor ao criar novos objetos. Como você deseja recuperar o texto correspondente de todas as páginas, é necessário chamar o método Accept da coleção Pages. [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) retorna um TextFragmentCollection contendo todos os fragmentos que correspondem aos critérios especificados pela expressão regular. O trecho de código a seguir mostra como pesquisar e obter texto de todas as páginas com base em uma expressão regular.

```cpp
void SearchAndGetTextFromPagesUsingRegularExpression()
{
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // Criar objeto TextAbsorber para encontrar todas as instâncias da frase de pesquisa de entrada
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(u"\\d{4}-\\d{4}"); // como 1999-2000

    // Definir opção de pesquisa de texto para especificar o uso de expressão regular
    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Aceitar o absorvedor para a primeira página do documento
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Obter os fragmentos de texto extraídos na coleção
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Percorrer os fragmentos
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"Texto :- {0}", textFragment->get_Text());
        Console::WriteLine(u"Posição :- {0}", textFragment->get_Position());
        Console::WriteLine(u"XIndent :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"YIndent :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"Fonte - Nome :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"Fonte - É Acessível :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"Fonte - Está Incorporada - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"Fonte - É Subconjunto :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"Tamanho da Fonte :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"Cor do Primeiro Plano :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```