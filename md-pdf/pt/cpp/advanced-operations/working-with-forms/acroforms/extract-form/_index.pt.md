---
title: Extrair Dados AcroForm usando C++
linktitle: Extrair Dados AcroForm
type: docs
weight: 30
url: /cpp/extract-form/
description: Esta seção explica como extrair formulários do seu documento PDF com Aspose.PDF para C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obter Valores de Todos os Campos do Documento PDF

Para obter valores de todos os campos em um documento PDF, você precisa navegar por todos os campos do formulário e então obter o valor utilizando a propriedade Value. Obtenha cada campo da coleção Form, no tipo de campo base chamado Field e acesse sua propriedade Value.

Os trechos de código a seguir mostram como obter os valores de todos os campos de um documento PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void ExtractDataFromForm()
{
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");

    // Obter valores de todos os campos
    for(auto wa : document->get_Form())
    {
        auto formField = System::DynamicCast<Aspose::Pdf::Forms::Field>(wa);

        Console::WriteLine(u"Nome do Campo : {0} ", formField->get_PartialName());
        Console::WriteLine(u"Valor : {0} ", formField->get_Value());
    }
}
```

## Obter Valor de um Campo Individual de Documento PDF

A propriedade Value do campo de formulário permite que você obtenha o valor de um campo específico. Para obter o valor, obtenha o campo de formulário da coleção Form do objeto Document. Este exemplo seleciona um [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field) e recupera seu valor usando a propriedade Value.

O trecho de código a seguir mostra como obter os valores dos campos individuais em um documento PDF.

```cpp
void GetValueFromIndividualField(){

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");

    // Obter um campo
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Obter valor do campo
    Console::WriteLine(u"PartialName : {0} ", textBoxField->get_PartialName());
    Console::WriteLine(u"Value : {0} ", textBoxField->get_Value());
}
```

Para obter o URL do botão de envio, use as seguintes linhas de código.

```cpp
void GetSubmitButtonURL()
{
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");
    auto act = System::DynamicCast<Aspose::Pdf::Annotations::SubmitFormAction>(document->get_Form()->idx_get(1)->get_OnActivated());

    if (act != nullptr)
        Console::WriteLine(act->get_Url()->get_Name());
}
```

## Obter Campos de Formulário de uma Região Específica do Arquivo PDF

Às vezes, você pode saber onde em um documento um campo de formulário está, mas não ter o nome dele. Por exemplo, se tudo o que você tem para prosseguir é um esquema de um formulário impresso. Com Aspose.PDF para C++, isso não é um problema. Você pode descobrir quais campos estão em uma determinada região de um arquivo PDF. Para obter campos de formulário de uma região específica de um arquivo PDF:

1. Abra o arquivo PDF usando o objeto Document.
1. Crie um objeto retângulo para obter campos nessa área
1. Obtenha o formulário da coleção Forms do documento.
1. Exiba os nomes e valores dos Campos

O seguinte trecho de código mostra como obter campos de formulário em uma região retangular específica de um arquivo PDF.
```

```cpp
void GetFormFieldsFromSpecificRegion()
{
    String _dataDir("C:\\Samples\\");

    // Abrir arquivo pdf
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"GetFieldsFromRegion.pdf");

    // Criar objeto retângulo para obter campos nessa área
    auto rectangle = MakeObject<Aspose::Pdf::Rectangle>(35, 30, 500, 500);

    // Obter campos na área retangular
    auto fields = document->get_Form()->GetFieldsInRect(rectangle);

    // Exibir nomes e valores dos campos
    for(auto field : fields)
    {
        // Exibir propriedades de posicionamento de imagem para todos os posicionamentos
        Console::WriteLine(u"Nome do Campo: {0} - Valor do Campo: {1}", field->get_FullName(), field->get_Value());
    }
}
```