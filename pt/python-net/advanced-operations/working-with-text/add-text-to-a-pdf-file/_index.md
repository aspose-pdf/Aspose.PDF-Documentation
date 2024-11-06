---
title: Adicionar Texto ao PDF usando Python
linktitle: Adicionar Texto ao PDF
type: docs
weight: 10
url: pt/python-net/add-text-to-pdf-file/
description: Este artigo descreve vários aspectos do trabalho com texto no Aspose.PDF. Aprenda como adicionar texto ao PDF, adicionar fragmentos HTML ou usar fontes OTF personalizadas.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Texto ao PDF usando Python",
    "alternativeHeadline": "Como adicionar Texto ao PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, adicionar texto ao pdf",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-text-to-pdf-file/"
    },
    "dateModified": "2024-02-04",
    "description": "Este artigo descreve vários aspectos do trabalho com texto no Aspose.PDF para Python. Aprenda como adicionar texto ao PDF, adicionar fragmentos HTML ou usar fontes OTF personalizadas."
}
</script>


## Adicionando Texto

1. Abra o documento PDF de entrada usando Aspose.PDF.
1. Selecione a página específica à qual você deseja adicionar o texto.
1. Crie um objeto TextFragment. Um fragmento de texto é criado com o conteúdo 'texto principal'. Este fragmento é posicionado nas coordenadas (100, 600) na página.
1. Configurando Propriedades do Texto. Várias propriedades do texto são definidas, como tamanho da fonte, tipo de fonte (Times New Roman), cor de fundo (cinza claro) e cor de primeiro plano (vermelho).
1. Crie o Objeto TextBuilder. Um objeto TextBuilder é instanciado com a página selecionada.
1. Anexe o Fragmento de Texto. O fragmento de texto criado anteriormente é anexado à página PDF usando o objeto TextBuilder.
1. Chame o método [document.save](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) e salve o arquivo PDF de saída.

O snippet de código a seguir mostra como adicionar texto em um arquivo PDF existente:

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Obter página específica
    page = document.pages[1]

    # Criar fragmento de texto
    text_fragment = ap.text.TextFragment("main text")
    text_fragment.position = ap.text.Position(100, 600)

    # Definir propriedades do texto
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Criar objeto TextBuilder
    builder = ap.text.TextBuilder(page)

    # Anexar o fragmento de texto à página PDF
    builder.append_text(text_fragment)

    # Salvar documento PDF resultante.
    document.save(output_pdf)             
```


## Carregando Fonte a partir de Stream

O trecho de código a seguir mostra como carregar uma fonte a partir de um objeto stream ao adicionar texto a um documento PDF.

```python

    import aspose.pdf as ap

    # Carregar arquivo PDF de entrada
    document = ap.Document()
    document.pages.add()
    # Criar objeto construtor de texto para a primeira página do documento
    text_builder = ap.text.TextBuilder(document.pages[1])
    # Criar fragmento de texto com uma string de exemplo
    text_fragment = ap.text.TextFragment("Hello world")

    if input_ttf != "":
        # Carregar a fonte TrueType no objeto stream
        font_stream = open(input_ttf, "rb")
        # Definir o nome da fonte para a string de texto
        text_fragment.text_state.font = ap.text.FontRepository.open_font(
            font_stream, ap.text.FontTypes.TTF
        )
        # Especificar a posição do Fragmento de Texto
        text_fragment.position = ap.text.Position(10, 10)
        # Adicionar o texto ao TextBuilder para que ele possa ser colocado sobre o arquivo PDF
        text_builder.append_text(text_fragment)
        # Salvar o documento PDF resultante.
        document.save(output_pdf)
