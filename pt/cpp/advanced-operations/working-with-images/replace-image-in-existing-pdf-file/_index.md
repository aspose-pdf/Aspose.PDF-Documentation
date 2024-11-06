---
title: Substituir Imagem em Arquivo PDF Existente usando C++
linktitle: Substituir Imagem
type: docs
weight: 70
url: pt/cpp/replace-image-in-existing-pdf-file/
description: Esta seção descreve como substituir uma imagem em um arquivo PDF existente usando a biblioteca ++.
lastmod: "2021-12-18"
---

O método Replace da coleção Images permite que você substitua uma imagem em um arquivo PDF existente.

A coleção Images pode ser encontrada na coleção Resources de uma página. Para substituir uma imagem:

1. Abra o arquivo PDF usando o objeto Document.
2. Substitua uma imagem específica, salve o arquivo PDF atualizado usando o método Save do objeto Document.

O trecho de código a seguir mostra como substituir uma imagem em um arquivo PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceImage() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");
    // Substituir uma imagem específica
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Replace(1, System::IO::File::OpenRead(u"lovely.jpg"));
    // Salvar arquivo PDF atualizado
    document->Save(_dataDir + u"output.pdf");
}
```