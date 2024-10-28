---
title: Criar Links em Arquivo PDF com C++
linktitle: Criar Links
type: docs
weight: 10
url: /cpp/create-links/
description: Esta seção explica como criar links em seu documento PDF com C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Criar Links

Ao adicionar um link para um aplicativo em um documento, é possível vincular a aplicativos a partir de um documento. Isso é útil quando você deseja que os leitores realizem uma determinada ação em um ponto específico de um tutorial, por exemplo, ou para criar um documento rico em recursos. Para criar um link de aplicativo:

1. [Crie um Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) objeto.
1. Obtenha a [Página](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) à qual você deseja adicionar o link.
1. Crie um objeto [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) usando os objetos Página e [Retângulo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle).
1. Set the link attributes using the [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) object.
1. Além disso, defina o objeto [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/) como propriedade Action.
1. Ao criar o objeto [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/), especifique o aplicativo que você deseja iniciar.
1. Adicione o link à propriedade [Annotations](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.annotations) do objeto Page.
1. Finalmente, salve o PDF atualizado usando o método Save do objeto Document.

O trecho de código a seguir mostra como criar um link para um aplicativo em um arquivo PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;

void CreateLink() 
{
    String _dataDir("C:\\Samples\\");
    // Create Document instance
    auto document = MakeObject<Document>(_dataDir + u"CreateApplicationLink.pdf");

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->idx_get(1);

    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::LaunchAction>(document, _dataDir + u"sample.pdf"));
    page->get_Annotations()->Add(link);

    // Save updated document
    document->Save(_dataDir + u"CreateApplicationLink.pdf");
}
```
### Criar Link de Documento PDF em um Arquivo PDF

Aspose.PDF para C++ permite que você adicione um link para um arquivo PDF externo, de forma que você possa ligar vários documentos juntos. Para criar um link de documento PDF:

1. Primeiro, crie um objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Em seguida, obtenha a [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) específica à qual você deseja adicionar o link.
1. Crie um objeto [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) usando os objetos Page e [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle).
1. Defina os atributos do link usando o objeto [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).
1. Defina a propriedade Action para o objeto [GoToRemoteAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_remote_action/).
1. Ao criar o objeto GoToRemoteAction, especifique o arquivo PDF que deve ser lançado, assim como o número da página que deve abrir.
1. Adicione o link à coleção de Annotations do objeto Page.
1. Salve o PDF atualizado usando o método Save do objeto Document.

O trecho de código a seguir mostra como criar um link de documento PDF em um arquivo PDF.

```cpp
void CreatePDFDocumentLink() 
{

    String _dataDir("C:\\Samples\\");
    // Create Document instance
    auto document = MakeObject<Document>(_dataDir + u"CreateDocumentLink.pdf");

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->idx_get(1);


    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());

    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToRemoteAction>(_dataDir + u"sample.pdf", 1));
    page->get_Annotations()->Add(link);

    // Save updated document
    document->Save(_dataDir + u"CreateDocumentLink_out.pdf");
}
```