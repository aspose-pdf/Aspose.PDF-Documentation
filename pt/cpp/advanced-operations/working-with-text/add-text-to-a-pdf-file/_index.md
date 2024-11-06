---
title: Adicionar Texto ao PDF usando C++
linktitle: Adicionar Texto ao PDF
type: docs
weight: 10
url: pt/cpp/adicionar-texto-ao-arquivo-pdf/
description: Este artigo descreve vários aspectos do trabalho com texto no Aspose.PDF. Aprenda como adicionar texto ao PDF, adicionar fragmentos HTML ou usar fontes OTF personalizadas.
lastmod: "2021-12-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionando Texto

Para adicionar texto a um arquivo PDF existente:

1. Abra o PDF de entrada usando o objeto Document.
2. Obtenha a página específica à qual você deseja adicionar o texto.
3. Crie um objeto TextFragment com o texto de entrada junto com outras propriedades de texto. O objeto TextBuilder criado a partir dessa página específica – à qual você deseja adicionar o texto – permite que você adicione o objeto TextFragment à página usando o método AppendText.
4. Chame o método Save do objeto Document e salve o arquivo PDF de saída.

O seguinte trecho de código mostra como adicionar texto em um arquivo PDF existente.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddingText() {
    
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de entrada
    String inputFileName("sample.pdf");
    // String para o nome do arquivo de saída
    String outputFileName("AddingText_out.pdf");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // obter página específica
    auto pdfPage = document->get_Pages()->idx_get(1);

    // criar fragmento de texto
    auto textFragment = MakeObject<TextFragment>("Aspose.PDF");
    textFragment->set_Position(MakeObject<Position>(80, 700));

    // definir propriedades do texto
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());

    // criar objeto TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(pdfPage);
    // anexar o fragmento de texto à página PDF
    textBuilder->AppendText(textFragment);

    // Salvar documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

## Carregando Fonte a partir de Stream

O trecho de código a seguir mostra como carregar Fonte a partir de um objeto Stream ao adicionar texto a um documento PDF.

```cpp
void LoadingFontFromStream() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("sample.pdf");
    String outputFileName("LoadingFontFromStream_out.pdf");

    String fontFile("C:\\Windows\\Fonts\\Arial.ttf");

    // Carregar arquivo PDF de entrada
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Criar objeto construtor de texto para a primeira página do documento
    auto textBuilder = MakeObject<TextBuilder>(document->get_Pages()->idx_get(1));
    // Criar fragmento de texto com string de exemplo
    auto textFragment = MakeObject<TextFragment>("Hello world");

    if (!fontFile.IsNullOrEmpty()) {
        // Carregar a fonte TrueType no objeto stream
        auto fontStream = System::IO::File::OpenRead(fontFile);
        // Definir o nome da fonte para a string de texto
        textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
        // Especificar a posição para o Fragmento de Texto
        textFragment->set_Position(MakeObject<Position>(10, 10));
        // Adicionar o texto ao TextBuilder para que ele possa ser colocado sobre o arquivo PDF
        textBuilder->AppendText(textFragment);

        // Salvar documento PDF resultante.
        document->Save(_dataDir + outputFileName);
    }
}
```

## Adicionar Texto usando TextParagraph

O trecho de código a seguir mostra como adicionar texto em um documento PDF usando a classe [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph).

```cpp
void AddTextUsingTextParagraph() {

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto document = MakeObject<Document>();

    String outputFileName("AddTextUsingTextParagraph_out.pdf");

    // Adicionar página à coleção de páginas do objeto Document
    auto page = document->get_Pages()->Add();
    auto builder = MakeObject<TextBuilder>(page);

    // Criar parágrafo de texto
    auto paragraph = MakeObject<TextParagraph>();

    // Definir indentação das linhas subsequentes
    paragraph->set_SubsequentLinesIndent(20);

    // Especificar o local para adicionar TextParagraph
    paragraph->set_Rectangle(MakeObject<Rectangle>(100, 300, 200, 700));

    // Especificar modo de quebra de linha
    paragraph->get_FormattingOptions()->set_WrapMode(TextFormattingOptions::WordWrapMode::ByWords);

    // Criar fragmento de texto
    auto fragment1 = MakeObject<TextFragment>("the quick brown fox jumps over the lazy dog");
    fragment1->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    fragment1->get_TextState()->set_FontSize(12);
    // Adicionar fragmento ao parágrafo
    paragraph->AppendLine(fragment1);
    // Adicionar parágrafo
    builder->AppendParagraph(paragraph);

    // Salvar documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}

```

## Adicionar Hiperlink ao TextSegment

Uma página PDF pode ser composta por um ou mais objetos TextFragment, onde cada objeto TextFragment pode ter uma ou mais instâncias de TextSegment. Para definir um hiperlink para o TextSegment, a propriedade Hyperlink da classe [TextSegment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_segment) pode ser utilizada enquanto fornece o objeto da instância Aspose.Pdf.WebHyperlink. Por favor, tente usar o seguinte trecho de código para realizar este requisito.

