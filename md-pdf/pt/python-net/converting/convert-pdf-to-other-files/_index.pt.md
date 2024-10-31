---
title: Converter PDF para EPUB, LaTeX, Texto, XPS em Python
linktitle: Converter PDF para outros formatos
type: docs
weight: 90
url: /python-net/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: converter, PDF, EPUB, LaText, Texto, XPS, Python
description: Este tópico mostra como converter um arquivo PDF para outros formatos de arquivo como EPUB, LaTeX, Texto, XPS etc usando Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Converter PDF para EPUB

{{% alert color="success" %}}
**Tente converter PDF para EPUB online**

Aspose.PDF para Python apresenta um aplicativo online gratuito ["PDF para EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF PDF para EPUB com App Gratuito](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Publicação Eletrônica">EPUB</abbr>** é um padrão de e-book livre e aberto do Fórum Internacional de Publicação Digital (IDPF).
 Arquivos têm a extensão .epub.  
EPUB é projetado para conteúdo redimensionável, o que significa que um leitor de EPUB pode otimizar o texto para um dispositivo de exibição específico. EPUB também suporta conteúdo de layout fixo. O formato é destinado como um formato único que editoras e casas de conversão podem usar internamente, bem como para distribuição e venda. Ele substitui o padrão Open eBook.

Aspose.PDF para Python também suporta o recurso de converter documentos PDF para o formato EPUB. Aspose.PDF para Python possui uma classe chamada 'EpubSaveOptions' que pode ser usada como o segundo argumento para o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods), para gerar um arquivo EPUB.  
Por favor, tente usar o seguinte trecho de código para cumprir este requisito com Python.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_epub.epub"
    # Abrir documento PDF
    document = ap.Document(input_pdf)

    # Instanciar opções de salvamento Epub
    save_options = ap.EpubSaveOptions()

    # Especificar o layout para conteúdos
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW

    # Salvar o documento ePUB
    document.save(output_pdf, save_options)
```

## Converter PDF para LaTeX/TeX

**Aspose.PDF para Python via .NET** suporta a conversão de PDF para LaTeX/TeX. O formato de arquivo LaTeX é um formato de arquivo de texto com marcação especial e usado no sistema de preparação de documentos baseado em TeX para composição tipográfica de alta qualidade.

{{% alert color="success" %}}
**Tente converter PDF para LaTeX/TeX online**

Aspose.PDF para Python apresenta-lhe a aplicação online gratuita ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para LaTeX/TeX com App Gratuito](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Para converter arquivos PDF para TeX, o Aspose.PDF tem a classe [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) que fornece a propriedade OutDirectoryPath para salvar imagens temporárias durante o processo de conversão.

O trecho de código a seguir mostra o processo de conversão de arquivos PDF para o formato TEX com Python.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_tex.tex"
    # Abrir documento PDF
    document = ap.Document(input_pdf)
    # Instanciar um objeto de LaTeXSaveOptions
    saveOptions = ap.LaTeXSaveOptions()
    document.save(output_pdf, saveOptions)
```

## Converter PDF para Texto

**Aspose.PDF para Python** suporta a conversão de todo o documento PDF e de uma única página para um arquivo de texto.

### Converter documento PDF para arquivo de texto

Você pode converter o documento PDF para um arquivo TXT usando a classe 'TextDevice'.

O trecho de código a seguir explica como extrair os textos de todas as páginas.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"
    # Abrir documento PDF
    document = ap.Document(input_pdf)

    # Criar dispositivo de texto
    textDevice = ap.devices.TextDevice()

    # Converter uma página específica e salvar
    textDevice.process(document.pages[1], output_pdf)
`
**Tente converter PDF para Texto online**

Aspose.PDF para Python apresenta a você o aplicativo online gratuito ["PDF para Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), onde você pode tentar investigar a funcionalidade e qualidade com que ele funciona.

[![Aspose.PDF Conversão PDF para Texto com Aplicativo Gratuito](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Converter PDF para XPS

**Aspose.PDF para Python** oferece a possibilidade de converter arquivos PDF para o formato <abbr title="XML Paper Specification">XPS</abbr>. Vamos tentar usar o trecho de código apresentado para converter arquivos PDF para o formato XPS com Python.

{{% alert color="success" %}}
**Tente converter PDF para XPS online**

Aspose.PDF para Python apresenta a você o aplicativo online gratuito ["PDF para XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), onde você pode tentar investigar a funcionalidade e qualidade com que ele funciona.

[![Aspose.PDF Conversão PDF para XPS com Aplicativo Gratuito](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

O tipo de arquivo XPS está principalmente associado à Especificação de Papel XML pela Microsoft Corporation. A Especificação de Papel XML (XPS), anteriormente codinomeada Metro e englobando o conceito de marketing Next Generation Print Path (NGPP), é a iniciativa da Microsoft para integrar a criação e visualização de documentos no sistema operacional Windows.

Para converter arquivos PDF para XPS, Aspose.PDF possui a classe [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) que é usada como o segundo argumento para o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) para gerar o arquivo XPS.

O trecho de código a seguir mostra o processo de conversão de um arquivo PDF para o formato XPS.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xps.xps"
    # Abrir documento PDF
    document = ap.Document(input_pdf)

    # Instanciar opções de salvamento XPS
    save_options = ap.XpsSaveOptions()

    # Salvar o documento XPS
    document.save(output_pdf, save_options)
```

## Converter PDF para XML

{{% alert color="success" %}}
**Tente converter PDF para XML online**

Aspose.PDF para Python apresenta a você o aplicativo online gratuito ["PDF to XML"](https://products.aspose.app/pdf/conversion/pdf-to-xml), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Conversão PDF para XML com Aplicativo Gratuito](pdf_to_xml.png)](https://products.aspose.app/pdf/conversion/pdf-to-xml)
{{% /alert %}}

<abbr title="Extensible Markup Language">XML</abbr> é uma linguagem de marcação e formato de arquivo para armazenar, transmitir e reconstruir dados arbitrários.

Aspose.PDF para Python também suporta o recurso de converter documentos PDF para o formato XML. Aspose.PDF para Python tem uma classe chamada 'XmlSaveOptions' que pode ser usada como o segundo argumento no método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) para gerar um arquivo XML. Por favor, tente usar o seguinte trecho de código para realizar este requisito com Python.

```python

    import aspose.pdf as ap

    def convert_pdf_to_xml(self, infile, outfile):
        path_infile = self.dataDir + infile
        path_outfile = self.dataDir + outfile

        # Abrir documento PDF

        document = ap.Document(path_infile)

        # Instanciar opções de salvamento XML
        save_options = ap.XmlSaveOptions()

        # Salvar o documento XML
        document.save(path_outfile, save_options)
        print(infile + " convertido em " + outfile)
```