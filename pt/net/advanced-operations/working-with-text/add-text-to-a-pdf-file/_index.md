---
title: Adicionar Texto a PDF usando C#
linktitle: Adicionar Texto ao PDF
type: docs
weight: 10
url: pt/net/add-text-to-pdf-file/
description: Este artigo descreve vários aspectos do trabalho com texto em Aspose.PDF. Aprenda como adicionar texto a PDF, adicionar fragmentos de HTML ou usar fontes OTF personalizadas.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/add-text-to-a-pdf-file/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Texto a PDF usando C#",
    "alternativeHeadline": "Como adicionar Texto ao PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, adicionar texto ao pdf",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-to-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artigo descreve vários aspectos do trabalho com texto em Aspose.PDF. Aprenda como adicionar texto a PDF, adicionar fragmentos de HTML ou usar fontes OTF personalizadas."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Para adicionar texto a um arquivo PDF existente:

1. Abra o PDF de entrada usando o objeto Document.
2. Obtenha a página específica à qual você deseja adicionar o texto.
3. Crie um objeto TextFragment com o texto de entrada junto com outras propriedades de texto. O objeto TextBuilder criado a partir dessa página específica – à qual você deseja adicionar o texto – permite adicionar o objeto TextFragment à página usando o método AppendText.
4. Chame o método Save do objeto Document e salve o arquivo PDF de saída.

## Adicionando Texto

O seguinte trecho de código mostra como adicionar texto em um arquivo PDF existente.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Abrir documento
Document pdfDocument = new Document(dataDir + "input.pdf");

// Obter página específica
Page pdfPage = (Page)pdfDocument.Pages[1];

// Criar fragmento de texto
TextFragment textFragment = new TextFragment("texto principal");
textFragment.Position = new Position(100, 600);

// Definir propriedades do texto
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray);
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Red);

// Criar objeto TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);

// Anexar o fragmento de texto à página PDF
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddText_out.pdf";

// Salvar o documento PDF resultante.
pdfDocument.Save(dataDir);
```
## Carregando Fonte de um Stream

O seguinte trecho de código mostra como carregar uma fonte de um objeto Stream ao adicionar texto a um documento PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string fontFile = "";

// Carregar arquivo PDF de entrada
Document doc = new Document(dataDir + "input.pdf");
// Criar objeto construtor de texto para a primeira página do documento
TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// Criar fragmento de texto com uma string de exemplo
TextFragment textFragment = new TextFragment("Hello world");

if (fontFile != "")
{
    // Carregar a fonte TrueType em um objeto stream
    using (FileStream fontStream = File.OpenRead(fontFile))
    {
        // Definir o nome da fonte para a string de texto
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // Especificar a posição para o Fragmento de Texto
        textFragment.Position = new Position(10, 10);
        // Adicionar o texto ao TextBuilder para que possa ser colocado sobre o arquivo PDF
        textBuilder.AppendText(textFragment);
    }

    dataDir = dataDir + "LoadingFontFromStream_out.pdf";

    // Salvar o documento PDF resultante.
    doc.Save(dataDir);
}
```
## Adicionar Texto Usando TextParagraph