```


## Adicionar Texto usando TextParagraph

O trecho de código a seguir mostra como adicionar texto em um documento PDF usando a classe [TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/).

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document()
    # Adicionar página à coleção de páginas do objeto Document
    page = document.pages.add()
    builder = ap.text.TextBuilder(page)
    # Criar parágrafo de texto
    paragraph = ap.text.TextParagraph()
    # Definir indentação das linhas subsequentes
    paragraph.subsequent_lines_indent = 20
    # Especificar o local para adicionar o TextParagraph
    paragraph.rectangle = ap.Rectangle(100, 300, 200, 700, False)
    # Especificar o modo de quebra de linha
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )
    # Criar fragmento de texto
    fragment1 = ap.text.TextFragment("the quick brown fox jumps over the lazy dog")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment1.text_state.font_size = 12
    # Adicionar fragmento ao parágrafo
    paragraph.append_line(fragment1)
    # Adicionar parágrafo
    builder.append_paragraph(paragraph)

    # Salvar documento PDF resultante.
    document.save(output_pdf)
```


## Adicionar Hiperlink ao TextSegment

Este código demonstra como criar conteúdo dinâmico e interativo em um documento PDF, incluindo hiperlinks para recursos externos.

Uma página PDF pode consistir em um ou mais objetos TextFragment, onde cada objeto TextFragment pode ter uma ou mais instâncias de [TextSegment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textsegment/).

Por favor, tente usar o seguinte trecho de código para realizar este requisito:

```python

    import aspose.pdf as ap

    # Criar instância de documento
    document = ap.Document()
    # Adicionar página à coleção de páginas do arquivo PDF
    page1 = document.pages.add()
    # Criar instância de TextFragment
    tf = ap.text.TextFragment("Sample Text Fragment")
    # Definir alinhamento horizontal para TextFragment
    tf.horizontal_alignment = ap.HorizontalAlignment.RIGHT
    # Criar um textsegment com texto de exemplo
    segment = ap.text.TextSegment(" ... Text Segment 1...")
    # Adicionar segmento à coleção de segmentos do TextFragment
    tf.segments.append(segment)
    # Criar um novo TextSegment
    segment = ap.text.TextSegment("Link to Google")
    # Adicionar segmento à coleção de segmentos do TextFragment
    tf.segments.append(segment)
    # Definir hiperlink para TextSegment
    segment.hyperlink = ap.WebHyperlink("www.google.com")
    # Definir cor de primeiro plano para o segmento de texto
    segment.text_state.foreground_color = ap.Color.blue
    # Definir formatação de texto como itálico
    segment.text_state.font_style = ap.text.FontStyles.ITALIC
    # Criar outro objeto TextSegment
    segment = ap.text.TextSegment("TextSegment without hyperlink")
    # Adicionar segmento à coleção de segmentos do TextFragment
    tf.segments.append(segment)
    # Adicionar TextFragment à coleção de parágrafos do objeto de página
    page1.paragraphs.add(tf)
    # Salvar o documento PDF resultante.
    document.save(output_pdf)
```


## Usar Fonte OTF

Aspose.PDF para Python via .NET oferece a funcionalidade de usar fontes Customizadas/TrueType ao criar/manipular conteúdos de arquivos PDF para que os conteúdos do arquivo sejam exibidos usando fontes diferentes das fontes padrão do sistema.

```python

    import aspose.pdf as ap

    # Criar nova instância de documento
    document = ap.Document()
    # Adicionar página à coleção de páginas do arquivo PDF
    page = document.pages.add()
    # Criar instância de TextFragment com texto de exemplo
    fragment = ap.text.TextFragment("Texto de exemplo na fonte OTF")
    # Ou você pode até especificar o caminho da fonte OTF no diretório do sistema
    fragment.text_state.font = ap.text.FontRepository.open_font(input_otf)
    # Especificar para incluir a fonte dentro do arquivo PDF, para que seja exibida corretamente,
    # Mesmo que a fonte específica não esteja instalada/presente na máquina de destino
    fragment.text_state.font.is_embedded = True
    # Adicionar TextFragment à coleção de parágrafos da instância de Page
    page.paragraphs.add(fragment)
    # Salvar o documento PDF resultante.
    document.save(output_pdf)
```


## Adicionar String HTML usando DOM

O próximo código Python utiliza a biblioteca Aspose.PDF para criar um documento PDF com um fragmento HTML. 

