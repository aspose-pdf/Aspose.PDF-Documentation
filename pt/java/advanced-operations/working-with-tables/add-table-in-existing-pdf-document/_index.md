---
title: Criar ou Adicionar Tabela em PDF 
linktitle: Criar ou Adicionar Tabela
type: docs
weight: 10
url: /pt/java/add-table-in-existing-pdf-document/
description: Aprenda como criar ou adicionar tabela a um documento PDF, aplicando estilo de célula, dividindo tabela em páginas e personalizando as linhas e colunas, etc.
lastmod: "2021-12-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Criando Tabela

O namespace Aspose.PDF contém classes chamadas [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table), [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/cell), e [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row) que fornecem funcionalidade para criar tabelas ao gerar documentos PDF do zero.

A tabela pode ser criada criando um objeto da Classe Table.

```java
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
```

### Adicionando Tabela em Documento PDF Existente

Para adicionar uma tabela a um arquivo PDF existente com Aspose.PDF para Java, siga os seguintes passos:

1. Carregue o arquivo de origem.

1. Inicializar uma tabela e definir suas colunas e linhas.
1. Definir configuração da tabela (definimos as bordas).
1. Preencher a tabela.
1. Adicionar a tabela a uma página.
1. Salvar o arquivo.

Os seguintes trechos de código mostram como adicionar texto em um arquivo PDF existente.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddTable {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void CreateTable() {
        Document doc = new Document(_dataDir + "input.pdf");
        // Inicializa uma nova instância da Tabela
        Table table = new Table();
        // Define a cor da borda da tabela como CinzaClaro
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // define a borda para as células da tabela
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // cria um loop para adicionar 10 linhas
        for (int row_count = 1; row_count < 10; row_count++) {
            // adiciona linha à tabela
            Row row = table.getRows().add();
            // adiciona células à tabela
            row.getCells().add("Coluna (" + row_count + ", 1)");
            row.getCells().add("Coluna (" + row_count + ", 2)");
            row.getCells().add("Coluna (" + row_count + ", 3)");
        }
        // Adiciona objeto tabela à primeira página do documento de entrada
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // Salva o documento atualizado contendo o objeto tabela
        doc.save(_dataDir + "document_with_table.pdf");
    }
```


### ColSpan e RowSpan em Tabelas Aspose.PDF usando Java

Aspose.PDF para Java fornece o método [setColSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) para mesclar as colunas em uma tabela e o método [setRowSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) para mesclar as linhas.

Usamos os métodos [setColSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setColSpan-int-) ou [setRowSpan](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setRowSpan-int-) no objeto [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell) que cria a célula da tabela. Após aplicar as propriedades necessárias, a célula criada pode ser adicionada à tabela.

```java
public static void AddTable_RowColSpan() {
        // Carregar documento PDF de origem
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Inicializa uma nova instância da Tabela
        Table table = new Table();
        // Define a cor da borda da tabela como LightGray
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // Define a borda para células da tabela
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getBlack()));
        // Adiciona a 1ª linha à tabela
        Row row1 = table.getRows().add();
        for (int cellCount = 1; cellCount < 5; cellCount++) {
            // Adiciona células à tabela
            row1.getCells().add("Teste 1 " + cellCount);
        }

        // Adiciona a 2ª linha à tabela
        Row row2 = table.getRows().add();
        row2.getCells().add("Teste 2 1");
        Cell cell = row2.getCells().add("Teste 2 2");
        cell.setColSpan(2);
        row2.getCells().add("Teste 2 4");

        // Adiciona a 3ª linha à tabela
        Row row3 = table.getRows().add();
        row3.getCells().add("Teste 3 1");
        row3.getCells().add("Teste 3 2");
        row3.getCells().add("Teste 3 3");
        row3.getCells().add("Teste 3 4");

        // Adiciona a 4ª linha à tabela
        Row row4 = table.getRows().add();
        row3.getCells().add("Teste 4 1");
        cell = row3.getCells().add("Teste 4 2");
        cell.setRowSpan(2);
        row3.getCells().add("Teste 4 3");
        row3.getCells().add("Teste 4 4");

        // Adiciona a 5ª linha à tabela
        row4 = table.getRows().add();
        row4.getCells().add("Teste 5 1");
        row4.getCells().add("Teste 5 3");
        row4.getCells().add("Teste 5 4");

        // Adiciona o objeto tabela à primeira página do documento de entrada
        page.getParagraphs().add(table);

        // Salva o documento atualizado contendo o objeto tabela
        pdfDocument.save(_dataDir + "document_with_table_out.pdf");
    }