O seguinte trecho de código mostra como adicionar texto em um documento PDF usando a classe [TextParagraph](https://reference.aspose.com/pdf/net/aspose.pdf.text/textparagraph).

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Abrir documento
Document doc = new Document();
// Adicionar página à coleção de páginas do objeto Document
Page page = doc.Pages.Add();
TextBuilder builder = new TextBuilder(page);
// Criar parágrafo de texto
TextParagraph paragraph = new TextParagraph();
// Definir indentação das linhas subsequentes
paragraph.SubsequentLinesIndent = 20;
// Especificar o local para adicionar TextParagraph
paragraph.Rectangle = new Aspose.Pdf.Rectangle(100, 300, 200, 700);
// Especificar modo de quebra de palavra
paragraph.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;
// Criar fragmento de texto
TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
fragment1.TextState.Font = FontRepository.FindFont("Times New Roman");
fragment1.TextState.FontSize = 12;
// Adicionar fragmento ao parágrafo
paragraph.AppendLine(fragment1);
// Adicionar parágrafo
builder.AppendParagraph(paragraph);

dataDir = dataDir + "AddTextUsingTextParagraph_out.pdf";

// Salvar o documento PDF resultante.
doc.Save(dataDir);
```
## Adicionar Hiperlink ao TextSegment

Uma página PDF pode conter um ou mais objetos TextFragment, onde cada objeto TextFragment pode ter uma ou mais instâncias de TextSegment. Para definir um hiperlink para TextSegment, a propriedade Hyperlink da classe [TextSegment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textsegment) pode ser usada fornecendo o objeto da instância Aspose.Pdf.WebHyperlink. Por favor, tente usar o seguinte trecho de código para realizar este requisito.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Criar instância de documento
Document doc = new Document();
// Adicionar página à coleção de páginas do arquivo PDF
Page page1 = doc.Pages.Add();
// Criar instância de TextFragment
TextFragment tf = new TextFragment("Fragmento de Texto Exemplo");
// Definir alinhamento horizontal para TextFragment
tf.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
// Criar um textsegment com texto de exemplo
TextSegment segment = new TextSegment(" ... Texto Segmento 1...");
// Adicionar segmento à coleção de segmentos de TextFragment
tf.Segments.Add(segment);
// Criar um novo TextSegment
segment = new TextSegment("Link para o Google");
// Adicionar segmento à coleção de segmentos de TextFragment
tf.Segments.Add(segment);
// Definir hiperlink para TextSegment
segment.Hyperlink = new Aspose.Pdf.WebHyperlink("www.google.com");
// Definir cor de primeiro plano para segmento de texto
segment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
// Definir formatação de texto como itálico
segment.TextState.FontStyle = FontStyles.Italic;
// Criar outro objeto TextSegment
segment = new TextSegment("TextSegment sem hiperlink");
// Adicionar segmento à coleção de segmentos de TextFragment
tf.Segments.Add(segment);
// Adicionar TextFragment à coleção de parágrafos do objeto de página
page1.Paragraphs.Add(tf);

dataDir = dataDir + "AddHyperlinkToTextSegment_out.pdf";

// Salvar o documento PDF resultante.
doc.Save(dataDir);
```
## Usar Fonte OTF

Aspose.PDF para .NET oferece a funcionalidade de usar fontes Custom/TrueType enquanto cria/manipula conteúdos de arquivos PDF para que os conteúdos sejam exibidos usando fontes diferentes das fontes padrão do sistema. A partir da versão Aspose.PDF para .NET 10.3.0, nós fornecemos suporte para Fontes de Tipo Aberto.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Criar nova instância de documento
Document pdfDocument = new Document();
// Adicionar página à coleção de páginas do arquivo PDF
Aspose.Pdf.Page page = pdfDocument.Pages.Add();
// Criar instância de TextFragment com texto de exemplo
TextFragment fragment = new TextFragment("Texto de exemplo em fonte OTF");
// Encontrar fonte dentro do diretório de fontes do sistema
// Fragment.TextState.Font = FontRepository.FindFont("HelveticaNeueLT Pro 45 Lt");
// Ou você pode até especificar o caminho da fonte OTF no diretório do sistema
fragment.TextState.Font = FontRepository.OpenFont(dataDir + "space age.otf");
// Especificar para emendar a fonte dentro do arquivo PDF, para que seja exibida corretamente,
// Mesmo que a fonte específica não esteja instalada/presente na máquina alvo
fragment.TextState.Font.IsEmbedded = true;
// Adicionar TextFragment à coleção de parágrafos da instância de Página
page.Paragraphs.Add(fragment);

dataDir = dataDir + "OTFFont_out.pdf";

// Salvar o documento PDF resultante.
pdfDocument.Save(dataDir);
```
## Adicionar String HTML usando DOM

A classe Aspose.Pdf.Generator.Text contém uma propriedade chamada IsHtmlTagSupported que possibilita a adição de tags/conteúdos HTML em arquivos PDF. O conteúdo adicionado é renderizado em tags HTML nativas em vez de aparecer como uma simples string de texto. Para suportar um recurso semelhante no novo Modelo de Objeto de Documento (DOM) do namespace Aspose.Pdf, a classe HtmlFragment foi introduzida.

A instância [HtmlFragment](https://reference.aspose.com/pdf/net/aspose.pdf/htmlfragment) pode ser usada para especificar os conteúdos HTML que devem ser colocados dentro do arquivo PDF. Semelhante ao TextFragment, o HtmlFragment é um objeto de nível de parágrafo e pode ser adicionado à coleção de parágrafos do objeto Page. Os seguintes trechos de código mostram os passos para colocar conteúdos HTML dentro de um arquivo PDF usando a abordagem DOM.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Instanciar objeto Document
Document doc = new Document();
// Adicionar uma página à coleção de páginas do arquivo PDF
Page page = doc.Pages.Add();
// Instanciar HtmlFragment com conteúdos HTML
HtmlFragment title = new HtmlFragment("<fontsize=10><b><i>Tabela</i></b></fontsize>");
// Definir informações de margem inferior
title.Margin.Bottom = 10;
// Definir informações de margem superior
title.Margin.Top = 200;
// Adicionar Fragmento HTML à coleção de parágrafos da página
page.Paragraphs.Add(title);

dataDir = dataDir + "AddHTMLUsingDOM_out.pdf";
// Salvar arquivo PDF
doc.Save(dataDir);
```
O seguinte trecho de código demonstra passos sobre como adicionar listas ordenadas HTML no documento:

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// O caminho para o documento de saída.
string outFile = dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf";
// Instanciar objeto Document
Document doc = new Document();
// Instanciar objeto HtmlFragment com o fragmento HTML correspondente
HtmlFragment t = new HtmlFragment("`<body style='line-height: 100px;'><ul><li>Primeiro</li><li>Segundo</li><li>Terceiro</li><li>Quarto</li><li>Quinto</li></ul>Texto após a lista.<br/>Próxima linha<br/>Última linha</body>`");
// Adicionar Página na Coleção de Páginas
Page page = doc.Pages.Add();
// Adicionar HtmlFragment dentro da página
page.Paragraphs.Add(t);
// Salvar o arquivo PDF resultante
doc.Save(outFile);
```

Você também pode definir a formatação de strings HTML usando o objeto TextState da seguinte forma:

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
HtmlFragment html = new HtmlFragment("algum texto");
html.TextState = new TextState();
html.TextState.Font = FontRepository.FindFont("Calibri");
```
Caso você defina alguns valores de atributos de texto via marcação HTML e, em seguida, forneça os mesmos valores nas propriedades TextState, eles sobrescreverão os parâmetros HTML pelas propriedades da instância TextState. Os trechos de código a seguir mostram o comportamento descrito.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Instanciar objeto Document
Document doc = new Document();
// Adicionar uma página à coleção de páginas do arquivo PDF
Page page = doc.Pages.Add();
// Instanciar HtmlFragment com conteúdos HTML
HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");
// A fonte de 'Verdana' será alterada para 'Arial'
title.TextState = new TextState("Arial");
title.TextState.FontSize = 20;
// Configurar informações da margem inferior
title.Margin.Bottom = 10;
// Configurar informações da margem superior
title.Margin.Top = 400;
// Adicionar fragmento HTML à coleção de parágrafos da página
page.Paragraphs.Add(title);
// Salvar arquivo PDF
dataDir = dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf";
// Salvar arquivo PDF
doc.Save(dataDir);
```
## Notas de Rodapé e Notas de Fim (DOM)

Notas de rodapé indicam notas no texto do seu documento usando números sobrescritos consecutivos. A nota real é recuada e pode ocorrer como uma nota de rodapé na parte inferior da página.

### Adicionando Nota de Rodapé

Em um sistema de referência de nota de rodapé, indique uma referência por:

- colocar um pequeno número acima da linha de tipo logo após o material de origem. Este número é chamado de identificador de nota. Ele fica ligeiramente acima da linha de texto.
- colocar o mesmo número, seguido por uma citação da sua fonte, na parte inferior da página. As notas de rodapé devem ser numéricas e cronológicas: a primeira referência é 1, a segunda é 2, e assim por diante.

A vantagem da nota de rodapé é que o leitor pode simplesmente olhar para baixo da página para descobrir a fonte de uma referência que lhe interessa.

Por favor, siga os passos especificados abaixo para criar uma Nota de Rodapé:

- Crie uma instância de Documento
- Crie um objeto de Página
- Crie um objeto de Fragmento de Texto
- Crie uma instância de Nota e passe seu valor para a propriedade TextFragment.FootNote
- Crie uma instância de Note e passe seu valor para a propriedade TextFragment.FootNote
- Adicione TextFragment à coleção de parágrafos de uma instância de página

### Estilo de linha personalizado para FootNote

O exemplo a seguir demonstra como adicionar notas de rodapé na parte inferior da página do Pdf e definir um estilo de linha personalizado.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Criar instância de Document
Document doc = new Document();
// Adicionar página à coleção de páginas do PDF
Page page = doc.Pages.Add();
// Criar objeto GraphInfo
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// Definir largura da linha como 2
graph.LineWidth = 2;
// Definir a cor para o objeto de gráfico
graph.Color = Aspose.Pdf.Color.Red;
// Definir valor da matriz de traço como 3
graph.DashArray = new int[] { 3 };
// Definir valor da fase de traço como 1
graph.DashPhase = 1;
// Definir estilo de linha de nota de rodapé para a página como gráfico
page.NoteLineStyle = graph;
// Criar instância de TextFragment
TextFragment text = new TextFragment("Hello World");
// Definir valor de FootNote para TextFragment
text.FootNote = new Note("nota de rodapé para texto de teste 1");
// Adicionar TextFragment à coleção de parágrafos da primeira página do documento
page.Paragraphs.Add(text);
// Criar segundo TextFragment
text = new TextFragment("Aspose.Pdf for .NET");
// Definir FootNote para o segundo fragmento de texto
text.FootNote = new Note("nota de rodapé para texto de teste 2");
// Adicionar segundo fragmento de texto à coleção de parágrafos do arquivo PDF
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomLineStyleForFootNote_out.pdf";

// Salvar o documento PDF resultante.
doc.Save(dataDir);
```
Podemos definir a formatação do Rótulo de Nota de Rodapé (identificador de nota) usando o objeto TextState da seguinte forma:

```csharp
TextFragment text = new TextFragment("texto de teste 1");
text.FootNote = new Note("nota de rodapé para texto de teste 1");
text.FootNote.Text = "21";
text.FootNote.TextState = new TextState();
text.FootNote.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
text.FootNote.TextState.FontStyle = FontStyles.Italic;
```

### Personalizar o rótulo da nota de rodapé

Por padrão, o número da FootNote é incremental, começando de 1. No entanto, podemos ter a necessidade de definir um rótulo de FootNote personalizado. Para atingir esse requisito, tente usar o seguinte trecho de código

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Criar instância de Document
Document doc = new Document();
// Adicionar página à coleção de páginas do PDF
Page page = doc.Pages.Add();
// Criar objeto GraphInfo
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// Definir largura da linha como 2
graph.LineWidth = 2;
// Definir a cor para o objeto gráfico
graph.Color = Aspose.Pdf.Color.Red;
// Definir valor de array de traço como 3
graph.DashArray = new int[] { 3 };
// Definir valor de fase de traço como 1
graph.DashPhase = 1;
// Definir estilo de linha de nota de rodapé para a página como gráfico
page.NoteLineStyle = graph;
// Criar instância de TextFragment
TextFragment text = new TextFragment("Olá Mundo");
// Definir valor de FootNote para TextFragment
text.FootNote = new Note("nota de rodapé para texto de teste 1");
// Especificar rótulo personalizado para FootNote
text.FootNote.Text = " Aspose(2015)";
// Adicionar TextFragment à coleção de parágrafos da primeira página do documento
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomizeFootNoteLabel_out.pdf";
```
## Adicionando Imagem e Tabela à Nota de Rodapé

Nas versões anteriores, o suporte a Nota de Rodapé era fornecido, mas era aplicável apenas ao objeto TextFragment. No entanto, a partir da versão Aspose.PDF para .NET 10.7.0, você também pode adicionar Nota de Rodapé a outros objetos dentro do documento PDF, como Tabela, Células etc. O seguinte trecho de código mostra os passos para adicionar Nota de Rodapé ao objeto TextFragment e depois adicionar objeto Imagem e Tabela à coleção de parágrafos da seção de Nota de Rodapé.

```csharp

// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();
TextFragment text = new TextFragment("algum texto");
page.Paragraphs.Add(text);

text.FootNote = new Note();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = dataDir + "aspose-logo.jpg";
image.FixHeight = 20;
text.FootNote.Paragraphs.Add(image);
TextFragment footNote = new TextFragment("texto da nota de rodapé");
footNote.TextState.FontSize = 20;
footNote.IsInLineParagraph = true;
text.FootNote.Paragraphs.Add(footNote);
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.Rows.Add().Cells.Add().Paragraphs.Add(new TextFragment("Linha 1 Célula 1"));
text.FootNote.Paragraphs.Add(table);

dataDir = dataDir + "AddImageAndTable_out.pdf";

// Salvar o documento PDF resultante.
doc.Save(dataDir);
```
## Como Criar Notas de Fim

Uma Nota de Fim é uma citação de fonte que direciona os leitores para um local específico no final do trabalho onde eles podem encontrar a fonte da informação ou palavras citadas ou mencionadas no trabalho. Ao usar notas de fim, sua frase citada ou parafraseada ou material resumido é seguido por um número em sobrescrito.

O exemplo a seguir demonstra como adicionar uma Nota de Fim na página do Pdf.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Criar instância de Document
Document doc = new Document();
// Adicionar página à coleção de páginas do PDF
Page page = doc.Pages.Add();
// Criar instância de TextFragment
TextFragment text = new TextFragment("Olá Mundo");
// Definir valor de FootNote para TextFragment
text.EndNote = new Note("nota de fim de amostra");
// Especificar etiqueta personalizada para FootNote
text.EndNote.Text = " Aspose(2015)";
// Adicionar TextFragment à coleção de parágrafos da primeira página do documento
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateEndNotes_out.pdf";
// Salvar o documento PDF resultante.
doc.Save(dataDir);
```
## Texto e Imagem como Parágrafo InLine

O layout padrão do arquivo PDF é o layout de fluxo (Topo-Esquerda para Baixo-Direita). Portanto, cada novo elemento adicionado ao arquivo PDF é adicionado no fluxo inferior direito. No entanto, podemos ter a necessidade de exibir vários elementos da página, ou seja, Imagem e Texto no mesmo nível (um após o outro). Uma abordagem pode ser criar uma instância de Tabela e adicionar ambos os elementos a objetos de célula individuais. No entanto, outra abordagem pode ser o parágrafo InLine. Ao definir a propriedade IsInLineParagraph de Imagem e Texto como verdadeira, esses parágrafos aparecerão como inline para outros elementos da página.

O seguinte trecho de código mostra como adicionar texto e Imagem como parágrafos InLine em arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Instancie a instância Document
Document doc = new Document();
// Adicione página à coleção de páginas da instância Document
Page page = doc.Pages.Add();
// Criar TextFragmnet
TextFragment text = new TextFragment("Olá Mundo.. ");
// Adicione fragmento de texto à coleção de parágrafos do objeto Page
page.Paragraphs.Add(text);
// Criar uma instância de imagem
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
// Definir imagem como parágrafo InLine para que apareça logo após
// O objeto de parágrafo anterior (TextFragment)
image.IsInLineParagraph = true;
// Especificar o caminho do arquivo de imagem
image.File = dataDir + "aspose-logo.jpg";
// Definir a altura da imagem (opcional)
image.FixHeight = 30;
// Definir a largura da imagem (opcional)
image.FixWidth = 100;
// Adicionar imagem à coleção de parágrafos do objeto de página
page.Paragraphs.Add(image);
// Re-inicializar o objeto TextFragment com conteúdos diferentes
text = new TextFragment(" Olá de novo..");
// Definir TextFragment como parágrafo InLine
text.IsInLineParagraph = true;
// Adicionar o TextFragment recém-criado à coleção de parágrafos da página
page.Paragraphs.Add(text);

dataDir = dataDir + "TextAndImageAsParagraph_out.pdf";
doc.Save(dataDir);
```
## Especificar o Espaçamento de Caracteres ao Adicionar Texto

Um texto pode ser adicionado na coleção de parágrafos de arquivos PDF usando a instância TextFragment ou utilizando o objeto TextParagraph e até mesmo você pode carimbar o texto dentro do PDF usando a classe TextStamp. Ao adicionar o texto, podemos ter a necessidade de especificar o espaçamento de caracteres para os objetos de texto. Para atender a essa necessidade, foi introduzida uma nova propriedade chamada propriedade CharacterSpacing. Por favor, veja as seguintes abordagens para cumprir essa exigência.

As seguintes abordagens mostram os passos para especificar o espaçamento de caracteres ao adicionar texto dentro de um documento PDF.

### Usando TextBuilder e TextFragment

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Criar instância de Document
Document pdfDocument = new Document();
// Adicionar página à coleção de páginas do Documento
Page page = pdfDocument.Pages.Add();
// Criar instância de TextBuilder
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// Criar instância de fragmento de texto com conteúdo de amostra
TextFragment wideFragment = new TextFragment("Texto com espaçamento de caracteres aumentado");
wideFragment.TextState.ApplyChangesFrom(new TextState("Arial", 12));
// Especificar o espaçamento de caracteres para TextFragment
wideFragment.TextState.CharacterSpacing = 2.0f;
// Especificar a posição do TextFragment
wideFragment.Position = new Position(100, 650);
// Anexar TextFragment à instância de TextBuilder
builder.AppendText(wideFragment);
dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndFragment_out.pdf";
// Salvar o documento PDF resultante.
pdfDocument.Save(dataDir);
```
### Usando TextParagraph

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Criar instância de Document
Document pdfDocument = new Document();
// Adicionar página à coleção de páginas do Documento
Page page = pdfDocument.Pages.Add();
// Criar instância de TextBuilder
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// Instanciar TextParagraph
TextParagraph paragraph = new TextParagraph();
// Criar instância de TextState para especificar nome e tamanho da fonte
TextState state = new TextState("Arial", 12);
// Especificar o espaçamento entre caracteres
state.CharacterSpacing = 1.5f;
// Anexar texto ao objeto TextParagraph
paragraph.AppendLine("Este é um parágrafo com espaçamento entre caracteres", state);
// Especificar a posição para TextParagraph
paragraph.Position = new Position(100, 550);
// Anexar TextParagraph à instância de TextBuilder
builder.AppendParagraph(paragraph);

dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf";
// Salvar o documento PDF resultante.
pdfDocument.Save(dataDir);
```
### Usando TextStamp

```csharp
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Criar instância de Documento
Document pdfDocument = new Document();
// Adicionar página à coleção de páginas do Documento
Page page = pdfDocument.Pages.Add();
// Instanciar TextStamp com texto de exemplo
TextStamp stamp = new TextStamp("Este é um carimbo de texto com espaçamento entre caracteres");
// Especificar o nome da fonte para o objeto Stamp
stamp.TextState.Font = FontRepository.FindFont("Arial");
// Especificar tamanho da fonte para TextStamp
stamp.TextState.FontSize = 12;
// Especificar espaçamento de caracteres como 1f
stamp.TextState.CharacterSpacing = 1f;
// Definir o XIndent para o Stamp
stamp.XIndent = 100;
// Definir o YIndent para o Stamp
stamp.YIndent = 500;
// Adicionar carimbo textual à instância de página
stamp.Put(page);
dataDir = dataDir + "CharacterSpacingUsingTextStamp_out.pdf";
// Salvar o documento PDF resultante.
pdfDocument.Save(dataDir);
```
## Criar documento PDF de várias colunas

Em revistas e jornais, vemos principalmente que as notícias são exibidas em várias colunas em páginas únicas, ao contrário dos livros onde os parágrafos de texto são impressos em toda a página da esquerda para a direita. Muitas aplicações de processamento de documentos como o Microsoft Word e o Adobe Acrobat Writer permitem aos usuários criar várias colunas em uma única página e depois adicionar dados a elas.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) também oferece o recurso de criar várias colunas dentro das páginas de documentos PDF.
[Aspose.PDF para .NET](https://docs.aspose.com/pdf/net/) também oferece a funcionalidade de criar múltiplas colunas dentro das páginas de documentos PDF.

O espaçamento entre colunas significa o espaço entre as colunas e o espaçamento padrão entre as colunas é de 1,25cm. Se a largura da coluna não for especificada, então o [Aspose.PDF para .NET](https://docs.aspose.com/pdf/net/) calcula automaticamente a largura de cada coluna de acordo com o tamanho da página e o espaçamento entre colunas.

Um exemplo é fornecido abaixo para demonstrar a criação de duas colunas com objetos Gráficos (Linha) e eles são adicionados à coleção de parágrafos de FloatingBox, que é então adicionada à coleção de parágrafos da instância da Página.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
// Especificar a informação de margem esquerda para o arquivo PDF
doc.PageInfo.Margin.Left = 40;
// Especificar a informação de margem direita para o arquivo PDF
doc.PageInfo.Margin.Right = 40;
Page page = doc.Pages.Add();

Aspose.Pdf.Drawing.Graph graph1 = new Aspose.Pdf.Drawing.Graph(500, 2);
// Adicionar a linha à coleção de parágrafos do objeto de seção
page.Paragraphs.Add(graph1);

// Especificar as coordenadas para a linha
float[] posArr = new float[] { 1, 2, 500, 2 };
Aspose.Pdf.Drawing.Line l1 = new Aspose.Pdf.Drawing.Line(posArr);
graph1.Shapes.Add(l1);
// Criar variáveis de string com texto contendo tags html

string s = "<font face=\"Times New Roman\" size=4>" +

"<strong> Como Evitar Golpes de Dinheiro</<strong> "
+ "</font>";
// Criar parágrafos de texto contendo texto HTML

HtmlFragment heading_text = new HtmlFragment(s);
page.Paragraphs.Add(heading_text);

Aspose.Pdf.FloatingBox box = new Aspose.Pdf.FloatingBox();
// Adicionar quatro colunas na seção
box.ColumnInfo.ColumnCount = 2;
// Definir o espaçamento entre as colunas
box.ColumnInfo.ColumnSpacing = "5";

box.ColumnInfo.ColumnWidths = "105 105";
TextFragment text1 = new TextFragment("Por Um Googler (O Blog Oficial do Google)");
text1.TextState.FontSize = 8;
text1.TextState.LineSpacing = 2;
box.Paragraphs.Add(text1);
text1.TextState.FontSize = 10;

text1.TextState.FontStyle = FontStyles.Italic;
// Criar um objeto gráfico para desenhar uma linha
Aspose.Pdf.Drawing.Graph graph2 = new Aspose.Pdf.Drawing.Graph(50, 10);
// Especificar as coordenadas para a linha
float[] posArr2 = new float[] { 1, 10, 100, 10 };
Aspose.Pdf.Drawing.Line l2 = new Aspose.Pdf.Drawing.Line(posArr2);
graph2.Shapes.Add(l2);

// Adicionar a linha à coleção de parágrafos do objeto de seção
box.Paragraphs.Add(graph2);

TextFragment text2 = new TextFragment(@"Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.");
box.Paragraphs.Add(text2);

page.Paragraphs.Add(box);

dataDir = dataDir + "CreateMultiColumnPdf_out.pdf";
// Salvar o arquivo PDF
doc.Save(dataDir);
```
## Trabalhando com Tabulações Personalizadas

Uma Tabulação Personalizada é um ponto de parada para tabulação. No processamento de texto, cada linha contém uma série de tabulações colocadas em intervalos regulares (por exemplo, a cada meio polegada). Elas podem ser alteradas, no entanto, pois a maioria dos processadores de texto permite que você defina as tabulações onde desejar. Quando você pressiona a tecla Tab, o cursor ou ponto de inserção salta para a próxima tabulação, que por si só é invisível. Embora as tabulações não existam no arquivo de texto, o processador de texto mantém controle sobre elas para que possa reagir corretamente à tecla Tab.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) permite que desenvolvedores utilizem tabulações personalizadas em documentos PDF. A classe Aspose.Pdf.Text.TabStop é usada para definir TABULAÇÕES personalizadas na classe [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment).

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) também oferece alguns tipos de líderes de tabulação pré-definidos como uma enumeração chamada, TabLeaderType cujos valores pré-definidos e suas descrições são fornecidos abaixo:
[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) também oferece alguns tipos predefinidos de guias, como uma enumeração chamada TabLeaderType, cujos valores predefinidos e suas descrições são fornecidos abaixo:

