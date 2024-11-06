---
title: Converter arquivo PDF para formato HTML 
linktitle: Converter arquivo PDF para formato HTML
type: docs
weight: 50
url: pt/cpp/convert-pdf-to-html/
lastmod: "2021-11-19"
description: Este tópico mostra como o Aspose.PDF permite converter arquivo PDF para formato HTML com a biblioteca C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF para C++** oferece muitos recursos para converter vários formatos de arquivo em documentos PDF e converter arquivos PDF em vários formatos de saída. Este artigo discute como converter um arquivo PDF em <abbr title="HyperText Markup Language">HTML</abbr>. Aspose.PDF para C++ fornece a capacidade de converter arquivos HTML em formato PDF usando a abordagem InLineHtml. Recebemos muitos pedidos de funcionalidade que converte um arquivo PDF em formato HTML e fornecemos esse recurso. Por favor, note que este recurso também suporta XHTML 1.0.

**Aspose.PDF para C++** suporta os recursos para converter um arquivo PDF em HTML. As principais tarefas que você pode realizar com a biblioteca Aspose.PDF estão listadas:

- converter PDF para HTML;
- dividir Saída para HTML de Múltiplas Páginas;
- especificar Pasta para Armazenar Arquivos SVG;
- comprimir Imagens SVG Durante a Conversão;
- especificar a Pasta de Imagens;
- criar Arquivos Subsequentes apenas com Conteúdo do Corpo;
- renderização de Texto transparente;
- renderização de camadas de documentos PDF.

Aspose.PDF para C++ fornece um código de duas linhas para transformar um arquivo PDF de origem em HTML. A `enumeração SaveFormat` contém o valor Html que permite salvar o arquivo de origem em HTML. O trecho de código a seguir mostra o processo de conversão de um arquivo PDF em HTML.

```cpp
void ConvertPDFtoHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // Salvar a saída em formato HTML
    document->Save(outfilename, SaveFormat::Html);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Tente converter PDF para HTML online**

Aspose.PDF para C++ apresenta a você a aplicação online gratuita ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF de PDF para HTML com Aplicativo Gratuito](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

## Dividindo a Saída em HTML de Múltiplas Páginas

Ao converter um arquivo PDF grande com várias páginas para o formato HTML, a saída aparece como uma única página HTML. Isso pode acabar ficando muito longo. Para controlar o tamanho da página, é possível dividir a saída em várias páginas durante a conversão de PDF para HTML. Tente usar o seguinte trecho de código.

```cpp
void ConvertPDFtoHTML_SplittingOutputToMultiPageHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto HTML Save Option
    auto htmlOptions = MakeObject<HtmlSaveOptions>();
    // Especificar para dividir a saída em várias páginas
    htmlOptions->set_SplitIntoPages(true);

    try {
    // Salvar a saída no formato HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Especificar Pasta para Armazenar Arquivos SVG

Durante a conversão de PDF para HTML, é possível especificar a pasta onde as imagens SVG devem ser salvas. Use a [`HtmlSaveOption class`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options) [`SpecialFolderForSvgImages property`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#ac1bb3905c599118fb3db67fd67a5a06f) para especificar um diretório especial de imagens SVG. Esta propriedade obtém ou define o caminho para o diretório no qual as imagens SVG devem ser salvas quando encontradas durante a conversão. Se o parâmetro estiver vazio ou nulo, então quaisquer arquivos SVG são salvos junto com outros arquivos de imagem.

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringSVGfiles()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo
    String infilename("sample.pdf");
    String outfilename("SaveSVGFiles_out.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de Opção de Salvamento em HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Especificar a pasta onde as imagens SVG são salvas durante a conversão de PDF para HTML
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // Salvar a saída no formato HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Comprimindo Imagens SVG Durante a Conversão

Para comprimir imagens SVG durante a conversão de PDF para HTML, tente usar o seguinte código:

```cpp
void ConvertPDFtoHTML_CompressingSVGimages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para o nome do arquivo
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de Opção de Salvar HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Especificar a pasta onde as imagens SVG são salvas durante a conversão de PDF para HTML
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // Salvar a saída no formato HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Especificando a Pasta de Imagens

Também podemos especificar a pasta em que as imagens serão salvas durante a conversão de PDF para HTML:

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringAllImages()
{
    std::clog << __func__ << ": Iniciar" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de Opção de Salvamento em HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Especificar a pasta onde todas as imagens são salvas durante a conversão de PDF para HTML
    htmlOptions->SpecialFolderForAllImages = (_dataDir + String("\\images\\"));

    // Salvar a saída em formato HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Terminar" << std::endl;
}
```

## Criar Arquivos Subsequentes Apenas com Conteúdo do Corpo

Recentemente, fomos solicitados a introduzir um recurso onde arquivos PDF são convertidos para HTML e o usuário pode obter apenas o conteúdo da tag `<body>` para cada página. Isso produziria um arquivo com CSS, detalhes de `<html>`, `<head>` e todas as páginas em outros arquivos apenas com conteúdos `<body>`.

Para atender a esse requisito, uma nova propriedade, HtmlMarkupGenerationMode, foi introduzida na classe [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options).

Com o seguinte trecho de código simples, você pode dividir o HTML de saída em páginas. Nas páginas de saída, todos os objetos HTML devem ir exatamente onde estão agora (processamento e saída de fontes, criação e saída de CSS, criação e saída de imagens), exceto que o HTML de saída conterá conteúdos atualmente colocados dentro das tags (agora as tags “body” serão omitidas). No entanto, ao usar essa abordagem, o link para o CSS é de responsabilidade do seu código, porque coisas como serão retiradas. Para esse fim, você pode ler o CSS via File.ReadAllText() e enviá-lo via AJAX para uma página web onde será aplicado por jQuery.

```cpp
void ConvertPDFtoHTML_CreateSubsequentFilesWithBodyContentsOnly()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo
    String infilename("sample.pdf");
    String outfilename("CreateSubsequentFiles_out.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de Opção de Salvamento HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->set_SplitIntoPages(true);

    // Salvar a saída em formato HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Renderização de Texto Transparente

Caso o arquivo PDF de origem/entrada contenha textos transparentes sombreados por imagens de primeiro plano, pode haver problemas de renderização de texto. Portanto, para atender a esses cenários, as propriedades [SaveShadowedTextsAsTransparentTexts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#a6269cf414eb8c252f0ba64a0baf2f9ef) e SaveTransparentTexts podem ser usadas.

```cpp
void ConvertPDFtoHTML_TransparentTextRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo
    String infilename("sample.pdf");
    String outfilename("TransparentTextRendering_out.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de Opção de Salvar HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->SaveShadowedTextsAsTransparentTexts = true;
    htmlOptions->SaveTransparentTexts = true;

    // Salvar a saída no formato HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Renderização de camadas de documentos PDF

Podemos renderizar camadas de documentos PDF em elementos de tipo de camada separada durante a conversão de PDF para HTML:

```cpp
void ConvertPDFtoHTML_DocumentLayersRendering()
{
    std::clog << __func__ << ": Iniciar" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo
    String infilename("sample.pdf");
    String outfilename("LayersRendering_out.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de opção de salvamento em HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Especificar para renderizar camadas de documentos PDF separadamente no HTML de saída
    htmlOptions->set_ConvertMarkedContentToLayers(true);

    // Salvar a saída no formato HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Terminar" << std::endl;
}
```