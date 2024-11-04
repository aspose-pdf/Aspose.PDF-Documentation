---
title: Substituir Texto em PDF 
linktitle: Substituir Texto em PDF
type: docs
weight: 40
url: /java/replace-text-in-a-pdf-document/
description: Saiba mais sobre várias maneiras de substituir e remover texto de PDF. Aspose.PDF permite substituir texto em uma região específica ou com uma expressão regular.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Substituir Texto em todas as páginas de um documento PDF

{{% alert color="primary" %}}

Você pode tentar encontrar e substituir o texto no documento usando Aspose.PDF e obter os resultados online neste [link](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Para substituir texto em todas as páginas de um documento PDF usando [Aspose.PDF para Java](https://products.aspose.com/pdf/java):

1. Primeiro use [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) para encontrar a frase específica a ser substituída.

1. Em seguida, percorra todos os [TextFragments](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber#getTextFragments--) para substituir o texto e alterar quaisquer outros atributos.
1. Por fim, salve o PDF de saída usando o método [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) da classe Document.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleReplaceText {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void ReplaceTextOnAllPages() {
        Document pdfDocument = new Document(_dataDir+"sample.pdf");

        // Criar objeto TextAbsorber para encontrar todas as instâncias da frase de busca de entrada
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Web");
        
        // Aceitar o absorvedor para a primeira página do documento
        pdfDocument.getPages().accept(textFragmentAbsorber);
        
        // Obter os fragmentos de texto extraídos na coleção
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
        
        // Percorrer os fragmentos
        for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
            // Atualizar texto e outras propriedades
            textFragment.setText("World Wide Web");
            textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getBlue());
            textFragment.getTextState().setBackgroundColor(Color.getGray());
        }
        // Salvar o arquivo PDF atualizado
        pdfDocument.save(_dataDir+"Updated_Text.pdf");
    }
}
```


## Substituir Texto em uma Região Específica da Página

Para substituir texto em uma região específica da página, primeiro precisamos instanciar o objeto TextFragmentAbsorber, especificar a região da página usando [TextSearchOptions.setRectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions#setRectangle-com.aspose.pdf.Rectangle-) e então iterar por todos os TextFragments para substituir o texto. Uma vez que essas operações são concluídas, só precisamos salvar o PDF de saída usando o método save do objeto Document.

O trecho de código a seguir mostra como substituir texto em todas as páginas de um documento PDF.

```java
 public static void ReplaceTextInParticularRegion(){
    // carregar arquivo PDF
    Document pdfDocument = new Document(_dataDir+"sample.pdf");

    // instanciar objeto TextFragment Absorber
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("PDF");

    // buscar texto dentro dos limites da página
    textFragmentAbsorber.getTextSearchOptions().setLimitToPageBounds(true);

    // especificar a região da página para as Opções de Busca de Texto
    textFragmentAbsorber.getTextSearchOptions().setRectangle(new Rectangle(100, 700, 400, 770));

    // buscar texto na primeira página do arquivo PDF
    pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);

    // iterar por cada TextFragment
    for(TextFragment tf : textFragmentAbsorber.getTextFragments())
    {
        // substituir texto por "---"
        tf.setText("---");
    }

    // Salvar o arquivo PDF atualizado
    pdfDocument.save(_dataDir+"Updated_Text.pdf");
}
```


## Substituir Texto com Base em uma Expressão Regular

Se você deseja substituir algumas frases com base em uma expressão regular, primeiro precisa encontrar todas as frases que correspondem a essa expressão regular específica usando o TextFragmentAbsorber. Você terá que passar a expressão regular como um parâmetro para o construtor do TextFragmentAbsorber. Você também precisa criar um objeto TextSearchOptions que especifique se a expressão regular está sendo usada ou não. Assim que obter as frases correspondentes em TextFragments, você precisará percorrer todas elas e atualizar conforme necessário. Por fim, você precisa salvar o PDF atualizado usando o método Save do objeto Document.

O snippet de código a seguir mostra como substituir texto com base em uma expressão regular.

```java
public static void ReplaceTextWithRegularExpression() {
    // carregar arquivo PDF
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // Criar objeto TextAbsorber para encontrar todas as instâncias da frase de pesquisa de entrada
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); 
    // como 1999-2000

    // Definir opção de pesquisa de texto para especificar o uso de expressão regular
    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

    // Aceitar o absorvedor para a primeira página do documento
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Obter os fragmentos de texto extraídos na coleção
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // Percorrer os fragmentos
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Atualizar texto e outras propriedades
        textFragment.setText("ABCD-EFGH");
        textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }

    // Salvar o arquivo PDF atualizado
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