|**Tipo de Líder de Guia**|**Descrição**|
| :- | :- |
|None|Sem líder de guia|
|Solid|Líder de guia sólido|
|Dash|Líder de guia tracejado|
|Dot|Líder de guia pontilhado|

Aqui está um exemplo de como configurar paradas de TAB personalizadas.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document _pdfdocument = new Document();
Page page = _pdfdocument.Pages.Add();

Aspose.Pdf.Text.TabStops ts = new Aspose.Pdf.Text.TabStops();
Aspose.Pdf.Text.TabStop ts1 = ts.Add(100);
ts1.AlignmentType = TabAlignmentType.Right;
ts1.LeaderType = TabLeaderType.Solid;
Aspose.Pdf.Text.TabStop ts2 = ts.Add(200);
ts2.AlignmentType = TabAlignmentType.Center;
ts2.LeaderType = TabLeaderType.Dash;
Aspose.Pdf.Text.TabStop ts3 = ts.Add(300);
ts3.AlignmentType = TabAlignmentType.Left;
ts3.LeaderType = TabLeaderType.Dot;

TextFragment header = new TextFragment("Este é um exemplo de formação de tabela com paradas de TAB", ts);
TextFragment text0 = new TextFragment("#$TABCabeçalho1 #$TABCabeçalho2 #$TABCabeçalho3", ts);

