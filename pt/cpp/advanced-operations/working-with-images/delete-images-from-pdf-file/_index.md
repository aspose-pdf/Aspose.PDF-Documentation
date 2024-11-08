---
title: Excluir Imagens de Arquivo PDF usando C++
linktitle: Excluir Imagens
type: docs
weight: 20
url: /pt/cpp/delete-images-from-pdf-file/
description: Esta seção explica como excluir Imagens de Arquivo PDF usando Aspose.PDF para C++.
lastmod: "2021-12-18"
---

Para excluir uma imagem de um arquivo PDF:

1. Crie um objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) e abra o arquivo PDF de entrada.
1. Obtenha a Página que contém a imagem da [coleção de Páginas](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) do objeto Document.
1. As imagens estão na coleção Images, encontrada na coleção de Recursos da página.
1. Exclua uma imagem com o método Delete da coleção Images.
1. Salve a saída usando o método Save do objeto Document.

O trecho de código a seguir mostra como excluir uma imagem de um arquivo PDF.

```cpp
void WorkingWithImages::DeleteImagesFromPDFFile()
{
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"DeleteImages.pdf");

    // Excluir uma imagem específica
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Delete(1);

    // Salvar arquivo PDF atualizado
    document->Save(_dataDir + u"DeleteImages_out.pdf");
}
```