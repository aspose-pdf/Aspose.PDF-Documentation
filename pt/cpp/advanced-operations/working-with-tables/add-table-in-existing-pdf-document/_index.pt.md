---
title: Criar ou Adicionar Tabela No PDF
linktitle: Criar ou Adicionar Tabela
type: docs
weight: 10
url: /cpp/add-table-in-existing-pdf-document/
description: Aspose.PDF para C++ é uma biblioteca usada para criar, ler e editar Tabelas PDF. Usando esta biblioteca, você pode paginar uma tabela na página PDF usando C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Criando Tabela usando C++

Tabelas são importantes ao trabalhar com documentos PDF. Elas fornecem ótimas funcionalidades para exibir informações de maneira sistemática.

Tabelas em um documento PDF organizam dados em linhas e colunas de maneira sistemática. A API Aspose.PDF para C++ permite que você adicione tabelas a um documento PDF, e adicione linhas e colunas a ele em suas aplicações C++. A classe [Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table/) é usada para adicionar uma tabela ao documento. Os seguintes passos podem ser seguidos para adicionar uma tabela a um documento PDF usando C++.

### Adicionando Tabela em Documento PDF Existente

Para adicionar uma tabela a um arquivo PDF existente com Aspose.PDF para C++, siga os seguintes passos:

1. Carregue o arquivo de origem.
1. Inicialize uma tabela e defina suas colunas e linhas.
1. Defina a configuração da tabela (definimos as bordas).
1. Preencha a tabela.
1. Adicione a tabela a uma página.
1. Salve o arquivo.

Os trechos de código a seguir mostram como adicionar texto em um arquivo PDF existente.

>Headers

```cpp
#include <system/date_time.h>
#include <system/io/file.h>
#include <system/console.h>
#include <data/data_table.h>
#include <data/data_column_collection.h>
#include <system/type_info.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/GraphInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderCornerStyle.h>
#include <Aspose.PDF.Cpp/Generator/ColumnAdjustment.h>
#include <Aspose.PDF.Cpp/Generator/ImageFileType.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/HtmlFragment.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
```

>Sample

