---
title: Converter arquivo PDF para outros formatos 
linktitle: Converter PDF para outros formatos 
type: docs
weight: 90
url: /cpp/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: Este tópico mostra como o Aspose.PDF permite converter arquivo PDF para outros formatos de arquivo.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Converter PDF para EPUB

{{% alert color="success" %}}
**Tente converter PDF para EPUB online**

Aspose.PDF para C++ apresenta a você a aplicação online gratuita ["PDF para EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), onde você pode tentar investigar a funcionalidade e qualidade com que funciona.

[![Aspose.PDF Conversão PDF para EPUB com Aplicativo Gratuito](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> (abreviação de Electronic Publication) é um padrão de e-book gratuito e aberto do International Digital Publishing Forum (IDPF). Os arquivos têm a extensão .epub.
EPUB é projetado para conteúdo redimensionável, o que significa que um leitor EPUB pode otimizar o texto para um dispositivo de exibição específico. EPUB também suporta conteúdo de layout fixo. O formato é destinado como um formato único que editoras e casas de conversão podem usar internamente, bem como para distribuição e venda. Ele substitui o padrão Open eBook.

Aspose.PDF para C++ também suporta o recurso de converter documentos PDF para o formato EPUB. Aspose.PDF para C++ possui uma classe chamada EpubSaveOptions que pode ser usada como o segundo argumento para o método [`Document.Save(..)`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa), para gerar um arquivo EPUB. Por favor, tente usar o seguinte trecho de código para cumprir este requisito com C++.

```cpp
void ConvertPDFtoEPUB()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo de entrada
    String infilename("sample.pdf");
    // String para nome do arquivo de saída
    String outfilename("PDFToEPUB_out.epub");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Salvar arquivo PDF no formato EPUB
    document->Save(_dataDir + outfilename, SaveFormat::Epub);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Converter PDF para LaTeX/TeX

**Aspose.PDF para C++** suporta a conversão de PDF para LaTeX/TeX. O formato de arquivo LaTeX é um formato de arquivo de texto com marcação especial e é usado no sistema de preparação de documentos baseado em TeX para composição tipográfica de alta qualidade.

Para converter arquivos PDF para TeX, o Aspose.PDF possui a classe [LaTeXSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.la_te_x_save_options) que fornece a propriedade OutDirectoryPath para salvar imagens temporárias durante o processo de conversão.

O trecho de código a seguir mostra o processo de conversão de arquivos PDF para o formato TEX com C++.

```cpp
void ConvertPDFtoLaTeX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo de entrada
    String infilename("sample.pdf");
    // String para nome do arquivo de saída
    String outfilename("PDFToTeX_out.tex");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar opção de salvamento LaTex
    auto saveOptions = MakeObject<LaTeXSaveOptions>();

    // Definir o caminho do diretório de saída para o objeto de opção de salvamento
    saveOptions->set_OutDirectoryPath(_dataDir);

    // Salvar arquivo PDF no formato LaTex
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Tente converter PDF para LaTeX/TeX online**

Aspose.PDF para C++ apresenta a você o aplicativo online gratuito ["PDF para LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF de PDF para LaTeX/TeX com Aplicativo Gratuito](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Converter PDF para Texto

**Aspose.PDF para C++** suporta a conversão de todo o documento PDF e página única para um arquivo de Texto.

### Converter todo o documento PDF para arquivo de Texto

Você pode converter um documento PDF para um arquivo TXT usando a classe [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/).

O trecho de código a seguir explica como extrair os textos de todas as páginas.

```cpp
void ConvertPDFDocToTXT()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo de entrada
    String infilename("sample.pdf");
    // String para nome do arquivo de saída
    String outfilename("input_Text_Extracted_out.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();
    ta->Visit(document);
    // Salvar o texto extraído no arquivo de texto
    System::IO::File::WriteAllText(_dataDir + outfilename, ta->get_Text());
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### Converter página PDF para arquivo de texto

Você pode converter um documento PDF para um arquivo TXT com Aspose.PDF para C++. Você deve usar a classe [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/) para resolver esta tarefa.

O trecho de código a seguir explica como extrair os textos das páginas específicas.

```cpp
void ConvertPDFPagestoTXT()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo de entrada
    String infilename("sample-4pages.pdf");
    // String para nome do arquivo de saída
    String outfilename("sample-4pages_out.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();

    auto pages = { 1, 3, 4 };
    try {
    for (auto page : pages)
    {
    ta->Visit(document->get_Pages()->idx_get(page));
    }
    // Salvar o texto extraído em arquivo de texto
    auto text = ta->get_Text();
    System::IO::File::WriteAllText(_dataDir + outfilename, text);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Tente converter PDF para Texto online**

Aspose.PDF para C++ apresenta a você um aplicativo online gratuito ["PDF para Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para Texto com Aplicativo Gratuito](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Converter PDF para XPS

**Aspose.PDF para C++** oferece a possibilidade de converter arquivos PDF para o formato <abbr title="XML Paper Specification">XPS</abbr>. Vamos tentar usar o trecho de código apresentado para converter arquivos PDF para o formato XPS com C++.

O tipo de arquivo XPS está principalmente associado à Especificação de Papel XML pela Microsoft Corporation. A Especificação de Papel XML (XPS), anteriormente codinome Metro e subsumindo o conceito de marketing Caminho de Impressão da Próxima Geração (NGPP), é a iniciativa da Microsoft para integrar a criação e visualização de documentos no sistema operacional Windows.

Para converter arquivos PDF para XPS, Aspose.PDF tem a classe [XpsSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xps_save_options) que é usada como o segundo argumento do método [Document.Save(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) para gerar o arquivo XPS.

O trecho de código a seguir mostra o processo de conversão de um arquivo PDF para o formato XPS.

```cpp
void ConvertPDFtoXPS()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para o nome do arquivo de entrada
    String infilename("sample.pdf");
    // String para o nome do arquivo de saída
    String outfilename("PDFToXPS_out.xps");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar opção de salvamento LaTex
    auto saveOptions = MakeObject<XpsSaveOptions>();

    // Salvar arquivo PDF no formato XPS
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Tente converter PDF para SVG online**

Aspose.PDF para C++ apresenta a você o aplicativo online gratuito ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.


[![Aspose.PDF Convertion PDF to SVG with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)