1. Instanciar Documento. Uma instância da classe Document é criada, representando o documento PDF.
1. Adicionar Página ao documento PDF.
1. Instanciar um objeto HtmlFragment com conteúdo HTML.
1. Definir Margens para o fragmento HTML. Neste caso, a margem inferior é definida para 10 pontos e a margem superior é definida para 200 pontos.
1. Adicionar Fragmento HTML à Página.
1. Salvar Arquivo PDF.

```python

    import aspose.pdf as ap

    # Instanciar objeto Document
    doc = ap.Document()
    # Adicionar uma página à coleção de páginas do arquivo PDF
    page = doc.pages.add()
    # Instanciar HtmlFragment com conteúdos HTML
    title = ap.HtmlFragment("<fontsize=10><b><i>Tabela</i></b></fontsize>")
    # Definir informações de margem inferior
    title.margin.bottom = 10
    # Definir informações de margem superior
    title.margin.top = 200
    # Adicionar Fragmento HTML à coleção de parágrafos da página
    page.paragraphs.add(title)
    # Salvar arquivo PDF
    doc.save(output_pdf)
```


### Estilo de linha personalizado para Nota de Rodapé

O exemplo a seguir demonstra como adicionar Notas de Rodapé na parte inferior da página do Pdf e definir um estilo de linha personalizado.

```python

    import aspose.pdf as ap

    # Criar instância de Documento
    doc = ap.Document()
    # Adicionar página à coleção de páginas do PDF
    page = doc.pages.add()
    # Criar objeto GraphInfo
    graph = ap.GraphInfo()
    # Definir a largura da linha como 2
    graph.line_width = 2
    # Definir a cor para o objeto gráfico
    graph.color = ap.Color.red
    # Definir o valor do array de traços como 3
    graph.dash_array = [3]
    # Definir o valor da fase de traço como 1
    graph.dash_phase = 1
    # Definir o estilo da linha da nota de rodapé para a página como gráfico
    page.note_line_style = graph
    # Criar instância de TextFragment
    text = ap.text.TextFragment("Hello World")
    # Definir valor da Nota de Rodapé para o TextFragment
    text.foot_note = ap.Note("nota de rodapé para texto de teste 1")
    # Adicionar TextFragment à coleção de parágrafos da primeira página do documento
    page.paragraphs.add(text)
    # Criar segundo TextFragment
    text = ap.text.TextFragment("Aspose.Pdf for .NET")
    # Definir Nota de Rodapé para o segundo fragmento de texto
    text.foot_note = ap.Note("nota de rodapé para texto de teste 2")
    # Adicionar segundo fragmento de texto à coleção de parágrafos do arquivo PDF
    page.paragraphs.add(text)
    # Salvar o documento PDF resultante.
    doc.save(output_pdf)
```


### Personalizar rótulo da Nota de Rodapé

O próximo trecho de código mostra como criar um documento PDF com um fragmento de texto contendo uma nota de rodapé.

Por padrão, o número da Nota de Rodapé é incremental a partir de 1. No entanto, podemos ter um requisito para definir um rótulo de Nota de Rodapé personalizado. Para atender a esse requisito, tente usar o seguinte trecho de código

```python

    import aspose.pdf as ap

    # Criar instância do Documento
    document = ap.Document()
    # Adicionar página à coleção de páginas do PDF
    page = document.pages.add()
    # Criar objeto GraphInfo
    graph = ap.GraphInfo()
    # Definir a largura da linha como 2
    graph.line_width = 2
    # Definir a cor para o objeto gráfico
    graph.color = ap.Color.red
    # Definir o valor do array de tracejado como 3
    graph.dash_array = [3]
    # Definir o valor da fase de tracejado como 1
    graph.dash_phase = 1
    # Definir o estilo da linha da nota de rodapé para a página como gráfico
    page.note_line_style = graph
    # Criar instância de TextFragment
    text = ap.text.TextFragment("Hello World")
    # Definir valor da Nota de Rodapé para o TextFragment
    text.foot_note = ap.Note("nota de rodapé para texto de teste 1")
    # Especificar rótulo personalizado para a Nota de Rodapé
    text.foot_note.text = " Aspose"
    # Adicionar TextFragment à coleção de parágrafos da primeira página do documento
    page.paragraphs.add(text)
    # Salvar o documento PDF resultante.
    document.save(output_pdf)
```