TextFragment text1 = new TextFragment("#$TABdado11 #$TABdado12 #$TABdado13", ts);
TextFragment text2 = new TextFragment("#$TABdado21 ", ts);
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("dado22 "));
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("dado23"));

page.Paragraphs.Add(header);
page.Paragraphs.Add(text0);
page.Paragraphs.Add(text1);
page.Paragraphs.Add(text2);

dataDir = dataDir + "CustomTabStops_out.pdf";
_pdfdocument.Save(dataDir);
```

## Como Adicionar Texto Transparente em PDF

Um arquivo PDF contém objetos de Imagem, Texto, Gráfico, anexo e Anotações e, ao criar um TextFragment, você pode definir informações de cor de fundo e de primeiro plano, bem como formatação de texto. O Aspose.PDF para .NET suporta a funcionalidade de adicionar texto com canal de cor Alpha. O seguinte trecho de código mostra como adicionar texto com cor transparente.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Criar instância de Document
Document doc = new Document();
// Criar página na coleção de páginas do arquivo PDF
Aspose.Pdf.Page page = doc.Pages.Add();

// Criar objeto Graph
Aspose.Pdf.Drawing.Graph canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
// Criar instância de retângulo com dimensões específicas
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 400, 400);
// Criar objeto de cor a partir do canal de cor Alpha
rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
// Adicionar retângulo à coleção de formas do objeto Graph
canvas.Shapes.Add(rect);
// Adicionar objeto graph à coleção de parágrafos do objeto de página
page.Paragraphs.Add(canvas);
// Definir valor para não alterar posição para o objeto graph
canvas.IsChangePosition = false;

// Criar instância de TextFragment com valor de amostra
TextFragment text = new TextFragment("texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente ");
// Criar objeto de cor a partir do canal Alpha
Aspose.Pdf.Color color = Aspose.Pdf.Color.FromArgb(30, 0, 255, 0);
// Definir informações de cor para a instância de texto
text.TextState.ForegroundColor = color;
// Adicionar texto à coleção de parágrafos da instância de página
page.Paragraphs.Add(text);

dataDir = dataDir + "AddTransparentText_out.pdf";
doc.Save(dataDir);
```
## Especificar o Espaçamento entre Linhas para Fontes

