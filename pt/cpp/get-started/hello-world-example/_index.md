---
title: Aspose.PDF С++ Example
linktitle: Hello World Example
type: docs
weight: 40
url: pt/cpp/hello-world-example/
description: Esta página mostra como usar programação simples para criar um documento PDF contendo texto - Hello World.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.6
---

Um exemplo "Hello World" é tradicionalmente usado para introduzir características de uma linguagem de programação ou software com um caso de uso simples.

Aspose.PDF para C++ é uma API de PDF rica em recursos que permite aos desenvolvedores incorporar capacidades de criação, manipulação e conversão de documentos PDF em seus aplicativos C++. Ele suporta o trabalho com muitos formatos de arquivo populares, incluindo PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX e formatos de arquivo de imagem. Neste artigo, estamos criando um documento PDF contendo o texto "Hello World!". Após instalar o Aspose.PDF para C++ em seu ambiente, você pode executar o exemplo de código abaixo para ver como a API Aspose.PDF funciona.

O trecho de código abaixo segue estas etapas:

1.
``` Crie uma [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) para o nome do caminho e o nome do arquivo.  
1. Instancie um objeto [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Neste passo, criaremos um documento PDF vazio com alguns metadados, mas sem páginas.  
1. Adicione uma [Página](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) ao objeto documento. Então, agora nosso documento terá uma página.  
1. [Salve](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) o documento PDF resultante  

O trecho de código a seguir é um programa Hello World para exibir o funcionamento do Aspose.PDF para a API C++.

```cpp
void ExampleSimple()
{
    // Buffer para armazenar o caminho combinado.
    String outputFileName;

    // String para o nome do caminho.
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo.
    String filename("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Adicionar texto à nova página
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Salvar PDF atualizado
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```