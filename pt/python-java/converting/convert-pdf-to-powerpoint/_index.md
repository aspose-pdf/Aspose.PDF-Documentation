---
title: Converter PDF para PowerPoint em Python
linktitle: Converter PDF para PowerPoint
type: docs
weight: 30
url: pt/python-java/convert-pdf-to-powerpoint/
description: Aspose.PDF permite que você converta PDF para o formato PPT (PowerPoint) usando Python. Uma maneira é converter PDF para PPTX com Slides como Imagens.
lastmod: "2023-04-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Visão Geral

É possível converter um arquivo PDF em um PowerPoint? Sim, você pode! E é fácil!
Este artigo explica como **converter PDF para PowerPoint usando Python**. Ele abrange os seguintes tópicos.

_Formato_: **PPTX**
- [Python PDF para PPTX](#python-pdf-to-pptx)
- [Python Converter PDF para PPTX](#python-pdf-to-pptx)
- [Python Como converter arquivo PDF para PPTX](#python-pdf-to-pptx)

_Formato_: **PowerPoint**
- [Python PDF para PowerPoint](#python-pdf-to-powerpoint)
- [Python Converter PDF para PowerPoint](#python-pdf-to-powerpoint)
- [Python Como converter arquivo PDF para PowerPoint](#python-pdf-to-powerpoint)


## Conversão de PDF para PowerPoint e PPTX em Python

**Aspose.PDF for Python via Java** permite acompanhar o progresso da conversão de PDF para PPTX.

Temos uma API chamada Aspose.Slides que oferece o recurso de criar e manipular apresentações PPT/PPTX. Esta API também fornece o recurso de converter arquivos PPT/PPTX para o formato PDF. Durante essa conversão, as páginas individuais do arquivo PDF são convertidas em slides separados no arquivo PPTX.

Durante a conversão de PDF para <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, o texto é renderizado como Texto, onde você pode selecioná-lo/atualizá-lo. Observe que, para converter arquivos PDF para o formato PPTX, Aspose.PDF fornece uma classe chamada [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions). Um objeto da classe PptxSaveOptions é passado como segundo argumento para o [`Document.Save(..) method`](https://reference.aspose.com/pdf/java/aspose.pdf/document/methods/save). O trecho de código a seguir mostra o processo de conversão de arquivos PDF para o formato PPTX.

## Conversão simples de PDF para PowerPoint usando Python e Aspose.PDF for Python

Para converter PDF para PPTX, o Aspose.PDF para Python aconselha a usar os seguintes passos de código.

<a name="csharp-pdf-to-powerpoint"><strong>Passos: Converter PDF para PowerPoint em Python</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Passos: Converter PDF para PPTX em Python</strong></a>

1. Crie uma instância da classe [Document](https://reference.aspose.com/pdf/java/aspose.pdf/document)
2. Crie uma instância da classe [PptxSaveOptions](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions)
3. Use o método **Save** do objeto **Document** para salvar o PDF como PPTX

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# Abrir documento PDF
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SeparateImages = True
save_options._OptimizeTextBoxes = True

# Salvar o arquivo no formato de documento do MS Word
document.save(output_pdf, save_options)
```


## Converter PDF para PPTX com Slides como Imagens

{{% alert color="success" %}}
**Tente converter PDF para PowerPoint online**

Aspose.PDF para Python apresenta a você o aplicativo online gratuito ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), onde você pode explorar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Caso você precise converter um PDF pesquisável em PPTX como imagens em vez de texto selecionável, Aspose.PDF fornece esse recurso através da classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/). Para conseguir isso, defina a propriedade [SlidesAsImages](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/#properties) da classe [PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/) como 'true', conforme mostrado no exemplo de código a seguir.

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# Abrir documento PDF
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SlidesAsImages = True

# Salvar o arquivo no formato de documento MS Word
document.save(output_pdf, save_options)
```


## Veja Também

Este artigo também cobre esses tópicos. Os códigos são os mesmos que acima.

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