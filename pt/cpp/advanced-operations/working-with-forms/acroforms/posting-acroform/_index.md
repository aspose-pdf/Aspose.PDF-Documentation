---
title: Posting AcroForm Data
linktitle: Posting AcroForm
type: docs
weight: 50
url: /pt/cpp/posting-acroform-data/
description: Você pode importar e exportar dados de formulário para um arquivo XML com o namespace Aspose.Pdf.Facades no Aspose.PDF para C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

AcroForm é um tipo importante de documento PDF. Você pode não apenas criar e editar um AcroForm usando o [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades), mas também importar e exportar dados de formulário para um arquivo XML. O namespace Aspose.Pdf.Facades no Aspose.PDF para C++ permite que você implemente outra funcionalidade do AcroForm, que ajuda a postar dados de um AcroForm para uma página web externa. Esta página web então lê as variáveis postadas e usa esses dados para processamento adicional. Esta funcionalidade é útil nos casos em que você não quer apenas manter os dados no arquivo PDF, mas sim enviá-los para o seu servidor e depois salvá-los em um banco de dados etc.

{{% /alert %}}

## Detalhes da implementação

Neste artigo, tentamos criar um AcroForm usando o [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades) e a classe [FormEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form_editor/). Também adicionamos um botão de envio e definimos seu URL de destino.

Os seguintes trechos de código mostram como criar o formulário e depois receber os dados postados na página web.
```cpp
using namespace System;
using namespace Aspose::Pdf;

void PostingExample() {

    // String _dataDir("C:\\Samples\\");
    // Crie uma instância da classe FormEditor e vincule arquivos pdf de entrada e saída
    auto editor = MakeObject<Aspose::Pdf::Facades::FormEditor>("input.pdf", "output.pdf");

    // Crie campos AcroForm - criei apenas dois campos para simplicidade
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"firstname", 1, 100, 600, 200, 625);
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"lastname", 1, 100, 550, 200, 575);

    // Adicione um botão de envio e defina a URL de destino
    editor->AddSubmitBtn(u"submitbutton", 1, u"Enviar", u"http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

    // Salve o arquivo pdf de saída
    editor->Save();
}
```