```cpp
using namespace System;
using namespace Aspose::Pdf;

void AddingTableInExistingPDFDocument() {
    
    String _dataDir("C:\\Samples\\");
    
    // Carregar documento PDF de origem
    auto document = MakeObject<Document>(_dataDir + u"AddTable.pdf");
    
    // Inicializa uma nova instância da Tabela
    auto table = MakeObject<Table>();
    
    // Definir a cor da borda da tabela como CinzaClaro
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));
    // Definir a borda para células da tabela
    table->set_DefaultCellBorder (MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Aspose::Pdf::Color::get_LightGray()));

    // Criar um loop para adicionar 10 linhas
    for (int row_count = 1; row_count < 10; row_count++)
    {
        // Adicionar linha à tabela
        auto row = table->get_Rows()->Add();
        // Adicionar células à tabela
        row->get_Cells()->Add(String::Format(u"Coluna ({0}, 1)", row_count));
        row->get_Cells()->Add(String::Format(u"Coluna ({0}, 2)", row_count));
        row->get_Cells()->Add(String::Format(u"Coluna ({0}, 3)", row_count));
    }

    // Adicionar objeto tabela à primeira página do documento de entrada
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    
    // Salvar documento atualizado contendo o objeto tabela
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

### ColSpan e RowSpan em Tabelas

Aspose.PDF para C++ apresenta uma propriedade [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) para mesclar as colunas em uma tabela e a propriedade [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) para mesclar as linhas.

Usamos a propriedade [ColSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#ae79c581d2245258699c98617e78c01d1) ou [RowSpan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell#a4eb7337d118314e6c2180670fb32721a) no objeto [Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell) que cria a célula da tabela. Após aplicar as propriedades necessárias, a célula criada pode ser adicionada à tabela.

```cpp
void AddTable_RowColSpan()
{
    String _dataDir("C:\\Samples\\");

    // Carregar documento PDF de origem
    auto document = MakeObject<Document>();
    document->get_Pages()->Add();

    // Inicializa uma nova instância da Tabela
    auto table = MakeObject<Table>();
    // Define a cor da borda da tabela como CinzaClaro
    table->set_Border(MakeObject<Aspose::Pdf::BorderInfo>(
        Aspose::Pdf::BorderSide::All, .5f, 
        Color::get_Black()));
        // Define a borda para células da tabela
    table->set_DefaultCellBorder(
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, .5f, 
            Color::get_Black()));
    

    // Adicionar 1ª linha à tabela
    auto row1 = table->get_Rows()->Add();
    for (int cellCount = 1; cellCount < 5; cellCount++)
    {
        // Adicionar células à tabela
        row1->get_Cells()->Add(String::Format(u"Teste 1 {0}", cellCount));
    }

    // Adicionar 2ª linha à tabela
    auto row2 = table->get_Rows()->Add();
    row2->get_Cells()->Add(u"Teste 2 1");
    auto cell = row2->get_Cells()->Add(u"Teste 2 2");
    cell->set_ColSpan(2);
    row2->get_Cells()->Add(u"Teste 2 4");

    // Adicionar 3ª linha à tabela
    auto row3 = table->get_Rows()->Add();
    row3->get_Cells()->Add(u"Teste 3 1");
    row3->get_Cells()->Add(u"Teste 3 2");
    row3->get_Cells()->Add(u"Teste 3 3");
    row3->get_Cells()->Add(u"Teste 3 4");

    // Adicionar 4ª linha à tabela
    auto row4 = table->get_Rows()->Add();
    row4->get_Cells()->Add(u"Teste 4 1");
    cell = row4->get_Cells()->Add(u"Teste 4 2");
    cell->set_RowSpan(2);
    row4->get_Cells()->Add(u"Teste 4 3");
    row4->get_Cells()->Add(u"Teste 4 4");


    // Adicionar 5ª linha à tabela
    auto row5 = table->get_Rows()->Add();
    row5->get_Cells()->Add(u"Teste 5 1");
    row5->get_Cells()->Add(u"Teste 5 3");
    row5->get_Cells()->Add(u"Teste 5 4");

    // Adicionar objeto tabela à primeira página do documento de entrada
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);

    // Salvar documento atualizado contendo o objeto tabela
    document->Save(_dataDir + u"document_with_table_out.pdf");
}
```

O resultado do código de execução abaixo é a tabela representada na imagem a seguir:

![Demonstração de ColSpan e RowSpan](colspan_rowspan.png)

## Trabalhando com Bordas, Margens e Espaçamento Interno

Note que ele também suporta a função de definir a borda, margens e espaçamento interno das células para tabelas, primeiro vamos entender o conceito de bordas, margens e espaçamento interno, que são apresentados no diagrama abaixo:

![Bordas, margens e espaçamento interno](set-border-style-margins-and-padding-of-table_1.png)

Verifique o desenho em detalhe. Ele mostra que as bordas da tabela, linhas e células se sobrepõem. Usando Aspose.PDF para C++ a tabela pode ter margens e as células podem ser indentadas. Para definir as margens das células, devemos definir o espaçamento interno das células.

## Bordas

Para definir as bordas dos objetos Table, [Row](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.row) e [Cell](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.cell), use as propriedades Table.Border, Row.Border e Cell.Border. Bordas de células também podem ser definidas usando a propriedade DefaultCellBorder da classe [Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) ou da classe Row. Todas as propriedades relacionadas a bordas discutidas acima são atribuídas a uma instância da classe Row, que é criada chamando seu construtor. A classe Row possui muitas sobrecargas que aceitam quase todos os parâmetros necessários para personalizar a borda.

## Margens ou Espaçamento Interno

O espaçamento interno da célula pode ser gerenciado usando a propriedade [DefaultCellPadding](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#ac64196de6dfed7550c3278892ed9dbe0) da classe Table. Todas as propriedades relacionadas ao espaçamento são atribuídas a uma instância da classe [MarginInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.margin_info/) que recebe informações sobre os parâmetros `Left`, `Right`, `Top` e `Bottom` para criar margens personalizadas.

![Margem e Borda na Tabela PDF](margin-border.png)

```cpp
void AddTable_MergingPadding() {

    String _dataDir("C:\\Samples\\");

    // Instanciar o objeto Document chamando seu construtor vazio
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Instanciar um objeto de tabela
    auto tab1 = MakeObject<Table>();
    // Adicionar a tabela na coleção de parágrafos da seção desejada
    page->get_Paragraphs()->Add(tab1);
    // Definir larguras das colunas da tabela
    tab1->set_ColumnWidths (u"50 50 50");
    // Definir borda padrão da célula usando o objeto BorderInfo
    tab1->set_DefaultCellBorder (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 0.1F));
    // Definir borda da tabela usando outro objeto BorderInfo personalizado
    tab1->set_Border (
        MakeObject<Aspose::Pdf::BorderInfo>(
            Aspose::Pdf::BorderSide::All, 1.0F));

    // Criar objeto MarginInfo e definir suas margens esquerda, inferior, direita e superior
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top (5.0f);
    margin->set_Left (5.0f);
    margin->set_Right (5.0f);
    margin->set_Bottom (5.0f);

    // Definir o espaçamento interno padrão da célula para o objeto MarginInfo
    tab1->set_DefaultCellPadding (margin);
    // Criar linhas na tabela e depois células nas linhas
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add();

    auto mytext = MakeObject<Aspose::Pdf::Text::TextFragment>(u"col3 com grande string de texto");
        
    row1->get_Cells()->idx_get(2)->get_Paragraphs()->Add(mytext);
    row1->get_Cells()->idx_get(2)->set_IsWordWrapped(false);
    

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // Salvar o Pdf
    document->Save(_dataDir + u"MarginsOrPadding_out.pdf");
}
```
Para criar uma tabela com canto arredondado, use a classe [BorderInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info) valor [RoundedBorderRadius](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.border_info#a6a2bed69dd034fba9ce439dcbe1fd3de) e defina o estilo de canto da tabela como arredondado.

```cpp
void AddTable_RoundedBorderRadius()
{
    // O caminho para o diretório de documentos.
    String _dataDir("C:\\Samples\\");

    auto tab1 = MakeObject<Aspose::Pdf::Table>();

    auto graph = MakeObject<GraphInfo>();
    graph->set_Color(Color::get_Red());
    // Crie um objeto BorderInfo em branco
    auto bInfo = MakeObject<BorderInfo>(BorderSide::All, graph);

    // Defina a borda como uma borda arredondada onde o raio do arredondamento é 15
    bInfo->set_RoundedBorderRadius(15);
    // Defina o estilo de canto da tabela como Redondo.
    tab1->set_CornerStyle (Aspose::Pdf::BorderCornerStyle::Round);
    // Defina as informações da borda da tabela
    tab1->set_Border(bInfo);
}
```

### Propriedade AutoFitToWindow na enumeração ColumnAdjustmentType

```cpp
void AddTable_AutoFitToWindow() {
    
    // O caminho para o diretório de documentos.
    String _dataDir("C:\\Samples\\");

    // Instanciar o objeto Pdf chamando seu construtor vazio
    auto document = MakeObject<Document>();

    // Criar a seção no objeto Pdf
    auto sec1 = document->get_Pages()->Add();

    // Instanciar um objeto de tabela
    auto tab1 = MakeObject<Aspose::Pdf::Table>();
    // Adicionar a tabela na coleção de parágrafos da seção desejada
    sec1->get_Paragraphs()->Add(tab1);

    // Definir larguras das colunas da tabela
    tab1->set_ColumnWidths (u"50 50 50");
    tab1->set_ColumnAdjustment (ColumnAdjustment::AutoFitToWindow);

    // Definir borda padrão da célula usando o objeto BorderInfo
    tab1->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 0.1F));

    // Definir borda da tabela usando outro objeto BorderInfo personalizado
    tab1->set_Border (MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::All, 1.0F));

    // Criar objeto MarginInfo e definir suas margens esquerda, inferior, direita e superior
    auto margin = MakeObject<MarginInfo>();
    margin->set_Top(5.0f);
    margin->set_Left(5.0f);
    margin->set_Right(5.0f);
    margin->set_Bottom(5.0f);

    // Definir o preenchimento padrão da célula para o objeto MarginInfo
    tab1->set_DefaultCellPadding(margin);

    // Criar linhas na tabela e depois células nas linhas
    auto row1 = tab1->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    auto row2 = tab1->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    
    // Salvar documento atualizado contendo objeto de tabela
    document->Save(_dataDir + u"AutoFitToWindow_out.pdf");
}
```

### Obter Largura da Tabela

Existem tarefas nas quais você precisa obter dinamicamente a largura da tabela.
A classe [Aspose.PDF.Table](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table) tem um método [GetWidth] para este propósito (https://reference.aspose.com/pdf/cpp/class/aspose.pdf.table#a3361cc8d4af87eec2e3da616c474ac1c). Por exemplo, você não definiu explicitamente a largura das colunas da tabela, e não definiu [ColumnAdjustment] (https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#afc01382935026dd569c96d77d09dc3a4) para AutoFitToContent. Neste caso, você pode obter a próxima largura da tabela.

```cpp
void GetTableWidth() {
    // Crie um novo documento
    auto document = MakeObject<Document>();
    
    // Adicionar página no documento
    auto page = document->get_Pages()->Add();

    // Inicializar nova tabela
    auto table = MakeObject<Table>();
    table->set_ColumnAdjustment(ColumnAdjustment::AutoFitToContent);
    
    // Adicionar linha na tabela
    auto row = table->get_Rows()->Add();

    // Adicionar célula na tabela
    auto cell = row->get_Cells()->Add(u"Texto Célula 1");
    cell = row->get_Cells()->Add(u"Texto Célula 2");
    // Obter largura da tabela
    Console::WriteLine(table->GetWidth());
}
```

## Adicionar Imagem SVG à Célula da Tabela

Aspose.PDF para C++ permite adicionar células de tabela a um arquivo PDF. Quando você cria uma tabela, pode adicionar texto ou imagens às células. Além disso, a API também oferece um recurso para converter arquivos SVG para PDF. Usando uma combinação dessas funções, é possível carregar uma imagem SVG e adicioná-la a uma célula da tabela.

O trecho de código a seguir mostra os passos para instanciar uma tabela e adicionar uma imagem SVG a uma célula da tabela.

```cpp
void InsertSVGObject() 
{
    String _dataDir("C:\\Samples\\");

    // Instanciar objeto Document
    auto document = MakeObject<Document>();
    // Criar uma instância de imagem
    auto img = MakeObject<Aspose::Pdf::Image>();

    // Definir tipo de imagem como SVG
    img->set_FileType(Aspose::Pdf::ImageFileType::Svg);
    // Caminho para o arquivo fonte
    img->set_File (_dataDir + u"SVGToPDF.svg");
    // Definir largura para instância de imagem
    img->set_FixWidth (50);
    // Definir altura para instância de imagem
    img->set_FixHeight(50);
    // Criar instância de tabela
    auto table = MakeObject<Aspose::Pdf::Table>();
    // Definir largura para células da tabela
    table->set_ColumnWidths (u"100 100");
    // Criar objeto de linha e adicioná-lo à instância de tabela
    auto row = table->get_Rows()->Add();
    // Criar objeto de célula e adicioná-lo à instância de linha
    auto cell = row->get_Cells()->Add();
    // Adicionar fragmento de texto à coleção de parágrafos do objeto de célula
    cell->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"First cell"));
    // Adicionar outra célula ao objeto de linha
    cell = row->get_Cells()->Add();
    // Adicionar imagem SVG à coleção de parágrafos da instância de célula recentemente adicionada
    cell->get_Paragraphs()->Add(img);
    // Criar objeto de página e adicioná-lo à coleção de páginas da instância de documento
    auto page = document->get_Pages()->Add();
    // Adicionar tabela à coleção de parágrafos do objeto de página
    page->get_Paragraphs()->Add(table);    
    // Salvar arquivo PDF
    document->Save(_dataDir + u"AddSVGObject_out.pdf");
}
```

## Usando Tags HTML dentro de Tabela

Para algumas tarefas, você precisará importar o conteúdo do banco de dados com algumas tags HTML e, em seguida, importar o conteúdo em um objeto Tabela. Ao importar conteúdo, as tags HTML devem ser exibidas dentro do documento PDF.

No trecho de código a seguir, você pode definir a cor da borda da tabela e definir a borda para as células da tabela. Depois, você criará um loop para adicionar 10 linhas. Adicione o objeto tabela à primeira página do documento de entrada e salve o documento atualizado.

```cpp
void AddHTMLFragmentToTableCell() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");    
    // Inicializa uma nova instância da Tabela
    auto table = MakeObject<Table>();
    // Define a cor da borda da tabela como LightGray
    table->set_Border(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // define a borda para as células da tabela
    table->set_DefaultCellBorder(new BorderInfo(BorderSide::All, .5f, Color::get_LightGray()));
    // cria um loop para adicionar 10 linhas       
    for (int row_count = 1; row_count < 10; row_count++) {
        SmartPtr<Cell> cell;
        // adiciona linha à tabela
        auto row = table->get_Rows()->Add();
        // adiciona células à tabela
        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Coluna <strong>({0}, 1)</strong>", row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Coluna <span style='color:red'>({0}, 2)</span>",row_count)));

        cell = row->get_Cells()->Add();
        cell->get_Paragraphs()->Add(new HtmlFragment(String::Format(u"Coluna <span style='text-decoration: underline'>([0}, 3)</span>", row_count)));
    }
    // Adiciona objeto tabela à primeira página do documento de entrada
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(table);
    // Salva o documento atualizado contendo o objeto tabela
    document->Save(_dataDir + u"AddHTMLObject_out.pdf");
}
```

## Inserir uma Quebra de Página entre as linhas da tabela

Normalmente, ao criar uma tabela dentro de um PDF, a tabela se estende para as páginas subsequentes quando atinge a margem inferior da tabela. Mas podemos ter um requisito para forçar a inserção de uma quebra de página quando um certo número de linhas for adicionado à tabela. O exemplo de código a seguir mostra os passos para inserir uma quebra de página ao adicionar 10 linhas a uma tabela.

O exemplo de código a seguir mostra os passos para inserir uma quebra de página quando 10 linhas são adicionadas à tabela.

```cpp
void InsertPageBreak() {
    String _dataDir("C:\\Samples\\");

    // Instanciar objeto Document
    auto document = MakeObject<Document>();
    
    // Adicionar página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->Add();

    // Criar instância de tabela
    auto tab = MakeObject<Table>();

    // Definir estilo de borda para a tabela
    tab->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // Definir estilo de borda padrão para a tabela com cor de borda como Vermelho
    tab->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    // Especificar largura das colunas da tabela
    tab->set_ColumnWidths(u"100 100");

    // Criar um loop para adicionar 200 linhas à tabela
    for (int counter = 0; counter <= 200; counter++) {
        auto row = MakeObject<Row>();
        tab->get_Rows()->Add(row);
        auto cell1 = MakeObject<Cell>();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Célula {0}, 0", counter)));
        row->get_Cells()->Add(cell1);

        auto cell2 = new Cell();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(String::Format(u"Célula {0}, 1", counter)));
        row->get_Cells()->Add(cell2);
        // Quando 10 linhas são adicionadas, renderizar nova linha em nova página
        if (counter % 10 == 0 && counter != 0)
            row->set_IsInNewPage(true);
    }
    // Adicionar tabela à coleção de parágrafos do arquivo PDF
    page->get_Paragraphs()->Add(tab);

    // Salvar o documento PDF
    document->Save(_dataDir + u"InsertPageBreak_out.pdf");
}
```

## Renderizar uma Tabela em Nova Página

Por padrão, os parágrafos são adicionados à coleção de Parágrafos de um objeto Page. No entanto, é possível renderizar uma tabela em uma nova página em vez de diretamente após o objeto de nível de parágrafo previamente adicionado na página.

### Exemplo: Como Renderizar uma Tabela em Nova Página usando C++

Para renderizar a tabela em uma nova página, use a propriedade [IsInNewPage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph#a614946048d22afb9dce4cd42346c7561) na classe [BaseParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.base_paragraph).
O trecho de código a seguir mostra como.

```cpp
void RenderTableOnNewPage()
{
    auto document = MakeObject<Document>();
    auto pageInfo = document->get_PageInfo();
    auto marginInfo = pageInfo->get_Margin();

    marginInfo->set_Left (37);
    marginInfo->set_Right (37);
    marginInfo->set_Top (37);
    marginInfo->set_Bottom (37);

    pageInfo->set_IsLandscape(true);

    auto table = MakeObject<Aspose::Pdf::Table>();
    table->set_ColumnWidths(u"50 100");
    // Página adicionada.
    auto curPage = document->get_Pages()->Add();
    for (int i = 1; i <= 120; i++)
    {
        auto row = table->get_Rows()->Add();
        row->set_FixedRowHeight(15);
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Conteúdo 1"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"HHHHH"));
    }
    auto paragraphs = curPage->get_Paragraphs();
    paragraphs->Add(table);

    //-------------------------------------

    auto document = MakeObject<Document>();
    auto table1 = MakeObject<Aspose::Pdf::Table>();
    table1->set_ColumnWidths(u"100 100");

    String _dataDir("C:\\Samples\\");

    for (int i = 1; i <= 10; i++)
    {
        auto row = table1->get_Rows()->Add();
        auto cell1 = row->get_Cells()->Add();
        cell1->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAAAAAA"));
        auto cell2 = row->get_Cells()->Add();
        cell2->get_Paragraphs()->Add(MakeObject<Aspose::Pdf::Text::TextFragment>(u"LAAGGGGGG"));
    }
    
    table1->set_IsInNewPage (true);
    // Eu quero manter a tabela 1 na próxima página, por favor...
    paragraphs->Add(table1);
    
    document->Save(_dataDir + u"IsNewPageProperty_Test_out.pdf");
}
```