## Adicionando Imagem e Tabela à Nota de Rodapé

Este código demonstra como criar um documento PDF com um fragmento de texto contendo uma nota de rodapé complexa que inclui uma imagem, texto e uma tabela usando Aspose.PDF para Python.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    text = ap.text.TextFragment("algum texto")
    page.paragraphs.add(text)

    text.foot_note = ap.Note()
    image = ap.Image()
    image.file = input_jpg
    image.fix_height = 20
    text.foot_note.paragraphs.add(image)
    foot_note = ap.text.TextFragment("texto da nota de rodapé")
    foot_note.text_state.font_size = 20
    foot_note.is_in_line_paragraph = True
    text.foot_note.paragraphs.add(foot_note)
    table = ap.Table()
    table.rows.add().cells.add().paragraphs.add(ap.text.TextFragment("Linha 1 Célula 1"))
    text.foot_note.paragraphs.add(table)

    # Salvar documento PDF resultante.
    document.save(output_pdf)
```

## Como Criar Notas de Fim

Uma Nota de Fim é uma citação de fonte que refere os leitores a um local específico no final do documento onde eles podem descobrir a fonte da informação ou palavras citadas ou mencionadas no documento.
 Quando se usam notas de fim, a sentença citada ou parafraseada ou o material resumido é seguido por um número sobrescrito.

Este código demonstra como adicionar um fragmento de texto com uma nota de fim a um documento PDF usando Aspose.PDF para Python:

```python

    import aspose.pdf as ap

    # Criar instância do Documento
    document = ap.Document()
    # Adicionar página à coleção de páginas do PDF
    page = document.pages.add()
    # Criar instância do TextFragment
    text = ap.text.TextFragment("Hello World")
    # Definir valor da Nota de Fim para o TextFragment
    text.end_note = ap.Note("nota de fim de exemplo")
    # Especificar rótulo personalizado para a Nota de Rodapé
    text.end_note.text = " Aspose"
    # Adicionar TextFragment à coleção de parágrafos da primeira página do documento
    page.paragraphs.add(text)
    # Salvar o documento PDF resultante.
    document.save(output_pdf)
```

## Texto e Imagem como Parágrafo Embutido

O layout padrão do arquivo PDF é o layout de fluxo (Topo-Esquerda para Baixo-Direita). Portanto, todo novo elemento adicionado ao arquivo PDF é adicionado no fluxo inferior direito. No entanto, podemos ter um requisito para exibir vários elementos de página, ou seja, Imagem e Texto no mesmo nível (um após o outro). Uma abordagem pode ser criar uma instância de Tabela e adicionar ambos os elementos a objetos de célula individualmente. No entanto, outra abordagem pode ser o parágrafo InLine. Ao definir a propriedade IsInLineParagraph da Imagem e Texto como verdadeira, esses parágrafos aparecerão como inline para outros elementos da página.

O snippet de código a seguir mostra como adicionar texto e imagem como parágrafos InLine em um arquivo PDF.

```python

    import aspose.pdf as ap

    # Instanciar a instância do Documento
    document = ap.Document()
    # Adicionar página à coleção de páginas da instância do Documento
    page = document.pages.add()
    # Criar TextFragment
    text = ap.text.TextFragment("Olá Mundo.. ")
    # Adicionar fragmento de texto à coleção de parágrafos do objeto Página
    page.paragraphs.add(text)
    # Criar uma instância de imagem
    image = ap.Image()
    # Definir imagem como parágrafo inline para que apareça logo após
    # O objeto de parágrafo anterior (TextFragment)
    image.is_in_line_paragraph = True
    # Especificar caminho do arquivo de imagem
    image.file = input_jpg
    # Definir altura da imagem (opcional)
    image.fix_height = 30
    # Definir largura da imagem (opcional)
    image.fix_width = 100
    # Adicionar imagem à coleção de parágrafos do objeto página
    page.paragraphs.add(image)
    # Re-inicializar o objeto TextFragment com diferentes conteúdos
    text = ap.text.TextFragment(" Olá novamente..")
    # Definir TextFragment como parágrafo inline
    text.is_in_line_paragraph = True
    # Adicionar o novo TextFragment criado à coleção de parágrafos da página
    page.paragraphs.add(text)
    # Salvar o documento PDF resultante.
    document.save(output_pdf)
