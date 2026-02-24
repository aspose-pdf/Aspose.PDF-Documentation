---
title: Converter PDF para EPUB, LaTeX, Texto, XPS em Python
linktitle: Converter PDF para outros formatos
type: docs
weight: 90
url: /pt/python-net/convert-pdf-to-other-files/
lastmod: "2025-09-27"
description: Este tópico mostra como converter um arquivo PDF para outros formatos de arquivo, como EPUB, LaTeX, Texto, XPS etc., usando Python.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como Converter PDF para outros formatos em Python
Abstract: O artigo fornece um guia abrangente sobre a conversão de arquivos PDF em vários formatos usando Aspose.PDF para Python. Ele cobre a conversão de PDFs em formatos EPUB, LaTeX/TeX, Texto, XPS e XML. Cada seção começa com um convite para experimentar aplicativos gratuitos online fornecidos pela Aspose para converter PDFs nos respectivos formatos, destacando a facilidade de uso e a qualidade dessas ferramentas.
---

## Converter PDF para EPUB

{{% alert color=\"success\" %}}
**Experimente converter PDF para EPUB online**

Aspose.PDF for Python apresenta a você um aplicativo gratuito online ["PDF para EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), onde você pode experimentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF PDF para EPUB com App Gratuito](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title=\"Electronic Publication\">EPUB</abbr> é um padrão de e‑book livre e aberto do International Digital Publishing Forum (IDPF). Arquivos têm a extensão .epub.
EPUB foi projetado para conteúdo refluível, o que significa que um leitor EPUB pode otimizar o texto para um determinado dispositivo de exibição. EPUB também suporta conteúdo de layout fixo. O formato destina‑se a ser um formato único que editores e casas de conversão podem usar internamente, bem como para distribuição e venda. Ele substitui o padrão Open eBook.

Aspose.PDF for Python também oferece o recurso de converter documentos PDF para o formato EPUB. Aspose.PDF for Python possui uma classe chamada 'EpubSaveOptions' que pode ser usada como segundo argumento para o método [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods), para gerar um arquivo EPUB.
Por favor, experimente usar o trecho de código a seguir para atender a este requisito com Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = (
        ap.EpubSaveOptions.RecognitionMode.FLOW
    )
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Converter PDF para LaTeX/TeX

**Aspose.PDF for Python via .NET** suporta a conversão de PDF para LaTeX/TeX.
O formato de arquivo LaTeX é um formato de texto com marcação especial e usado em sistemas de preparação de documentos baseados em TeX para tipografia de alta qualidade.

{{% alert color=\"success\" %}}
**Experimente converter PDF para LaTeX/TeX online**

Aspose.PDF for Python apresenta a você um aplicativo gratuito online ["PDF para LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), onde você pode experimentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF PDF para LaTeX/TeX com App Gratuito](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Para converter arquivos PDF para TeX, Aspose.PDF tem a classe [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) que fornece a propriedade OutDirectoryPath para salvar imagens temporárias durante o processo de conversão.

O trecho de código a seguir mostra o processo de conversão de arquivos PDF para o formato TEX com Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.LaTeXSaveOptions()

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## Converter PDF para Texto

**Aspose.PDF for Python** suporta a conversão de documento PDF completo e de página única para um arquivo de Texto. Você pode converter um documento PDF para um arquivo TXT usando a classe 'TextDevice'. O trecho de código a seguir explica como extrair o texto de todas as páginas.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color=\"success\" %}}
**Experimente converter PDF para Texto online**

Aspose.PDF for Python apresenta a você um aplicativo gratuito online ["PDF para Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), onde você pode experimentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF PDF para Texto com App Gratuito](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Converter PDF para XPS

**Aspose.PDF for Python** oferece a possibilidade de converter arquivos PDF para o formato XPS. Vamos tentar usar o trecho de código apresentado para converter arquivos PDF para o formato XPS com Python.

{{% alert color=\"success\" %}}
**Experimente converter PDF para XPS online**

Aspose.PDF for Python apresenta a você um aplicativo gratuito online ["PDF para XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), onde você pode experimentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF PDF para XPS com App Gratuito](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

O tipo de arquivo XPS está principalmente associado ao XML Paper Specification da Microsoft Corporation. O XML Paper Specification (XPS), anteriormente chamado de código Metro e que abrange o conceito de marketing Next Generation Print Path (NGPP), é a iniciativa da Microsoft para integrar a criação e visualização de documentos ao sistema operacional Windows.

Para converter arquivos PDF para XPS, Aspose.PDF tem a classe [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) que é usada como segundo argumento para o método [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) para gerar o arquivo XPS.

O trecho de código a seguir mostra o processo de conversão de arquivo PDF para o formato XPS.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Converter PDF para MD

O Aspose.PDF possui a classe 'MarkdownSaveOptions()', que converte um documento PDF para o formato Markdown (MD) enquanto preserva imagens e recursos.

1. Carregue o PDF fonte usando 'ap.Document'.
1. Crie uma instância de 'MarkdownSaveOptions'.
1. Defina 'resources_directory_name' como 'images' – as imagens extraídas serão armazenadas nesta pasta.
1. Salve o documento Markdown convertido usando as opções configuradas.
1. Imprima uma mensagem de confirmação após a conversão.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.MarkdownSaveOptions()
    # save_options.extract_vector_graphics = True
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

Um arquivo Markdown com texto e imagens vinculadas armazenadas na pasta de imagens especificada.

## Converter PDF para MobiXML

Este método converte um documento PDF para o formato MOBI (MobiXML), que é comumente usado para eBooks em dispositivos Kindle.

1. Carregue o documento PDF fonte usando 'ap.Document'.
1. Salve o documento com o formato 'ap.SaveFormat.MOBI_XML'.
1. Imprima uma mensagem de confirmação quando a conversão estiver concluída.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.save(path_outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
