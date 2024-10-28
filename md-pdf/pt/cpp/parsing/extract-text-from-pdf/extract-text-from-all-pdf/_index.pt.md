---
title: Extrair texto de todas as páginas de um PDF usando C++
linktitle: Extrair texto do PDF
type: docs
weight: 10
url: /cpp/extract-text-from-all-pdf/
description: Este artigo descreve várias maneiras de extrair texto de documentos PDF usando Aspose.PDF em C++. De páginas inteiras, de uma parte específica, com base em colunas, etc.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Texto de Todas as Páginas de um Documento PDF

Extrair texto de um documento PDF é uma exigência comum. No exemplo a seguir, você verá como o Aspose.PDF para C++ permite extrair texto de todas as páginas de um documento PDF. Você precisa criar um objeto da classe [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). Depois disso, abra o PDF usando a classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) e chame o método 'Accept' da coleção [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). A classe [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) absorve o texto do documento e retorna na propriedade 'Text'. O trecho de código a seguir mostra como extrair texto de todas as páginas de um documento PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ExtractTextFromAllThePages() {

    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para nome do arquivo
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Criar objeto TextAbsorber para extrair texto
    auto textAbsorber = MakeObject<TextAbsorber>();
    // Aceitar o absorvedor para todas as páginas
    document->get_Pages()->Accept(textAbsorber);
    // Obter o texto extraído
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
Chame o método **Accept** em uma página específica do objeto Document. O Índice é o número da página específica de onde o texto precisa ser extraído.

```cpp
void ExtractTextFromParticularPage() {

    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para nome do arquivo
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Criar objeto TextAbsorber para extrair texto
    auto textAbsorber = MakeObject<TextAbsorber>();
    // Aceitar o absorvedor para todas as páginas
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // Obter o texto extraído
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extrair Texto das Páginas usando Dispositivo de Texto

Você pode usar a classe [TextDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.text_device/) para extrair texto de um arquivo PDF. TextDevice usa TextAbsorber em sua implementação, assim, de fato, eles fazem a mesma coisa, mas TextDevice foi implementado apenas para unificar a abordagem "Device" para extrair qualquer coisa da página, como ImageDevice, PageDevice, etc. TextAbsorber pode extrair texto de Página, PDF inteiro ou XForm, este TextAbsorber é mais universal

### Extrair texto de todas as páginas

Os passos a seguir e o trecho de código mostram como extrair texto de um PDF usando o dispositivo de texto.

1. Crie um objeto da classe Document com o arquivo PDF de entrada especificado
1. Crie um objeto da classe TextDevice
1. Use um objeto da classe TextExtractOptions para especificar as opções de extração
1. Use o método Process da classe TextDevice para converter os conteúdos em texto
1. Salve o texto no arquivo de saída

```cpp
void ExtractTextUsingTextDevice() {

    std::clog << __func__ << ": Start" << std::endl;
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para o nome do arquivo
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto builder = MakeObject<System::Text::StringBuilder>();
    // String para armazenar o texto extraído
    String extractedText;

    for (auto page : document->get_Pages()) {
        auto textStream = MakeObject<System::IO::MemoryStream>();
        // Criar dispositivo de texto
        auto textDevice = MakeObject<Aspose::Pdf::Devices::TextDevice>();

        // Definir opções de extração de texto - definir modo de extração de texto (Bruto ou Puro)
        auto textExtOptions = MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure);

        textDevice->set_ExtractionOptions(textExtOptions);

        // Converter uma página específica e salvar texto no stream
        textDevice->Process(page, textStream);

        // Fechar stream de memória
        textStream->Close();

        // Obter texto do stream de memória
        extractedText = System::Text::Encoding::get_Unicode()->GetString(textStream->ToArray());
        builder->Append(extractedText);

    }
    // Salvar o texto extraído no arquivo de texto
    System::IO::File::WriteAllText(_dataDir + outfilename, builder->ToString());
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Extrair Texto de uma região específica da página

A classe [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) fornece a capacidade de extrair texto de uma página específica ou de todas as páginas de um documento PDF. Esta classe retorna o texto extraído na propriedade 'Text'. No entanto, se tivermos a necessidade de extrair texto de uma região específica da página, podemos usar a propriedade **Rectangle** de [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/). A propriedade Rectangle aceita um objeto Rectangle como valor e, usando esta propriedade, podemos especificar a região da página da qual precisamos extrair o texto.

O método **Accept** de uma página é chamado para extrair o texto. Crie objetos das classes [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) e [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). Chame o método 'Accept' na página individual, como **Page** Index, do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/). O **Index** é o número da página específica de onde o texto precisa ser extraído. Você pode obter texto da propriedade 'Text' da classe [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). O trecho de código a seguir mostra como extrair texto de uma página individual.

```cpp
void ExtractTextFromParticularPageRegion() {

    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para nome do arquivo
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Criar objeto TextAbsorber para extrair texto
    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
    textAbsorber->get_TextSearchOptions()->set_Rectangle(MakeObject<Rectangle>(100, 200, 250, 350));

    // Aceitar o absorvedor para todas as páginas
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // Obter o texto extraído
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;

}
```
## Extrair texto com base em colunas

PDF é um formato muito popular, e por boas razões: com PDF, você pode ter praticamente certeza de que seu documento será exibido e impresso da mesma forma em diferentes computadores.

No entanto, documentos PDF sofrem com a desvantagem de que geralmente não possuem informações sobre o que é conteúdo em parágrafos, tabelas, figuras, informações de cabeçalho/rodapé, e assim por diante.

