---
title: Adicionar Texto ao Arquivo PDF 
linktitle: Adicionar Texto ao Arquivo PDF
type: docs
weight: 10
url: /java/add-text-to-pdf-file/
description: Este artigo descreve vários aspectos do trabalho com texto no Aspose.PDF. Aprenda como adicionar texto ao PDF, adicionar fragmentos HTML ou usar fontes OTF personalizadas.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Para adicionar texto a um arquivo PDF existente:

1. Abra o PDF de entrada usando o objeto Document.
2. Obtenha a página específica à qual você deseja adicionar o texto.
3. Crie um objeto TextFragment com o texto de entrada junto com outras propriedades de texto. O objeto TextBuilder criado a partir daquela página específica – à qual você deseja adicionar o texto – permite que você adicione o objeto TextFragment à página usando o método AppendText.
4. Chame o método Save do objeto Document e salve o arquivo PDF de saída.

## Adicionando Texto

O código a seguir mostra como adicionar texto em um arquivo PDF existente.

```java
public static void AddingText() {
    // Carregar o arquivo PDF
    Document document = new Document(_dataDir + "sample.pdf");

    // obter página específica
    Page pdfPage = document.getPages().get_Item(1);
    // criar fragmento de texto
    TextFragment textFragment = new TextFragment("Aspose.PDF");
    textFragment.setPosition(new Position(80, 700));

    // definir propriedades do texto
    textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
    textFragment.getTextState().setFontSize(14);
    textFragment.getTextState().setForegroundColor(Color.getBlue());
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());

    // criar objeto TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // anexar o fragmento de texto à página PDF
    textBuilder.appendText(textFragment);

    // Salvar o documento PDF resultante.
    document.save(_dataDir + "AddText_out.pdf");
}
```


## Carregando Fonte a partir de Stream

O trecho de código a seguir mostra como carregar uma fonte a partir de um objeto Stream ao adicionar texto a um documento PDF.

```java
import com.aspose.pdf.*;
import com.aspose.pdf.text.FontTypes;

import java.io.FileInputStream;
import java.io.FileNotFoundException;  
//...
public static void LoadingFontFromStream() throws FileNotFoundException{
    
    String fontFile = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf";

    // Carregar arquivo PDF de entrada
    Document doc = new Document(_dataDir + "input.pdf");
    // Criar objeto construtor de texto para a primeira página do documento
    TextBuilder textBuilder = new TextBuilder(doc.getPages().get_Item(1));
    // Criar fragmento de texto com string de exemplo
    TextFragment textFragment = new TextFragment("Hello world");
    
    if (fontFile != "")
    {
        // Carregar a fonte TrueType no objeto stream
        FileInputStream fontStream=new FileInputStream(fontFile);            
        // Definir o nome da fonte para a string de texto
        textFragment.getTextState().setFont (FontRepository.openFont(fontStream, FontTypes.TTF));
        // Especificar a posição para o Fragmento de Texto
        textFragment.setPosition(new Position(10, 10));
        // Adicionar o texto ao TextBuilder para que ele possa ser colocado sobre o arquivo PDF
        textBuilder.appendText(textFragment);
        
        _dataDir = _dataDir + "LoadingFontFromStream_out.pdf";
    
        // Salvar o documento PDF resultante.
        doc.save(_dataDir); 
    }       
}
```


## Adicionar Texto usando TextParagraph

O trecho de código a seguir mostra como adicionar texto em um documento PDF usando a classe [TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph).

```java
public static void AddTextUsingTextParagraph() {
    // Abrir documento
    Document doc = new Document();
    // Adicionar página à coleção de páginas do objeto Document
    Page page = doc.getPages().add();
    TextBuilder builder = new TextBuilder(page);
    // Criar parágrafo de texto
    TextParagraph paragraph = new TextParagraph();
    // Definir recuo das linhas subsequentes
    paragraph.setSubsequentLinesIndent (20);
    // Especificar o local para adicionar TextParagraph
    paragraph.setRectangle(new Rectangle(100, 300, 200, 700));
    // Especificar modo de quebra de linha
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    // Criar fragmento de texto
    TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
    fragment1.getTextState().setFont (FontRepository.findFont("Times New Roman"));
    fragment1.getTextState().setFontSize (12);
    // Adicionar fragmento ao parágrafo
    paragraph.appendLine(fragment1);
    // Adicionar parágrafo
    builder.appendParagraph(paragraph);

    _dataDir = _dataDir + "AddTextUsingTextParagraph_out.pdf";

    // Salvar documento PDF resultante.
    doc.save(_dataDir);        
}
```


## Adicionar Hiperlink ao TextSegment

Uma página PDF pode ser composta por um ou mais objetos TextFragment, onde cada objeto TextFragment pode ter uma ou mais instâncias de TextSegment. Para definir um hiperlink para TextSegment, a propriedade Hyperlink da classe TextSegment pode ser usada ao fornecer o objeto da instância Aspose.Pdf.WebHyperlink. Por favor, tente usar o seguinte trecho de código para cumprir este requisito.

