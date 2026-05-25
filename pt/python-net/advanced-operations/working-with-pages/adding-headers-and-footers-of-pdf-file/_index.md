---
title: Adicionar Cabeçalhos e Rodapés de PDF em Python
linktitle: Adicionando Cabeçalho e Rodapé ao PDF
type: docs
weight: 50
url: /pt/python-net/add-headers-and-footers-of-pdf-file/
description: Aprenda como adicionar cabeçalhos e rodapés a arquivos PDF em Python usando texto, imagens e conteúdo estruturado.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicione cabeçalhos e rodapés a arquivos PDF com Python
Abstract: Este artigo mostra como adicionar cabeçalhos e rodapés a documentos PDF com Aspose.PDF for Python via .NET. Ele abrange texto, numeração de páginas, HTML, imagem, tabela e conteúdo de cabeçalho e rodapé baseado em LaTeX.
---

Use esta página para adicionar conteúdo de cabeçalho e rodapé consistentes em todas as páginas PDF com **Aspose.PDF for Python via .NET**.

Você pode criar cabeçalhos e rodapés com [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/), e [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) objetos, então aplique-os através de [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) em cada página.

## Adicionando Cabeçalhos e Rodapés como Fragmentos de Texto

Adicione cabeçalhos e rodapés de texto simples a todas as páginas de um PDF. Ele cria [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objetos, inserções [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) elementos neles, define [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) para posicionamento adequado, e anexa-os a cada página no documento. O resultado é um PDF onde cada página exibe texto de cabeçalho e rodapé consistentes.

O trecho de código a seguir demonstra como adicionar cabeçalhos e rodapés como fragmentos de texto em um PDF usando Python:

1. Crie fragmentos de texto para o cabeçalho e o rodapé.
1. Crie objetos HeaderFooter e adicione os fragmentos de texto a eles.
1. Defina as configurações de margem para controlar a colocação do cabeçalho e do rodapé.
1. Carregue o documento PDF a partir do arquivo de entrada.
1. Iterar por todas as páginas do documento.
1. Atribua o cabeçalho e o rodapé a cada página.
1. Salve o PDF modificado no arquivo de saída.

```python
import aspose.pdf as ap

def add_header_and_footer_as_text(input_file, output_file):
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Este método é útil para adicionar títulos consistentes, indicadores de página ou avisos legais na parte superior e inferior de cada página. Você também pode estendê-lo para incluir imagens ou conteúdo dinâmico, como números de página.

## Adicionando Cabeçalhos e Rodapés para Numeração de Páginas

Adicione numeração automática de páginas aos cabeçalhos e rodapés de um documento PDF usando Aspose.PDF for Python. Usando as variáveis internas $p (número da página atual) e $P (número total de páginas), o script insere dinamicamente a numeração de páginas em cada página. Os cabeçalhos exibem o formato ‘Page X from Y’, enquanto os rodapés mostram ‘Page X / Y’. The [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) garante o posicionamento adequado em cada página.

1. Crie um TextFragment para o cabeçalho usando "Página $p de $P" para exibir a página atual e o total de páginas.
1. Crie um objeto HeaderFooter e adicione o texto do cabeçalho a ele.
1. Crie um TextFragment para o rodapé usando "Page $p / $P" para um estilo de numeração alternativo.
1. Crie um objeto Footer e adicione o texto do rodapé.
1. Defina as configurações de margem (esquerda = 50, superior = 20) e aplique-as tanto ao cabeçalho quanto ao rodapé.
1. Abra o documento PDF a partir do arquivo de entrada.
1. Percorra todas as páginas e atribua o cabeçalho e o rodapé a cada página.
1. Salve o PDF atualizado no caminho de saída.

```python
import aspose.pdf as ap

def using_header_and_footer_for_page_numbering(input_file, output_file):
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Adicionando Cabeçalhos e Rodapés como Fragmentos HTML

Aplicar cabeçalhos e rodapés formatados em HTML a cada página de um documento PDF usando Aspose.PDF for Python. Ao usar [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), o script permite que a formatação de texto rico — como negrito e itálico — apareça no cabeçalho e no rodapé. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) é aplicado para posicionamento adequado, e os mesmos elementos formatados são anexados a cada página no documento.

O trecho de código a seguir demonstra como adicionar cabeçalhos e rodapés como fragmentos HTML a um PDF usando Python:

1. Crie um trecho de cabeçalho HTML usando HtmlFragment—incluindo texto estilizado como '<strong>' para negrito.
1. Crie um objeto HeaderFooter e adicione o cabeçalho HTML a ele.
1. Crie um trecho de rodapé HTML usando '<i>' para estilo itálico.
1. Crie um objeto Footer e adicione o HTML do rodapé a ele.
1. Configure as margens (esquerda = 50, superior = 20) e atribua-as tanto ao cabeçalho quanto ao rodapé.
1. Carregue o documento PDF usando 'ap.Document()'.
1. Percorra todas as páginas e atribua o cabeçalho e o rodapé a cada uma.
1. Salve o PDF modificado no caminho de saída especificado.

