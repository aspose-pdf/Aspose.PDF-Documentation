---
title: Obter e Definir Propriedades de Página
type: docs
weight: 20
url: /pt/cpp/get-and-set-page-properties/
description: Você pode obter e definir propriedades de página do seu arquivo PDF usando a biblioteca C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para C++** permite que você leia e defina propriedades de páginas em um arquivo PDF em suas aplicações C++. Esta seção mostra como obter o número de páginas em um arquivo PDF, obter informações sobre propriedades de página do PDF, como cor e definir propriedades de página, obter uma página específica do arquivo PDF, etc.

## Obter Número de Páginas em um Arquivo PDF

Ao trabalhar com documentos, você frequentemente quer saber quantas páginas eles contêm. Com o Aspose.PDF, isso não leva mais do que duas linhas de código.

Para obter o número de páginas em um arquivo PDF:

1. Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Em seguida, use a propriedade Count da coleção [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) (do objeto Document) para obter o número total de páginas no documento.

O trecho de código a seguir mostra como obter o número de páginas de um arquivo PDF.

```cpp
void GetNumberOfPages() {
    // Abrir documento
    String _dataDir("C:\\Samples\\");
    String srcFileName("GetNumberofPages.pdf");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);

    // Obter contagem de páginas
    std::cout << "Contagem de Páginas : " << srcDocument->get_Pages()->get_Count() << std::endl;
}
```

### Obter contagem de páginas sem salvar o documento

Às vezes, geramos os arquivos PDF em tempo real e durante a criação do arquivo PDF, podemos nos deparar com a necessidade (criação de Índice etc.) de obter a contagem de páginas do arquivo PDF sem salvar o arquivo no sistema ou fluxo. Então, para atender a esse requisito, um método [ProcessParagraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a1773e7b6a887eaddd602073e29939a6f) foi introduzido na classe Document. Por favor, dê uma olhada no trecho de código a seguir que mostra os passos para obter a contagem de páginas sem salvar o documento.

```cpp
void GetPageCountWithoutSavingTheDocument() {
    // Instanciar a instância do Document
    auto document = MakeObject<Document>();

    // Adicionar página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->Add();
    // Criar instância do loop
    for (int i = 0; i < 300; i++)
        // Adicionar TextFragment à coleção de parágrafos do objeto página
        page->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Teste de contagem de páginas"));
    // Processar os parágrafos no arquivo PDF para obter a contagem de páginas precisa
    document->ProcessParagraphs();
    // Imprimir número de páginas no documento
    std::cout << "Número de páginas no documento = " << document->get_Pages()->get_Count();
}
```

## Get Page Properties
### Acessando Propriedades da Página

A classe [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) fornece todas as propriedades relacionadas a uma página específica do PDF. Todas as páginas dos arquivos PDF estão contidas na coleção [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

A partir daí, é possível acessar objetos Page individuais usando seu índice ou percorrer a coleção, usando um loop foreach, para obter todas as páginas. Uma vez que uma página individual é acessada, podemos obter suas propriedades. O trecho de código a seguir mostra como obter propriedades da página.

```cpp
void AccessingPageProperties() {

    String _dataDir("C:\\Samples\\");
    String pdfDocument("GetProperties.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + pdfDocument);

    // Obter página específica
    auto pdfPage = document->get_Pages()->idx_get(1);
    // Obter propriedades da página
    Console::WriteLine(u"ArtBox : Altura={0},Largura={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_ArtBox()->get_Height(), pdfPage->get_ArtBox()->get_Width(),
        pdfPage->get_ArtBox()->get_LLX(), pdfPage->get_ArtBox()->get_LLY(),
        pdfPage->get_ArtBox()->get_URX(), pdfPage->get_ArtBox()->get_URY());

    Console::WriteLine(u"->get_BleedBox() : Altura={0},Largura={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_BleedBox()->get_Height(), pdfPage->get_BleedBox()->get_Width(),
        pdfPage->get_BleedBox()->get_LLX(), pdfPage->get_BleedBox()->get_LLY(),
        pdfPage->get_BleedBox()->get_URX(), pdfPage->get_BleedBox()->get_URY());

    Console::WriteLine(u"get_CropBox() : Altura={0},Largura={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_CropBox()->get_Height(), pdfPage->get_CropBox()->get_Width(),
        pdfPage->get_CropBox()->get_LLX(), pdfPage->get_CropBox()->get_LLY(),
        pdfPage->get_CropBox()->get_URX(), pdfPage->get_CropBox()->get_URY());

    Console::WriteLine(u"get_MediaBox() : Altura={0},Largura={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_MediaBox()->get_Height(), pdfPage->get_MediaBox()->get_Width(),
        pdfPage->get_MediaBox()->get_LLX(), pdfPage->get_MediaBox()->get_LLY(),
        pdfPage->get_MediaBox()->get_URX(), pdfPage->get_MediaBox()->get_URY());

    Console::WriteLine(u"get_TrimBox() : Altura={0},Largura={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_TrimBox()->get_Height(), pdfPage->get_TrimBox()->get_Width(),
        pdfPage->get_TrimBox()->get_LLX(), pdfPage->get_TrimBox()->get_LLY(),
        pdfPage->get_TrimBox()->get_URX(), pdfPage->get_TrimBox()->get_URY());

    Console::WriteLine(u"Retângulo : Altura={0},Largura={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_Rect()->get_Height(), pdfPage->get_Rect()->get_Width(),
        pdfPage->get_Rect()->get_LLX(), pdfPage->get_Rect()->get_LLY(),
        pdfPage->get_Rect()->get_URX(), pdfPage->get_Rect()->get_URY());

    Console::WriteLine(u"Número da Página : {0}", pdfPage->get_Number());
    Console::WriteLine(u"Rotação : {0}", pdfPage->get_Rotate());
}
```