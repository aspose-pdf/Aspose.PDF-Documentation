---
title: Adicionando Anexo ao Documento PDF
linktitle: Adicionando Anexo ao Documento PDF
type: docs
weight: 10
url: /pt/cpp/add-attachment-to-pdf-document/
description: Esta página descreve como adicionar um anexo a um arquivo PDF com a biblioteca Aspose.PDF para C++
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Os anexos podem conter uma ampla variedade de informações e podem ser de vários tipos de arquivos. Este artigo explica como adicionar um anexo a um arquivo PDF.

1. Crie um novo projeto C++.
1. Adicione uma referência à DLL Aspose.PDF.
1. Crie um objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Crie um objeto [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) com o arquivo que você está adicionando e a descrição do arquivo.
1. Adicione o objeto [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) à coleção [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document), usando o método Add da coleção.

A coleção [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) contém todos os anexos no arquivo PDF. O trecho de código a seguir mostra como adicionar um anexo em um documento PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithAttachments::AddingAttachment()
{

String _dataDir("C:\\Samples\\");


// Abrir documento

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddAttachment.pdf");


// Configurar novo arquivo para ser adicionado como anexo

auto fileSpecification = MakeObject<FileSpecification>(_dataDir + u"test.txt", u"Arquivo de texto de exemplo");


// Adicionar anexo à coleção de anexos do documento

pdfDocument->get_EmbeddedFiles()->Add(fileSpecification);


// Salvar nova saída

pdfDocument->Save(_dataDir + u"AddAttachment_out.pdf");
}
```