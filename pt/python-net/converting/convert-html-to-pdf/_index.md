---
title: Converter HTML para PDF em Python
linktitle: Converter arquivo HTML para PDF
type: docs
weight: 40
url: /pt/python-net/convert-html-to-pdf/
lastmod: "2025-09-27"
description: Aprenda como converter conteúdo HTML em um documento PDF usando Aspose.PDF para Python via .NET
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como converter HTML para PDF usando Aspose.PDF para Python
Abstract: O Aspose.PDF for Python via .NET oferece uma solução robusta para criar arquivos PDF a partir de páginas da web e código HTML bruto dentro de aplicações. Este artigo fornece um guia sobre como converter HTML para PDF usando Python, descrevendo o uso do Aspose.PDF for Python, uma API de manipulação de PDF que permite a conversão perfeita de documentos HTML para o formato PDF. O processo de conversão pode ser personalizado conforme necessário. O artigo inclui um exemplo de código Python que demonstra o processo de conversão, que envolve criar uma instância da classe HtmlLoadOptions, inicializar um objeto Document e salvar o documento PDF de saída usando o método Document.Save(). Além disso, a Aspose oferece uma ferramenta online para converter HTML em PDF, permitindo que os usuários explorem a funcionalidade e a qualidade do processo de conversão.
---

## Conversão de HTML para PDF em Python

**Aspose.PDF for Python** é uma API de manipulação de PDF que permite converter quaisquer documentos HTML existentes para PDF de forma perfeita. O processo de conversão de HTML para PDF pode ser flexivelmente personalizado.

## Converter HTML para PDF

O exemplo de código Python a seguir mostra como converter um documento HTML para PDF.

1. Crie uma instância da classe [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
1. Inicialize o objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Salve o documento PDF de saída chamando o método **document.save()**.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Tente converter HTML para PDF online**

Aspose apresenta a você a aplicação gratuita online ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF HTML para PDF usando Aplicativo Gratuito](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Converter HTML para PDF usando tipo de mídia

Este exemplo mostra como converter um arquivo HTML para PDF usando Aspose.PDF para Python via .NET com opções de renderização específicas.

1. Crie uma instância da classe [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/). O 'html_media_type' aplica regras CSS destinadas à exibição em tela. A propriedade 'html_media_type' pode ter múltiplos valores. Você pode defini-la como HtmlMediaType.SCREEN ou HtmlMediaType.PRINT.
1. Carregue o HTML em um ap.Document usando as opções de carregamento.
1. Salve o documento como PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.html_media_type = ap.HtmlMediaType.SCREEN
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Converter HTML para PDF com regra CSS de página prioritária

Alguns documentos podem conter configurações de layout que utilizam [the Page rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@page), o que pode gerar ambiguidades ao gerar o layout. Você pode controlar a prioridade usando a propriedade 'is_priority_css_page_rule'. Se essa propriedade for definida como 'True', a regra CSS será aplicada primeiro.

1. Crie uma instância da classe [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
1. Defina 'is_priority_css_page_rule = False' para desabilitar a priorização das regras CSS @page, permitindo que outros estilos tenham precedência.
1. Carregue o HTML em um ap.Document com as opções configuradas.
1. Salve o documento como PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    # load_options.is_priority_css_page_rule = False
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Converter HTML para PDF com fontes incorporadas

Este exemplo mostra como converter um arquivo HTML para PDF incorporando fontes. Se você precisar de um documento PDF com fontes incorporadas, deve definir 'is_embed_fonts' como True.

1. Crie 'HtmlLoadOptions()' para configurar a conversão de HTML para PDF.
1. Defina 'is_embed_fonts = True' para garantir que todas as fontes usadas no HTML sejam incorporadas diretamente ao PDF, preservando a fidelidade visual.
1. Carregue o HTML em um ap.Document com essas opções.
1. Salve o documento como PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.is_embed_fonts = True
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Renderizar conteúdo em página única durante a conversão de HTML para PDF

Este exemplo demonstra como converter um arquivo HTML em um PDF de página única usando Aspose.PDF para Python.
Você pode exibir todo o conteúdo em uma página usando a propriedade 'is_render_to_single_page'.

1. Crie uma instância de 'HtmlLoadOptions()' para configurar o processo de conversão.
1. Ative 'is_render_to_single_page' para renderizar todo o conteúdo HTML em uma única página PDF contínua.
1. Carregue o documento com as opções configuradas em um 'ap.Document'.
1. Salve o resultado como um arquivo PDF.

```python
    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = ap.HtmlLoadOptions()
    options.is_render_to_single_page = True

    doc = ap.Document(path_infile, options)
    doc.save(path_outfile)
```

## Converter MHTML para PDF

Este exemplo mostra como converter um arquivo MHT (MHTML) em um documento PDF usando Aspose.PDF para Python com dimensões de página específicas.

1. Crie uma instância de ap.MhtLoadOptions() para configurar o processamento do arquivo MHT.
1. Defina vários parâmetros, como o tamanho da página.
1. Inicialize o documento com o arquivo de entrada e as opções de carregamento configuradas.
1. Salve o documento resultante como PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    load_options = ap.MhtLoadOptions()
    load_options.page_info.width = 842
    load_options.page_info.height= 1191
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```