```python
import aspose.pdf as ap

def add_header_and_footer_as_html(input_file, output_file):
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Usar HtmlFragment permite formatação rica com estilos embutidos ou marcação HTML, oferecendo mais flexibilidade de design em comparação com texto simples.

## Adicionando Cabeçalhos e Rodapés como Imagens

Adicionar cabeçalhos e rodapés baseados em imagem a cada página de um documento PDF usando Aspose.PDF for Python. O mesmo arquivo de imagem é usado tanto para o cabeçalho quanto para o rodapé em todas as páginas. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) posiciona as imagens, e a imagem ajusta‑se automaticamente para caber dentro da área de cabeçalho/rodapé.

O seguinte trecho de código demonstra como adicionar cabeçalhos e rodapés como imagens a um PDF usando Python:

1. Carregue a imagem em um objeto ‘ap.Image’ e prepare-a para uso como cabeçalho.
1. Crie um objeto HeaderFooter e anexe a imagem do cabeçalho a ele.
1. Carregue a mesma imagem novamente para usar como rodapé.
1. Crie um objeto Footer e adicione a imagem do rodapé a ele.
1. Carregue o documento PDF de entrada usando 'ap.Document()'.
1. Iterar por todas as páginas do documento.
1. Aplicar margens (esquerda = 50) para posicionar tanto o cabeçalho quanto o rodapé.
1. Atribua o cabeçalho e o rodapé a cada página no PDF.
1. Salve o PDF atualizado no arquivo de saída especificado.

Esta técnica é ideal para aplicar logotipos ou marcas d'água em documentos, na área de cabeçalho/rodapé.

```python
import aspose.pdf as ap

def add_header_and_footer_as_image(input_file, image_file, output_file):
    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Adicionando Cabeçalhos e Rodapés como Tabela

Adicione cabeçalhos e rodapés estruturados, baseados em tabelas, a todas as páginas de um documento PDF usando Aspose.PDF for Python. [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) objetos oferecem melhor controle de layout, alinhamento e formatação consistente para cabeçalhos e rodapés complexos. O texto do cabeçalho está centralizado enquanto o texto do rodapé está alinhado à esquerda, ambos usando fonte Arial 12pt. As larguras das colunas são calculadas dinamicamente com base nas dimensões da página para garantir o posicionamento adequado.

Este trecho de código adiciona cabeçalhos e rodapés (usando tabelas) a cada página de um documento PDF com Aspose.PDF for Python via .NET.

1. Definir estilos de texto usando [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) para cabeçalho e rodapé (fonte, tamanho, alinhamento).
1. Criar [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objetos para o cabeçalho e rodapé.
1. Construir o cabeçalho [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) com uma única linha e uma célula contendo o texto do cabeçalho.
1. Construa o rodapé [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) com uma única linha e célula contendo o texto do rodapé.
1. Adicione as tabelas ao correspondente [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objetos.
1. Definir rodapé [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) para posicionamento horizontal adequado.
1. Abrir o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando métodos apropriados.
1. Itere por todas as páginas e atribua o cabeçalho e rodapé baseados em tabela a cada página.
1. Salvar o modificado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para o arquivo de saída.

```python
import aspose.pdf as ap

def add_header_and_footer_as_table(input_file, output_file):
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Adicionando Cabeçalhos e Rodapés como LaTeX

Adicionar cabeçalhos e rodapés contendo conteúdo formatado em LaTeX a todas as páginas de um documento PDF usando Aspose.PDF for Python. LaTeX permite a renderização de símbolos matemáticos, datas, marcas de copyright e outras formatações avançadas. O cabeçalho inclui uma data dinâmica, enquanto o rodapé exibe um símbolo de copyright juntamente com o número da página atual e a contagem total de páginas.

O seguinte trecho de código mostra como usar [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) nos cabeçalhos e rodapés de um PDF usando Aspose.PDF for Python via .NET.

1. Abrir o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando métodos apropriados.
1. Determine o número total de páginas a ser usado em rodapés dinâmicos.
1. Iterar por todas as páginas do documento.
1. Criar um [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objeto para o cabeçalho.
1. Criar um [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para o texto do cabeçalho que contém comandos LaTeX (por exemplo, `\\today\\`).
1. Criar um [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objeto para o rodapé.
1. Criar um [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para o texto do rodapé incluindo símbolos LaTeX e numeração de páginas.
1. Adicionar o [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para o objeto de cabeçalho/rodapé correspondente.
1. Vincule o cabeçalho e o rodapé à página atual.
1. Salvar o modificado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para o arquivo de saída.

```python
import aspose.pdf as ap

def add_header_and_footer_as_latex(input_file, output_file):
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTeX Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = (
                f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            )
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Tópicos de página relacionados

- [Trabalhe com páginas PDF em Python](/pdf/pt/python-net/working-with-pages/)
- [Adicionar numeração de páginas ao PDF em Python](/pdf/pt/python-net/add-page-number/)
- [Carimbar páginas PDF em Python](/pdf/pt/python-net/stamping/)
- [Formatar documentos PDF em Python](/pdf/pt/python-net/formatting-pdf-document/)