```


O resultado do código de execução abaixo é a tabela mostrada na imagem a seguir:

![Demonstração de ColSpan e RowSpan](colspan_rowspan.png)

## Trabalhando com Bordas, Margens e Preenchimento

Aspose.PDF para Java permite que os desenvolvedores criem tabelas em documentos PDF. De acordo com o Modelo de Objeto de Documento do Aspose.PDF, uma tabela é um elemento de nível de parágrafo.

Observe que ele também suporta o recurso de definir estilo de borda, margens e preenchimento de célula para tabelas. Antes de entrar em mais detalhes técnicos, é importante entender os conceitos de borda, margens e preenchimento que são apresentados abaixo em um diagrama:

![Bordas, margens e preenchimento](set-border-style-margins-and-padding-of-table_1.png)

Na figura acima, você pode ver que as bordas da tabela, linha e célula se sobrepõem. Usando Aspose.PDF, uma tabela pode ter margens e as células podem ter preenchimentos. Para definir margens de célula, precisamos definir o preenchimento da célula.

## Bordas

Para definir as bordas dos objetos [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table), [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row) e [Cell](https://reference.aspose.com/pdf/java/com.aspose.pdf/cell), use os métodos [Table.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setBorder-com.aspose.pdf.BorderInfo-), [Row.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setBorder-com.aspose.pdf.BorderInfo-) e [Cell.setBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Cell#setBorder-com.aspose.pdf.BorderInfo-).
 Bordas de células também podem ser definidas usando a classe [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table) ou [Row](https://reference.aspose.com/pdf/java/com.aspose.pdf/row) método [DefaultCellBorder](https://reference.aspose.com/pdf/java/com.aspose.pdf/Row#setDefaultCellBorder-com.aspose.pdf.BorderInfo-). Todas as propriedades relacionadas a bordas discutidas acima são atribuídas a uma instância da classe Row, que é criada chamando seu construtor. A classe Row tem muitas sobrecargas que aceitam quase todos os parâmetros necessários para personalizar a borda.

## Margens ou Espaçamento Interno

O espaçamento interno de células pode ser gerenciado usando o método [DefaultCellPadding](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#setDefaultCellPadding-com.aspose.pdf.MarginInfo-) da classe Table. Todas as propriedades relacionadas ao preenchimento são atribuídas a uma instância da classe [MarginInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/MarginInfo) que recebe informações sobre os parâmetros `Left`, `Right`, `Top` e `Bottom` para criar margens personalizadas.

No exemplo a seguir, a largura da borda da célula é definida como 0.1 ponto, a largura da borda da tabela é definida como 1 ponto e o preenchimento da célula é definido como 5 pontos.

![Margem e Borda em Tabela PDF](margin-border.png)

```java
public static void MargingPadding() {
        // Instanciar o objeto Document chamando seu construtor vazio
        Document doc = new Document();
        Page page = doc.getPages().add();
        // Instanciar um objeto de tabela
        Table tab1 = new Table();
        // Adicionar a tabela na coleção de parágrafos da seção desejada
        page.getParagraphs().add(tab1);
        // Definir larguras de coluna da tabela
        tab1.setColumnWidths ("50 50 50");
        // Definir borda de célula padrão usando o objeto BorderInfo
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));
        // Definir borda da tabela usando outro objeto BorderInfo personalizado
        tab1.setBorder (new BorderInfo(BorderSide.All, 1F));

        // Criar objeto MarginInfo e definir suas margens esquerda, inferior, direita e superior
        MarginInfo margin = new MarginInfo();
        margin.setTop (5f);
        margin.setLeft (5f);
        margin.setRight (5f);
        margin.setBottom (5f);

        // Definir o preenchimento padrão da célula para o objeto MarginInfo
        tab1.setDefaultCellPadding(margin);

        // Criar linhas na tabela e depois células nas linhas
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 com uma longa string de texto");

        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Salvar o PDF
        doc.save(_dataDir + "MarginsOrPadding_out.pdf");
    }
}
```

Para criar uma tabela com cantos arredondados, use o valor `RoundedBorderRadius` da classe [BorderInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/BorderInfo) e defina o estilo dos cantos da tabela como arredondado.

```java
    public static void RoundedBorderRadius() {
        Document doc = new Document();
        Page page = doc.getPages().add();

        // Instanciar um objeto de tabela
        Table tab1 = new Table();

        // Adicionar a tabela na coleção de parágrafos da seção desejada
        page.getParagraphs().add(tab1);

        GraphInfo graph = new GraphInfo();
        graph.setColor(Color.getRed());
        // Criar um objeto BorderInfo em branco
        BorderInfo bInfo = new BorderInfo(BorderSide.All, graph);
        // Definir a borda como uma borda arredondada onde o raio do arredondamento é 15
        bInfo.setRoundedBorderRadius(15);
        // Definir o estilo do canto da tabela como Arredondado.
        tab1.setCornerStyle(BorderCornerStyle.Round);
        // Definir as informações da borda da tabela
        tab1.setBorder(bInfo);
        // Criar linhas na tabela e depois células nas linhas
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();

        TextFragment mytext = new TextFragment("col3 com uma longa string de texto");

        row1.getCells().get_Item(2).getParagraphs().add(mytext);
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Salvar o PDF
        doc.save(_dataDir + "BorderRadius_out.pdf");
    }
