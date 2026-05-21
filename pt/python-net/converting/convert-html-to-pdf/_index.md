---
title: Converter HTML para PDF em Python
linktitle: Converter HTML para arquivo PDF
type: docs
weight: 40
url: /pt/python-net/convert-html-to-pdf/
lastmod: "2026-05-21"
description: Aprenda como converter HTML e MHTML para PDF em Python com Aspose.PDF for Python via .NET, incluindo configurações de mídia CSS, fontes incorporadas e saída de PDF marcado.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como converter HTML para PDF em Python com Aspose.PDF
Abstract: Este artigo explica como converter arquivos HTML e MHTML para PDF usando Aspose.PDF for Python via .NET. Ele cobre o fluxo de trabalho básico de HTML para PDF e mostra como controlar a renderização com tipos de mídia, prioridade de regras de página CSS, fontes incorporadas, saída de página única e geração de estrutura lógica para PDFs etiquetados acessíveis.
---

## Conversão de HTML para PDF em Python

**Aspose.PDF for Python via .NET** permite converter documentos HTML existentes para PDF com opções flexíveis de renderização. Você pode ajustar finamente como a saída é gerada para corresponder ao seu layout, estilo, acessibilidade e requisitos de arquivamento.

## Converter HTML para PDF

O exemplo Python a seguir mostra o fluxo de trabalho básico para converter um documento HTML em PDF.

1. Crie uma instância de [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) classe.
1. Inicializar um [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto com o arquivo HTML de origem.
1. Salve o documento PDF de saída chamando `document.save()`.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Conversões relacionadas

- [Converter PDF para HTML](/pdf/pt/python-net/convert-pdf-to-html/) quando você precisa de saída pronta para web a partir de arquivos PDF existentes.
- [Converter outros formatos de arquivo para PDF](/pdf/pt/python-net/convert-other-files-to-pdf/) para fluxos de trabalho de conversão de EPUB, XPS, texto e PostScript.
- [Converter imagens para PDF](/pdf/pt/python-net/convert-images-format-to-pdf/) quando o conteúdo de origem é baseado em imagem, em vez de marcação HTML.

{{% alert color="success" %}}
**Tente converter HTML para PDF online**

Aspose apresenta o aplicativo online ["HTML para PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), onde você pode testar a qualidade da conversão e a saída.

[![Aspose.PDF Conversão HTML para PDF usando App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Converter HTML para PDF usando tipo de mídia

Este exemplo mostra como converter um arquivo HTML para PDF usando opções de renderização específicas.

1. Crie uma instância de [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) classe.
1. Definir `html_media_type` para aplicar regras CSS destinadas a layouts de tela ou impressão, como `HtmlMediaType.SCREEN` ou `HtmlMediaType.PRINT`.
1. Carregue o HTML em um `ap.Document` usando as opções de carregamento.
1. Salve o documento como um PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.html_media_type = ap.HtmlMediaType.SCREEN
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Priorize o CSS `@page` regra durante a conversão de HTML para PDF

Alguns documentos usam [o `@page` regra](https://developer.mozilla.org/en-US/docs/Web/CSS/@page) para layout de página. Se esses estilos entrarem em conflito com outras configurações, você pode controlar a prioridade com `is_priority_css_page_rule`.

1. Crie uma instância de [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) classe.
1. Definir `is_priority_css_page_rule = False` para permitir que outros estilos tenham precedência sobre `@page` regras.
1. Carregue o HTML em um `ap.Document` com as opções configuradas.
1. Salve o documento como um PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
# load_options.is_priority_css_page_rule = False
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Converter HTML para PDF com fontes incorporadas

Este exemplo mostra como converter um arquivo HTML em PDF enquanto incorpora fontes. Se precisar que o PDF de saída preserve a tipografia original, defina `is_embed_fonts` para `True`.

1. Criar `HtmlLoadOptions()` para configurar a conversão de HTML para PDF.
1. Definir `is_embed_fonts = True` incorporar as fontes usadas no HTML diretamente no PDF.
1. Carregue o HTML em um `ap.Document` com estas opções.
1. Salve o documento como um PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.is_embed_fonts = True
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Renderizar conteúdo HTML em uma única página PDF

Este exemplo demonstra como converter um arquivo HTML em um PDF de página única usando Aspose.PDF for Python via .NET. Use o `is_render_to_single_page` propriedade quando você deseja que o conteúdo HTML completo seja renderizado em uma única página contínua.

1. Criar uma instância de `HtmlLoadOptions()` para configurar o processo de conversão.
1. Habilitar `is_render_to_single_page` para renderizar todo o conteúdo HTML em uma página.
1. Carregue o documento com as opções configuradas em um `ap.Document`.
1. Salve o resultado como um arquivo PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

options = ap.HtmlLoadOptions()
options.is_render_to_single_page = True

doc = ap.Document(path_infile, options)
doc.save(path_outfile)
```

## Criar estrutura lógica a partir de tags HTML

A estrutura lógica, também chamada de Tagged PDF, preserva a hierarquia semântica do HTML original, como cabeçalhos, parágrafos e listas. Isso torna o PDF resultante mais acessível, pesquisável e adequado para fluxos de trabalho de documentos estruturados.

Ao habilitar a estrutura lógica durante a conversão, o DOM HTML é mapeado para uma árvore de tags PDF em vez de ser renderizado apenas como conteúdo visual.

Para atender aos requisitos de acessibilidade, um PDF deve incluir elementos de estrutura lógica que definam a ordem de leitura, forneçam texto alternativo para leitores de tela e preservem a hierarquia do conteúdo.

> A qualidade da estrutura lógica no PDF de saída depende diretamente da qualidade da marcação HTML original. HTML mal estruturado ou inválido pode resultar em marcação incompleta ou imprecisa no PDF convertido.

1. Crie uma instância de HtmlLoadOptions para controlar como o HTML é convertido.
1. Ative a marcação semântica para que o PDF contenha elementos estruturados.
1. Abra o arquivo HTML usando as opções configuradas.
1. Salve o PDF estruturado.

```python
import aspose.pdf as ap

# Path to the source HTML
input_html_path = "input.html"
# Path for the Logical Structure PDF
output_pdf_path = "output_logical_structure.pdf"
# Initialize HtmlLoadOptions
options = ap.HtmlLoadOptions()
# Convert HTML markup to PDF logical structure elements
options.create_logical_structure = True
# Open PDF document
with ap.Document(input_html_path, options) as document:
    # Save PDF document
    document.save(output_pdf_path)
```

## Converter MHTML para PDF

Este exemplo mostra como converter um arquivo MHT ou MHTML em um documento PDF usando Aspose.PDF for Python via .NET com dimensões de página específicas.

1. Criar uma instância de `ap.MhtLoadOptions()` para configurar o processamento de arquivos MHTML.
1. Defina vários parâmetros, como o tamanho da página.
1. Inicialize o documento com o arquivo de entrada e as opções de carregamento configuradas.
1. Salve o documento resultante como um PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
load_options = ap.MhtLoadOptions()
load_options.page_info.width = 842
load_options.page_info.height = 1191
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```
