---
title: Convert PDF to Microsoft Word Documents in C++
linktitle: Convert PDF to Word
type: docs
weight: 10
url: /cpp/convert-pdf-to-word/
lastmod: "2021-11-19"
description: Aspose.PDF for C++ library permite que você converta PDF para formato Word usando C++ com facilidade e controle total. Esses formatos incluem DOC e DOCX. Saiba mais sobre como ajustar a conversão de documentos PDF para Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Visão Geral

Este artigo explica como converter documentos PDF para Microsoft Word usando C++. Ele abrange esses tópicos.

_Formato_: **DOC**
- [C++ PDF para DOC](#cpp-pdf-to-doc)
- [C++ Converter PDF para DOC](#cpp-pdf-to-doc)
- [C++ Como converter arquivo PDF para DOC](#cpp-pdf-to-doc)

_Formato_: **DOCX**
- [C++ PDF para DOCX](#cpp-pdf-to-docx)
- [C++ Converter PDF para DOCX](#cpp-pdf-to-docx)
- [C++ Como converter arquivo PDF para DOCX](#cpp-pdf-to-docx)

_Formato_: **Formato Microsoft Word DOC**
- [C++ PDF para Word](#cpp-pdf-to-word-doc)
- [C++ Converter PDF para Word](#cpp-pdf-to-word-doc)

- [C++ Como converter arquivo PDF para Word](#cpp-pdf-to-word-doc)

_Format_: **Formato Microsoft Word DOCX**
- [C++ PDF para Word](#cpp-pdf-to-word-docx)
- [C++ Converter PDF para Word](#cpp-pdf-to-word-docx)
- [C++ Como converter arquivo PDF para Word](#cpp-pdf-to-word-docx)

Outros tópicos abordados por este artigo
- [Veja Também](#see-also)

## Conversões de PDF para Word em C++

Uma das características mais populares é a conversão de PDF para DOC do Microsoft Word, o que torna o conteúdo fácil de manipular. O Aspose.PDF para C++ permite converter arquivos PDF para DOC.

## Converter arquivo PDF para DOC (Word 97-2003)

Converta arquivo PDF para o formato DOC com facilidade e total controle. O Aspose.PDF para C++ é flexível e suporta uma ampla variedade de conversões. Converter páginas de documentos PDF para imagens, por exemplo, é um recurso muito popular.

Uma conversão que muitos dos nossos clientes solicitaram é de PDF para DOC: converter um arquivo PDF em um documento do Microsoft Word. Clientes querem isso porque arquivos PDF não podem ser facilmente editados, enquanto documentos Word podem. Algumas empresas querem que seus usuários sejam capazes de manipular texto, tabelas e imagens em arquivos que começaram como PDFs.

Mantendo viva a tradição de tornar as coisas simples e compreensíveis, o Aspose.PDF para C++ permite que você transforme um arquivo PDF de origem em um arquivo DOC com duas linhas de código. Para realizar esse recurso, introduzimos uma enumeração chamada SaveFormat e seu valor .Doc permite que você salve o arquivo de origem no formato Microsoft Word.

O seguinte trecho de código em C++ mostra o processo de conversão de um arquivo PDF para o formato DOC.

<a name="cpp-pdf-to-doc" id="cpp-pdf-to-doc"><strong>Passos: Converter PDF para DOC em C++</strong></a> | <a name="cpp-pdf-to-word-doc" id="cpp-pdf-to-word-doc"><strong>Passos: Converter PDF para formato DOC do Microsoft Word em C++</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) com o documento PDF de origem.
2. Salve-o no formato **SaveFormat::Doc** chamando o método **Document->Save()**.

```cpp
void ConvertPDFtoWord()
{
    std::clog << __func__ << ": Início" << std::endl;
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para o nome do arquivo
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // Salvar o arquivo no formato de documento do MS
        document->Save(_dataDir + outfilename, SaveFormat::Doc);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Fim" << std::endl;
}
```

O seguinte trecho de código mostra o processo de conversão de um arquivo PDF para DOC versão Avançada:

```cpp
void ConvertPDFtoWordDocAdvanced()
{
    std::clog << __func__ << ": Início" << std::endl;
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para o nome do arquivo
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::Doc);
    // Definir o modo de reconhecimento como Fluxo
    saveOptions->set_Mode(DocSaveOptions::RecognitionMode::Flow);
    // Definir a proximidade horizontal como 2.5
    saveOptions->set_RelativeHorizontalProximity(2.5f);
    // Ativar o valor para reconhecer marcadores durante o processo de conversão
    saveOptions->set_RecognizeBullets(true);

    try {
        // Salvar o arquivo no formato de documento do MS
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Fim" << std::endl;
}
```
{{% alert color="success" %}}
**Tente converter PDF para DOC online**

Aspose.PDF para C++ apresenta a você o aplicativo online gratuito ["PDF para DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Converter PDF para DOC](pdf_to_doc.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Converter PDF para DOCX

Aspose.PDF para C++ API permite que você leia e converta documentos PDF para DOCX usando a linguagem C++. DOCX é um formato bem conhecido para documentos do Microsoft Word cuja estrutura foi alterada de binário simples para uma combinação de arquivos XML e binários. Arquivos Docx podem ser abertos com o Word 2007 e versões posteriores, mas não com as versões anteriores do MS Word que suportam extensões de arquivo DOC.

O seguinte trecho de código C++ mostra o processo de conversão de um arquivo PDF para o formato DOCX.


<a name="cpp-pdf-to-docx" id="cpp-pdf-to-docx"><strong>Passos: Converter PDF para DOCX em C++</strong></a> | <a name="cpp-pdf-to-word-docx" id="cpp-pdf-to-word-docx"><strong>Passos: Converter PDF para o formato Microsoft Word DOCX em C++</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) com o documento PDF de origem.
2. Salve-o no formato **SaveFormat::DocX** chamando o método **Document->Save()**.

```cpp
void ConvertPDFtoWord_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para o nome do arquivo
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // Salvar o arquivo no formato de documento MS
        document->Save(_dataDir + outfilename, SaveFormat::DocX);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

A classe [`DocSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) tem uma propriedade chamada Format que oferece a capacidade de especificar o formato do documento resultante, ou seja, DOC ou DOCX. Para converter um arquivo PDF para o formato DOCX, por favor, passe o valor Docx da enumeração DocSaveOptions.DocFormat.

Por favor, veja o trecho de código a seguir que fornece a capacidade de converter um arquivo PDF para o formato DOCX com C++.

```cpp
void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::DocX);

    // Definir outros parâmetros do DocSaveOptions
    // ...

    // Salvar o arquivo no formato de documento do MS

    try {
        // Salvar o arquivo no formato de documento do MS
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="warning" %}}
**Tente converter PDF para DOCX online**

Aspose.PDF para C++ apresenta a você a aplicação online gratuita ["PDF para DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Convertion PDF para Word App Gratuito](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Veja Também

Este artigo também aborda estes tópicos. Os códigos são os mesmos que acima.

_Formato_: **Formato Microsoft Word DOC**
- [Código C++ PDF para Word](#cpp-pdf-to-word-doc)
- [API C++ PDF para Word](#cpp-pdf-to-word-doc)
- [Programação C++ PDF para Word](#cpp-pdf-to-word-doc)
- [Biblioteca C++ PDF para Word](#cpp-pdf-to-word-doc)
- [Salvar PDF como Word em C++ ](#cpp-pdf-to-word-doc)
- [Gerar Word a partir de PDF em C++](#cpp-pdf-to-word-doc)
- [Criar Word a partir de PDF em C++](#cpp-pdf-to-word-doc)
- [Conversor C++ PDF para Word](#cpp-pdf-to-word-doc)

_Formato_: **Formato Microsoft Word DOCX**

- [Código C++ PDF para Word](#cpp-pdf-to-word-docx)
- [C++ PDF para Word API](#cpp-pdf-to-word-docx)
- [C++ PDF para Word Programaticamente](#cpp-pdf-to-word-docx)
- [C++ PDF para Word Biblioteca](#cpp-pdf-to-word-docx)
- [C++ Salvar PDF como Word](#cpp-pdf-to-word-docx)
- [C++ Gerar Word a partir de PDF](#cpp-pdf-to-word-docx)
- [C++ Criar Word a partir de PDF](#cpp-pdf-to-word-docx)
- [C++ PDF para Word Conversor](#cpp-pdf-to-word-docx)

_Format_: **DOC**
- [C++ PDF para DOC Código](#cpp-pdf-to-doc)
- [C++ PDF para DOC API](#cpp-pdf-to-doc)
- [C++ PDF para DOC Programaticamente](#cpp-pdf-to-doc)
- [C++ PDF para DOC Biblioteca](#cpp-pdf-to-doc)
- [C++ Salvar PDF como DOC](#cpp-pdf-to-doc)
- [C++ Gerar DOC a partir de PDF](#cpp-pdf-to-doc)
- [C++ Criar DOC a partir de PDF](#cpp-pdf-to-doc)
- [C++ PDF para DOC Conversor](#cpp-pdf-to-doc)

_Format_: **DOC**
- [C++ PDF para DOCX Código](#cpp-pdf-to-docx)
- [C++ PDF para DOCX API](#cpp-pdf-to-docx)
- [C++ PDF para DOCX Programaticamente](#cpp-pdf-to-docx)
- [C++ PDF para DOCX Biblioteca](#cpp-pdf-to-docx)
- [C++ Salvar PDF como DOCX](#cpp-pdf-to-docx)

- [C++ Gerar DOCX a partir de PDF](#cpp-pdf-to-docx)
- [C++ Criar DOCX a partir de PDF](#cpp-pdf-to-docx)  
- [Conversor C++ de PDF para DOCX](#cpp-pdf-to-docx)