```


### Propriedade AutoFitToWindow na enumeração ColumnAdjustmentType

```java
 public static void AutoFitToWindowProperty() {
        // Instanciar o objeto Pdf chamando seu construtor vazio
        Document doc = new Document();
        // Criar a seção no objeto Pdf
        Page sec1 = doc.getPages().add();

        // Instanciar um objeto de tabela
        Table tab1 = new Table();
        // Adicionar a tabela na coleção de parágrafos da seção desejada
        sec1.getParagraphs().add(tab1);

        // Definir larguras de coluna da tabela
        tab1.setColumnWidths("50 50 50");
        tab1.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);

        // Definir borda de célula padrão usando o objeto BorderInfo
        tab1.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1F));

        // Definir borda da tabela usando outro objeto BorderInfo personalizado
        tab1.setBorder(new BorderInfo(BorderSide.All, 1F));

        // Criar objeto MarginInfo e definir suas margens esquerda, inferior, direita e superior
        MarginInfo margin = new MarginInfo();
        margin.setTop(5f);
        margin.setLeft(5f);
        margin.setRight(5f);
        margin.setBottom(5f);

        // Definir o preenchimento de célula padrão para o objeto MarginInfo
        tab1.setDefaultCellPadding(margin);

        // Criar linhas na tabela e, em seguida, células nas linhas
        Row row1 = tab1.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add("col3");
        Row row2 = tab1.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");

        // Salvar documento atualizado contendo objeto tabela
        doc.save(_dataDir + "AutoFitToWindow_out.pdf");
    }
```


### Obter Largura da Tabela

Às vezes, é necessário obter a largura da tabela dinamicamente. A classe Aspose.PDF.Table possui um método [GetWidth](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table#getWidth--) para esse propósito. Por exemplo, você não definiu a largura das colunas da tabela explicitamente e definiu [ColumnAdjustment](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColumnAdjustment) para AutoFitToContent. Nesse caso, você pode obter a largura da tabela da seguinte forma.

```java
public static void GetTableWidth() {
        // Criar um novo documento
        Document doc = new Document();
        // Adicionar página no documento
        Page page = doc.getPages().add();

        // Inicializar nova tabela
        Table table = new Table();

        // Adicionar a tabela na coleção de parágrafos da seção desejada
        page.getParagraphs().add(table);
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);

        // Adicionar linha na tabela
        Row row = table.getRows().add();
        // Adicionar célula na tabela
        row.getCells().add("Texto da Célula 1");
        row.getCells().add("Texto da Célula 2");
        // Obter largura da tabela
        System.out.println(table.getWidth());
    }
