---
title: Trabalhando com Formulários XFA usando C++
linktitle: Formulários XFA
type: docs
weight: 20
url: /pt/cpp/xfa-forms/
description: Aspose.PDF para C++ API permite que você trabalhe com campos XFA e XFA Acroform em um documento PDF. O Aspose.PDF.Facades.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Formulários XFA é a Arquitetura de Formulários XML, uma família de especificações XML proprietárias que foram propostas e desenvolvidas pela JetForm para melhorar o manuseio de formulários web. Também pode ser usado em arquivos PDF começando com a especificação PDF 1.5.

Preencha campos XFA com a classe [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form/) por [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades).

## Preencher campos XFA

O trecho de código a seguir mostra como preencher campos em um formulário XFA.

```cpp
using namespace System;
using namespace System::Collections::Generic;

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void FillXFA() {
    String _dataDir("C:\\Samples\\");

    // Carregar formulário XFA
    auto document = MakeObject<Document>(_dataDir + u"FillXFAFields.pdf");

    // Obter nomes dos campos do formulário XFA
    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // Definir valores dos campos

    document->get_Form()->get_XFA()->idx_set(names->idx_get(0),u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(1),u"Field 1");

    // Salvar o documento atualizado
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```

## Converter XFA para AcroForm

{{% alert color="primary" %}}

Tente online
Você pode verificar a qualidade da conversão Aspose.PDF e visualizar os resultados online neste link: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Formulários dinâmicos são baseados em uma especificação XML conhecida como XFA, a “Arquitetura de Formulários XML”. As informações sobre o formulário (no que diz respeito a um PDF) são muito vagas – especifica que campos existem, com propriedades e eventos JavaScript, mas não especifica qualquer renderização.

Atualmente, o PDF suporta dois métodos diferentes para integrar dados e formulários PDF:

- AcroForms (também conhecidos como formulários Acrobat), introduzidos e incluídos na especificação do formato PDF 1.2.
- Formulários Adobe XML Forms Architecture (XFA), introduzidos na especificação do formato PDF 1.5 como um recurso opcional (A especificação XFA não está incluída na especificação PDF, é apenas referenciada.)

Não podemos extrair ou manipular páginas de Formulários XFA, porque o conteúdo do formulário é gerado em tempo de execução (durante a visualização do formulário XFA) dentro do aplicativo tentando exibir ou renderizar o formulário XFA. Aspose.PDF tem um recurso que permite aos desenvolvedores converter formulários XFA em AcroForms padrão.

```cpp
void ConvertXFAtoAcroForms() {

    String _dataDir("C:\\Samples\\");

    // Carregar formulário XFA
    auto document = MakeObject<Document>(_dataDir + u"DynamicXFAToAcroForm.pdf");

    // Defina o tipo de campos de formulário como AcroForm padrão
    document->get_Form()->set_Type(Aspose::Pdf::Forms::FormType::Standard);

    // Salvar o PDF resultante
    document->Save(_dataDir + u"Standard_AcroForm_out.pdf");
}
```

## Obter propriedades do campo XFA

Para acessar as propriedades dos campos, primeiro use Document.Form.XFA.Teamplate para acessar o modelo de campo. O trecho de código a seguir mostra as etapas para obter as coordenadas X e Y de um campo de formulário XFA.

```cpp
void GetXFAProprties() {

    String _dataDir("C:\\Samples\\");
    // Carregar formulário XFA
    auto document = MakeObject<Document>(_dataDir + u"GetXFAProperties.pdf");

    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // Definir valores dos campos
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 1");

    // Obter posição do campo
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"x")->get_Value());

    // Obter posição do campo
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"y")->get_Value());

    // Salvar o documento atualizado
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```