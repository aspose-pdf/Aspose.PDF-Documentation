---
title: Converter formatos PDF para PDF/A
linktitle: Converter formatos PDF para PDF/A
type: docs
weight: 100
url: pt/cpp/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: Este tópico mostra como o Aspose.PDF permite converter um arquivo PDF em um arquivo PDF compatível com PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for C++** permite que você converta um arquivo PDF em um arquivo PDF compatível com <abbr title="Portable Document Format / A">PDF/A</abbr>. Antes de fazer isso, o arquivo deve ser validado. Este tópico explica como.

{{% alert color="primary" %}}

Por favor, note que seguimos o Adobe Preflight para validar a conformidade com PDF/A. Todas as ferramentas do mercado têm sua própria "representação" de conformidade com PDF/A. Por favor, consulte este artigo sobre ferramentas de validação de PDF/A para referência. Escolhemos os produtos da Adobe para verificar como o Aspose.PDF produz arquivos PDF porque a Adobe está no centro de tudo relacionado ao PDF.

{{% /alert %}}

Converta o arquivo usando o método Convert da classe Document. Antes de converter o PDF para um arquivo compatível com PDF/A, valide o PDF usando o método Validate. O resultado da validação é armazenado em um arquivo XML e, em seguida, esse resultado também é passado para o método Convert. Você também pode especificar a ação para os elementos que não podem ser convertidos usando a enumeração ConvertErrorAction. 

## Converter arquivo PDF para PDF/A-1b

O trecho de código a seguir mostra como converter arquivos PDF para PDF compatível com PDF/A-1b.

```cpp
void ConverttoPDFA_1b()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo de entrada
    String infilename("sample.pdf");
    // String para nome do arquivo de log
    String logfilename("log.xml");
    // String para nome do arquivo de saída
    String outfilename("PDFToPDFA_out.pdf");

    // Abrir documento
    auto document = new Document(_dataDir + infilename);

    // Converter para documento compatível com PDF/A
    // Durante o processo de conversão, a validação também é realizada
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

    // Salvar documento de saída
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
Para realizar apenas a validação, use a seguinte linha de código:

```cpp
void ConverttoPDFA_1b_Validation()
{
    std::clog << __func__ << ": Início" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo de entrada
    String infilename("sample.pdf");
    // String para nome do arquivo de log
    String logfilename("log.xml");

    // Abrir documento
    auto document = new Document(_dataDir + infilename);

    // Converter para documento compatível com PDF/A
    // Durante o processo de conversão, a validação também é realizada
    document->Validate(_dataDir + logfilename, PdfFormat::PDF_A_1B);
    std::clog << __func__ << ": Fim" << std::endl;
}
```

## Converter arquivo PDF para PDF/A-3b

Aspose.PDF para C++ também suporta o recurso de converter um arquivo PDF para o formato PDF/A-3b.

```cpp
void ConverttoPDFA_3b()
{
    std::clog << __func__ << ": Início" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo de entrada
    String infilename("sample.pdf");
    // String para nome do arquivo de log
    String logfilename("log.xml");
    // String para nome do arquivo de saída
    String outfilename("PDFToPDFA3b_out.pdf");

    // Abrir documento
    auto document = new Document(_dataDir + infilename);

    // Converter para documento compatível com PDF/A
    // Durante o processo de conversão, a validação também é realizada
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3B, ConvertErrorAction::Delete);

    // Salvar documento de saída
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Fim" << std::endl;
}
```

## Convert PDF file to PDF/A-2u

Aspose.PDF para C++ também suporta o recurso de converter um arquivo PDF para o formato PDF/A-2u.

```cpp
void ConverttoPDFA_2u()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo de entrada
     String infilename("sample.pdf");
    // String para nome do arquivo de log
    String logfilename("log.xml");
    // String para nome do arquivo de saída
    String outfilename("PDFToPDFA3b_out.pdf");

    // Abrir documento
    auto document = new Document(_dataDir + infilename);

    // Converter para documento compatível com PDF/A
    // Durante o processo de conversão, a validação também é realizada
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // Salvar documento de saída
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convert PDF file to PDF/A-3u

