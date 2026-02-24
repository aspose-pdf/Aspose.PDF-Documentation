---
title: Converter PDF para HTML em Python
linktitle: Converter PDF para formato HTML
type: docs
weight: 50
url: /pt/python-net/convert-pdf-to-html/
lastmod: "2025-09-27"
description: Este tópico mostra como converter um arquivo PDF para o formato HTML usando a biblioteca Aspose.PDF para Python via .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como Converter PDF para HTML em Python
Abstract: Este artigo fornece um guia abrangente sobre a conversão de arquivos PDF para HTML usando Python, especificamente através da biblioteca Aspose.PDF para Python via .NET. Ele descreve os passos necessários para realizar essa conversão programaticamente, destacando a criação de um objeto `Document` a partir do PDF de origem e a utilização do `HtmlSaveOptions` para salvar o documento em formato HTML. O artigo inclui um trecho conciso de código Python demonstrando o processo de conversão. Além disso, apresenta uma ferramenta online, a aplicação "PDF to HTML" da Aspose.PDF, para que os usuários explorem a funcionalidade e a qualidade da conversão. O artigo está estruturado para abranger diversos tópicos relacionados, garantindo uma compreensão completa do uso do Python para a conversão de PDF para HTML.
---

## Converter PDF para HTML

**Aspose.PDF for Python via .NET** oferece muitos recursos para converter diversos formatos de arquivo em documentos PDF e converter arquivos PDF em vários formatos de saída. Este artigo discute como converter um arquivo PDF em <abbr title="HyperText Markup Language">HTML</abbr>. Você pode usar apenas algumas linhas de código Python para converter PDF para HTML. Pode ser necessário converter PDF para HTML se você quiser criar um site ou adicionar conteúdo a um fórum online. Uma maneira de converter PDF para HTML é usar programaticamente o Python.

{{% alert color="success" %}}
**Tente converter PDF para HTML online**

Aspose.PDF para Python apresenta a você uma aplicação gratuita online ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), onde você pode experimentar a funcionalidade e a qualidade do seu funcionamento.

[![Conversão Aspose.PDF de PDF para HTML com Aplicativo Gratuito](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Passos: Converter PDF para HTML em Python

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o documento PDF de origem.
1. Salve-o em [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) chamando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para HTML salvando imagens na pasta especificada

Esta função converte um arquivo PDF para o formato HTML usando Aspose.PDF para Python via .NET. Todas as imagens extraídas são armazenadas em uma pasta especificada em vez de serem incorporadas no arquivo HTML.

1. Configure as opções de salvamento HTML.
1. Salve como HTML com imagens externas.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_all_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para HTML multipágina

Esta função converte um arquivo PDF em HTML multipágina, onde cada página do PDF é exportada como um arquivo HTML separado. Isso torna a saída mais fácil de navegar e reduz o tempo de carregamento para PDFs grandes.

1. Carregue o PDF de origem usando 'ap.Document'.
1. Crie 'HtmlSaveOptions' e 'set split_into_pages'.
1. Salve o documento como HTML com páginas divididas em arquivos separados.
1. Imprima uma mensagem de confirmação.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para HTML salvando imagens SVG na pasta especificada

Esta função converte um PDF para o formato HTML armazenando todas as imagens como arquivos SVG em uma pasta especificada, em vez de incorporá‑las diretamente no HTML.

1. Carregue o PDF de origem usando 'ap.Document'.
1. Crie 'HtmlSaveOptions' e 'set special_folder_for_svg_images' para a pasta de destino.
1. Salve o documento como HTML com imagens SVG externas.
1. Imprima uma mensagem de confirmação.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para HTML e salvar imagens SVG compactadas

Este trecho converte um PDF para o formato HTML, armazenando todas as imagens como arquivos SVG em uma pasta especificada e comprimindo‑as para reduzir o tamanho do arquivo.

1. Carregue o documento PDF usando 'ap.Document'.
1. Crie 'HtmlSaveOptions' e:
- Defina 'special_folder_for_svg_images' para armazenar imagens SVG externamente.
- Ative 'compress_svg_graphics_if_any' para comprimir imagens SVG.
1. Salve o documento como HTML com imagens SVG externas comprimidas.
1. Imprima uma mensagem de confirmação.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.special_folder_for_svg_images = self.data_dir
    save_options.compress_svg_graphics_if_any = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para HTML com controle de Imagens Raster Incorporadas

Este trecho converte um PDF para o formato HTML, incorporando imagens raster como fundos de página PNG. Essa abordagem preserva a qualidade da imagem e o layout da página dentro do HTML.

1. Carregue o documento PDF usando 'ap.Document'.
1. Crie 'HtmlSaveOptions' e defina 'raster_images_saving_mode' como 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'.
1. Salve o documento como HTML com imagens raster incorporadas.
1. Imprima uma mensagem de confirmação.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.raster_images_saving_mode = apdf.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para página HTML contendo apenas o corpo

Esta função converte um PDF para formato HTML, gerando conteúdo 'apenas corpo' sem tags extras de 'html' ou 'head', e divide a saída em páginas separadas.

1. Carregue o documento PDF usando 'ap.Document'.
1. Crie 'HtmlSaveOptions' e configure:
- 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' para gerar apenas o conteúdo da 'body'.
- 'split_into_pages' para criar arquivos HTML separados para cada página do PDF.
1. Salve o documento como HTML com as opções especificadas.
1. Imprima uma mensagem de confirmação.

```python

from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.html_markup_generation_mode = apdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para HTML com Renderização de Texto Transparente

Esta função converte um PDF para formato HTML, renderizando todo o texto como transparente, incluindo textos com sombra, o que preserva a fidelidade visual ao permitir estilização flexível no HTML de saída.

1. Carregue o documento PDF usando 'ap.Document'.
1. Crie 'HtmlSaveOptions' e configure:
- 'save_transparent_texts' para renderizar texto normal como transparente.
- 'save_shadowed_texts_as_transparent_texts' para renderizar texto com sombra como transparente.
1. Salve o documento como HTML com renderização de texto transparente.
1. Imprima uma mensagem de confirmação.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Converter PDF para HTML com Renderização de Camadas de Documento

Esta função converte um PDF para formato HTML, preservando as camadas do documento ao converter conteúdo marcado em camadas separadas no HTML de saída. Isso permite que elementos em camadas (como anotações, fundos e sobreposições) sejam renderizados com precisão.

1. Carregue o documento PDF usando 'ap.Document'.
1. Crie 'HtmlSaveOptions' e habilite 'convert_marked_content_to_layers' para preservar as camadas.
1. Salve o documento como HTML com conteúdo em camadas.
1. Imprima uma mensagem de confirmação.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers  = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```