```


## Adicionar Objeto SVG à Célula da Tabela

Aspose.PDF para Java suporta o recurso de adicionar uma célula de tabela em um arquivo PDF. Ao criar uma tabela, é possível adicionar texto ou imagens nas células. Além disso, a API também oferece o recurso de converter arquivos SVG para o formato PDF. Usando uma combinação desses recursos, é possível carregar uma imagem SVG e adicioná-la em uma célula da tabela.

O trecho de código a seguir mostra as etapas para criar uma instância de tabela e adicionar uma imagem SVG dentro de uma célula da tabela.

```java
 public static void AddSVGObjectToTableCell() {
        // Instanciar objeto Document
        Document doc = new Document();
        // Criar uma instância de imagem
        com.aspose.pdf.Image img = new com.aspose.pdf.Image();
        // Definir tipo de imagem como SVG
        img.setFileType (com.aspose.pdf.ImageFileType.Svg);
        // Caminho para o arquivo de origem
        img.setFile (_dataDir + "SVGToPDF.svg");
        // Definir largura para instância de imagem
        img.setFixWidth (50);
        // Definir altura para instância de imagem
        img.setFixHeight (50);
        // Criar instância de tabela
        com.aspose.pdf.Table table = new com.aspose.pdf.Table();
        // Definir largura para células da tabela
        table.setColumnWidths ("100 100");
        // Criar objeto de linha e adicioná-lo à instância de tabela
        com.aspose.pdf.Row row = table.getRows().add();
        // Criar objeto de célula e adicioná-lo à instância de linha
        com.aspose.pdf.Cell cell = row.getCells().add();
        // Adicionar fragmento de texto à coleção de parágrafos do objeto de célula
        cell.getParagraphs().add(new TextFragment("First cell"));
        // Adicionar outra célula ao objeto de linha
        cell = row.getCells().add();
        // Adicionar imagem SVG à coleção de parágrafos da instância de célula recém-adicionada
        cell.getParagraphs().add(img);
        // Criar objeto de página e adicioná-lo à coleção de páginas da instância de documento
        Page page = doc.getPages().add();
        // Adicionar tabela à coleção de parágrafos do objeto de página
        page.getParagraphs().add(table);
        // Salvar arquivo PDF
        doc.save(_dataDir + "AddSVGObject_out.pdf");
    }
```


## Adicionar Tags HTML em uma Tabela

Aspose.PDF para Java permite adicionar um novo Fragmento HTML em um Parágrafo do seu arquivo PDF.

{{% alert color="primary" %}}

Por favor, leve em consideração que o uso de Tags HTML dentro de um elemento de tabela aumenta o tempo de geração do documento, já que a API precisa processar as Tags HTML de acordo e renderizá-las no documento PDF de saída.

{{% /alert %}}

```java
  public static void AddHTMLFragmentToTableCell() {
        Document doc = new Document(_dataDir + "input.pdf");
        // Inicializa uma nova instância da Tabela
        Table table = new Table();
        // Define a cor da borda da tabela como Cinza Claro
        table.setBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // define a borda para as células da tabela
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, .5f, Color.getLightGray()));
        // cria um loop para adicionar 10 linhas
        for (int row_count = 1; row_count < 10; row_count++) {
            Cell cell;
            // adiciona linha à tabela
            Row row = table.getRows().add();
            // adiciona células à tabela
            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Coluna <strong>(" + row_count + ", 1)</strong>"));

            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Coluna <span style='color:red'>(" + row_count + ", 2)</span>"));

            cell = row.getCells().add();
            cell.getParagraphs().add(new HtmlFragment("Coluna <span style='text-decoration: underline'>(" + row_count + ", 3)</span>"));
        }
        // Adiciona o objeto tabela à primeira página do documento de entrada
        doc.getPages().get_Item(1).getParagraphs().add(table);
        // Salva o documento atualizado contendo o objeto tabela
        doc.save(_dataDir + "AddHTMLObject_out.pdf");
    }

}
```


## Inserir uma Quebra de Página entre as linhas da tabela

Como comportamento padrão, ao criar uma tabela dentro de um arquivo PDF, a tabela flui para as páginas subsequentes quando atinge a margem inferior da tabela. No entanto, podemos ter um requisito para forçar a inserção de uma quebra de página quando um certo número de linhas é adicionado à tabela. O trecho de código a seguir mostra as etapas para inserir uma quebra de página quando 10 linhas são adicionadas à tabela.

```java
    public static void InsertPageBreak() {
        // Instanciar instância do Documento
        Document doc = new Document();
        // Adicionar página à coleção de páginas do arquivo PDF
        Page page = doc.getPages().add();
        // Criar instância de tabela
        Table tab = new Table();
        // Definir estilo de borda para a tabela
        tab.setBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // Definir estilo de borda padrão para a tabela com cor de borda como Vermelho
        tab.setDefaultCellBorder (new BorderInfo(BorderSide.All, Color.getRed()));
        // Especificar largura das colunas da tabela
        tab.setColumnWidths ("100 100");
        // Criar um loop para adicionar 200 linhas à tabela
        for (int counter = 0; counter <= 200; counter++) {
            Row row = new Row();
            tab.getRows().add(row);
            Cell cell1 = new Cell();
            cell1.getParagraphs().add(new TextFragment("Cell " + counter + ", 0"));
            row.getCells().add(cell1);
            Cell cell2 = new Cell();
            cell2.getParagraphs().add(new TextFragment("Cell " + counter + ", 1"));
            row.getCells().add(cell2);
            // Quando 10 linhas são adicionadas, renderizar nova linha em nova página
            if (counter % 10 == 0 && counter != 0)
                row.setInNewPage(true);
        }
        // Adicionar tabela à coleção de parágrafos do arquivo PDF
        page.getParagraphs().add(tab);

        // Salvar o documento PDF
        doc.save(_dataDir + "InsertPageBreak_out.pdf");
    }
