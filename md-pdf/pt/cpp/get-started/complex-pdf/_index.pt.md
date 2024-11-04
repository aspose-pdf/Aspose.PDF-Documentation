---
title: Criando um PDF complexo 
linktitle: Criando um PDF complexo
type: docs
weight: 60
url: /cpp/complex-pdf-example/
description: Aspose.PDF para C++ permite criar documentos mais complexos que contêm imagens, fragmentos de texto e tabelas em um único documento.
lastmod: "2021-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

O exemplo [Hello, World](/pdf/cpp/hello-world-example/) mostrou etapas simples para criar um documento PDF usando C++ e Aspose.PDF. Neste artigo, vamos dar uma olhada em como criar um documento mais complexo com C++ e Aspose.PDF para C++. Como exemplo, pegaremos um documento de uma empresa fictícia que opera serviços de balsa para passageiros.
Nosso documento conterá uma imagem, dois fragmentos de texto (cabeçalho e parágrafo) e uma tabela. Para construir tal documento, usaremos a abordagem baseada em DOM. Você pode ler mais na seção [Noções básicas da API DOM](/pdf/cpp/basics-of-dom-api/).

Se criarmos um documento do zero, precisamos seguir certas etapas:

1. Crie uma [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) para o nome do caminho e o nome do arquivo.  
1. Instancie um objeto [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Neste passo, criaremos um documento PDF vazio com alguns metadados, mas sem páginas.  
1. Adicione uma [Página](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) ao objeto de documento. Assim, agora nosso documento terá uma página.  
1. Adicione uma [Imagem](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image) à Página.  
1. Crie um [Fragmento de Texto](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) para o cabeçalho. Para o cabeçalho, usaremos a fonte Arial com tamanho de fonte 24pt e alinhamento centralizado.  
1. Adicione o cabeçalho aos [Parágrafos](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170) da página.  
1. Crie um [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) para a descrição. Para a descrição, usaremos a fonte Arial com tamanho de fonte 24pt e alinhamento centralizado.
1. Adicione (descrição) aos Parágrafos da página.
1. Crie uma tabela, adicione propriedades da tabela.
1. Adicione (tabela) aos [Parágrafos](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170) da página.
1. Salve um documento "Complex.pdf".

```cpp
void ExampleComplex()
{
    String outputFileName;

    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo.
    String filename("Complex.pdf");

    // Inicializar objeto de documento
    auto document = MakeObject<Document>();
    // Adicionar página
    auto page = document->get_Pages()->Add();

    // Adicionar imagem
    String imageFileName = _dataDir + String(u"logo.png");

    // Adicionar imagem à coleção Imagens dos Recursos da Página
    auto rectangle = MakeObject<Rectangle>(20, 730, 120, 830);
    page->AddImage(imageFileName, rectangle);

    // Adicionar Cabeçalho
    auto header = MakeObject<TextFragment>(u"Novas rotas de ferry no outono de 2020");
    auto textFragementState = header->get_TextState();
    textFragementState->set_Font(FontRepository::FindFont(u"Arial"));
    textFragementState->set_FontSize(24);
    header->set_HorizontalAlignment(HorizontalAlignment::Center);
    auto position = MakeObject<Aspose::Pdf::Text::Position>(130, 720);
    header->set_Position(position);
    page->get_Paragraphs()->Add(header);

    // Adicionar descrição
    String descriptionText(u"Os visitantes devem comprar ingressos online e os ingressos são limitados a 5.000 por dia. O serviço de ferry está operando com metade da capacidade e em horário reduzido. Espere filas.");
    auto description = MakeObject<TextFragment>(descriptionText);
    description->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    description->get_TextState()->set_FontSize(14);
    description->set_HorizontalAlignment(HorizontalAlignment::Left);
    page->get_Paragraphs()->Add(description);

    // Adicionar tabela
    auto table = MakeObject<Table>();
    table->set_ColumnWidths(u"200");

    table->set_Border(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, 1.0f, Aspose::Pdf::Color::get_DarkSlateGray()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, .5f, Aspose::Pdf::Color::get_Black()));
    table->get_Margin()->set_Bottom(10);
    table->get_DefaultCellTextState()->set_Font(FontRepository::FindFont(u"Helvetica"));

    auto headerRow = table->get_Rows()->Add();
    headerRow->get_Cells()->Add(u"Partidas da Cidade");
    headerRow->get_Cells()->Add(u"Partidas da Ilha");

    for (auto headerRowCell : headerRow->get_Cells())
    {
        headerRowCell->set_BackgroundColor(Color::get_Gray());
        headerRowCell->get_DefaultCellTextState()->set_ForegroundColor(Color::get_WhiteSmoke());
    }

    String arrivals[10] = { u"6:00",u"6:45", u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45" };
    String departures[10] = { u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45", u"11:00", u"11:45" };

    for (int i = 0; i < 10; i++)
    {
        auto dataRow = table->get_Rows()->Add();
        dataRow->get_Cells()->Add(arrivals[i]);
        dataRow->get_Cells()->Add(departures[i]);
    }

    page->get_Paragraphs()->Add(table);

    // Salvar PDF atualizado
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```