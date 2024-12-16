---
title: Preencher AcroForm
linktitle: Preencher AcroForm
type: docs
weight: 20
url: /pt/cpp/fill-form/
description: Esta seção explica como preencher um campo de formulário em um documento PDF com Aspose.PDF para C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Documentos PDF são os melhores, e realmente o tipo de arquivo preferido, para criar Formulários.

Este tópico explica como preencher formulários PDF usando Aspose.PDF para C++.

Aspose.PDF para C++ permite que você preencha um campo de formulário, obtenha o campo da coleção de Formulários do objeto Document.

Vamos ver o seguinte exemplo de como resolver esta tarefa:

```cpp
using namespace System;
using namespace Aspose::Pdf;

void FillAcroform()
{
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"FillFormField.pdf");

    // Obter um campo
    auto textBoxField = System::DynamicCast<Aspose::Pdf::Forms::TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Modificar valor do campo
    textBoxField->set_Value(u"Valor a ser preenchido no campo");

    // Salvar documento atualizado
    document->Save(_dataDir + u"FillFormField_out.pdf");

}
```