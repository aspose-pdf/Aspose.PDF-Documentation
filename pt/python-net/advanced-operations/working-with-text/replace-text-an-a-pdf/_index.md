---
title: Substituir Texto em PDF com Python
linktitle: Substituir Texto em PDF
type: docs
weight: 40
url: /pt/python-net/replace-text-in-pdf/
description: Aprenda como substituir, reorganizar e remover texto em documentos PDF usando Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Substitua, remova e ajuste o conteúdo de texto em PDF usando Python
Abstract: Este artigo aborda fluxos de trabalho práticos de substituição de texto em documentos PDF usando Aspose.PDF for Python via .NET. Inclui a substituição de texto em várias páginas, a limitação da substituição a regiões específicas, o ajuste do layout do texto durante a substituição, o trabalho com correspondência baseada em expressões regulares, a substituição de fontes e a remoção de conteúdo de texto quando necessário.
---

Estes exemplos mostram como **modificar ou remover texto em um PDF existente**.

Use esta página quando precisar atualizar valores de texto, remover conteúdo indesejado ou aplicar regras de substituição de texto em páginas de PDF.

## Substituir texto existente

### Substituir texto em todas as páginas do documento PDF

{{% alert color="primary" %}}

Você pode tentar encontrar e substituir o texto no documento usando Aspose.PDF e obter os resultados online neste [link](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

A substituição de texto é uma necessidade comum ao atualizar ou corrigir o conteúdo em documentos PDF existentes — por exemplo, alterar nomes de produtos, corrigir erros de digitação ou atualizar a terminologia em várias páginas.

O Aspose.PDF for Python via .NET oferece um método poderoso e eficiente para pesquisar e substituir texto programaticamente através do [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) classe.

Este exemplo demonstra como encontrar todas as ocorrências de uma frase específica (neste caso, "Black cat") e substituí‑las por uma nova frase ("White dog") em todo o documento PDF.

1. Especifique frases de busca e substituição. Defina o texto que você deseja encontrar e o texto pelo qual deseja substituí-lo.
1. Carregue o PDF Document.
1. Crie um Text Absorber. Um TextFragmentAbsorber é inicializado com a frase de pesquisa. Ele varre o documento em busca de todas as ocorrências da frase fornecida.
1. Aplicar o Absorber a Todas as Páginas. Isso percorre todas as páginas e coleta fragmentos de texto correspondentes à frase.
1. Substitua cada fragmento encontrado. Cada ocorrência de "Black cat" deve ser alterada para "White dog".
1. Salvar o PDF Atualizado.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_on_all_pages(infile, outfile):
    search_phrase = "PDF"
    replace_phrase = "pdf"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Substituir texto em região de página específica

Às vezes, pode ser necessário substituir texto apenas dentro de uma área específica de uma página PDF, em vez de pesquisar todo o documento — por exemplo, atualizar um cabeçalho, rodapé ou uma célula de tabela em uma posição conhecida.

A biblioteca Aspose.PDF for Python via .NET habilita esta funcionalidade ao utilizar o [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) em conjunto com a pesquisa de texto baseada em região.

Este exemplo demonstra como encontrar e substituir todas as ocorrências de uma frase alvo dentro de uma região retangular definida em uma página específica.

1. Especifique frases de busca e substituição.
1. Carregue o PDF Document.
1. Crie um Text Absorber para pesquisa. Inicialize um TextFragmentAbsorber para encontrar o texto desejado.
1. Restrinja a Área de Busca. O retângulo especifica os limites de coordenadas x e y na página.
1. Aplique o Absorber a uma página específica. Isso realiza a pesquisa e coleta fragmentos de texto correspondentes dentro da área especificada.
1. Substitua o texto encontrado. Cada ocorrência de 'doc' na região definida torna‑se 'DOC'.
1. Salvar o PDF Atualizado.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_in_particular_page_region(infile, outfile):
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Redimensionar e deslocar texto sem alterar o tamanho da fonte

Ao substituir texto em um PDF, às vezes você deseja ajustar ou reposicionar o novo texto dentro de uma área específica sem modificar o tamanho da fonte.
Aspose.PDF for Python via .NET fornece opções para ajustar o layout e o espaçamento do texto mantendo o tamanho da Font original intacto.

1. Carregue o PDF Document.
1. Colete todos os fragmentos de texto na página usando um 'TextFragmentAbsorber'.
1. Selecione o Fragmento para Modificar.
1. Desloque e redimensione o retângulo de texto.
1. Ajustar espaçamento de texto. Habilite o ajuste de espaçamento para que o texto se encaixe dentro do retângulo modificado.
1. Substitua o texto do fragmento.
1. Salvar o PDF Atualizado.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Redimensionar e deslocar um parágrafo no PDF

Ao trabalhar com PDFs, às vezes é necessário substituir ou expandir um parágrafo mantendo-o visualmente alinhado com o layout da página. O Aspose.PDF permite redimensionar o retângulo delimitador do parágrafo e ajustar o espaçamento para acomodar o novo texto, tudo isso sem alterar o tamanho da fonte.

1. Carregue o PDF Document.
1. Use 'TextFragmentAbsorber' para coletar todos os fragmentos de texto na página.
1. Selecione o Fragmento para Modificar.
1. Redimensione e desloque o parágrafo. Use a caixa de mídia da página para determinar os limites e ajustar o retângulo.
1. Ajustar espaçamento. Isso modifica o espaçamento entre palavras/letras em vez de mudar o tamanho da fonte.
1. Substitua o texto do fragmento.
1. Salvar o PDF Modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Substituir Texto e Expandir Automaticamente a Fonte para Preencher a Área de Destino

Substitua texto em um PDF enquanto redimensiona e expande automaticamente a fonte para preencher uma área retangular específica. Usando a biblioteca Aspose.PDF for Python via .NET, o código ajusta dinamicamente o tamanho da fonte e o espaçamento para que o novo conteúdo de texto se encaixe perfeitamente dentro de uma caixa delimitadora definida — sem cálculos manuais de fonte.

1. Carregue o PDF.
1. Capturar Fragmentos de Texto.
1. Selecione um Fragmento Específico.
1. Definir Retângulo de Destino.
1. Ativar opções de ajuste de texto.
1. Substituir Texto.
1. Salvar o Document.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_expand_font(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Substituir texto e ajustá-lo em um retângulo

Substitua texto em um documento PDF garantindo que o novo conteúdo caiba dentro da área retangular do texto original, reduzindo automaticamente o tamanho da fonte quando necessário.

Usando a biblioteca Aspose.PDF for Python via .NET, esta função ajusta tanto o layout do texto quanto o tamanho da Font dinamicamente, preservando a estrutura do Document enquanto impede o overflow.

1. Crie um objeto TextFragmentAbsorber para extrair todos os fragmentos de texto da primeira página.
1. Acesse um Fragmento de Texto Específico.
1. Definir a Área de Substituição.
1. Configure as opções de ajuste de texto. Defina duas opções principais de substituição:
    - Ajuste de tamanho da fonte - 'SHRINK_TO_FIT' reduz automaticamente o tamanho da fonte se o novo texto for muito longo.
    - Ajuste de espaçamento - 'ADJUST_SPACE_WIDTH' mantém o espaçamento proporcional.
1. Substitua o Texto.
1. Salvar o PDF Modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Substituir Automaticamente Texto de Espaço Reservado e Reorganizar Layout do PDF

Substitua o texto de espaço reservado dentro de um PDF (por exemplo, modelos ou formulários) por dados reais, como nomes ou informações da empresa.
Ele ajusta automaticamente o layout da página para caber o novo texto enquanto aplica formatação personalizada (Font, cor, tamanho).

1. Importar e carregar o PDF.
1. Crie um Text Absorber para o Placeholder.
1. Aplique o Absorber a todas as páginas.
1. Iterar pelos fragmentos de texto encontrados.
1. Aplicar Formatação de Texto Personalizada.
1. Salvar o Documento Atualizado.

```python
import sys
import aspose.pdf as ap
from os import path

def automatically_rearrange_page_contents(input_file, output_file):
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### Substituir texto com base em uma expressão regular

Ao trabalhar com documentos PDF, pode ser necessário substituir texto que segue um padrão em vez de uma frase específica — por exemplo, números de telefone, códigos ou formatos semelhantes a datas.

Aspose.PDF for Python via .NET permite que você execute tais substituições usando expressões regulares (regex) com a classe TextFragmentAbsorber.

Este exemplo demonstra como encontrar padrões de texto (neste caso, qualquer texto que corresponda ao formato ####-####, como 1234-5678) e substituí‑los com uma string formatada 'ABC1-2XZY'. Também mostra como personalizar a fonte, a cor e o tamanho do texto substituído.

O trecho de código a seguir mostra como substituir texto com base em uma expressão regular.

1. Carregue o PDF Document.
1. Crie um Absorvedor de Texto baseado em Regex. Inicialize o TextFragmentAbsorber com um padrão de expressão regular.
1. Ativar o Modo de Expressão Regular. O parâmetro 'True' ativa o modo de pesquisa por expressão regular.
1. Aplique o Absorber a uma Página. Isso varre a página em busca de todos os fragmentos de texto que correspondem ao padrão regex definido.
1. Substitua cada correspondência por um novo texto e aplique estilo personalizado.
1. Salvar o Documento Modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_based_on_regex(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## Substituir fontes ou remover fontes não usadas

### Substituir fontes em arquivo PDF existente

Ocasionalmente, você precisa padronizar ou atualizar fontes em um PDF — por exemplo, substituindo uma fonte desatualizada ou proprietária por uma mais acessível. A biblioteca Aspose.PDF for Python via .NET permite detectar e substituir fontes programaticamente, garantindo tipografia consistente e compatibilidade de documentos.

Este exemplo demonstra como substituir todas as instâncias de uma fonte específica (por exemplo, 'Arial-BoldMT') por outra fonte (por exemplo, 'Verdana') em todo um documento PDF.

O trecho de código a seguir mostra como substituir a fonte dentro do documento PDF:

1. Abra o PDF Document.
1. Inicialize um TextFragmentAbsorber.
1. Use o Absorber para extrair fragmentos de texto de cada página do documento.
1. Identificar e substituir fontes. O script verifica se a fonte atual de um fragmento é 'Arial-BoldMT'. Se verdadeiro, substitui-a pela fonte 'Verdana' usando o método FontRepository.find_font().
1. Salvar o Documento Modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_fonts(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### Remover fontes não utilizadas

Com o tempo, os documentos PDF podem acumular fontes não usadas ou incorporadas que aumentam o tamanho do arquivo e desaceleram o processamento. Essas fontes não usadas frequentemente permanecem mesmo após edições ou substituições de texto, especialmente ao trabalhar com PDFs grandes ou complexos.

A biblioteca Aspose.PDF for Python via .NET fornece uma maneira eficiente de remover fontes redundantes usando a classe TextEditOptions. Isso não apenas otimiza o seu documento, mas também garante que ele use somente as fontes realmente aplicadas ao texto visível.

O método 'remove_unused_fonts()' é uma maneira simples, porém poderosa, de otimizar arquivos PDF removendo dados de fontes redundantes.

Este exemplo demonstra como:

- Escaneie um PDF em busca de fontes não usadas.
- Remova-os com segurança.
- Reatribua os fragmentos de texto ativos para uma fonte consistente (por exemplo, Times New Roman).

1. Abra o PDF Document.
1. Configure as Opções de Edição de Texto. Isso instrui o motor a eliminar quaisquer Font incorporados que não estejam sendo usados no texto visível.
1. Crie um TextAbsorber com Opções. Um TextFragmentAbsorber extrai fragmentos de texto do documento para edição.
1. Reatribua uma Fonte Padrão. Depois que o absorvedor coletar todos os fragmentos, itere sobre eles e aplique uma fonte consistente.
1. Salvar o PDF limpo.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_unused_fonts(input_file, output_file):
    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(
        ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS
    )

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )

    # Save the updated PDF document
    document.save(output_file)
```

## Remover todo o Texto

### Remover texto do PDF

Remova todo o conteúdo de texto de um arquivo PDF mantendo as imagens, formas e estruturas de layout intactas.
Ao usar TextFragmentAbsorber, o código varre eficientemente todo o documento e exclui cada fragmento de texto encontrado em cada página.

1. Carregue o PDF Document.
1. Um objeto TextFragmentAbsorber é criado para detectar e manipular fragmentos de texto no PDF.
1. Remover todo o conteúdo de texto. O método 'absorber.remove_all_text()' remove cada elemento de texto do documento carregado, deixando os componentes não textuais intocados.
1. Salvar o Documento Atualizado.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber1(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### Remover todo o Texto de uma Página Específica

Remova todo o texto de uma única página de um documento PDF usando a classe TextFragmentAbsorber no Aspose.PDF.
Ao contrário da remoção de todo o documento, este método realiza a limpeza de texto ao nível da página, deletando texto apenas da página escolhida, enquanto deixa todas as demais páginas intactas.

1. Carregue o arquivo PDF.
1. Crie uma instância de TextFragmentAbsorber.
1. Remover todo o texto da primeira página.
1. Salvar o PDF Modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber2(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### Remover todo o texto de uma área específica na página PDF

Remova todo o texto de uma região retangular específica em uma página usando o TextFragmentAbsorber do Aspose.PDF.
Em vez de limpar uma página inteira, este método realiza a remoção direcionada de texto, permitindo controle preciso sobre qual parte da página é afetada.

1. Carregue o PDF Document.
1. Crie um TextFragmentAbsorber.
1. Defina a Área Alvo (Retângulo).
1. Remover Texto da Região Especificada.
1. Preserve o resto do documento.
1. Salvar o PDF Modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber3(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(
            document.pages[1], ap.Rectangle(10, 200, 120, 600, True)
        )
        document.save(outfile)
```

### Remova todo o Texto oculto de um documento PDF

Remova todo o texto de uma região retangular específica em uma página usando o TextFragmentAbsorber do Aspose.PDF.
Em vez de limpar uma página inteira, este método realiza a remoção direcionada de texto, permitindo controle preciso sobre qual parte da página é afetada.

1. Carregue o PDF Document.
1. Crie um TextFragmentAbsorber.
1. Defina a Área Alvo (Retângulo).
1. Remover Texto da Região Especificada.
1. Preserve o resto do documento.
1. Salvar o PDF Modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_hidden_text(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(
            ap.text.TextReplaceOptions.ReplaceAdjustment.NONE
        )
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```

## Tópicos de Texto Relacionados

- [Trabalhe com texto em PDF usando Python](/pdf/pt/python-net/working-with-text/)
- [Adicionando texto ao PDF](/pdf/pt/python-net/add-text-to-pdf-file/)
- [Pesquisar e extrair texto de PDF em Python](/pdf/pt/python-net/search-and-get-text-from-pdf/)
- [Formatar texto PDF em Python](/pdf/pt/python-net/text-formatting-inside-pdf/)
