---
title: Substituir Texto em PDF usando C++
linktitle: Substituir Texto em PDF
type: docs
weight: 40
url: pt/cpp/replace-text-in-pdf/
description: Saiba mais sobre várias maneiras de substituir e remover texto de um PDF. Aspose.PDF permite substituir texto em uma região específica ou com uma expressão regular.
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Às vezes, surge a tarefa de corrigir ou substituir texto em um documento PDF. Tentar fazer isso manualmente será uma tarefa assustadora, então aqui está a solução para esse problema.

Honestamente, editar um arquivo PDF não é uma tarefa fácil. Portanto, uma situação em que você precisa encontrar e substituir uma palavra por outra enquanto edita um arquivo PDF será muito difícil, pois levará muito tempo para fazê-lo. Além disso, você pode encontrar muitos problemas com seu resultado, como formatação ou fontes quebradas. Se você deseja encontrar e substituir texto facilmente em arquivos PDF, recomendamos que use o software da biblioteca Aspose.Pdf, pois ele fará o trabalho em minutos.

Neste artigo, mostraremos como encontrar e substituir texto com sucesso em seus arquivos PDF usando o Aspose.PDF para C++.

## Substituir Texto em todas as páginas do documento PDF

{{% alert color="primary" %}}

Você pode tentar encontrar e substituir o texto no documento usando Aspose.PDF e obter os resultados online neste [link](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Para substituir texto em todas as páginas de um documento PDF, primeiro você precisa usar TextFragmentAbsorber para encontrar a frase específica que deseja substituir. Depois disso, você precisa percorrer todos os TextFragments para substituir o texto e alterar quaisquer outros atributos. Uma vez feito isso, você só precisa salvar o PDF de saída usando o método Save do objeto Document. O trecho de código a seguir mostra como substituir texto em todas as páginas de um documento PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextOnAllPages() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Criar objeto TextAbsorber para encontrar todas as instâncias da frase de pesquisa de entrada
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("Web");

    // Aceitar o absorvedor para a primeira página do documento
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Obter os fragmentos de texto extraídos na coleção
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Percorrer os fragmentos
    for (auto textFragment : textFragmentCollection) {
        // Atualizar texto e outras propriedades
        textFragment->set_Text(u"World Wide Web");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // Salvar o arquivo PDF atualizado
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Substituir Texto em uma Região Específica da Página

Para substituir texto em uma região específica da página, primeiro precisamos instanciar o objeto TextFragmentAbsorber, especificar a região da página usando a propriedade TextSearchOptions.Rectangle e depois iterar por todos os TextFragments para substituir o texto. Uma vez que essas operações são concluídas, só precisamos salvar o PDF de saída usando o método Save do objeto Document. O código a seguir mostra como substituir texto em todas as páginas de um documento PDF.

```cpp
void ReplaceTextInParticularRegion() {

    String _dataDir("C:\\Samples\\");

    // carregar arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // instanciar objeto TextFragment Absorber
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // procurar texto dentro dos limites da página
    textFragmentAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);

    // especificar a região da página para Opções de Pesquisa de Texto
    textFragmentAbsorber->get_TextSearchOptions()->set_Rectangle(new Rectangle(100, 700, 400, 770));

    // procurar texto da primeira página do arquivo PDF
    document->get_Pages()->idx_get(1)->Accept(textFragmentAbsorber);

    // iterar por cada TextFragment
    for (auto tf : textFragmentAbsorber->get_TextFragments()) {
        // substituir texto por "---"
        tf->set_Text(u"---");
    }

    // Salvar o arquivo PDF atualizado
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Substituir Texto com Base em uma Expressão Regular

Se você deseja substituir algumas frases com base em uma expressão regular, primeiro precisa encontrar todas as frases que correspondem a essa expressão regular específica usando TextFragmentAbsorber. Você terá que passar a expressão regular como um parâmetro para o construtor TextFragmentAbsorber. Você também precisa criar um objeto TextSearchOptions que especifica se a expressão regular está sendo usada ou não. Assim que você obtiver as frases correspondentes em TextFragments, você precisa percorrer todas elas e atualizar conforme necessário. Finalmente, você precisa salvar o PDF atualizado usando o método Save do objeto Document. O trecho de código a seguir mostra como substituir texto com base em uma expressão regular.

```cpp
void ReplaceTextWithRegularExpression() {

    String _dataDir("C:\\Samples\\");

    // load PDF file
    auto document = MakeObject<Document>(_dataDir + u"Sample.pdf");
    // Create TextAbsorber object to find all instances of the input search phrase
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("\\d{4}-\\d{4}");
    // like 1999-2000

    // Set text search option to specify regular expression usage
    auto textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Accept the absorber for first page of document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Loop through the fragments
    for (auto textFragment : textFragmentCollection) {
        // Update text and other properties
        textFragment->set_Text(u"ABCD-EFGH");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }

    // Save the updated PDF file
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Substituir fontes em arquivo PDF existente

Aspose.PDF para C++ suporta a capacidade de substituir texto em um documento PDF. No entanto, às vezes você tem a necessidade de substituir apenas a fonte sendo usada dentro do documento PDF. Então, em vez de substituir o texto, apenas a fonte utilizada é substituída. Uma das sobrecargas do construtor TextFragmentAbsorber aceita um objeto TextEditOptions como argumento e podemos usar o valor RemoveUnusedFonts da enumeração TextEditOptions.FontReplace para atender aos nossos requisitos. O seguinte trecho de código mostra como substituir a fonte dentro do documento PDF.

```cpp
void ReplaceFonts() {
    String _dataDir("C:\\Samples\\");

    // Instanciar objeto Document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Procurar fragmentos de texto e definir a opção de edição como remover fontes não utilizadas
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(
        MakeObject<TextEditOptions>(TextEditOptions::FontReplace::RemoveUnusedFonts));

    // Aceitar o absorvedor para todas as páginas do documento
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Percorrer todos os TextFragments
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();
    for (auto textFragment : textFragmentCollection) {
        String fontName = textFragment->get_TextState()->get_Font()->get_FontName();
        // se o nome da fonte for ArialMT, substituir o nome da fonte por Arial
        if (fontName.Equals(u"ArialMT")) {
            textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        }
    }

    // Salvar o arquivo PDF atualizado
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

No próximo trecho de código, você verá como usar uma fonte não inglesa ao substituir texto:

```cpp
void UseNonEnglishFontWhenReplacingText() {

    String _dataDir("C:\\Samples\\");

    // Instanciar objeto Documento
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Vamos mudar todas as palavras "PDF" para algum texto em japonês com fonte específica
    // MSGothic que pode estar instalada no sistema operacional
    // Além disso, pode ser outra fonte que suporte hieróglifos
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // Criar instância de opções de pesquisa de texto
    auto searchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(searchOptions);

    // Aceitar o absorvedor para todas as páginas do documento
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Obter os fragmentos de texto extraídos em uma coleção
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Percorrer os fragmentos
    for (auto textFragment : textFragmentCollection) {
        // Atualizar texto e outras propriedades
        textFragment->set_Text(u"ファイル");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"TakaoMincho"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // Salvar o documento atualizado
    document->Save(_dataDir + u"Japanese_Text.pdf");
}
```

## A Substituição de Texto deve reorganizar automaticamente o Conteúdo da Página

Aspose.PDF para C++ suporta encontrar e substituir texto dentro de um arquivo PDF. Recentemente, no entanto, alguns clientes tiveram problemas ao substituir texto, onde um determinado TextFragment é substituído por um conteúdo menor e algum espaço em branco extra é exibido no PDF resultante, ou se o TextFragment for substituído por uma string mais longa, então as palavras se sobrepõem ao conteúdo existente da página. Assim, foi necessário introduzir um mecanismo que, após substituir o texto dentro do documento PDF, reorganizasse seu conteúdo.

Para atender aos cenários mencionados, o Aspose.PDF para C++ foi aprimorado para que tais problemas não ocorram ao substituir texto dentro de um arquivo PDF. O seguinte trecho de código demonstra como substituir texto dentro de um arquivo PDF e o conteúdo da página deve ser reordenado automaticamente.

```cpp
void RearrangeContent() {
    String _dataDir("C:\\Samples\\");

    // Instanciar objeto Document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Criar objeto TextFragment Absorber com expressão regular
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("[PDF,Web]");

    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Você também pode especificar a opção ReplaceAdjustment.WholeWordsHyphenation para
    // quebrar o texto na próxima linha ou na linha atual se a linha atual ficar muito longa ou
    // curta após a substituição:
    //textFragmentAbsorber->get_TextReplaceOptions()->set_ReplaceAdjustmentAction(TextReplaceOptions::ReplaceAdjustment::WholeWordsHyphenation);

    // Aceitar o absorvedor para todas as páginas do documento
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Obter os fragmentos de texto extraídos na coleção
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Substituir cada TextFragment
    for (auto textFragment : textFragmentCollection) {
        // Definir fonte do fragmento de texto sendo substituído
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        // Definir tamanho da fonte
        textFragment->get_TextState()->set_FontSize(10);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
        // Substituir o texto por uma string maior que o espaço reservado
        textFragment->set_Text(u"Isto é uma string maior para o teste desta funcionalidade");
    }
    // Salvar PDF resultante
    document->Save(_dataDir + u"RearrangeContentsUsingTextReplacement_out.pdf");
}
```

## Renderização de Símbolos Substituíveis durante a criação de PDF

Símbolos substituíveis são símbolos especiais em uma string de texto que podem ser substituídos por conteúdo correspondente em tempo de execução. Os símbolos substituíveis atualmente suportados pelo novo Modelo de Objeto de Documento do namespace Aspose.PDF são `$P`, `$p,` `\n`, `\r`. O `$p` e `$P` são usados para lidar com a numeração de páginas em tempo de execução. `$p` é substituído pelo número da página onde a classe atual Paragraph está. `$P` é substituído pelo número total de páginas no documento. Ao adicionar `TextFragment` à coleção de parágrafos de documentos PDF, ele não suporta quebra de linha dentro do texto. No entanto, para adicionar texto com uma quebra de linha, por favor, use `TextFragment` com `TextParagraph`:

- use "\r\n" ou Environment.NewLine em TextFragment em vez de um único "\n";
- crie um objeto TextParagraph. Isso adicionará texto com divisão de linhas;
- adicione o TextFragment com TextParagraph.AppendLine;
- adicione o TextParagraph com TextBuilder.AppendParagraph.

```cpp
void RenderingReplaceableSymbols() {

    String _dataDir("C:\\Samples\\");

    // carregar arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->Add();

    // Inicializar novo TextFragment com texto contendo marcadores de nova linha necessários
    auto textFragment = MakeObject<TextFragment>("Applicant Name: \r\n Joe Smoe");

    // Definir propriedades do fragmento de texto, se necessário
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());

    // Criar objeto TextParagraph
    auto par = MakeObject<TextParagraph>();

    // Adicionar novo TextFragment ao parágrafo
    par->AppendLine(textFragment);

    // Definir posição do parágrafo
    par->set_Position(MakeObject<Position>(100, 600));

    // Criar objeto TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);

    // Adicionar o TextParagraph usando TextBuilder
    textBuilder->AppendParagraph(par);

    document->Save(_dataDir + u"RenderingReplaceableSymbols_out.pdf");
}
```

## Símbolos substituíveis na área de Cabeçalho/Rodapé

O símbolo substituível também pode ser colocado dentro da seção de cabeçalho/rodapé do arquivo PDF. Revise o trecho de código a seguir para ver como adicionar um símbolo substituível a uma seção de rodapé.

```csharp
void ReplaceableSymbolsInHeaderFooterArea() {

    auto document = MakeObject<Document>();
    auto page = doc.getPages().add();

    auto marginInfo = MakeObject<MarginInfo>();
    marginInfo->set_Top(90);
    marginInfo->set_Bottom(50);
    marginInfo->set_Left(50);
    marginInfo->set_Right(50);

    // Atribuir a instância marginInfo à propriedade Margin do PageInfo
    page.getPageInfo()->set_Margin(marginInfo);

    auto hfFirst = MakeObject<HeaderFooter>();
    page->set_Header(hfFirst);
    hfFirst->get_Margin()->set_Left(50);
    hfFirst->get_Margin()->set_Right(50);

    // Instanciar um parágrafo de texto que armazenará o conteúdo a ser exibido como cabeçalho
    auto t1 = MakeObject<TextFragment>("título do relatório");
    t1->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t1->get_TextState()->set_FontSize(16);
    t1->get_TextState()->set_ForegroundColor(Color::get_Black());
    t1->get_TextState()->set_FontStyle(FontStyles::Bold);
    t1->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t1->get_TextState()->set_LineSpacing(5.0f);
    hfFirst->get_Paragraphs()->Add(t1);

    auto t2 = MakeObject<TextFragment>("Nome_Relatório");
    t2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t2->get_TextState()->set_ForegroundColor(Color::get_Black());
    t2->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t2->get_TextState()->set_LineSpacing(5.0f);
    t2->get_TextState()->set_FontSize(12);
    hfFirst->get_Paragraphs()->Add(t2);

    // Criar um objeto HeaderFooter para a seção
    auto hfFoot = MakeObject<HeaderFooter>();

    // Definir o objeto HeaderFooter para rodapé ímpar e par
    page->set_Footer(hfFoot);
    hfFoot->get_Margin()->set_Left(50);
    hfFoot->get_Margin()->set_Right(50);

    // Adicionar um parágrafo de texto contendo o número da página atual do total de páginas
    auto t3 = MakeObject<TextFragment>("Gerado na data de teste");
    auto t4 = MakeObject<TextFragment>("nome do relatório ");
    auto t5 = MakeObject<TextFragment>("Página $p de $P");

    // Instanciar um objeto Table
    auto tab2 = MakeObject<Table>();

    // Adicionar a tabela na coleção de parágrafos da seção desejada
    hfFoot->get_Paragraphs()->Add(tab2);

    // Definir as larguras das colunas da tabela
    tab2->set_ColumnWidths(u"165 172 165");

    // Criar linhas na tabela e depois células nas linhas
    auto row3 = tab2->get_Rows()->Add();

    row3->get_Cells()->Add();
    row3->get_Cells()->Add();
    row3->get_Cells()->Add();

    // Definir o alinhamento vertical do texto como centralizado
    row3->get_Cells()->idx_get(0)->set_Alignment(HorizontalAlignment::Left);
    row3->get_Cells()->idx_get(1)->set_Alignment(HorizontalAlignment::Center);
    row3->get_Cells()->idx_get(2)->set_Alignment(HorizontalAlignment::Right);

    row3->get_Cells()->idx_get(0)->get_Paragraphs()->Add(t3);
    row3->get_Cells()->idx_get(1)->get_Paragraphs()->Add(t4);
    row3->get_Cells()->idx_get(2)->get_Paragraphs()->Add(t5);

    auto table = MakeObject<Table>();

    table->set_ColumnWidths(u"33% 33% 34%");
    table->set_DefaultCellPadding(new MarginInfo());
    table->get_DefaultCellPadding()->set_Top(10);
    table->get_DefaultCellPadding()->set_Bottom(10);

    // Adicionar a tabela na coleção de parágrafos da seção desejada
    page.getParagraphs().add(table);

    // Definir a borda padrão da célula usando o objeto BorderInfo
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.1f));

    // Definir a borda da tabela usando outro objeto BorderInfo personalizado
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1.0f));

    table->set_RepeatingRowsCount(1);

    // Criar linhas na tabela e depois células nas linhas
    auto row1 = table->get_Rows()->Add();

    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    String CRLF ("\r\n");

    for (int i = 0; i <= 10; i++) {
        auto row = table->get_Rows()->Add();
        row->set_IsRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            SharedPtr<Cell> c1;
            if (c == 2)
                c1 = row->get_Cells()->Add(
                    u"Aspose.Total para C++ é uma compilação de todos os componentes Java oferecidos pela Aspose. É compilado em uma"
                    + CRLF
                    + u"base diária para garantir que contenha as versões mais atualizadas de cada um dos nossos componentes Java. "
                    + CRLF
                    + u"base diária para garantir que contenha as versões mais atualizadas de cada um dos nossos componentes Java. "
                    + CRLF
                    + u"Usando Aspose.Total para C++ desenvolvedores podem criar uma ampla gama de aplicações.");
            else
                c1 = row->get_Cells()->Add(u"item1" + c);
            c1->set_Margin(new MarginInfo());
            c1->get_Margin()->set_Left(30);
            c1->get_Margin()->set_Top(10);
            c1->get_Margin()->set_Bottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```

## Remover Todo o Texto do Documento PDF

### Remover Todo o Texto usando Operadores

Em algumas operações de texto, você precisa remover todo o texto do documento PDF, e para isso, geralmente precisa definir o texto encontrado como um valor de string vazio. O fato é que alterar o texto para um conjunto de fragmentos de texto causa uma série de operações para verificar e ajustar a posição do texto. Elas são necessárias em scripts de edição de texto. A dificuldade reside no fato de que você não pode determinar quantos pedaços de texto serão deletados no script onde eles são processados no loop.

Portanto, recomendamos usar uma abordagem diferente para o cenário de remover todo o texto das páginas do PDF.

O seguinte trecho de código mostra como resolver essa tarefa rapidamente.

```cpp
void RemoveAllTextUsingOperators() {

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Percorrer todas as páginas do Documento PDF
    for (int i = 1; i <= document->get_Pages()->get_Count(); i++) {
        auto page = document->get_Pages()->idx_get(i);
        auto operatorSelector = MakeObject<OperatorSelector>(MakeObject<Aspose::Pdf::Operators::TextShowOperator>());
        // Selecionar todo o texto na página
        page->get_Contents()->Accept(operatorSelector);
        // Excluir todo o texto
        page->get_Contents()->Delete(operatorSelector->get_Selected());
    }
    // Salvar o documento
    document->Save(_dataDir + u"RemoveAllText_out.pdf");
}
```