```java
public static void AddHyperlinkToTextSegment() {
    // Criar instância de documento
    Document doc = new Document();
    // Adicionar página à coleção de páginas do arquivo PDF
    Page page1 = doc.getPages().add();

    // Criar instância de TextFragment
    TextFragment tf = new TextFragment("Fragmento de Texto Exemplo");
    // Definir alinhamento horizontal para TextFragment
    tf.setHorizontalAlignment(HorizontalAlignment.Right);

    // Criar um textsegment com texto de exemplo
    TextSegment segment = new TextSegment(" ... Segmento de Texto 1...");
    // Adicionar segmento à coleção de segmentos do TextFragment
    tf.getSegments().add(segment);

    // Criar um novo TextSegment
    segment = new TextSegment("Link para o Google");
    // Adicionar segmento à coleção de segmentos do TextFragment

    tf.getSegments().add(segment);

    // Definir hiperlink para TextSegment
    segment.setHyperlink(new com.aspose.pdf.WebHyperlink("www.aspose.com"));

    // Definir cor de primeiro plano para o segmento de texto
    segment.getTextState().setForegroundColor(com.aspose.pdf.Color.getBlue());

    // Definir formatação de texto como itálico
    segment.getTextState().setFontStyle(FontStyles.Italic);

    // Criar outro objeto TextSegment
    segment = new TextSegment("TextSegment sem hiperlink");

    // Adicionar segmento à coleção de segmentos do TextFragment
    tf.getSegments().add(segment);

    // Adicionar TextFragment à coleção de parágrafos do objeto página
    page1.getParagraphs().add(tf);

    _dataDir = _dataDir + "AddHyperlinkToTextSegment_out.pdf";

    // Salvar documento PDF resultante.
    doc.save(_dataDir);

}
```


## Use OTF Font

Aspose.PDF for Java oferece a funcionalidade de usar fontes Customizadas/TrueType ao criar/manipular conteúdos de arquivo PDF para que os conteúdos do arquivo sejam exibidos usando fontes diferentes das fontes padrão do sistema. A partir do lançamento do Aspose.PDF para Java 10.4.0, oferecemos suporte para Fontes Open Type.

```java
public static void UseOTFFont() {
    // Criar nova instância de documento
    Document pdfDocument = new Document();
    // Adicionar página à coleção de páginas do arquivo PDF
    Page page = pdfDocument.getPages().add();
    // Criar instância de TextFragment com texto de exemplo
    TextFragment fragment = new TextFragment("Texto de exemplo na fonte OTF");
    // Ou você pode até especificar o caminho da fonte OTF no diretório do sistema
    fragment.getTextState().setFont(FontRepository.openFont("/home/aspose/.fonts/Montserrat-Black.otf"));
    // Especificar para incorporar a fonte dentro do arquivo PDF, para que seja exibida corretamente,
    // Mesmo que a fonte específica não esteja instalada/presente na máquina de destino
    fragment.getTextState().getFont().setEmbedded(true);
    // Adicionar TextFragment à coleção de parágrafos da instância de Page
    page.getParagraphs().add(fragment);
    // Salvar o documento PDF resultante.
    pdfDocument.save(_dataDir + "OTFFont_out.pdf");
}
```


## Adicionar String HTML usando DOM

A classe Aspose.Pdf.Generator.Text contém uma propriedade chamada IsHtmlTagSupported, que possibilita adicionar tags/conteúdos HTML em arquivos PDF. O conteúdo adicionado é renderizado em tags HTML nativas em vez de aparecer como uma simples string de texto. Para suportar um recurso semelhante no novo Modelo de Objeto de Documento (DOM) do namespace Aspose.Pdf, a classe HtmlFragment foi introduzida.

A instância [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlFragment) pode ser usada para especificar os conteúdos HTML que devem ser colocados dentro do arquivo PDF. Semelhante ao TextFragment, o HtmlFragment é um objeto de nível de parágrafo e pode ser adicionado à coleção de parágrafos do objeto Page. Os seguintes trechos de código mostram as etapas para colocar conteúdos HTML dentro de um arquivo PDF usando a abordagem DOM.