Aspose.PDf para C++ - é uma ferramenta fácil de usar, que permite extrair texto com base em colunas.

```cpp
void ExtractTextBasedOnColumns() {

    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para nome do arquivo
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Criar objeto TextAbsorber para extrair texto
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>();


    // Aceitar o absorvedor para todas as páginas
    document->get_Pages()->Accept(textFragmentAbsorber);

    auto tfc = textFragmentAbsorber->get_TextFragments();
    for (auto tf : tfc)
    {
        // Precisa reduzir o tamanho da fonte pelo menos 70%
        auto size = tf->get_TextState()->get_FontSize() * 0.7f;
        tf->get_TextState()->set_FontSize(size);
    }
    auto stream = MakeObject<System::IO::MemoryStream>();
    document->Save(stream);
    document = MakeObject<Document>(stream);
    auto textAbsorber = MakeObject<TextAbsorber>();
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### Segunda abordagem - Usando ScaleFactor

Nesta nova versão, também introduzimos várias melhorias no TextAbsorber e no mecanismo interno de formatação de texto. Agora, durante a extração de texto usando o modo 'Puro', você pode especificar a opção [ScaleFactor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_extraction_options#a4f9a173765d483b493c31e416f8b035a) e essa pode ser outra abordagem para extrair texto de um documento PDF com múltiplas colunas além da abordagem mencionada acima. Este fator de escala pode ser configurado para ajustar a grade que é utilizada para o mecanismo interno de formatação de texto durante a extração de texto. Especificar os valores de ScaleFactor entre 1 e 0.1 (inclusive 0.1) tem o mesmo efeito que a redução da fonte.

Especificar os valores de ScaleFactor entre 0.1 e -0.1 é tratado como valor zero, mas faz com que o algoritmo calcule automaticamente o fator de escala necessário durante a extração de texto. O cálculo é baseado na largura média dos glifos da fonte mais popular na página, mas não podemos garantir que no texto extraído nenhuma string da coluna alcance o início da próxima coluna. Observe que se o valor de ScaleFactor não for especificado, o valor padrão de 1.0 será usado. Isso significa que não haverá escalonamento. Se o valor de ScaleFactor especificado for mais que 10 ou menos que -0.1, o valor padrão de 1.0 será usado.

Sugerimos o uso de escalonamento automático (ScaleFactor = 0) ao processar um grande número de arquivos PDF para extração de conteúdo de texto. Ou definir manualmente a redução redundante da largura da grade (cerca de ScaleFactor = 0.5). No entanto, você não deve determinar se o escalonamento é necessário para documentos concretos ou não. Se você definir a redução redundante da largura da grade para o documento (que não precisa disso), o conteúdo de texto extraído permanecerá totalmente adequado. Por favor, dê uma olhada no seguinte trecho de código.

```cpp
void ExtractTextUsingScaleFactor() {

    std::clog << __func__ << ": Start" << std::endl;
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para o nome do arquivo
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->set_ExtractionOptions(MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure));
    // Definir fator de escala para 0.5 é suficiente para dividir colunas na maioria dos documentos
    // A definição de zero permite ao algoritmo escolher o fator de escala automaticamente
    textAbsorber->get_ExtractionOptions()->set_ScaleFactor(0.5); /* 0; */
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Extrair Texto Destacado de Documento PDF

Em vários cenários de extração de texto de um documento PDF, você pode ter a necessidade de extrair apenas o texto destacado do documento PDF. Para implementar essa funcionalidade, adicionamos os métodos TextMarkupAnnotation.GetMarkedText() e TextMarkupAnnotation.GetMarkedTextFragments() na API. Você pode extrair o texto destacado do documento PDF filtrando TextMarkupAnnotation e usando os métodos mencionados. O trecho de código a seguir mostra como você pode extrair o texto destacado de um documento PDF.

```cpp
void ExtractHighlightedText() {

    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para nome do arquivo
    String infilename("sample-highlight.pdf");
    String outfilename("extracted-text.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Loop através de todas as anotações
    for (auto annotation : document->get_Pages()->idx_get(1)->get_Annotations())
    {
        // Filtrar TextMarkupAnnotation
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Highlight)
        {
        auto highlightedAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::HighlightAnnotation>(annotation);

        // Recuperar fragmentos de texto destacados
        auto collection = highlightedAnnotation->GetMarkedTextFragments();
        for (auto tf : collection)
        {
            // Exibir texto destacado
            String s = tf->get_Text();
            std::cout << s << std::endl;
        }
        }
    }
}
```

## Acessar Elementos de Fragmento de Texto e Segmento a partir de XML

Às vezes, precisamos acessar itens TextFragment ou TextSegment ao processar documentos PDF gerados a partir de XML. Aspose.PDF para C++ fornece acesso a esses itens por nome. O trecho de código abaixo mostra como usar essa funcionalidade.

```cpp
void AccessTextFragmentandSegmentElementsXML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para o nome do arquivo
    String infilename("sample-doc.xml");
    String outfilename("sample-doc.pdf");

    auto document = MakeObject<Document>();
    document->BindXml(_dataDir + infilename);

    System::SharedPtr<Page> page = System::DynamicCast<Aspose::Pdf::Page>(document->GetObjectById(u"mainSection"));
    // Faça algumas operações com a página
    // ...

    System::SharedPtr<TextSegment> segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(document->GetObjectById(u"product_description"));
    // Faça algumas operações com o segmento
    // ...
    document->Save(_dataDir + outfilename);

    std::clog << __func__ << ": Finish" << std::endl;
}
```