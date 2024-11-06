---
title: Criar Documento PDF
linktitle: Criar PDF
type: docs
weight: 10
url: pt/cpp/create-pdf-document/
description: Este artigo descreve como Criar e formatar o Documento PDF com Aspose.PDF para C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Estamos sempre procurando uma maneira de gerar documentos PDF e trabalhar com eles em projetos C++ de forma mais exata, precisa e eficaz. Ter funções fáceis de usar de uma biblioteca nos permite focar mais no trabalho, e menos nos detalhes demorados de tentar gerar PDFs, seja em C++.

## Gerar PDF usando C++

A API Aspose.PDF para C++ permite criar e ler arquivos PDF usando C++. A API pode ser utilizada em uma variedade de aplicações C++ incluindo WinForms, e várias outras. Neste artigo, vamos mostrar como usar a API Aspose.PDF para C++ para facilmente gerar e ler arquivos PDF em aplicações C++.

### Como Criar um Arquivo PDF Simples

Para criar um arquivo PDF usando C++, os seguintes passos podem ser usados.

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
1. Adicione um objeto [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) à coleção 'Pages' do objeto Document
1. Adicione [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) à coleção [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs) da página
1. Salve o documento PDF resultante

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateDocument() {
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo.
    String outputFileName("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Adicione texto à nova página
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Salve o PDF atualizado
    document->Save(_dataDir + outputFileName);
}
```
## Criar um documento PDF pesquisável

Aspose.PDF para C++ permite que você crie PDFs do zero e manipule os existentes. Quando você adiciona elementos de texto a um PDF, o PDF resultante é pesquisável. No entanto, se convertermos uma imagem contendo texto para um arquivo PDF, o conteúdo dentro do PDF não é pesquisável. No entanto, como solução alternativa, podemos usar OCR no arquivo resultante para torná-lo pesquisável. Portanto, primeiro você precisa instalar o Tesseract-OCR no seu sistema, e você terá um aplicativo de console tesseract.

Segue o código completo para atender a esse requisito:

```cpp
void CreateSearchableDocument() {
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");
    // String para nome do arquivo.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);
    bool convertResult = false;
    try
    {
        convertResult = document->Convert(CallBackGetHocr);
    }
    catch (Exception ex)
    {
        std::cerr << ex->get_Message() << std::endl;
    }
    document->Dispose();
}

static String CallBackGetHocr(System::SharedPtr<System::Drawing::Image> img)
{
    String tmpFile = System::IO::Path::GetTempFileNameSafe();

    auto bmp = MakeObject<System::Drawing::Bitmap>(img);

    bmp->Save(tmpFile, System::Drawing::Imaging::ImageFormat::get_Bmp());
    String inputFile = String::Format(u"\"{0}\"", tmpFile);
    String outputFile = String::Format(u"\"{0}\"", tmpFile);
    String arguments = inputFile + u" " + outputFile + u" -l eng hocr";
    String tesseractProcessName = u"C:\\Program Files\\Tesseract-OCR\\Tesseract.exe";

    auto psi = MakeObject<System::Diagnostics::ProcessStartInfo>(tesseractProcessName, arguments);
    psi->set_UseShellExecute(true);
    psi->set_CreateNoWindow(true);
    psi->set_WindowStyle(System::Diagnostics::ProcessWindowStyle::Hidden);
    psi->set_WorkingDirectory(System::IO::Path::GetDirectoryName(tesseractProcessName));

    auto p = MakeObject<System::Diagnostics::Process>(psi);
    p->Start();
    p->WaitForExit();

    auto streamReader = MakeObject<System::IO::StreamReader>(tmpFile + u".hocr");
    String text = streamReader->ReadToEnd();
    streamReader->Close();

    if (System::IO::File::Exists(tmpFile))
        System::IO::File::Delete(tmpFile);
    if (System::IO::File::Exists(tmpFile + u".hocr"))
        System::IO::File::Delete(tmpFile + u".hocr");

    return text;
}
```