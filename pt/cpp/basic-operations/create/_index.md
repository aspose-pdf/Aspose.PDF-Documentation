---
title: Criar Documento PDF usando C++
linktitle: Criar
type: docs
weight: 10
url: /pt/cpp/create-document/
description: A tarefa mais popular e básica ao trabalhar com um arquivo PDF é criar um documento do zero. Use a biblioteca Aspose.PDF para C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para C++** API permite que desenvolvedores de aplicativos C++ integrem funcionalidades de processamento de documentos PDF em suas aplicações. Pode ser usado para criar e ler arquivos PDF sem a necessidade de qualquer outro software instalado na máquina subjacente. Aspose.PDF para C++ pode ser usado em uma variedade de tipos de aplicações C++, como QT, MFC e aplicativos de console.

## Como criar um arquivo PDF usando C++

Para criar um arquivo PDF usando C++, os seguintes passos podem ser utilizados.

1. Instanciar um objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
1. Adicionar uma [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) ao objeto do documento
1. Crie um objeto [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/)
1. Adicione [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) à coleção [Paragraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs/) da página
1. Salve o documento PDF resultante

```cpp
void CreatePDF() {
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo.
    String filename("sample-new.pdf");

    // Inicializar objeto do documento
    auto document = MakeObject<Document>();
    // Adicionar página
    auto page = document->get_Pages()->Add();

    // Adicionar texto à nova página
    auto textFragment = MakeObject<TextFragment>(u"Hello World!");
    page->get_Paragraphs()->Add(textFragment);

    // Salvar PDF atualizado
    String outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```