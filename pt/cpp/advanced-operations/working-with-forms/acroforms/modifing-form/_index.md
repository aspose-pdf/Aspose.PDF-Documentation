---
title: Modificando AcroForm
linktitle: Modificando AcroForm
type: docs
weight: 40
url: /pt/cpp/modifing-form/
description: Modificando formulário em seu arquivo PDF com a biblioteca Aspose.PDF para C++. Você pode adicionar ou remover campos em um formulário existente, obter e definir limite de campo e etc.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obter ou Definir Limite de Campo

O método SetFieldLimit(field, limit) da classe FormEditor permite que você defina um limite de campo, o número máximo de caracteres que podem ser inseridos em um campo.

```cpp
void SetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    textBoxField->set_MaxLen(15);
    document->Save(_dataDir + u"GetValuesFromAllFields.pdf");
}
```

Da mesma forma, o Aspose.PDF tem um método que obtém o limite de campo usando a abordagem DOM. O trecho de código a seguir mostra os passos.

```cpp
void GetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    Console::WriteLine(u"Limite: {0}", textBoxField->get_MaxLen());        
}
```

Você também pode definir e obter o mesmo valor usando o namespace *Aspose.PDF.Facades* usando o seguinte trecho de código.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void SetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // Adicionando Campo com limite
    auto form = MakeObject<Aspose::Pdf::Facades::FormEditor>(_dataDir + u"input.pdf", _dataDir + u"SetFieldLimit_out.pdf");
    form->SetFieldLimit(u"textbox1", 15);
    form->Save();
}
```

```cpp
void GetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // Adicionando Campo com limite
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"input.pdf");
    Console::WriteLine(u"Limite: {0}", form->GetFieldLimit(u"textbox1"));
}
```
## Definir Fonte Personalizada para o Campo do Formulário

Os campos de formulário em arquivos PDF da Adobe podem ser configurados para usar fontes padrão específicas. Nas versões iniciais do Aspose.PDF, apenas as 14 fontes padrão eram suportadas. Versões posteriores permitiram que os desenvolvedores aplicassem qualquer fonte. Para definir e atualizar a fonte padrão usada para campos de formulário, utilize a classe DefaultAppearance (Font font, double size, Color color). Esta classe pode ser encontrada no namespace Aspose.PDF.InteractiveFeatures. Para usar este objeto, utilize a propriedade DefaultAppearance da classe Field.

O trecho de código a seguir mostra como definir a fonte padrão para campos de formulário PDF.

```cpp
void SetCustomFontForField() {

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = new Document(_dataDir + u"FormFieldFont14.pdf");

    // Obter campo de formulário específico do documento
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Criar objeto de fonte
    auto font = Aspose::Pdf::Text::FontRepository::FindFont(u"ComicSansMS");

    // Definir as informações de fonte para o campo de formulário

    textBoxField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(font, 10, System::Drawing::Color::get_Black()));

    // Salvar documento atualizado
    document->Save(_dataDir + u"FormFieldFont14.pdf");
}
```

## Excluir campos de um formulário existente

Todos os campos do formulário estão contidos na coleção Form do objeto Document. Esta coleção fornece diferentes métodos que gerenciam campos de formulário, incluindo o método Delete. Se você quiser excluir um campo específico, passe o nome do campo como um parâmetro para o método Delete e, em seguida, salve o documento PDF atualizado. O trecho de código a seguir mostra como excluir um campo específico de um documento PDF.

```cpp
void DeleteFormField() {    
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = new Document(_dataDir + u"DeleteFormField.pdf");

    // Excluir um campo específico pelo nome
    document->get_Form()->Delete(u"textbox1");
    
    // Salvar documento modificado
    document->Save(_dataDir + u"DeleteFormField_out.pdf");
}
```