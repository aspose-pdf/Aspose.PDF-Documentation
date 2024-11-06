---
title: Converter PDF para Microsoft PowerPoint em C++
linktitle: Converter PDF para PowerPoint
type: docs
weight: 30
url: pt/cpp/convert-pdf-to-powerpoint/
description: Aspose.PDF permite converter PDF para o formato PowerPoint usando C++. Existe a possibilidade de converter PDF para PPTX com Slides como Imagens.
lastmod: "2021-11-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Visão Geral

Este artigo explica como **converter formatos PDF para PowerPoint usando C++**. Ele cobre os seguintes tópicos.

_Formato_: **PPTX**
- [C++ PDF para PPTX](#cpp-pdf-to-pptx)
- [C++ Converter PDF para PPTX](#cpp-pdf-to-pptx)
- [C++ Como converter arquivo PDF para PPTX](#cpp-pdf-to-pptx)

_Formato_: **Formato Microsoft PowerPoint PPTX**
- [C++ PDF para PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Converter PDF para PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Como converter arquivo PDF para PowerPoint](#cpp-pdf-to-powerpoint-pptx)

Outros tópicos abordados por este artigo.
- [Veja Também](#see-also)

## Conversões de PDF para PowerPoint em C++

**Aspose.PDF for C++** permite acompanhar o progresso da conversão de PDF para PPTX.

Durante a conversão de PDF para <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, o texto é renderizado como Texto onde você pode selecioná-lo/atualizá-lo. Por favor, note que para converter arquivos PDF para o formato PPTX, a Aspose.PDF fornece uma classe chamada [`PptxSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options). Um objeto da classe PptxSaveOptions é passado como segundo argumento para o método [`Document.Save(..) method`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa). O seguinte trecho de código mostra o processo para converter arquivos PDF em formato PPTX.

## Conversão simples de PDF para PPTX com Aspose.PDF para C++

Para converter PDF para PPTX, a Aspose.PDF para C++ recomenda usar as seguintes etapas de código.

<a name="cpp-pdf-to-pptx" id="cpp-pdf-to-pptx"><strong>Etapas: Converter PDF para PPTX em C++</strong></a> | <a name="cpp-pdf-to-powerpoint-pptx" id="cpp-pdf-to-powerpoint-pptx"><strong>Etapas: Converter PDF para formato PowerPoint PPTX em C++</strong></a>

1. Crie uma instância da classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
2. Crie uma instância da classe [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options).
3. Use o método **Save** do objeto **Document** para _salvar o PDF como PPTX_.

```cpp
void ConvertPDFtoPPTX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Salvar a saída no formato PPTX
    document->Save(_dataDir + outfilename, SaveFormat::Pptx);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Converter PDF para PPTX com Slides como Imagens

Caso você precise converter um PDF pesquisável para PPTX como imagens em vez de texto selecionável, o Aspose.PDF fornece tal recurso por meio da classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options). Para conseguir isso, defina a propriedade [SlidesAsImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#aeca0659ae24ea7cdeb171d941440dcb2) da classe [PptxSaveOptios](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) para 'true', como mostrado no exemplo de código a seguir.

```cpp
void ConvertPDFtoPPTX_SlidesAsImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    pptxOptions->set_SlidesAsImages(true);

    // Salvar a saída no formato PPTX
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Detalhes de Progresso da Conversão para PPTX

O Aspose.PDF para C++ permite que você acompanhe o progresso da conversão de PDF para PPTX. O [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) class fornece a propriedade [CustomProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#ac9ad606c4b4d7249c5f299fd8d766474) que pode ser especificada para um método personalizado para rastrear o progresso da conversão conforme mostrado no exemplo de código a seguir.

```cpp
void ConvertPDFtoPPTX_ProgressDetailConversion()
{
    std::clog << __func__ << ": Iniciar" << std::endl;
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para o nome do arquivo
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    //pptxOptions->set_SlidesAsImages(true);
    //Especificar Manipulador de Progresso Personalizado
    pptxOptions->set_CustomProgressHandler(ShowProgressOnConsole);

    // Salvar a saída no formato PPTX
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Terminar" << std::endl;
}
```
A seguir está o método personalizado para exibir a conversão de progresso.

```cpp
void ShowProgressOnConsole(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    switch (eventInfo->EventType)
    {
    case ProgressEventType::TotalProgress:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Progresso da conversão : " << eventInfo->Value << std::endl;
    break;
    case ProgressEventType::ResultPageCreated:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Página de resultado " << eventInfo->Value << " de " << eventInfo->MaxValue << " layout criado." << std::endl;
    break;
    case ProgressEventType::ResultPageSaved:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Página de resultado " << eventInfo->Value << " de " << eventInfo->MaxValue << " exportada." << std::endl;
    break;
    case ProgressEventType::SourcePageAnalysed:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Página de origem " << eventInfo->Value << " de " << eventInfo->MaxValue << " analisada." << std::endl;
    break;
    default:
    break;
    }
}
```

{{% alert color="success" %}}
**Tente converter PDF para PowerPoint online**

Aspose.PDF para C++ apresenta a você o aplicativo online gratuito ["PDF para PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Conversão de PDF para PPTX com Aplicativo Gratuito](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Veja Também

Este artigo também cobre estes tópicos. Os códigos são os mesmos acima.

_Formato_: **PowerPoint**
- [C++ PDF para Código PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF para API PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF para PowerPoint Programaticamente](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF para Biblioteca PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Salvar PDF como PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Gerar PowerPoint a partir do PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ Criar PowerPoint a partir do PDF](#cpp-pdf-to-powerpoint-pptx)

- [C++ Conversor de PDF para PowerPoint](#cpp-pdf-to-powerpoint-pptx)

_Format_: **Formato Microsoft PowerPoint PPTX**
- [C++ PDF para PowerPoint PPTX Código](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF para PowerPoint PPTX API](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF para PowerPoint PPTX Programaticamente](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF para PowerPoint PPTX Biblioteca](#cpp-pdf-to-powerpoint-pptx)
- [C++ Salvar PDF como PowerPoint PPTX](#cpp-pdf-to-powerpoint-pptx)
- [C++ Gerar PowerPoint PPTX de PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ Criar PowerPoint PPTX de PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ Conversor de PDF para PowerPoint PPTX](#cpp-pdf-to-powerpoint-pptx)

_Format_: **PPTX**
- [C++ PDF para PPTX Código](#cpp-pdf-to-pptx)
- [C++ PDF para PPTX API](#cpp-pdf-to-pptx)
- [C++ PDF para PPTX Programaticamente](#cpp-pdf-to-pptx)
- [C++ PDF para PPTX Biblioteca](#cpp-pdf-to-pptx)
- [C++ Salvar PDF como PPTX](#cpp-pdf-to-pptx)
- [C++ Gerar PPTX de PDF](#cpp-pdf-to-pptx)
- [C++ Criar PPTX de PDF](#cpp-pdf-to-pptx)
- [C++ Conversor de PDF para PPTX](#cpp-pdf-to-pptx)