```cpp
void AddHyperlinkToTextSegment() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("AddHyperlinkToTextSegment_out.pdf");

    // Criar instância do documento
    auto document = MakeObject<Document>();

    // Adicionar página à coleção de páginas do arquivo PDF
    auto page1 = document->get_Pages()->Add();

    // Criar instância de TextFragment
    auto tf = MakeObject<TextFragment>("Fragmento de Texto de Exemplo");
    // Definir alinhamento horizontal para TextFragment
    tf->set_HorizontalAlignment(HorizontalAlignment::Right);

    // Criar um textsegment com texto de exemplo
    auto segment = MakeObject<TextSegment>(" ... Segmento de Texto 1...");
    // Adicionar segmento à coleção de segmentos do TextFragment
    tf->get_Segments()->Add(segment);

    // Criar um novo TextSegment
    segment = MakeObject<TextSegment>("Link para Google");
    // Adicionar segmento à coleção de segmentos do TextFragment

    tf->get_Segments()->Add(segment);

    // Definir hiperlink para TextSegment
    segment->set_Hyperlink(MakeObject<Aspose::Pdf::WebHyperlink>("www.aspose.com"));

    // Definir cor de primeiro plano para o segmento de texto
    segment->get_TextState()->set_ForegroundColor(Color::get_Blue());

    // Definir formatação de texto como itálico
    segment->get_TextState()->set_FontStyle(FontStyles::Italic);

    // Criar outro objeto TextSegment
    segment = MakeObject<TextSegment>(u"TextSegment sem hiperlink");

    // Adicionar segmento à coleção de segmentos do TextFragment
    tf->get_Segments()->Add(segment);

    // Adicionar TextFragment à coleção de parágrafos do objeto página
    page1->get_Paragraphs()->Add(tf);

    // Salvar documento PDF resultante.
    document->Save(_dataDir + outputFileName);

}
```

## Use OTF Font

Aspose.PDF for С++ oferece o recurso de usar fontes Custom/TrueType ao criar/manipular conteúdos de arquivos PDF para que os conteúdos do arquivo sejam exibidos usando fontes diferentes das fontes padrão do sistema.