```

## Especificar espaçamento de caracteres ao adicionar texto

O próximo trecho de código mostra como gerar um documento PDF contendo um fragmento de texto com espaçamento aumentado entre caracteres.

O texto pode ser adicionado dentro de uma coleção de parágrafos de arquivos PDF usando a instância TextFragment ou usando o objeto TextParagraph e até mesmo você pode carimbar o texto dentro do PDF usando a classe TextStamp.

### Usando TextBuilder e TextFragment

```python

    import aspose.pdf as ap

    # Criar instância de Documento
    document = ap.Document()
    # Adicionar página à coleção de páginas do Documento
    document.pages.add()
    # Criar instância de TextBuilder
    builder = ap.text.TextBuilder(document.pages[1])
    # Criar instância de fragmento de texto com conteúdo de exemplo
    wide_fragment = ap.text.TextFragment("Texto com espaçamento aumentado entre caracteres")
    wide_fragment.text_state.apply_changes_from(ap.text.TextState("Arial", 12))
    # Especificar espaçamento de caracteres para TextFragment
    wide_fragment.text_state.character_spacing = 2.0
    # Especificar a posição do TextFragment
    wide_fragment.position = ap.text.Position(100, 650)
    # Anexar TextFragment à instância de TextBuilder
    builder.append_text(wide_fragment)
    # Salvar documento PDF resultante.
    document.save(output_pdf)
```


### Usando TextParagraph

```python

    import aspose.pdf as ap

    # Criar instância do Documento
    document = ap.Document()
    # Adicionar página à coleção de páginas do Documento
    document.pages.add()
    # Criar instância do TextBuilder
    builder = ap.text.TextBuilder(document.pages[1])
    # Instanciar instância do TextParagraph
    paragraph = ap.text.TextParagraph()
    # Criar instância do TextState para especificar o nome e tamanho da fonte
    state = ap.text.TextState(12.0)
    state.font = ap.text.FontRepository.find_font("Arial")
    # Especificar o espaçamento entre caracteres
    state.character_spacing = 1.5
    # Adicionar texto ao objeto TextParagraph
    tt = "Este é um parágrafo com espaçamento entre caracteres"
    paragraph.append_line(tt, state)
    # Especificar a posição para o TextParagraph
    paragraph.position = ap.text.Position(100, 550)
    # Adicionar TextParagraph à instância do TextBuilder
    builder.append_paragraph(paragraph)
    # Salvar o documento PDF resultante.
    document.save(output_pdf)
```

### Usando TextStamp

```python

    import aspose.pdf as ap

    # Criar instância do Documento
    document = ap.Document()
    # Adicionar página à coleção de páginas do Documento
    page = document.pages.add()
    # Instanciar instância do TextStamp com texto de exemplo
    stamp = ap.TextStamp("Este é um carimbo de texto com espaçamento entre caracteres")
    # Especificar o nome da fonte para o objeto Stamp
    stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    # Especificar o tamanho da fonte para o TextStamp
    stamp.text_state.font_size = 12
    # Especificar o espaçamento entre caracteres como 1
    stamp.text_state.character_spacing = 1
    # Definir o x_indent para o Stamp
    stamp.x_indent = 100
    # Definir o y_indent para o Stamp
    stamp.y_indent = 500
    # Adicionar carimbo textual à instância da página
    stamp.put(page)
    # Salvar o documento PDF resultante.
    document.save(output_pdf)