## Substituir fontes em arquivo PDF existente

O Aspose.PDF para Java suporta a capacidade de substituir texto em documento PDF. No entanto, às vezes é necessário apenas substituir a fonte que está sendo usada dentro do documento PDF. Assim, em vez de substituir o texto, apenas a fonte em uso é substituída. Uma das sobrecargas do construtor TextFragmentAbsorber aceita um objeto TextEditOptions como argumento e podemos usar o valor RemoveUnusedFonts da enumeração TextEditOptions.FontReplace para atender nossos requisitos.

O seguinte trecho de código mostra como substituir a fonte dentro do documento PDF.

```java
public static void ReplaceFonts() {
    // Instanciar objeto Documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Pesquisar fragmentos de texto e definir opção de edição como remover fontes não utilizadas
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(
            new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

    // Aceitar o absorvente para todas as páginas do documento
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // percorrer todos os TextFragments
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection)
    {
        String fontName = textFragment.getTextState().getFont().getFontName();
        // se o nome da fonte for ArialMT, substituir o nome da fonte por Arial
        if (fontName.equals("ArialMT")) {
            textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        }
    }

    // Salvar o arquivo PDF atualizado
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


### Use Non-English (Japanese) Font When Replacing Text

O seguinte trecho de código mostra como substituir texto por caracteres japoneses. Observe que, para adicionar texto em japonês, você precisa usar uma fonte que suporte caracteres japoneses (por exemplo, MSGothic).

```java
public static void UseNonEnglishFontWhenReplacingText() {

    // Instanciar objeto Document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Vamos mudar cada palavra "page" para algum texto japonês com fonte específica
    // TakaoMincho que pode estar instalada no sistema operacional
    // Além disso, pode ser outra fonte que suporte hieróglifos
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("page");

    // Criar instância de opções de pesquisa de texto
    TextSearchOptions searchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(searchOptions);

    // Aceitar o absorvedor para todas as páginas do documento
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Obter os fragmentos de texto extraídos na coleção
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    
    // Percorrer os fragmentos
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Atualizar texto e outras propriedades
        textFragment.setText("ファイル");
        textFragment.getTextState().setFont(FontRepository.findFont("MSGothic"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }
    // Salvar o documento atualizado
    pdfDocument.save(_dataDir + "Japanese_Text.pdf");
}
```


## A Substituição de Texto deve reorganizar automaticamente o Conteúdo da Página

O Aspose.PDF para Java suporta o recurso de buscar e substituir texto dentro do arquivo PDF. No entanto, recentemente, alguns clientes encontraram problemas durante a substituição de texto quando um determinado TextFragment é substituído por conteúdos menores e alguns espaços extras são exibidos no PDF resultante ou, caso o TextFragment seja substituído por uma string mais longa, as palavras se sobrepõem aos conteúdos existentes da página. Portanto, a exigência era introduzir um mecanismo para que, uma vez que o texto dentro de um documento PDF seja substituído, os conteúdos sejam reorganizados.

Para atender aos cenários mencionados acima, o Aspose.PDF para Java foi aprimorado para que tais problemas não apareçam ao substituir texto dentro do arquivo PDF. O trecho de código a seguir mostra como substituir texto dentro do arquivo PDF e o conteúdo da página deve ser reorganizado automaticamente.

```java
public static void RearrangeContent() {
    // Carregar arquivo PDF de origem
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Criar objeto TextFragment Absorber com expressão regular
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[PDF,Web]");

    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
    
    // Você também pode especificar a opção ReplaceAdjustment.WholeWordsHyphenation para quebrar o texto na próxima ou atual linha
    // se a linha atual se tornar muito longa ou curta após a substituição:
    // textFragmentAbsorber.getTextReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.WholeWordsHyphenation);

    // Aceitar o absorber para todas as páginas do documento
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Obter os fragmentos de texto extraídos na coleção
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // Substituir cada TextFragment
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Definir fonte do fragmento de texto sendo substituído
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        // Definir tamanho da fonte
        textFragment.getTextState().setFontSize(10);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
        // Substituir o texto por uma string maior que o espaço reservado
        textFragment.setText("Esta é uma string maior para o teste deste recurso");
    }
    // Salvar PDF resultante
    pdfDocument.save(_dataDir + "RearrangeContentsUsingTextReplacement_out.pdf");
}
```


## Renderização de Símbolos Substituíveis durante a criação de PDF

Símbolos substituíveis são símbolos especiais em uma string de texto que podem ser substituídos pelo conteúdo correspondente em tempo de execução. Os símbolos substituíveis atualmente suportados pelo novo Document Object Model do namespace Aspose.PDF são `$P`, `$p`, `\n`, `\r`. O `$p` e `$P` são usados para lidar com a numeração de páginas em tempo de execução. `$p` é substituído pelo número da página onde a classe Paragraph atual está. `$P` é substituído pelo número total de páginas no documento. Ao adicionar [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) à coleção de parágrafos dos documentos PDF, ele não suporta quebra de linha dentro do texto. No entanto, para adicionar texto com quebra de linha, por favor use [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) com [TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph):

- use "\r\n" ou Environment.NewLine em TextFragment em vez de um único "\n";
- crie um objeto TextParagraph.
 Ele adicionará texto com divisão de linha;
- adicione o TextFragment com TextParagraph.AppendLine;
- adicione o TextParagraph com TextBuilder.AppendParagraph.

```java
public static void RenderingReplaceableSymbols() {
    // carregar arquivo PDF
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    Page page = pdfDocument.getPages().add();

    // Inicializar novo TextFragment com texto contendo marcadores de nova linha necessários
    TextFragment textFragment = new TextFragment("Nome do Candidato: " + System.lineSeparator() + " Joe Smoe");

    // Definir propriedades do fragmento de texto, se necessário
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());

    // Criar objeto TextParagraph
    TextParagraph par = new TextParagraph();

    // Adicionar novo TextFragment ao parágrafo
    par.appendLine(textFragment);

    // Definir posição do parágrafo
    par.setPosition (new Position(100, 600));

    // Criar objeto TextBuilder
    TextBuilder textBuilder = new TextBuilder(page);
    // Adicionar o TextParagraph usando TextBuilder
    textBuilder.appendParagraph(par);

    _dataDir = _dataDir + "RenderingReplaceableSymbols_out.pdf";
    pdfDocument.save(_dataDir);
}
```

## Símbolos substituíveis na área de Cabeçalho/Rodapé

Símbolos substituíveis também podem ser colocados na seção de Cabeçalho/Rodapé do arquivo PDF. Por favor, veja o trecho de código a seguir para detalhes sobre como adicionar um símbolo substituível na seção de rodapé.

```java
public static void ReplaceableSymbolsInHeaderFooterArea() {
    Document doc = new Document();
    Page page = doc.getPages().add();

    MarginInfo marginInfo = new MarginInfo();
    marginInfo.setTop(90);
    marginInfo.setBottom(50);
    marginInfo.setLeft(50);
    marginInfo.setRight(50);

    // Atribuir a instância de marginInfo à propriedade Margin de sec1.PageInfo
    page.getPageInfo().setMargin(marginInfo);

    HeaderFooter hfFirst = new HeaderFooter();
    page.setHeader(hfFirst);
    hfFirst.getMargin().setLeft(50);
    hfFirst.getMargin().setRight(50);

    // Instanciar um parágrafo de texto que armazenará o conteúdo a ser exibido como cabeçalho
    TextFragment t1 = new TextFragment("título do relatório");
    t1.getTextState().setFont(FontRepository.findFont("Arial"));
    t1.getTextState().setFontSize(16);
    t1.getTextState().setForegroundColor(Color.getBlack());
    t1.getTextState().setFontStyle(FontStyles.Bold);
    t1.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t1.getTextState().setLineSpacing(5f);
    hfFirst.getParagraphs().add(t1);

    TextFragment t2 = new TextFragment("Nome_Relatório");
    t2.getTextState().setFont(FontRepository.findFont("Arial"));
    t2.getTextState().setForegroundColor(Color.getBlack());
    t2.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t2.getTextState().setLineSpacing(5f);
    t2.getTextState().setFontSize(12);
    hfFirst.getParagraphs().add(t2);

    // Criar um objeto HeaderFooter para a seção
    HeaderFooter hfFoot = new HeaderFooter();

    // Definir o objeto HeaderFooter para rodapé ímpar e par
    page.setFooter(hfFoot);
    hfFoot.getMargin().setLeft(50);
    hfFoot.getMargin().setRight(50);

    // Adicionar um parágrafo de texto contendo o número da página atual do número total de páginas
    TextFragment t3 = new TextFragment("Gerado em data de teste");
    TextFragment t4 = new TextFragment("nome do relatório ");
    TextFragment t5 = new TextFragment("Página $p de $P");

    // Instanciar um objeto de tabela
    Table tab2 = new Table();

    // Adicionar a tabela na coleção de parágrafos da seção desejada
    hfFoot.getParagraphs().add(tab2);

    // Definir a largura das colunas da tabela
    tab2.setColumnWidths("165 172 165");

    // Criar linhas na tabela e depois células nas linhas
    Row row3 = tab2.getRows().add();

    row3.getCells().add();
    row3.getCells().add();
    row3.getCells().add();

    // Definir o alinhamento vertical do texto como centralizado
    row3.getCells().get_Item(0).setAlignment(HorizontalAlignment.Left);
    row3.getCells().get_Item(1).setAlignment(HorizontalAlignment.Center);
    row3.getCells().get_Item(2).setAlignment(HorizontalAlignment.Right);

    row3.getCells().get_Item(0).getParagraphs().add(t3);
    row3.getCells().get_Item(1).getParagraphs().add(t4);
    row3.getCells().get_Item(2).getParagraphs().add(t5);

    Table table = new Table();

    table.setColumnWidths("33% 33% 34%");
    table.setDefaultCellPadding(new MarginInfo());
    table.getDefaultCellPadding().setTop(10);
    table.getDefaultCellPadding().setBottom(10);

    // Adicionar a tabela na coleção de parágrafos da seção desejada
    page.getParagraphs().add(table);

    // Definir o contorno padrão das células usando o objeto BorderInfo
    table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));

    // Definir o contorno da tabela usando outro objeto BorderInfo personalizado
    table.setBorder(new BorderInfo(BorderSide.All, 1f));

    table.setRepeatingRowsCount(1);

    // Criar linhas na tabela e depois células nas linhas
    Row row1 = table.getRows().add();

    row1.getCells().add("col1");
    row1.getCells().add("col2");
    row1.getCells().add("col3");
    String CRLF = "\r\n";

    for (int i = 0; i <= 10; i++) {
        Row row = table.getRows().add();
        row.setRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            Cell c1;
            if (c == 2)
                c1 = row.getCells().add(
                        "Aspose.Total para Java é uma compilação de todos os componentes Java oferecidos pela Aspose. É compilado em uma"
                                + CRLF
                                + "base diária para garantir que contenha as versões mais atualizadas de cada um dos nossos componentes Java. "
                                + CRLF
                                + "base diária para garantir que contenha as versões mais atualizadas de cada um dos nossos componentes Java. "
                                + CRLF
                                + "Usando Aspose.Total para Java, os desenvolvedores podem criar uma ampla gama de aplicações.");
            else
                c1 = row.getCells().add("item1" + c);
            c1.setMargin(new MarginInfo());
            c1.getMargin().setLeft(30);
            c1.getMargin().setTop(10);
            c1.getMargin().setBottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```


## Remover Todo o Texto do Documento PDF

### Remover Todo o Texto usando Operadores

Em algumas operações de texto, é necessário remover todo o texto de um documento PDF e, para isso, geralmente é preciso definir o texto encontrado como um valor de string vazio. O ponto é que alterar o texto para uma multitude de fragmentos de texto invoca uma série de operações de verificação e ajuste de posição do texto. Elas são essenciais nos cenários de edição de texto. A dificuldade é que você não pode determinar quantos fragmentos de texto serão removidos no cenário em que eles são processados em um loop.

Portanto, recomendamos usar outra abordagem para o cenário de remoção de todo o texto das páginas PDF. Por favor, considere o seguinte trecho de código que funciona muito rapidamente.

```java
public static void RemoveAllTextUsingOperators() {
    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Loop através de todas as páginas do Documento PDF
    for (int i = 1; i <= pdfDocument.getPages().size(); i++) {
        Page page = pdfDocument.getPages().get_Item(i);
        OperatorSelector operatorSelector = new OperatorSelector(new com.aspose.pdf.operators.TextShowOperator());
        // Selecionar todo o texto da página
        page.getContents().accept(operatorSelector);
        // Excluir todo o texto
        page.getContents().delete(operatorSelector.getSelected());
    }
    // Salvar o documento
    pdfDocument.save(_dataDir + "RemoveAllText_out.pdf");
}
```