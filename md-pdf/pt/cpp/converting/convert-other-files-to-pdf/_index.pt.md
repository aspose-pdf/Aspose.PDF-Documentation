---
linktitle: Converter outros formatos de arquivo para PDF
type: docs
weight: 80
url: /cpp/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: Este tópico mostra como o Aspose.PDF permite converter outros formatos de arquivo para documento PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Converter EPUB para PDF

**Aspose.PDF para C++** permite que você simplesmente converta arquivos EPUB para o formato PDF.

<abbr title="publicação eletrônica">EPUB</abbr> (abreviação de publicação eletrônica) é um padrão de e-book gratuito e aberto do International Digital Publishing Forum (IDPF). Os arquivos têm a extensão .epub. O EPUB é projetado para conteúdo refluível, o que significa que um leitor de EPUB pode otimizar o texto para um dispositivo de exibição específico.

O EPUB também suporta conteúdo de layout fixo. O formato é destinado como um único formato que editoras e casas de conversão podem usar internamente, assim como para distribuição e venda. Ele substitui o padrão Open eBook. A versão EPUB 3 também é endossada pelo Book Industry Study Group (BISG), uma importante associação comercial de livros para melhores práticas padronizadas, pesquisa, informação e eventos, para empacotamento de conteúdo.

Passos de conversão:

1. Crie uma [String Class](https://reference.aspose.com/pdf/cpp/class/system.string) para o nome do caminho e o nome do arquivo.
1. Crie uma instância da classe [EpubLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options).
1. Crie uma instância da classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) com o nome do arquivo de origem mencionado e opções.
1. Carregue e [Salve](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) o arquivo de entrada.

O próximo trecho de código mostra como converter arquivos EPUB para o formato PDF com C++.

```cpp
void ConvertEPUBtoPDF()
{
    std::clog << "EPUB to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("aliceDynamic.epub");
    String outfilename("epub_test.pdf");
    auto options = MakeObject<EpubLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "EPUB to PDF convert: End" << std::endl;
}
```
{{% alert color="success" %}}
**Tente converter EPUB para PDF online**