```


## Ocultar Bordas de Células Abrangidas

Ao adicionar células a uma tabela, as bordas das células abrangidas podem aparecer quando elas se quebram em outra linha. Tais bordas abrangidas podem ser ocultadas conforme mostrado no exemplo de código a seguir.

```java
Document doc = new Document();
com.aspose.pdf.Page page = doc.getPages().add();

//Instanciar um objeto de tabela que será aninhado dentro de outerTable que se quebrará
//dentro da mesma página
com.aspose.pdf.Table mytable = new com.aspose.pdf.Table();
mytable.setBroken(TableBroken.Vertical);
mytable.setDefaultCellBorder(new BorderInfo(BorderSide.All));
mytable.setRepeatingColumnsCount(2);
page.getParagraphs().add(mytable);

//Adicionar Linha de Cabeçalho
com.aspose.pdf.Row row = mytable.getRows().add();
Cell cell = row.getCells().add("cabeçalho 1");
cell.setColSpan(2);
cell.setBackgroundColor(Color.getLightGray());
Cell header3 = row.getCells().add("cabeçalho 3");
Cell cell2 = row.getCells().add("cabeçalho 4");
cell2.setColSpan(2);
cell2.setBackgroundColor(Color.getLightBlue());
row.getCells().add("cabeçalho 6");
Cell cell3 = row.getCells().add("cabeçalho 7");
cell3.setColSpan(2);
cell3.setBackgroundColor(Color.getLightGreen());
Cell cell4 = row.getCells().add("cabeçalho 9");
cell4.setColSpan(3);
cell4.setBackgroundColor(Color.getLightCoral());
row.getCells().add("cabeçalho 12");
row.getCells().add("cabeçalho 13");
row.getCells().add("cabeçalho 14");
row.getCells().add("cabeçalho 15");
row.getCells().add("cabeçalho 16");
row.getCells().add("cabeçalho 17");

for (int rowCounter = 0; rowCounter < 1; rowCounter++)
{
  //Criar linhas na tabela e depois células nas linhas
  com.aspose.pdf.Row row1 = mytable.getRows().add();
  row1.getCells().add("col "+rowCounter+", 1");
  row1.getCells().add("col "+rowCounter+", 2");
  row1.getCells().add("col "+rowCounter+", 3");
  row1.getCells().add("col "+rowCounter+", 4");
  row1.getCells().add("col "+rowCounter+", 5");
  row1.getCells().add("col "+rowCounter+", 6");
  row1.getCells().add("col "+rowCounter+", 7");
  row1.getCells().add("col "+rowCounter+", 8");
  row1.getCells().add("col "+rowCounter+", 9");
  row1.getCells().add("col "+rowCounter+", 10");
  row1.getCells().add("col "+rowCounter+", 11");
  row1.getCells().add("col "+rowCounter+", 12");
  row1.getCells().add("col "+rowCounter+", 13");
  row1.getCells().add("col "+rowCounter+", 14");
  row1.getCells().add("col "+rowCounter+", 15");
  row1.getCells().add("col "+rowCounter+", 16");
  row1.getCells().add("col "+rowCounter+", 17");
}
doc.save(dataDir + "3_out.pdf");
```