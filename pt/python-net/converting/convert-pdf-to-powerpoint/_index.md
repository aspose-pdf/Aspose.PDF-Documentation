---
title: Converter PDF para PowerPoint em Python
linktitle: Converter PDF para PowerPoint
type: docs
weight: 30
url: /pt/python-net/convert-pdf-to-powerpoint/
description: Aspose.PDF permite converter PDF para o formato PPT (PowerPoint) usando Python. Uma forma é a possibilidade de converter PDF para PPTX com Slides como Imagens.
lastmod: "2022-12-23"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Visão Geral

É possível converter um arquivo PDF em um PowerPoint? Sim, você pode! E é fácil!
Este artigo explica como **converter PDF para PowerPoint usando Python**. Ele cobre estes tópicos.

_Formato_: **PPTX**
- [Python PDF para PPTX](#python-pdf-to-pptx)
- [Python Converter PDF para PPTX](#python-pdf-to-pptx)
- [Python Como converter arquivo PDF para PPTX](#python-pdf-to-pptx)

_Formato_: **PowerPoint**
- [Python PDF para PowerPoint](#python-pdf-to-powerpoint)
- [Python Converter PDF para PowerPoint](#python-pdf-to-powerpoint)
- [Python Como converter arquivo PDF para PowerPoint](#python-pdf-to-powerpoint)


## Conversão de PDF para PowerPoint e PPTX em Python

**Aspose.PDF for Python via .NET** permite acompanhar o progresso da conversão de PDF para PPTX.

Temos uma API chamada Aspose.Slides que oferece a funcionalidade de criar e manipular apresentações PPT/PPTX. Esta API também fornece a funcionalidade de converter arquivos PPT/PPTX para o formato PDF. Durante essa conversão, as páginas individuais do arquivo PDF são convertidas em slides separados no arquivo PPTX.

Durante a conversão de PDF para <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, o texto é renderizado como Texto onde você pode selecioná-lo/atualizá-lo. Por favor, note que para converter arquivos PDF para o formato PPTX, o Aspose.PDF fornece uma classe chamada [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). Um objeto da classe PptxSaveOptions é passado como segundo argumento para o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods). O trecho de código a seguir mostra o processo para converter arquivos PDF em formato PPTX.

## Conversão simples de PDF para PowerPoint usando Python e Aspose.PDF para Python

Para converter PDF para PPTX, o Aspose.PDF para Python aconselha a usar os seguintes passos de código.

<a name="csharp-pdf-to-powerpoint"><strong>Passos: Converter PDF para PowerPoint em Python</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Passos: Converter PDF para PPTX em Python</strong></a>

1. Crie uma instância da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
2. Crie uma instância da classe [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/)
3. Use o método **Save** do objeto **Document** para salvar o PDF como PPTX

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx.pptx"
    # Abrir documento PDF
    document = ap.Document(input_pdf)
    # Instanciar a instância de PptxSaveOptions
    save_option = ap.PptxSaveOptions()
    # Salvar o arquivo no formato MS PowerPoint
    document.save(output_pdf, save_option)
```

## Converter PDF para PPTX com Slides como Imagens


{{% alert color="success" %}}
**Tente converter PDF para PowerPoint online**

Aspose.PDF para Python apresenta a você o aplicativo online gratuito ["PDF para PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para PPTX com Aplicativo Gratuito](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Caso você precise converter um PDF pesquisável para PPTX como imagens em vez de texto selecionável, o Aspose.PDF oferece esse recurso por meio da classe [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). Para conseguir isso, defina a propriedade [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) da classe [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) como 'true', conforme mostrado no exemplo de código a seguir.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_pptx_with_slides_as_images.pptx"
    # Abrir documento PDF
    documento = ap.Document(input_pdf)
    # Instanciar instância de PptxSaveOptions
    save_option = ap.PptxSaveOptions()
    save_option.slides_as_images = True
    # Salvar o arquivo no formato MS PowerPoint
    documento.save(output_pdf, save_option)
```


## Veja Também

Este artigo também aborda estes tópicos. Os códigos são os mesmos que acima.

_Formato_: **PowerPoint**
- [Código Python PDF para PowerPoint](#python-pdf-to-powerpoint)
- [API Python PDF para PowerPoint](#python-pdf-to-powerpoint)
- [Python PDF para PowerPoint Programaticamente](#python-pdf-to-powerpoint)
- [Biblioteca Python PDF para PowerPoint](#python-pdf-to-powerpoint)
- [Python Salvar PDF como PowerPoint](#python-pdf-to-powerpoint)
- [Python Gerar PowerPoint a partir de PDF](#python-pdf-to-powerpoint)
- [Python Criar PowerPoint a partir de PDF](#python-pdf-to-powerpoint)
- [Conversor Python PDF para PowerPoint](#python-pdf-to-powerpoint)

_Formato_: **PPTX**
- [Código Python PDF para PPTX](#python-pdf-to-pptx)
- [API Python PDF para PPTX](#python-pdf-to-pptx)
- [Python PDF para PPTX Programaticamente](#python-pdf-to-pptx)
- [Biblioteca Python PDF para PPTX](#python-pdf-to-pptx)
- [Python Salvar PDF como PPTX](#python-pdf-to-pptx)
- [Python Gerar PPTX a partir de PDF](#python-pdf-to-pptx)
- [Python Criar PPTX a partir de PDF](#python-pdf-to-pptx)

- [Conversor Python PDF para PPTX](#python-pdf-to-pptx)