Aspose.PDF para C++ apresenta a você um aplicativo online gratuito ["EPUB para PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF EPUB para PDF com Aplicativo Gratuito](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Converter Texto para PDF

**Aspose.PDF para C++** suporta o recurso de conversão de texto simples e arquivo de texto pré-formatado para o formato PDF.

Converter texto para PDF significa adicionar fragmentos de texto à página PDF. No caso de arquivos de texto, lidamos com 2 tipos de texto: pré-formatação (por exemplo, 25 linhas com 80 caracteres por linha) e texto não formatado (texto simples). Dependendo de nossas necessidades, podemos controlar essa adição nós mesmos ou confiar aos algoritmos da biblioteca.

### Converter arquivo de texto simples para PDF

No caso do arquivo de texto simples, podemos usar a seguinte técnica:

1. Crie uma [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) para nome de caminho e nome de arquivo.
1. Leia o arquivo de texto fonte usando [TextReader](https://reference.aspose.com/pdf/cpp/class/system.i_o.text_reader/.)
1. Instancie o Objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Adicione uma [Página](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) à coleção de páginas do documento.
1. Crie um novo objeto de TextFragment e passe o objeto TextReader para seu construtor.
1. Adicione um novo parágrafo de texto na coleção de parágrafos e passe o objeto TextFragment.
1. Carregue e [Salve](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) o arquivo de entrada.

```cpp
void ConvertTextToPDF()
{
    std::clog << "Texto para PDF: Início" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.txt");
    String outfilename("TextToPDF.pdf");

    // Leia o arquivo de texto fonte
    String content = System::IO::File::ReadAllText(_dataDir + infilename);

    // Instancie um objeto Document chamando seu construtor vazio
    auto document = MakeObject<Document>();

    // Adicione uma nova página na coleção Pages do Document
    auto page = document->get_Pages()->Add();

    // Crie uma instância de TextFragment e passe o texto do objeto reader para seu construtor como argumento
    auto text = MakeObject<TextFragment>(content);

    // Adicione um novo parágrafo de texto na coleção de parágrafos e passe o objeto TextFragment
    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Salve o arquivo PDF resultante
    document->Save(_dataDir + outfilename);
    std::clog << "Texto para PDF: Fim" << std::endl;
}
```
### Converter arquivo de texto pré-formatado para PDF

Converter texto pré-formatado é como texto simples, mas você precisa fazer algumas ações adicionais, como definir margens, tipo e tamanho da fonte. Obviamente, a fonte deve ser monoespaçada (por exemplo, Courier New).

Siga estas etapas para converter texto pré-formatado em PDF com C++:

1. Instancie um objeto Document chamando seu construtor vazio.
1. Defina margens esquerda e direita para melhor apresentação.
1. Instancie o objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) e adicione uma nova página na coleção Pages.
1. Carregue e [Salve](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) o arquivo de imagem de entrada.

```CPP
void ConvertPreFormattedTextToPdf()
{
    std::clog << "Texto pré-formatado para conversão de PDF: Início" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("rfc822.txt");
    String outfilename("TextToPDF.pdf");
    // Leia o arquivo de texto como array de string
    auto lines = System::IO::File::ReadAllLines(_dataDir + infilename);

    // Instancie um objeto Document chamando seu construtor vazio
    auto document = MakeObject<Document>();

    // Adicione uma nova página na coleção Pages do Document
    auto page = document->get_Pages()->Add();

    // Defina margens esquerda e direita para melhor apresentação
    page->get_PageInfo()->get_Margin()->set_Left(20);
    page->get_PageInfo()->get_Margin()->set_Right(10);
    page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
    page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);

    for (int index = 0; index < lines->get_Length(); index++)
    {
        // verifique se a linha contém o caractere "form feed"
        // veja https://en.wikipedia.org/wiki/Page_break
        auto line = lines->idx_get(index);
        if (line.StartsWith(u"\x0c"))
        {
        if (document->get_Pages()->get_Count() > 3) break;
        page = document->get_Pages()->Add();
        // Defina margens esquerda e direita para melhor apresentação
        page->get_PageInfo()->get_Margin()->set_Left(20);
        page->get_PageInfo()->get_Margin()->set_Right(10);
        page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
        page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);
        }
        else
        {
        // Crie uma instância de TextFragment e
        // passe a linha para seu construtor como argumento
        auto text = MakeObject<TextFragment>(line);

        // Adicione um novo parágrafo de texto na coleção de parágrafos e passe o objeto TextFragment
        page->get_Paragraphs()->Add(text);
        }
    }

    // Salve o arquivo PDF resultante
    document->Save(_dataDir + outfilename);
    std::clog << "Texto pré-formatado para conversão de PDF: Fim" << std::endl;
}
```

{{% alert color="success" %}}
**Tente converter TEXTO para PDF online**

Aspose.PDF para C++ apresenta a você o aplicativo online gratuito ["Texto para PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão TEXTO para PDF com Aplicativo Gratuito](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

## Converter XPS para PDF

**Aspose.PDF para C++** suporta a funcionalidade de conversão de arquivos <abbr title="XML Paper Specification">XPS</abbr> para o formato PDF. Confira este artigo para resolver suas tarefas.

O tipo de arquivo XPS está principalmente associado à Especificação de Papel XML pela Microsoft Corporation. A Especificação de Papel XML (XPS), anteriormente codinome Metro e subsumindo o conceito de marketing Next Generation Print Path (NGPP), é a iniciativa da Microsoft para integrar a criação e visualização de documentos em seu sistema operacional Windows.

{{% alert color="primary" %}}

O formato de arquivo é basicamente um arquivo XML compactado que é usado principalmente para distribuição e armazenamento. É muito difícil de editar e é principalmente implementado pela Microsoft.

{{% /alert %}}

Para converter XPS para PDF com Aspose.PDF para C++, introduzimos uma classe chamada [XpsLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options) que é usada para inicializar um objeto [LoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options). Posteriormente, este objeto é passado como um argumento durante a inicialização do objeto Document e ajuda o mecanismo de renderização de PDF a determinar o formato de entrada do documento de origem.

O trecho de código a seguir mostra o processo de conversão de um arquivo XPS para o formato PDF com C++.

```cpp
void ConvertXPStoPDF()
{
    std::clog << "XPS to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.oxps");
    String outfilename("XPStoPDF.pdf");
    auto options = MakeObject<XpsLoadOptions>();
    try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
    };
    std::clog << "XPS to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Tente converter o formato XPS para PDF online**

Aspose.PDF para C++ apresenta a você o aplicativo online gratuito ["XPS para PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Conversão XPS para PDF com Aplicativo Gratuito](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Converter XML para PDF

O formato XML é usado para armazenar dados estruturados. Existem várias maneiras de converter <abbr title="Extensible Markup Language">XML</abbr> para PDF no Aspose.PDF.

## Converter XSL-FO para PDF

1. Crie uma [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) para o nome do caminho e o nome do arquivo.
1. Instancie o [objeto XslFoLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options).
1. Defina a estratégia de tratamento de erros.
1. Instancie o [Objeto Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. [Salvar](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) o arquivo de imagem de entrada.

```cpp
void Convert_XSLFO_to_PDF()
{
    std::clog << "XSL-FO para PDF converter: Iniciar" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilenameXSL("c:\\samples\\employees.xslt");
    String infilenameXML("c:\\samples\\employees.xml");

    String outfilename("XMLFOtoPDF.pdf");
    // Instanciar objeto XslFoLoadOption
    auto options = new XslFoLoadOptions(infilenameXSL);
    // Configurar estratégia de tratamento de erros
    options->ParsingErrorsHandlingType = XslFoLoadOptions::ParsingErrorsHandlingTypes::ThrowExceptionImmediately;
    // Criar objeto Document
    auto document = MakeObject<Document>(infilenameXML, options);
    document->Save(_dataDir + outfilename);
}
```

{{% alert color="success" %}}
**Tente converter XML para PDF online**

Aspose.PDF para C++ apresenta-lhe a aplicação gratuita online ["XML para PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.
[![Aspose.PDF Conversão XML para PDF com App Gratuito](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}