```


## Criar documento PDF com múltiplas colunas

[Aspose.PDF para Python via .NET](https://docs.aspose.com/pdf/python-net/) também oferece o recurso de criar várias colunas dentro das páginas de documentos PDF. Para criar um arquivo PDF com múltiplas colunas, podemos fazer uso da classe FloatingBox, pois ela fornece a propriedade column_info para especificar o número de colunas dentro de FloatingBox e também podemos especificar o espaçamento entre as colunas e as larguras das colunas usando as propriedades column_spacing e width, respectivamente.

Espaçamento de coluna significa o espaço entre as colunas e o espaçamento padrão entre as colunas é de 1,25 cm. Se a largura da coluna não for especificada, então o [Aspose.PDF para Python via .NET](https://docs.aspose.com/pdf/python-net/) calcula a largura de cada coluna automaticamente de acordo com o tamanho da página e o espaçamento entre colunas.

Um exemplo é dado abaixo para demonstrar a criação de duas colunas com objetos de Gráficos (Linha) e eles são adicionados à coleção de parágrafos de FloatingBox, que é então adicionada à coleção de parágrafos da instância Page.

```python

    import aspose.pdf as ap

    document = ap.Document()
    # Especificar a informação da margem esquerda para o arquivo PDF
    document.page_info.margin.left = 40
    # Especificar a informação da margem direita para o arquivo PDF
    document.page_info.margin.right = 40
    page = document.pages.add()

    graph1 = ap.drawing.Graph(500, 2)
    # Adicionar a linha à coleção de parágrafos do objeto seção
    page.paragraphs.add(graph1)

    # Especificar as coordenadas para a linha
    pos1 = [1.0, 2.0, 500.0, 2.0]
    l1 = ap.drawing.Line(pos1)
    graph1.shapes.append(l1)
    # Criar variáveis de string com texto contendo tags html
    s = (
        '<font face="Times New Roman" size=4>'
        + "<strong> Como Evitar Golpes de Dinheiro</<strong> "
        + "</font>"
    )
    # Criar parágrafos de texto contendo texto HTML
    heading_text = ap.HtmlFragment(s)
    page.paragraphs.add(heading_text)

    box = ap.FloatingBox()
    # Adicionar quatro colunas na seção
    box.column_info.column_count = 2
    # Definir o espaçamento entre as colunas
    box.column_info.column_spacing = "5"

    box.column_info.column_widths = "105 105"
    text1 = ap.text.TextFragment("Por Um Googler (O Blog Oficial do Google)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)
    text1.text_state.font_size = 10

    text1.text_state.font_style = ap.text.FontStyles.ITALIC
    # Criar um objeto de gráficos para desenhar uma linha
    graph2 = ap.drawing.Graph(50, 10)
    # Especificar as coordenadas para a linha
    pos2 = [1.0, 10.0, 100.0, 10.0]
    l2 = ap.drawing.Line(pos2)
    graph2.shapes.append(l2)

    # Adicionar a linha à coleção de parágrafos do objeto seção
    box.paragraphs.add(graph2)

    text2 = ap.text.TextFragment(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales."
    )
    box.paragraphs.add(text2)
    page.paragraphs.add(box)
    # Salvar arquivo PDF
    document.save(output_pdf)
```


## Trabalhando com Paradas de Tabulação Personalizadas

Este trecho de código Python mostra como criar um documento PDF contendo fragmentos de texto organizados usando paradas de tabulação para simular uma estrutura de tabela.

Aqui está um exemplo de como definir paradas de TAB personalizadas.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()

    ts = ap.text.TabStops()
    ts1 = ts.add(100.0)
    ts1.alignment_type = ap.text.TabAlignmentType.RIGHT
    ts1.leader_type = ap.text.TabLeaderType.SOLID
    ts2 = ts.add(200.0)
    ts2.alignment_type = ap.text.TabAlignmentType.CENTER
    ts2.leader_type = ap.text.TabLeaderType.DASH
    ts3 = ts.add(300.0)
    ts3.alignment_type = ap.text.TabAlignmentType.LEFT
    ts3.leader_type = ap.text.TabLeaderType.DOT

    header = ap.text.TextFragment(
        "Este é um exemplo de formação de tabela com paradas de TAB", ts
    )
    text0 = ap.text.TextFragment("#$TABCabeçalho1 #$TABCabeçalho2 #$TABCabeçalho3", ts)

    text1 = ap.text.TextFragment("#$TABdado11 #$TABdado12 #$TABdado13", ts)
    text2 = ap.text.TextFragment("#$TABdado21 ", ts)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("dado22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("dado23"))

    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    document.save(output_pdf)
```


## Como Adicionar Texto Transparente em PDF

Um arquivo PDF contém objetos de Imagem, Texto, Gráfico, Anexos, Anotações e, ao criar TextFragment, você pode definir informações de cor de primeiro plano, cor de fundo, bem como formatação de texto. O Aspose.PDF para Python via .NET suporta o recurso de adicionar texto com canal de cor Alpha.

O trecho de código a seguir mostra como adicionar texto com cor transparente.

```python

    import aspose.pdf as ap

    # Criar instância do Documento
    document = ap.Document()
    # Criar página para a coleção de páginas do arquivo PDF
    page = document.pages.add()

    # Criar instância de TextFragment com valor de exemplo
    text = ap.text.TextFragment(
        "texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente texto transparente "
    )
    # Criar objeto de cor a partir do canal Alpha
    color = ap.Color.from_argb(30, 0, 255, 0)
    # Definir informações de cor para a instância de texto
    text.text_state.foreground_color = color
    # Adicionar texto à coleção de parágrafos da instância da página
    page.paragraphs.add(text)

    document.save(output_pdf)
```


## Especificar Espaçamento entre Linhas para Fontes

Cada fonte tem um quadrado abstrato, cuja altura é a distância pretendida entre linhas de tipo no mesmo tamanho de tipo. Este quadrado é chamado de quadrado em e é a grade de design na qual os contornos dos glifos são definidos. Muitas letras da fonte de entrada têm pontos que são colocados fora dos limites do quadrado em da fonte, então para exibir a fonte corretamente, é necessário o uso de uma configuração especial.

O próximo trecho de código carrega um PDF, adiciona um fragmento de texto com espaçamento entre linhas específico usando uma fonte TrueType, e salva o documento PDF modificado:

```python

    import aspose.pdf as ap

    # Carregar arquivo PDF de entrada
    document = ap.Document()
    # Criar TextFormattingOptions com LineSpacingMode.FULL_SIZE
    options = ap.text.TextFormattingOptions()
    options.line_spacing = ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE

    # Criar fragmento de texto com string de exemplo
    text_fragment = ap.text.TextFragment("Hello world")

    # Carregar a fonte TrueType no objeto stream
    font_stream = open(input_ttf, "rb")
    # Definir o nome da fonte para a string de texto
    text_fragment.text_state.font = ap.text.FontRepository.open_font(
        font_stream, ap.text.FontTypes.TTF
    )
    # Especificar a posição para o Fragmento de Texto
    text_fragment.position = ap.text.Position(100, 600)
    # Definir TextFormattingOptions do fragmento atual para predefinido (que aponta para LineSpacingMode.FULL_SIZE)
    text_fragment.text_state.formatting_options = options
    page = document.pages.add()
    page.paragraphs.add(text_fragment)

    # Salvar documento PDF resultante
    document.save(output_pdf)
```


## Obter Largura do Texto Dinamicamente

Este trecho de código Python realiza uma comparação entre as medições de strings obtidas de um objeto de fonte e um objeto de estado de texto no Aspose.PDF:

```python

    import math as ap

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if mt.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("Medição inesperada de string de fonte!")

    if mt.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("Medição inesperada de string de fonte!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        print(str(c_code) + "-" + c + "-" + str(ts_measure))

        if mt.fabs(fn_measure - ts_measure) > 0.001:
            print("A medição da string de fonte e estado não coincide!")

        c_code += 1
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>