```cpp
void UseOTFFont() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("OTFFont_out.pdf");

    // Criar nova instância de documento
    auto document = MakeObject<Document>();

    // Adicionar página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->Add();

    // Criar instância de TextFragment com texto de exemplo
    auto fragment = MakeObject<TextFragment>("Texto de exemplo em fonte OTF");

    // Ou você pode até especificar o caminho da fonte OTF no diretório do sistema
    fragment->get_TextState()->set_Font(FontRepository::OpenFont(u"C:\\Samples\\Fonts\\Montserrat-Black.otf"));
    // Especificar para incorporar a fonte dentro do arquivo PDF, para que seja exibida corretamente,
    // Mesmo que a fonte específica não esteja instalada/presente na máquina de destino
    fragment->get_TextState()->get_Font()->set_IsEmbedded(true);
    // Adicionar TextFragment à coleção de parágrafos da instância Page
    page->get_Paragraphs()->Add(fragment);
    // Salvar documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

## Adicionar String HTML usando DOM

A classe Aspose.Pdf.Generator.Text contém uma propriedade chamada IsHtmlTagSupported, que possibilita adicionar tags/conteúdos HTML em arquivos PDF. O conteúdo adicionado é renderizado em tags HTML nativas, em vez de aparecer como uma simples string de texto. Para suportar um recurso semelhante no novo Modelo de Objeto de Documento (DOM) do namespace Aspose.Pdf, a classe HtmlFragment foi introduzida.

A instância [HtmlFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_fragment) pode ser usada para especificar os conteúdos HTML que devem ser colocados dentro do arquivo PDF. Semelhante ao TextFragment, o HtmlFragment é um objeto de nível de parágrafo e pode ser adicionado à coleção de parágrafos do objeto Página. Os seguintes trechos de código mostram os passos para colocar conteúdos HTML dentro de um arquivo PDF usando a abordagem DOM.

```cpp
void AddingHtmlString() {
    
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de entrada
    String inputFileName("sample.pdf");

    // String para o nome do arquivo de saída
    String outputFileName("sample_html_out.pdf");

    // criar instância do Documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Adicionar uma página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->Add();

    // Instanciar HtmlFragment com conteúdos HTML
    auto title = MakeObject<HtmlFragment>("<h1 style=\"color:blue\"><strong>HTML String Demo</strong></h1>");

    // definir MarginInfo para detalhes de margem
    auto margin = MakeObject<MarginInfo>();
    margin->set_Bottom(10);
    margin->set_Top(200);
    // Definir informações de margem
    title->set_Margin(margin);

    // Adicionar Fragmento HTML à coleção de parágrafos da página
    page->get_Paragraphs()->Add(title);
    // Salvar arquivo PDF
    document->Save(_dataDir + outputFileName);
}
```

O seguinte trecho de código demonstra as etapas de como adicionar listas ordenadas em HTML ao documento:

```cpp
void AddHTMLOrderedListIntoDocuments() {
    
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de saída
    String outputFileName("AddHTMLOrderedListIntoDocuments_out.pdf");

    // Instanciar objeto Document    
    auto document = MakeObject<Document>();

    // Instanciar objeto HtmlFragment com o fragmento HTML correspondente
    auto htmlFragment = MakeObject<HtmlFragment>(
        "<div style=\"font-family: sans-serif\"><ul><li>Primeiro</li><li>Segundo</li><li>Terceiro</li><li>Quarto</li><li>Quinto</li></ul><p>Texto após a lista.</p><p>Próxima linha<br/>Última linha</p></div>");
    // Adicionar Página na Coleção de Páginas
    auto page = document->get_Pages()->Add();

    // Adicionar HtmlFragment dentro da página
    page->get_Paragraphs()->Add(htmlFragment);

    // Salvar arquivo PDF resultante
    document->Save(_dataDir + outputFileName);
}
```

Você também pode definir a formatação de string HTML usando o objeto TextState da seguinte forma:

```cpp
void AddHTMLStringFormatting() {
    
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de saída
    String outputFileName("sample_html_out.pdf");

    // Instanciar objeto Document    
    auto document = MakeObject<Document>();

    // Adicionar Página na Coleção de Páginas
    auto page = document->get_Pages()->Add();

    // Instanciar HtmlFragment com conteúdos HTML
    auto title = MakeObject<HtmlFragment>("<h1><strong>Demonstração de String HTML</strong></h1>");

    auto textState = MakeObject<TextState>(12);

    textState->set_Font(FontRepository::FindFont(u"Calibri"));
    textState->set_ForegroundColor(Color::get_Green());
    textState->set_BackgroundColor(Color::get_Coral());
    title->set_TextState(textState);

    // Adicionar Fragmento HTML à coleção de parágrafos da página
    page->get_Paragraphs()->Add(title);
    // Salvar arquivo PDF
    document->Save(_dataDir + outputFileName);
}
```

Caso você defina alguns valores de atributos de texto via marcação HTML e, em seguida, forneça os mesmos valores nas propriedades do TextState, eles substituirão os parâmetros HTML pelos valores das propriedades da instância do TextState. Os seguintes trechos de código mostram o comportamento descrito.

```cpp
void AddHTMLUsingDOMAndOverwrite() {

    String _dataDir("C:\\Samples\\");
    // String para o nome do arquivo de saída
    String outputFileName("AddHTMLUsingDOMAndOverwrite_out.pdf");

    // Instanciar objeto Document    
    auto document = MakeObject<Document>();

    // Adicionar página na coleção de páginas
    auto page = document->get_Pages()->Add();

    // Instanciar HtmlFragment com conteúdos HTML
    auto title = MakeObject<HtmlFragment>("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");

    // A família de fontes de 'Verdana' será redefinida para 'Arial'
    title->set_TextState(new TextState(u"Arial Black"));
    title->set_TextState(new TextState(20));

    // Definir informações de margem inferior
    title->get_Margin()->set_Bottom(10);
    // Definir informações de margem superior
    title->get_Margin()->set_Top(400);
    // Adicionar Fragmento HTML à coleção de parágrafos da página
    page->get_Paragraphs()->Add(title);
    // Salvar arquivo PDF
    document->Save(_dataDir + outputFileName);
}
```

## FootNotes e EndNotes (DOM)

FootNotes indicam notas no texto do seu documento utilizando números sobrescritos consecutivos. A nota propriamente dita é indentada e pode aparecer como uma nota de rodapé na parte inferior da página.

### Adicionando FootNote

Em um sistema de referência por nota de rodapé, indique uma referência por:

- colocando um pequeno número acima da linha do tipo diretamente após o material de origem. Este número é chamado de identificador de nota. Ele se posiciona ligeiramente acima da linha de texto.
- colocando o mesmo número, seguido por uma citação da sua fonte, na parte inferior da página. As notas de rodapé devem ser numéricas e cronológicas: a primeira referência é 1, a segunda é 2, e assim por diante.

A vantagem de usar notas de rodapé é que o leitor pode simplesmente olhar para baixo na página para descobrir a fonte de uma referência que lhes interessa.

Siga os próximos passos:

- Crie uma instância de [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
- Crie um objeto [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)

- Crie um objeto [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment)
- Crie uma instância de Note e passe seu valor para a propriedade TextFragment [FootNote](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#abe1663009fbceed84a0a392527463219)
- Adicione TextFragment à coleção de parágrafos de uma instância de página

```cpp
void AddFootNote() {
    
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de saída
    String inputFileName("sample.pdf");
    String outputFileName("sample_footnote_out.pdf");

    // Instanciar objeto Document    
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Adicionar Página na Coleção de Páginas
    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>();
    note->set_Text(u"Demo");
    t->set_FootNote(note);

    // criar instância de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // definir valor de FootNote para TextFragment
    text->set_FootNote(MakeObject<Note>("nota de rodapé para texto de teste 1"));
    // adicionar TextFragment à coleção de parágrafos da primeira página do documento
    page->get_Paragraphs()->Add(text);
    // criar segundo TextFragment
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // definir FootNote para o segundo fragmento de texto
    text->set_FootNote(MakeObject<Note>("nota de rodapé para texto de teste 2"));
    // adicionar segundo fragmento de texto à coleção de parágrafos do arquivo PDF
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### Estilo de linha personalizado para nota de rodapé

O exemplo a seguir demonstra como adicionar notas de rodapé ao final da página do Pdf e definir um estilo de linha personalizado.

```cpp
void CustomFootNote_Line() {
    
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de saída    
    String outputFileName("customFootNote_Line.pdf");

    // Criar instância do documento
    auto document = MakeObject<Document>();

    // adicionar página à coleção de páginas do PDF
    auto page = document->get_Pages()->Add();
    
    // criar objeto GraphInfo
    auto graph = MakeObject<GraphInfo>();
    // definir largura da linha como 2
    graph->set_LineWidth(2);
    // definir a cor para o objeto gráfico
    graph->set_Color(Color::get_Red());
    // definir valor do array de traços como 3
    graph->set_DashArray(MakeArray<int>(3));
    // definir valor da fase de traços como 1
    graph->set_DashPhase(1);
    // definir estilo de linha de nota de rodapé para a página como gráfico
    page->set_NoteLineStyle(graph);

    // criar instância TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // definir valor da nota de rodapé para TextFragment
    text->set_FootNote(MakeObject<Note>("nota de rodapé para o texto de teste 1"));
    // adicionar TextFragment à coleção de parágrafos da primeira página do documento
    page->get_Paragraphs()->Add(text);
    // criar segundo TextFragment
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // definir nota de rodapé para o segundo fragmento de texto
    text->set_FootNote(MakeObject<Note>("nota de rodapé para o texto de teste 2"));
    // adicionar segundo fragmento de texto à coleção de parágrafos do arquivo PDF
    page->get_Paragraphs()->Add(text);
    // salvar o arquivo PDF
    document->Save(_dataDir + outputFileName);
}
```

Podemos definir o formato do Rótulo de Nota de Rodapé (identificador de nota) usando o objeto TextState da seguinte forma:

```csharp
void AddCustomFootNoteLabel() {
    
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada    
    String inputFileName("sample.pdf");

    // String para nome do arquivo de saída    
    String outputFileName("sample_footnote.pdf");

    // Criar instância do Documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>("Demo");
    t->set_FootNote(note);

    // criar instância de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // definir valor de Nota de Rodapé para TextFragment
    text->set_FootNote(MakeObject<Note>("nota de rodapé para texto de teste 1"));
    text->get_FootNote()->set_Text(u"21");

    auto ts = MakeObject<TextState>();
    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_FontStyle(FontStyles::Italic);
    text->get_FootNote()->set_TextState(ts);

    // adicionar TextFragment à coleção de parágrafos da primeira página do documento
    page->get_Paragraphs()->Add(text);
    // criar segundo TextFragment
    text = MakeObject<TextFragment>(u"Aspose.Pdf for C++");
    // definir Nota de Rodapé para o segundo fragmento de texto
    text->set_FootNote(MakeObject<Note>("nota de rodapé para texto de teste 2"));
    // adicionar segundo fragmento de texto à coleção de parágrafos do arquivo PDF
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### Personalizar etiqueta de nota de rodapé

Por padrão, o número da nota de rodapé é incremental começando do 1. No entanto, podemos ter um requisito para definir uma etiqueta de nota de rodapé personalizada. Para atender a esse requisito, por favor, tente usar o seguinte trecho de código

```cpp
void CustomFootNote_Label() {

    String _dataDir("C:\\Samples\\");
    // String para nome do arquivo de saída    
    String outputFileName("CustomizeFootNoteLabel_out.pdf");

    // Criar instância de Documento
    auto document = MakeObject<Document>();

    // Adicionar página à coleção de páginas do PDF
    auto page = document->get_Pages()->Add();

    // Criar objeto GraphInfo
    auto graph = MakeObject<GraphInfo>();

    // Definir largura da linha como 2
    graph->set_LineWidth(2);

    // Definir a cor para o objeto gráfico
    graph->set_Color(Color::get_Red());

    // Definir valor do array de traços como 3
    graph->set_DashArray(MakeArray<int>(3));

    // Definir valor da fase de traço como 1
    graph->set_DashPhase(1);

    // Definir estilo da linha de nota de rodapé para a página como gráfico
    page->set_NoteLineStyle(graph);

    // Criar instância de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // Definir valor da nota de rodapé para o TextFragment
    text->set_FootNote(MakeObject<Note>("nota de rodapé para texto de teste 1"));
    // Especificar etiqueta personalizada para a nota de rodapé
    text->get_FootNote()->set_Text(u" Aspose(2021)");
    // Adicionar TextFragment à coleção de parágrafos da primeira página do documento
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Adicionando Imagem e Tabela à Nota de Rodapé

O trecho de código a seguir mostra as etapas para adicionar [Nota de Rodapé](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#a017ff999979d9f799b8e3cd32ab95722) ao objeto [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) e, em seguida, adicionar o objeto Imagem e Tabela à coleção de parágrafos da seção Nota de Rodapé.

```cpp

void AddingImageAndTableToFootnote() {
    
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de saída    
    String outputFileName("AddImageAndTableToFootNote_out.pdf");

    // Criar instância de Documento
    auto document = new Document();
    // Adicionar página à coleção de páginas do PDF
    auto page = document->get_Pages()->Add();

    // Criar instância de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");

    page->get_Paragraphs()->Add(text);

    text->set_FootNote(MakeObject<Note>());
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.jpg");
    image->set_FixHeight(20);

    text->get_FootNote()->get_Paragraphs()->Add(image);

    auto footNote = MakeObject<TextFragment>("texto da nota de rodapé");
    footNote->get_TextState()->set_FontSize(20);
    footNote->set_IsInLineParagraph(true);
    text->get_FootNote()->get_Paragraphs()->Add(footNote);
    
    auto table = MakeObject<Table>();
    table->get_Rows()->Add()->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Linha 1 Célula 1"));
    text->get_FootNote()->get_Paragraphs()->Add(table);

    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Como Criar Notas de Fim

Uma Nota de Fim é uma citação de fonte que refere os leitores a um local específico no final do documento onde eles podem encontrar a fonte da informação ou das palavras citadas ou mencionadas no documento. Ao usar notas de fim, sua frase citada ou parafraseada ou o material resumido é seguido por um número sobrescrito.

O exemplo a seguir demonstra como adicionar uma Nota de Fim na página do Pdf.

```cpp
void HowToCreateEndNotes() {
    
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de saída    
    String outputFileName("endNote_out.pdf");

    // Criar instância do Documento
    auto document = new Document();
    // Adicionar página à coleção de páginas do PDF
    auto page = document->get_Pages()->Add();

    // criar instância de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");

    // definir valor de FootNote para TextFragment
    text->set_EndNote(MakeObject<Note>("exemplo de Nota de Fim"));

    // especificar rótulo personalizado para FootNote
    text->get_EndNote()->set_Text(u" Aspose(2021)");
    // adicionar TextFragment à coleção de parágrafos da primeira página do documento
    page->get_Paragraphs()->Add(text);
    // salvar o arquivo PDF
    document->Save(_dataDir + outputFileName);
}
```

## Texto e Imagem como Parágrafo InLine

O layout padrão do arquivo PDF é o layout de fluxo (de cima para baixo, da esquerda para a direita). Portanto, todo novo elemento adicionado ao arquivo PDF é adicionado no fluxo inferior direito. No entanto, podemos ter um requisito para exibir vários elementos de página, ou seja, Imagem e Texto no mesmo nível (um após o outro). Uma abordagem pode ser criar uma instância de Tabela e adicionar ambos os elementos a objetos de célula individuais. No entanto, outra abordagem pode ser o parágrafo InLine. Ao definir a propriedade IsInLineParagraph da Imagem e do Texto como verdadeira, esses parágrafos aparecerão como inline para outros elementos da página.

O trecho de código a seguir mostra como adicionar texto e Imagem como parágrafos InLine no arquivo PDF.

```cpp
void TextAndImageAsInLineParagraph() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("TextAndImageAsParagraph_out.pdf");

    // Instanciar instância de Documento
    auto document = MakeObject<Document>();

    // Adicionar página à coleção de páginas da instância do Documento
    auto page = document->get_Pages()->Add();

    // Criar TextFragment
    auto text = MakeObject<TextFragment>("Hello World.. ");
    // Adicionar fragmento de texto à coleção de parágrafos do objeto Page
    page->get_Paragraphs()->Add(text);

    // Criar uma instância de imagem
    auto image = MakeObject<Image>();

    // Definir imagem como parágrafo inline para que apareça logo após
    // O objeto de parágrafo anterior (TextFragment)
    image->set_IsInLineParagraph(true);

    // Especificar caminho do arquivo de imagem
    image->set_File(_dataDir + u"aspose-logo.jpg");
    // Definir altura da imagem (opcional)
    image->set_FixHeight(30);
    // Definir largura da imagem (opcional)
    image->set_FixWidth(100);
    // Adicionar imagem à coleção de parágrafos do objeto de página
    page->get_Paragraphs()->Add(image);
    // Re-inicializar objeto TextFragment com conteúdos diferentes
    text = MakeObject<TextFragment>(" Hello Again..");
    // Definir TextFragment como parágrafo inline
    text->set_IsInLineParagraph(true);
    // Adicionar o novo TextFragment criado à coleção de parágrafos da página
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Especificar espaçamento de caracteres ao adicionar texto

O texto pode ser adicionado à coleção de parágrafos de um PDF usando uma instância de TextFragment ou um objeto TextParagraph, e você pode até carimbar texto dentro de um PDF usando a classe TextStamp. Ao adicionar texto, pode ser necessário especificar o espaçamento entre os caracteres para objetos de texto. Para atender a esse requisito, uma nova propriedade foi introduzida com o nome de Property CharacterSpacing.

Considere os seguintes métodos para atender a esse requisito.

Os métodos a seguir mostram as etapas para especificar o espaçamento de caracteres ao adicionar texto dentro de um documento PDF.

### Usando TextBuilder e TextFragment

```cpp
// Especificar espaçamento de caracteres ao adicionar texto usando TextBuilder e TextFragment
void CharacterSpacing_TextFragment() {
    
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de saída    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Criar instância de Document
    auto document = MakeObject<Document>();
    // Adicionar página à coleção de páginas do Document
    auto page = document->get_Pages()->Add();

    // Criar instância de TextBuilder
    auto builder = MakeObject<TextBuilder>(page);

    // Criar instância de fragmento de texto com conteúdo de exemplo
    auto wideFragment = MakeObject<TextFragment>("Texto com espaçamento de caracteres aumentado");
    wideFragment->get_TextState()->ApplyChangesFrom(MakeObject<TextState>("Arial", 12));

    // Especificar espaçamento de caracteres para TextFragment
    wideFragment->get_TextState()->set_CharacterSpacing(2.0f);

    // Especificar a posição do TextFragment
    wideFragment->set_Position(MakeObject<Position>(100, 650));

    // Anexar TextFragment à instância de TextBuilder
    builder->AppendText(wideFragment);

    // Salvar documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

### Usando TextParagraph

```cpp
void CharacterSpacing_TextParagraph() {
    
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de saída
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Criar uma instância de Document
    auto document = MakeObject<Document>();

    // Adicionar página à coleção de páginas do Document
    auto page = document->get_Pages()->Add();

    // Criar uma instância de TextBuilder
    auto builder = MakeObject<TextBuilder>(page);

    // Instanciar uma instância de TextParagraph
    auto paragraph = MakeObject<TextParagraph>();

    // Criar uma instância de TextState para especificar o nome e tamanho da fonte
    auto state = MakeObject<TextState>("Arial", 12);

    // Especificar o espaçamento entre caracteres
    state->set_CharacterSpacing(1.5f);

    // Anexar texto ao objeto TextParagraph
    paragraph->AppendLine(u"Este é um parágrafo com espaçamento entre caracteres", state);

    // Especificar a posição para TextParagraph
    paragraph->set_Position(MakeObject<Position>(100, 550));

    // Anexar TextParagraph à instância de TextBuilder
    builder->AppendParagraph(paragraph);

    // Salvar o documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

### Usando TextStamp

```cpp
void CharacterSpacing_TextStamp() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("CharacterSpacingUsingTextStamp_out.pdf");
    // Criar uma instância de Document
    auto document = MakeObject<Document>();

    // Adicionar página à coleção de páginas do Documento    
    auto page = document->get_Pages()->Add();

    // Instanciar uma instância de TextStamp com texto de exemplo
    auto stamp = MakeObject<TextStamp>("Este é um carimbo de texto com espaçamento entre caracteres");

    // Especificar o nome da fonte para o objeto Stamp
    stamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    // Especificar o tamanho da fonte para TextStamp
    stamp->get_TextState()->set_FontSize(12);
    // Especificar espaçamento de caracteres como 1f
    stamp->get_TextState()->set_CharacterSpacing(1.0f);
    // Definir o XIndent para Stamp
    stamp->set_XIndent(100);
    // Definir o YIndent para Stamp
    stamp->set_YIndent(500);
    // Adicionar carimbo textual à instância da página
    stamp->Put(page);
    // Salvar o documento PDF resultante.
    document->Save(_dataDir + outputFileName);
}
```

## Criar documento PDF de Múltiplas Colunas

Este tópico mostra como você pode criar um PDF de múltiplas colunas usando Aspose.Pdf para C++.

Hoje em dia, vemos frequentemente notícias exibidas em várias colunas em páginas separadas, ao invés de em livros, onde parágrafos de texto são principalmente impressos em todas as páginas da esquerda para a direita. Muitas aplicações de processamento de documentos, como Microsoft Word e Adobe Acrobat Writer, permitem que os usuários criem várias colunas em uma única página e depois adicionem dados a elas.

Aspose.Pdf para C++ também oferece a capacidade de criar várias colunas nas páginas de documentos PDF. Para criar um PDF com várias colunas, podemos usar a classe [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box), pois ela fornece uma propriedade ColumnInfo.ColumnCount para especificar o número de colunas dentro do FloatingBox, e também podemos especificar o espaçamento das colunas e as larguras das colunas usando ColumnInfo .ColumnSpacing e ColumnInfo .ColumnWidths, respectivamente.

Um exemplo é dado abaixo para demonstrar a criação de duas colunas com objetos Graphs (Line) e eles são adicionados à coleção de parágrafos do FloatingBox, que é então adicionada à coleção de parágrafos da instância Page.

```cpp
void CreateMultiColumn() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("CreateMultiColumnPdf_out.pdf");

    // Criar nova instância de documento
    auto document = MakeObject<Document>();

    // Especificar as informações da margem esquerda para o arquivo PDF
    document->get_PageInfo()->get_Margin()->set_Left(40);

    // Especificar as informações da margem direita para o arquivo PDF
    document->get_PageInfo()->get_Margin()->set_Right(40);

    // Adicionar página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->Add();

    auto graph1 = MakeObject<Aspose::Pdf::Drawing::Graph>(500, 2);

    // Adicionar a linha à coleção de parágrafos do objeto de seção
    page->get_Paragraphs()->Add(graph1);

    // Especificar as coordenadas para a linha
    auto posArr = MakeArray<float>({ 1, 2, 500, 2 });
    auto l1 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr);
    graph1->get_Shapes()->Add(l1);

    // Criar variáveis de string com texto contendo tags HTML
    String s ("<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">\
<strong> Como evitar golpes de dinheiro</<strong> </span>");

    // Criar parágrafos de texto contendo texto HTML

    auto heading_text = MakeObject<HtmlFragment>(s);
    page->get_Paragraphs()->Add(heading_text);

    auto box = MakeObject<FloatingBox>();

    // Adicionar quatro colunas na seção
    box->get_ColumnInfo()->set_ColumnCount(2);
    // Definir o espaçamento entre as colunas
    box->get_ColumnInfo()->set_ColumnSpacing(u"5");

    box->get_ColumnInfo()->set_ColumnWidths(u"105 105");
    auto text1 = MakeObject<TextFragment>("Por A Googler (O Blog Oficial do Google)");
    text1->get_TextState()->set_FontSize(8);
    text1->get_TextState()->set_LineSpacing(2);
    text1->get_TextState()->set_FontSize(10);
    text1->get_TextState()->set_FontStyle(FontStyles::Italic);

    box->get_Paragraphs()->Add(text1);

    // Criar um objeto de gráficos para desenhar uma linha
    auto graph2 = MakeObject<Aspose::Pdf::Drawing::Graph>(50, 10);
    // Especificar as coordenadas para a linha
    auto posArr2 = MakeArray<float>({ 1, 10, 100, 10 });

    auto l2 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr2);
    graph2->get_Shapes()->Add(l2);

    // Adicionar a linha à coleção de parágrafos do objeto de seção
    box->get_Paragraphs()->Add(graph2);

    auto text2 = MakeObject<TextFragment>(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. \
        Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue.\
        Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur \
        ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean \
        posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. \
        Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, \
        risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam \
        luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, \
        sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, \
        pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,\
        iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus \
        mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla.\
        Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,\
        iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique\
        ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\
        Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. \
        Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box->get_Paragraphs()->Add(text2);

    page->get_Paragraphs()->Add(box);

    // Salvar arquivo PDF
    document->Save(_dataDir + outputFileName);
}
```

## Trabalhando com Paradas de Tabulação Personalizadas

Uma Parada de Tabulação é um ponto de parada para tabulação. No processamento de texto, cada linha contém um número de paradas de tabulação colocadas em intervalos regulares (por exemplo, a cada meia polegada). Elas podem ser alteradas, no entanto, visto que a maioria dos processadores de texto permite que você defina paradas de tabulação onde quiser. Quando você pressiona a tecla Tab, o cursor ou ponto de inserção salta para a próxima parada de tabulação, que por si só é invisível. Embora as paradas de tabulação não existam no arquivo de texto, o processador de texto as rastreia para que possa reagir corretamente à tecla Tab.

Aqui está um exemplo de como configurar paradas de tabulação personalizadas.

```cpp
void CustomTabStops() {
    String _dataDir("C:\\Samples\\");
    String outputFileName("CustomTabStops_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto ts = MakeObject<TabStops>();
    auto ts1 = ts->Add(100);

    ts1->set_AlignmentType(TabAlignmentType::Right);
    ts1->set_LeaderType(TabLeaderType::Solid);

    auto ts2 = ts->Add(200);
    ts2->set_AlignmentType(TabAlignmentType::Center);
    ts2->set_LeaderType(TabLeaderType::Dash);

    auto ts3 = ts->Add(300);
    ts3->set_AlignmentType(TabAlignmentType::Left);
    ts3->set_LeaderType(TabLeaderType::Dot);

    auto header = MakeObject<TextFragment>("Este é um exemplo de formação de tabela com paradas de tabulação", ts);
    auto text0 =  MakeObject<TextFragment>("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    auto text1 = MakeObject<TextFragment>("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    auto text2 = MakeObject<TextFragment>("#$TABdata21 ", ts);
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data22 "));
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data23"));
              
    page->get_Paragraphs()->Add(header);
    page->get_Paragraphs()->Add(text0);
    page->get_Paragraphs()->Add(text1);
    page->get_Paragraphs()->Add(text2);

    document->Save(_dataDir + outputFileName);
}
```

## Como Adicionar Texto Transparente em PDF

PDF 1.4 (um formato de arquivo suportado pelo Acrobat 5) foi a primeira versão de PDF a suportar transparência. Este PDF chegou ao mercado na mesma época que o Adobe Illustrator 9.

Um arquivo PDF contém objetos de Imagem, Texto, Gráfico, anexos, Anotações e, ao criar TextFragment, você pode definir informações de cor de primeiro plano, fundo, bem como formatação de texto. Aspose.PDF para C++ suporta o recurso de adicionar texto com canal de cor Alpha. O trecho de código a seguir mostra como adicionar texto com cor transparente.

```cpp
void AddTransparentText() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("AddTransparentText_out.pdf");

    // Criar instância do Documento
    auto document = MakeObject<Document>();    
    // Criar página para coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->Add();

    // Criar objeto Graph
    auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

    // Criar instância de retângulo com certas dimensões
    auto rect = MakeObject<Aspose::Pdf::Drawing::Rectangle>(100, 100, 400, 400);
    // Criar objeto de cor do canal de cor Alpha
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;

    auto alphaColor = Color::FromArgb(alpha, red, green, blue);

    rect->get_GraphInfo()->set_FillColor(alphaColor);

    // Adicionar retângulo à coleção de formas do objeto Graph
    canvas->get_Shapes()->Add(rect);

    // Adicionar objeto gráfico à coleção de parágrafos do objeto página
    page->get_Paragraphs()->Add(canvas);

    // Definir valor para não mudar a posição do objeto gráfico
    canvas->set_IsChangePosition(false);

    // Criar instância de TextFragment com valor de exemplo
    auto text = MakeObject<TextFragment>(
        "texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente ");
    // Criar objeto de cor do canal Alpha
    alpha = 30;
    alphaColor = Color::FromArgb(alpha, red, green, blue);
    // Definir informações de cor para instância de texto
    text->get_TextState()->set_ForegroundColor(alphaColor);
    // Adicionar texto à coleção de parágrafos da instância de página
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Especificar Espaçamento entre Linhas para Fontes

A classe [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) possui uma enumeração [LineSpacingMode](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91) que é projetada para fontes específicas, por exemplo, fonte de entrada "HPSimplified.ttf". Além disso, a classe [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) tem uma propriedade [LineSpacing](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91a9e120eead36071a90367e425c96b5eaf) do tipo LineSpacingMode. Você só precisa definir LineSpacing em LineSpacingMode.FullSize. O trecho de código para obter uma fonte exibida corretamente seria o seguinte:

```cpp
void SpecifyLineSpacingForFonts() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("SpecifyLineSpacing_out.pdf");

    String fontFile ("hp-simplified-265.ttf");

    // Carregar arquivo PDF de entrada
    auto document = MakeObject<Document>();
    
    // Criar TextFormattingOptions com LineSpacingMode.FullSize
    auto formattingOptions = MakeObject<TextFormattingOptions>();
    formattingOptions->set_LineSpacing(TextFormattingOptions::LineSpacingMode::FullSize);
    
    // Criar fragmento de texto com string de exemplo
    auto textFragment = MakeObject<TextFragment>("Hello world");

    // Carregar a fonte TrueType no objeto de fluxo
    auto fontStream = System::IO::File::OpenRead(_dataDir + fontFile);
    
    // Definir o nome da fonte para a string de texto
    textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
    // Especificar a posição para o Fragmento de Texto
    textFragment->set_Position(MakeObject<Position>(100, 600));
    // Definir TextFormattingOptions do fragmento atual para pré-definido (que aponta para
    // LineSpacingMode.FullSize)
    textFragment->get_TextState()->set_FormattingOptions(formattingOptions);
    
    // Adicionar o texto ao TextBuilder para que possa ser colocado sobre o arquivo PDF    
    auto page = document->get_Pages()->Add();
    page->get_Paragraphs()->Add(textFragment);

    // Salvar documento PDF resultante
    document->Save(_dataDir + outputFileName);
}
```

## Obter Largura do Texto Dinamicamente

A classe [Aspose.Pdf.Text.TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) mostra como obter a largura do texto dinamicamente em um documento PDF.

Às vezes, é necessário obter a largura do texto dinamicamente. O Aspose.PDF para C++ inclui dois métodos para medição da largura de strings. Você pode invocar o método [MeasureString](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state#a084c1781028cd3483c82b4fd4cec4967) das classes Aspose.Pdf.Text.Font ou Aspose.Pdf.Text.TextState (ou ambas). O trecho de código abaixo mostra como usar essa funcionalidade.

```cpp
void GetTextWidthDynamicaly() {
    auto font = FontRepository::FindFont(u"Arial");
    auto ts = MakeObject<TextState>();

    ts->set_Font(font);
    ts->set_FontSize(14);

    if (Math::Abs(font->MeasureString(u"A", 14) - 9.337) > 0.001)
        Console::WriteLine(u"Medida de string de fonte inesperada!");

    if (Math::Abs(ts->MeasureString(u"z") - 7.0) > 0.001)
        Console::WriteLine(u"Medida de string de fonte inesperada!");

    for (char c = 'A'; c <= 'z'; c++) {
        String v(c);
        double fnMeasure = font->MeasureString(v, 14);
        double tsMeasure = ts->MeasureString(v);

        if (Math::Abs(fnMeasure - tsMeasure) > 0.001)
            Console::WriteLine(u"A medição da string de fonte e estado não coincide!");
    }
}
```