```java
public static void AddingHtmlString() {
    // Instanciar objeto Document
    Document doc = new Document();
    // Adicionar uma página à coleção de páginas do arquivo PDF
    Page page = doc.getPages().add();
    // Instanciar HtmlFragment com conteúdos HTML
    HtmlFragment title = new HtmlFragment("<h1 style=\"color:blue\"><strong>HTML String Demo</strong></h1>");
    // definir MarginInfo para detalhes de margem
    MarginInfo Margin = new MarginInfo();
    Margin.setBottom(10);
    Margin.setTop(200);
    // Definir informações de margem
    title.setMargin(Margin);
    // Adicionar Fragmento HTML à coleção de parágrafos da página
    page.getParagraphs().add(title);
    // Salvar arquivo PDF
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


O seguinte trecho de código demonstra as etapas de como adicionar listas ordenadas em HTML ao documento:

```java
public static void AddHTMLOrderedListIntoDocuments() {
    // Instanciar objeto Document
    Document doc = new Document();
    // Instanciar objeto HtmlFragment com o fragmento HTML correspondente
    HtmlFragment t = new HtmlFragment(
            "<div style=\"font-family: sans-serif\"><ul><li>Primeiro</li><li>Segundo</li><li>Terceiro</li><li>Quarto</li><li>Quinto</li></ul><p>Texto após a lista.</p><p>Próxima linha<br/>Última linha</p></div>");
    // Adicionar Página na Coleção de Páginas
    Page page = doc.getPages().add();
    // Adicionar HtmlFragment dentro da página
    page.getParagraphs().add(t);
    // Salvar arquivo PDF resultante
    doc.save(_dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf");
}
```

Você também pode definir a formatação da string HTML usando o objeto TextState da seguinte forma:

```java
public static void AddHTMLStringFormatting() {
    // Instanciar objeto Document
    Document doc = new Document();
    // Adicionar uma página à coleção de páginas do arquivo PDF
    Page page = doc.getPages().add();
    // Instanciar HtmlFragment com conteúdos HTML
    HtmlFragment title = new HtmlFragment("<h1><strong>Demo de String HTML</strong></h1>");
    TextState textState = new TextState(12);
    textState.setFont(FontRepository.findFont("Calibri"));
    textState.setForegroundColor(Color.getGreen());
    textState.setBackgroundColor(Color.getCoral());
    title.setTextState(textState);

    // Adicionar Fragmento HTML à coleção de parágrafos da página
    page.getParagraphs().add(title);
    // Salvar arquivo PDF
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


No caso de definir alguns valores de atributos de texto via marcação HTML e, em seguida, fornecer os mesmos valores nas propriedades de TextState, eles substituirão os parâmetros HTML pelas propriedades da instância TextState. Os trechos de código a seguir mostram o comportamento descrito.

```java
public static void AddHTMLUsingDOMAndOverwrite() {
    // Instanciar objeto Documento
    Document doc = new Document();
    // Adicionar uma página à coleção de páginas do arquivo PDF
    Page page = doc.getPages().add();
    // Instanciar HtmlFragment com conteúdos HTML
    HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>A tabela contém texto</i></b></p>");
    // A fonte 'Verdana' será redefinida para 'Arial'
    title.setTextState(new TextState("Arial Black"));
    title.setTextState(new TextState(20));
    // Definir informações de margem inferior
    title.getMargin().setBottom(10);
    // Definir informações de margem superior
    title.getMargin().setTop(400);
    // Adicionar fragmento HTML à coleção de parágrafos da página
    page.getParagraphs().add(title);
    // Salvar arquivo PDF
    doc.save(_dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf");
}
```


## FootNotes e EndNotes (DOM)

FootNotes indicam notas no texto do seu documento usando números sobrescritos consecutivos. A nota real é indentada e pode ocorrer como uma nota de rodapé na parte inferior da página.

### Adicionando FootNote

Em um sistema de referência por nota de rodapé, indique uma referência por:

- colocando um número pequeno acima da linha de texto diretamente após o material fonte. Este número é chamado de identificador de nota. Ele fica ligeiramente acima da linha de texto.
- colocando o mesmo número, seguido por uma citação da sua fonte, na parte inferior da página. As notas de rodapé devem ser numéricas e cronológicas: a primeira referência é 1, a segunda é 2, e assim por diante.

A vantagem das notas de rodapé é que o leitor pode simplesmente olhar para baixo na página para descobrir a fonte de uma referência que lhes interessa.

Por favor, siga os passos especificados abaixo para criar uma FootNote:

- Crie uma instância de Document
- Crie um objeto Page
- Crie um objeto TextFragment

- Crie uma instância de Note e passe seu valor para a propriedade TextFragment.FootNote
- Adicionar TextFragment à coleção de parágrafos de uma instância de página

### Estilo de linha personalizado para FootNote

O exemplo a seguir demonstra como adicionar notas de rodapé na parte inferior da página PDF e definir um estilo de linha personalizado.

```java
public static void AddFootNote() {
    // criar instância de Document
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("Demo");
    t.setFootNote(note);

    // criar instância de TextFragment
    TextFragment text = new TextFragment("Hello World");
    // definir valor de FootNote para TextFragment
    text.setFootNote(new Note("nota de rodapé para texto de teste 1"));
    // adicionar TextFragment à coleção de parágrafos da primeira página do documento
    page.getParagraphs().add(text);
    // criar segundo TextFragment
    text = new TextFragment("Aspose.Pdf for Java");
    // definir FootNote para o segundo fragmento de texto
    text.setFootNote(new Note("nota de rodapé para texto de teste 2"));
    // adicionar segundo fragmento de texto à coleção de parágrafos do arquivo PDF
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


Podemos definir a formatação do Rótulo de Nota de Rodapé (identificador da nota) usando o objeto TextState da seguinte forma:

```java
public static void AddCustomFootNoteLabel() {
    // criar instância do Documento
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("Demo");
    t.setFootNote(note);

    // criar instância de TextFragment
    TextFragment text = new TextFragment("Hello World");
    // definir valor da Nota de Rodapé para o TextFragment
    text.setFootNote(new Note("nota de rodapé para o texto de teste 1"));
    text.getFootNote().setText("21");
    TextState ts = new TextState();
    ts.setForegroundColor(Color.getBlue());
    ts.setFontStyle(FontStyles.Italic);
    text.getFootNote().setTextState(ts);

    // adicionar TextFragment à coleção de parágrafos da primeira página do documento
    page.getParagraphs().add(text);
    // criar segundo TextFragment
    text = new TextFragment("Aspose.Pdf for Java");
    // definir Nota de Rodapé para o segundo fragmento de texto
    text.setFootNote(new Note("nota de rodapé para o texto de teste 2"));
    // adicionar segundo fragmento de texto à coleção de parágrafos do arquivo PDF
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


### Personalizar rótulo de nota de rodapé

Por padrão, o número da Nota de Rodapé é incremental a partir de 1. No entanto, podemos ter um requisito para definir um rótulo de Nota de Rodapé personalizado. Para cumprir esse requisito, tente usar o seguinte trecho de código

```java
public static void CustomFootNote_Label() {
    // Criar instância do Documento
    Document document = new Document();
    // Adicionar página à coleção de páginas do PDF
    Page page = document.getPages().add();
    // Criar objeto GraphInfo
    GraphInfo graph = new GraphInfo();
    // Definir largura da linha como 2
    graph.setLineWidth(2);
    // Definir a cor para o objeto gráfico
    graph.setColor(Color.getRed());
    // Definir valor do array de traços como 3
    graph.setDashArray(new int[] { 3 });
    // Definir valor da fase de traço como 1
    graph.setDashPhase(1);
    // Definir estilo de linha de nota de rodapé para a página como gráfico
    page.setNoteLineStyle(graph);

    // Criar instância do TextFragment
    TextFragment text = new TextFragment("Hello World");
    // Definir valor da Nota de Rodapé para o TextFragment
    text.setFootNote(new Note("nota de rodapé para texto de teste 1"));
    // Especificar rótulo personalizado para a Nota de Rodapé
    text.getFootNote().setText(" Aspose(2021)");
    // Adicionar TextFragment à coleção de parágrafos da primeira página do documento
    page.getParagraphs().add(text);

    document.save(_dataDir + "CustomizeFootNoteLabel_out.pdf");
}
```


## Adicionando Imagem e Tabela à Nota de Rodapé

Nas versões anteriores, o suporte para Nota de Rodapé era fornecido, mas era aplicável apenas ao objeto TextFragment. No entanto, a partir da versão Aspose.PDF para Java 10.7.0, você também pode adicionar Nota de Rodapé a outros objetos dentro do documento PDF, como Tabela, Células etc. O trecho de código a seguir mostra as etapas para adicionar Nota de Rodapé ao objeto TextFragment e, em seguida, adicionar objeto Imagem e Tabela à coleção de parágrafos da seção de Nota de Rodapé.

```java
public static void AddingImageAndTableToFootnote() {
    // Criar instância do Documento
    Document document = new Document();
    // Adicionar página à coleção de páginas do PDF
    Page page = document.getPages().add();
    // Criar instância do TextFragment
    TextFragment text = new TextFragment("Hello World");

    page.getParagraphs().add(text);

    text.setFootNote(new Note());
    Image image = new Image();
    image.setFile(_dataDir + "aspose-logo.jpg");
    image.setFixHeight(20);
    text.getFootNote().getParagraphs().add(image);
    TextFragment footNote = new TextFragment("texto da nota de rodapé");
    footNote.getTextState().setFontSize(20);
    footNote.setInLineParagraph(true);
    text.getFootNote().getParagraphs().add(footNote);
    Table table = new Table();
    table.getRows().add().getCells().add().getParagraphs().add(new TextFragment("Linha 1 Célula 1"));
    text.getFootNote().getParagraphs().add(table);

    page.getParagraphs().add(text);

    document.save(_dataDir + "AddImageAndTable_out.pdf");
}
```


## Como Criar Notas de Fim

Uma Nota de Fim é uma citação de fonte que refere os leitores a um lugar específico no final do trabalho onde eles podem encontrar a fonte da informação ou palavras citadas ou mencionadas no trabalho. Ao usar notas de fim, sua frase citada ou parafraseada ou material resumido é seguido por um número sobrescrito.

O exemplo a seguir demonstra como adicionar uma Nota de Fim na página do PDF.

```java
public static void HowToCreateEndNotes() {
    Document doc = new Document();
    // adiciona página à coleção de páginas do PDF
    Page page = doc.getPages().add();
    // cria instância de TextFragment
    TextFragment text = new TextFragment("Hello World");
    // define valor de Nota de Fim para TextFragment
    text.setEndNote(new Note("nota de fim de exemplo"));
    // especifica rótulo personalizado para Nota de Fim
    text.getEndNote().setText(" Aspose(2021)");
    // adiciona TextFragment à coleção de parágrafos da primeira página do documento
    page.getParagraphs().add(text);
    // salva o arquivo PDF
    doc.save(_dataDir + "EndNote.pdf");
}
```


## Texto e Imagem como Parágrafo Inline

O layout padrão do arquivo PDF é o layout de fluxo (Topo-Esquerda para Baixo-Direita). Portanto, todo novo elemento adicionado ao arquivo PDF é adicionado no fluxo inferior direito. No entanto, podemos ter a necessidade de exibir vários elementos da página, ou seja, Imagem e Texto no mesmo nível (um após o outro). Uma abordagem pode ser criar uma instância de Tabela e adicionar ambos os elementos a objetos de célula individuais. No entanto, outra abordagem pode ser o parágrafo Inline. Ao definir a propriedade IsInLineParagraph da Imagem e do Texto como verdadeira, esses parágrafos aparecerão como inline para outros elementos da página.

O trecho de código a seguir mostra como adicionar texto e imagem como parágrafos Inline no arquivo PDF.

```java
 public static void TextAndImageAsInLineParagraph() {
    // Instanciar a instância do Documento
    Document doc = new Document();
    // Adicionar página à coleção de páginas da instância do Documento
    Page page = doc.getPages().add();
    // Criar TextFragment
    TextFragment text = new TextFragment("Olá Mundo.. ");
    // Adicionar fragmento de texto à coleção de parágrafos do objeto Page
    page.getParagraphs().add(text);
    // Criar uma instância de imagem
    Image image = new Image();
    // Definir imagem como parágrafo inline para que apareça logo após
    // O objeto de parágrafo anterior (TextFragment)
    image.setInLineParagraph (true);
    // Especificar caminho do arquivo de imagem
    image.setFile(_dataDir + "aspose-logo.jpg");
    // Definir altura da imagem (opcional)
    image.setFixHeight(30);
    // Definir largura da imagem (opcional)
    image.setFixWidth(100);
    // Adicionar imagem à coleção de parágrafos do objeto page
    page.getParagraphs().add(image);
    // Reinicializar o objeto TextFragment com conteúdos diferentes
    text = new TextFragment(" Olá Novamente..");
    // Definir TextFragment como parágrafo inline
    text.setInLineParagraph (true);
    // Adicionar o TextFragment recém-criado à coleção de parágrafos da página
    page.getParagraphs().add(text);
    
    doc.save(_dataDir+"TextAndImageAsParagraph_out.pdf");
}
```


## Especificar Espaçamento de Caracteres ao Adicionar Texto

Um texto pode ser adicionado dentro da coleção de parágrafos de arquivos PDF usando a instância TextFragment ou usando o objeto TextParagraph e até mesmo você pode estampar o texto dentro do PDF usando a classe TextStamp. Ao adicionar o texto, podemos ter um requisito de especificar o espaçamento de caracteres para os objetos de texto. Para cumprir este requisito, uma nova propriedade chamada propriedade CharacterSpacing foi introduzida. Por favor, dê uma olhada nas seguintes abordagens para cumprir este requisito.

As seguintes abordagens mostram os passos para especificar o espaçamento de caracteres ao adicionar texto dentro de um documento PDF.

## Usando TextBuilder e TextFragment

```java
 public static void CharacterSpacing_TextFragment(){
    // Criar instância de Document
    Document pdfDocument = new Document();
    // Adicionar página à coleção de páginas do Document
    Page page = pdfDocument.getPages().add();
    // Criar instância de TextBuilder
    TextBuilder builder = new TextBuilder(page);
    // Criar instância de fragmento de texto com conteúdo de exemplo
    TextFragment wideFragment = new TextFragment("Texto com espaçamento de caracteres aumentado");
    wideFragment.getTextState().applyChangesFrom(new TextState("Arial", 12));
    // Especificar espaçamento de caracteres para TextFragment
    wideFragment.getTextState().setCharacterSpacing(2.0f);
    // Especificar a posição do TextFragment
    wideFragment.setPosition(new Position(100, 650));
    // Anexar TextFragment à instância de TextBuilder
    builder.appendText(wideFragment);        
    // Salvar documento PDF resultante.
    pdfDocument.save(_dataDir+ "CharacterSpacingUsingTextBuilderAndFragment_out.pdf");
}
```


## Usando TextBuilder e TextParagraph

```java
public static void CharacterSpacing_TextParagraph() {
    // Criar instância do documento
    Document pdfDocument = new Document();
    // Adicionar página à coleção de páginas do documento
    Page page = pdfDocument.getPages().add();
    // Criar instância do TextBuilder
    TextBuilder builder = new TextBuilder(page);
    // Instanciar instância do TextParagraph
    TextParagraph paragraph = new TextParagraph();
    // Criar instância do TextState para especificar o nome e o tamanho da fonte
    TextState state = new TextState("Arial", 12);
    // Especificar o espaçamento entre caracteres
    state.setCharacterSpacing (1.5f);
    // Anexar texto ao objeto TextParagraph
    paragraph.appendLine("Este é um parágrafo com espaçamento entre caracteres", state);
    // Especificar a posição para o TextParagraph
    paragraph.setPosition (new Position(100, 550));
    // Anexar TextParagraph à instância do TextBuilder
    builder.appendParagraph(paragraph);
    // Salvar documento PDF resultante.
    pdfDocument.save(_dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf");
}
```


## Usando TextStamp

```java
public static void CharacterSpacing_TextStamp() {
    // Criar instância do Documento
    Document pdfDocument = new Document();
    // Adicionar página à coleção de páginas do Documento
    Page page = pdfDocument.getPages().add();
    // Instanciar instância de TextStamp com texto de exemplo
    TextStamp stamp = new TextStamp("Este é um carimbo de texto com espaçamento de caracteres");
    // Especificar o nome da fonte para o objeto Stamp
    stamp.getTextState().setFont(FontRepository.findFont("Arial"));
    // Especificar o tamanho da fonte para TextStamp
    stamp.getTextState().setFontSize(12);
    // Especificar o espaçamento de caracteres como 1f
    stamp.getTextState().setCharacterSpacing (1f);
    // Definir o XIndent para Stamp
    stamp.setXIndent(100);
    // Definir o YIndent para Stamp
    stamp.setYIndent(500);
    // Adicionar carimbo textual à instância da página
    stamp.put(page);        
    // Salvar o documento PDF resultante.
    pdfDocument.save(_dataDir+"CharacterSpacingUsingTextStamp_out.pdf");        
}
```

## Criar documento PDF com várias colunas

Em revistas e jornais, vemos principalmente que as notícias são exibidas em várias colunas em uma única página, ao contrário dos livros onde os parágrafos de texto são impressos na página inteira da posição esquerda para a direita.
 Muitos aplicativos de processamento de documentos, como Microsoft Word e Adobe Acrobat Writer, permitem que os usuários criem várias colunas em uma única página e, em seguida, adicionem dados a elas.

O Aspose.PDF para Java também oferece o recurso de criar várias colunas dentro das páginas de documentos PDF. Para criar um arquivo PDF com várias colunas, podemos usar a classe Aspose.Pdf.FloatingBox, pois ela fornece a propriedade ColumnInfo.ColumnCount para especificar o número de colunas dentro do FloatingBox e também podemos especificar o espaçamento entre colunas e as larguras das colunas usando as propriedades ColumnInfo.ColumnSpacing e ColumnInfo.ColumnWidths, respectivamente. Por favor, note que o FloatingBox é um elemento dentro do Modelo de Objeto de Documento e pode ter posicionamento obsoleto em comparação com o posicionamento relativo (i.e., Texto, Gráfico, Imagem, etc).
Espaçamento entre colunas significa o espaço entre as colunas e o espaçamento padrão entre as colunas é de 1,25 cm. Se a largura da coluna não for especificada, então o Aspose.PDF for Java calcula a largura de cada coluna automaticamente de acordo com o tamanho da página e o espaçamento entre as colunas.

Um exemplo é dado abaixo para demonstrar a criação de duas colunas com objetos Graphs (Linha) e eles são adicionados à coleção de parágrafos de FloatingBox, que é então adicionada à coleção de parágrafos da instância de Page.

```java
public static void CreateMultiColumn() {
    Document doc = new Document();
    // Especificar a informação de margem esquerda para o arquivo PDF
    doc.getPageInfo().getMargin().setLeft(40);
    
    // Especificar a informação de margem direita para o arquivo PDF
    doc.getPageInfo().getMargin().setRight(40);
    
    Page page = doc.getPages().add();

    com.aspose.pdf.drawing.Graph graph1 = new com.aspose.pdf.drawing.Graph(500, 2);
    
    // Adicionar a linha à coleção de parágrafos do objeto seção
    page.getParagraphs().add(graph1);

    // Especificar as coordenadas para a linha
    float[] posArr = new float[] { 1, 2, 500, 2 };
    com.aspose.pdf.drawing.Line l1 = new com.aspose.pdf.drawing.Line(posArr);
    graph1.getShapes().add(l1);
    
    // Criar variáveis de string com texto contendo tags html
    String s = "<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">"
                +"<strong> Como Evitar fraudes financeiras</<strong> </span>";
    
    // Criar parágrafos de texto contendo texto HTML

    HtmlFragment heading_text = new HtmlFragment(s);
    page.getParagraphs().add(heading_text);

    FloatingBox box = new FloatingBox();
    
    // Adicionar quatro colunas na seção
    box.getColumnInfo().setColumnCount(2);
    // Definir o espaçamento entre as colunas
    box.getColumnInfo().setColumnSpacing("5");

    box.getColumnInfo().setColumnWidths("105 105");
    TextFragment text1 = new TextFragment("Por Um Googler (O Blog Oficial do Google)");
    text1.getTextState().setFontSize (8);
    text1.getTextState().setLineSpacing (2);
    text1.getTextState().setFontSize (10);
    text1.getTextState().setFontStyle (FontStyles.Italic);

    box.getParagraphs().add(text1);
    
    // Criar um objeto gráficos para desenhar uma linha
    com.aspose.pdf.drawing.Graph graph2 = new com.aspose.pdf.drawing.Graph(50, 10);
    // Especificar as coordenadas para a linha
    float[] posArr2 = new float[] { 1, 10, 100, 10 };
    com.aspose.pdf.drawing.Line l2 = new com.aspose.pdf.drawing.Line(posArr2);
    graph2.getShapes().add(l2);

    // Adicionar a linha à coleção de parágrafos do objeto seção
    box.getParagraphs().add(graph2);

    TextFragment text2 = new TextFragment("Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. "
    +"Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue."
    +"Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur "
    +"ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean "
    +"posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. "
    +"Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, "
    +"risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam "
    +"luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, "
    +"sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, "
    +"pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,"
    +"iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus "
    +"mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla."
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,"
    +"iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique"
    +"ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
    +"Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. "
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box.getParagraphs().add(text2);

    page.getParagraphs().add(box);

    // Salvar arquivo PDF
    doc.save(_dataDir + "CreateMultiColumnPdf_out.pdf");        
}
```


## Trabalhando com Paradas de Tabulação Personalizadas

Uma Parada de Tabulação é um ponto de parada para tabulação. No processamento de texto, cada linha contém várias paradas de tabulação colocadas em intervalos regulares (por exemplo, a cada meia polegada). Elas podem ser alteradas, no entanto, já que a maioria dos processadores de texto permite que você defina paradas de tabulação onde quiser. Quando você pressiona a tecla Tab, o cursor ou ponto de inserção pula para a próxima parada de tabulação, que é invisível. Embora as paradas de tabulação não existam no arquivo de texto, o processador de texto as acompanha para que possa reagir corretamente à tecla Tab.

[Aspose.PDF para Java](https://docs.aspose.com/pdf/java/) permite que os desenvolvedores usem paradas de tabulação personalizadas em documentos PDF. A classe Aspose.Pdf.Text.TabStop é usada para definir paradas de TAB personalizadas na classe [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment).

[Aspose.PDF para Java](https://docs.aspose.com/pdf/java/) também oferece alguns tipos de líderes de tabulação predefinidos como uma enumeração chamada TabLeaderType cujos valores predefinidos e suas descrições são fornecidos abaixo:

|**Tipo de Líder de Tabulação**|**Descrição**|
| :- | :- |
|None|Sem líder de tabulação|
|Solid|Líder de tabulação sólido|
|Dash|Líder de tabulação tracejado|
|Dot|Líder de tabulação pontilhado|

Aqui está um exemplo de como definir paradas de TAB personalizadas.

```java
public static void CustomTabStops() {
    Document pdfdocument = new Document();
    Page page = pdfdocument.getPages().add();

    com.aspose.pdf.TabStops ts = new com.aspose.pdf.TabStops();
    com.aspose.pdf.TabStop ts1 = ts.add(100);
    ts1.setAlignmentType(TabAlignmentType.Right);
    ts1.setLeaderType (TabLeaderType.Solid);
    
    com.aspose.pdf.TabStop ts2 = ts.add(200);
    ts2.setAlignmentType(TabAlignmentType.Center);
    ts2.setLeaderType (TabLeaderType.Dash);

    com.aspose.pdf.TabStop ts3 = ts.add(300);
    ts3.setAlignmentType(TabAlignmentType.Left);
    ts3.setLeaderType (TabLeaderType.Dot);

    TextFragment header = new TextFragment("Este é um exemplo de formação de tabela com paradas de TAB", ts);
    TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data22 "));
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data23"));

    page.getParagraphs().add(header);
    page.getParagraphs().add(text0);
    page.getParagraphs().add(text1);
    page.getParagraphs().add(text2);
    
    pdfdocument.save(_dataDir + "CustomTabStops_out.pdf"); 
}
```


## Como Adicionar Texto Transparente em PDF

Um arquivo PDF contém objetos de Imagem, Texto, Gráfico, anexo, Anotações e, ao criar TextFragment, você pode definir informações de cor de primeiro plano, cor de fundo, bem como formatação de texto. O Aspose.PDF para Java suporta o recurso de adicionar texto com canal de cor Alpha. O snippet de código a seguir mostra como adicionar texto com cor transparente.

```java
  public static void AddTransparentText() {
    // Criar instância de Documento
    Document pdfdocument = new Document();
    // Criar página para a coleção de páginas do arquivo PDF
    Page page = pdfdocument.getPages().add();

    // Criar objeto Gráfico
    Graph canvas = new Graph(100, 400);
    // Criar instância de retângulo com certas dimensões
    com.aspose.pdf.drawing.Rectangle rect = new com.aspose.pdf.drawing.Rectangle(100, 100, 400, 400);
    // Criar objeto de cor a partir do canal de cor Alpha
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;
    Color alphaColor = Color.fromArgb(alpha, red, green, blue);
    rect.getGraphInfo().setFillColor(alphaColor);
    // Adicionar retângulo à coleção de formas do objeto Gráfico
    canvas.getShapes().add(rect);
    // Adicionar objeto gráfico à coleção de parágrafos do objeto página
    page.getParagraphs().add(canvas);
    // Definir valor para não alterar a posição do objeto gráfico
    canvas.setChangePosition(false);

    // Criar instância de TextFragment com valor de exemplo
    TextFragment text = new TextFragment(
            "texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente ");
    // Criar objeto de cor a partir do canal Alpha
    alpha = 30;
    alphaColor = Color.fromArgb(alpha, red, green, blue);
    // Definir informações de cor para a instância de texto
    text.getTextState().setForegroundColor (alphaColor);
    // Adicionar texto à coleção de parágrafos da instância de página
    page.getParagraphs().add(text);
    
    pdfdocument.save(_dataDir + "AddTransparentText_out.pdf");
}
```


## Especificar Espaçamento de Linha para Fontes

Cada fonte possui um quadrado abstrato, cuja altura é a distância pretendida entre linhas de texto no mesmo tamanho de tipo. Este quadrado é chamado de `quadrado em` e é a grade de design na qual os contornos dos glifos são definidos. Muitas letras da fonte de entrada têm pontos que estão posicionados fora dos limites do `quadrado em` da fonte, então, para exibir a fonte corretamente, é necessário o uso de uma configuração especial. O objeto TextFragment possui um conjunto de opções de formatação de texto que são acessíveis através do método [TextState.getFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#getFormattingOptions--).
Este método retorna a classe [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions).
 Esta classe tem uma enumeração [LineSpacingMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions.LineSpacingMode) que é projetada para fontes específicas, por exemplo, fonte de entrada "HPSimplified.ttf". Além disso, a classe [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions) tem um método [setLineSpacing](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions#setLineSpacing-int-) do tipo LineSpacingMode. Você só precisa definir LineSpacing em LineSpacingMode.FullSize. O trecho de código para exibir uma fonte corretamente seria como o seguinte:

```java
public static void SpecifyLineSpacingForFonts() {
    String fontFile = _dataDir + "hp-simplified.ttf";
    // Carregar arquivo PDF de entrada
    Document doc = new Document();
    // Criar TextFormattingOptions com LineSpacingMode.FullSize
    TextFormattingOptions formattingOptions = new TextFormattingOptions();
    formattingOptions.setLineSpacing(TextFormattingOptions.LineSpacingMode.FullSize);

    // Criar objeto text builder para a primeira página do documento
    // TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
    // Criar fragmento de texto com string de exemplo
    TextFragment textFragment = new TextFragment("Hello world");

    // Carregar a fonte TrueType no objeto stream
    FileInputStream fontStream;
    try {
        fontStream = new FileInputStream(fontFile);
    } catch (FileNotFoundException e) {
        e.printStackTrace();
        return;
    }

    // Definir o nome da fonte para a string de texto
    textFragment.getTextState().setFont(FontRepository.openFont(fontStream, FontTypes.TTF));
    // Especificar a posição para o Fragmento de Texto
    textFragment.setPosition(new Position(100, 600));
    // Definir TextFormattingOptions do fragmento atual para predefinido (que aponta para
    // LineSpacingMode.FullSize)
    textFragment.getTextState().setFormattingOptions(formattingOptions);
    // Adicionar o texto ao TextBuilder para que ele possa ser colocado sobre o arquivo PDF
    // textBuilder.AppendText(textFragment);
    Page page = doc.getPages().add();
    page.getParagraphs().add(textFragment);

    // Salvar documento PDF resultante
    doc.save(_dataDir + "SpecifyLineSpacing_out.pdf");
}
```

## Obter Largura do Texto Dinamicamente

Às vezes, é necessário obter a largura do texto dinamicamente. Aspose.PDF para Java inclui dois métodos para medição da largura de string. Você pode invocar o método [MeasureString](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState#measureString--) das classes com.aspose.pdf.Font ou com.aspose.pdf.TextState (ou ambas). O trecho de código abaixo mostra como usar essa funcionalidade.

```java
public static void GetTextWidthDynamicaly() {
    Font font = FontRepository.findFont("Arial");
    TextState ts = new TextState();
        ts.setFont(font);
        ts.setFontSize(14);
        if (Math.abs(font.measureString("A", 14) - 9.337) > 0.001)
            System.out.println("Medida inesperada da string da fonte!");

        if (Math.abs(ts.measureString("z") - 7.0) > 0.001)
        System.out.println("Medida inesperada da string da fonte!");

        for (char c = 'A'; c <= 'z'; c++)
        {
            double fnMeasure = font.measureString(String.valueOf(c), 14);
            double tsMeasure = ts.measureString(String.valueOf(c));

            if (Math.abs(fnMeasure - tsMeasure) > 0.001)
                System.out.println("A medição da string da fonte e do estado não corresponde!");
        }
}
```