Aspose.PDF para C++ também suporta o recurso de converter um arquivo PDF para o formato PDF/A-3u.

```cpp
void ConverttoPDFA_3u()
{
    std::clog << __func__ << ": Iniciar" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo de entrada
    String infilename("sample.pdf");
    // String para nome do arquivo de log
    String logfilename("log.xml");
    // String para nome do arquivo de saída
    String outfilename("PDFToPDFA3b_out.pdf");

    // Abrir documento
    auto document = new Document(_dataDir + infilename);

    // Converter para documento compatível com PDF/A
    // Durante o processo de conversão, a validação também é realizada
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // Salvar documento de saída
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Terminar" << std::endl;
}
```

## Adicionar Anexo ao arquivo PDF/A

Caso você tenha a necessidade de anexar arquivos ao formato de conformidade PDF/A, então recomendamos usar o valor PDF_A_3A da enumeração Aspose.PDF.PdfFormat.

PDF/A_3a é o formato que fornece o recurso de anexar qualquer formato de arquivo como um anexo ao arquivo compatível com PDF/A.

```cpp
void ConverttoPDFA_AddAttachment()
{
    std::clog << __func__ << ": Iniciar" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo de entrada
    String infilename("sample.pdf");
    // String para nome do arquivo de log
    String logfilename("log.xml");
    // String para nome do arquivo de saída
    String outfilename("PDFToPDFA3b_out.pdf");

    // Abrir documento
    auto document = new Document(_dataDir + infilename);

    // Configurar novo arquivo para ser adicionado como anexo
    auto fileSpecification = MakeObject<FileSpecification>(_dataDir + String("aspose-logo.jpg"), String("Arquivo de imagem grande"));
    // Adicionar anexo à coleção de anexos do documento
    document->get_EmbeddedFiles()->Add(fileSpecification);

    // Converter para documento compatível com PDF/A
    // Durante o processo de conversão, a validação também é realizada
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3A, ConvertErrorAction::Delete);

    // Salvar documento de saída
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Terminar" << std::endl;
}
```

## Substituir fontes ausentes por fontes alternativas

De acordo com os padrões PDFA, as fontes devem estar incorporadas no documento PDFA. No entanto, se as fontes não estiverem incorporadas no documento de origem ou existirem na máquina, o PDFA falha na validação. Neste caso, temos a necessidade de substituir fontes ausentes por algumas fontes alternativas da máquina. Podemos substituir fontes ausentes usando o método SimpleFontSubsituation conforme a seguir durante a conversão de PDF para PDFA.

```cpp
void ConverttoPDFA_ReplaceFont()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo de entrada
    String infilename("sample.pdf");
    // String para nome do arquivo de log
    String logfilename("log.xml");
    // String para nome do arquivo de saída
    String outfilename("PDFToPDFA3b_out.pdf");

    // Abrir documento
    auto document = new Document(_dataDir + infilename);

    System::SharedPtr<Aspose::Pdf::Text::Font> originalFont;
    try
    {
        originalFont = FontRepository::FindFont(String("AgencyFB"));
    }
    catch (Exception)
    {
        // Fonte está ausente na máquina de destino
        auto substitutions = FontRepository::get_Substitutions();
        auto substitution = MakeObject<SimpleFontSubstitution>(String("AgencyFB"), String("Helvetica"));
        substitutions->Add(substitution);
    }

    // Converter para documento compatível com PDF/A
    try {
        // Durante o processo de conversão, a validação também é realizada
        document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

        // Salvar documento de saída
        document->Save(_dataDir + outfilename);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="primary" %}}
**Tente converter PDF para PDF/A online**

Aspose.PDF para C++ apresenta a você o aplicativo online gratuito ["PDF para PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF de PDF para PDF/A com Aplicativo Gratuito](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}