Cada fonte possui um quadrado abstrato, cuja altura é a distância pretendida entre linhas do mesmo tamanho de tipo.
Cada fonte possui um quadrado abstrato, cuja altura é a distância pretendida entre linhas de texto no mesmo tamanho de fonte.

```csharp
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string fontFile = dataDir + "HPSimplified.TTF";
// Carregar arquivo PDF de entrada
Document doc = new Document();
//Criar TextFormattingOptions com LineSpacingMode.FullSize
TextFormattingOptions formattingOptions = new TextFormattingOptions();
formattingOptions.LineSpacing = TextFormattingOptions.LineSpacingMode.FullSize;

// Criar objeto construtor de texto para a primeira página do documento
//TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// Criar fragmento de texto com string de exemplo
TextFragment textFragment = new TextFragment("Hello world");

if (fontFile != "")
{
    // Carregar a fonte TrueType em objeto de fluxo
    using (FileStream fontStream = System.IO.File.OpenRead(fontFile))
    {
        // Definir o nome da fonte para a string de texto
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // Especificar a posição para o Fragmento de Texto
        textFragment.Position = new Position(100, 600);
        //Definir TextFormattingOptions do fragmento atual para predefinido (que aponta para LineSpacingMode.FullSize)
        textFragment.TextState.FormattingOptions = formattingOptions;
        // Adicionar o texto ao TextBuilder para que possa ser colocado sobre o arquivo PDF
        //textBuilder.AppendText(textFragment);
        var page = doc.Pages.Add();
        page.Paragraphs.Add(textFragment);
    }

    dataDir = dataDir + "SpecifyLineSpacing_out.pdf";
    // Salvar o documento PDF resultante
    doc.Save(dataDir);
}
```
## Obter Largura do Texto Dinamicamente

Às vezes, é necessário obter a largura do texto dinamicamente. O Aspose.PDF para .NET inclui dois métodos para medição da largura de strings. Você pode invocar o método [MeasureString](https://reference.aspose.com/pdf/net/aspose.pdf.text/font/methods/measurestring) das classes Aspose.Pdf.Text.Font ou Aspose.Pdf.Text.TextState (ou ambos). O trecho de código abaixo mostra como usar essa funcionalidade.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Text.Font font = FontRepository.FindFont("Arial");
TextState ts = new TextState();
ts.Font = font;
ts.FontSize = 14;

if (Math.Abs(font.MeasureString("A", 14) - 9.337) > 0.001)
    Console.WriteLine("Medida de string de fonte inesperada!");

if (Math.Abs(ts.MeasureString("z") - 7.0) > 0.001)
    Console.WriteLine("Medida de string de fonte inesperada!");

for (char c = 'A'; c <= 'z'; c++)
{
    double fnMeasure = font.MeasureString(c.ToString(), 14);
    double tsMeasure = ts.MeasureString(c.ToString());

    if (Math.Abs(fnMeasure - tsMeasure) > 0.001)
        Console.WriteLine("Medição de string de fonte e estado não coincidem!");
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

