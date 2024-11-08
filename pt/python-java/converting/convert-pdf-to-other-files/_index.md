---
title: Converter PDF para EPUB, LaTeX, Texto, XPS em Python
linktitle: Converter PDF para outros formatos
type: docs
weight: 90
url: /pt/python-java/convert-pdf-to-other-files/
lastmod: "2023-04-06"
keywords: converter, PDF, EPUB, LaText, Texto, XPS, Python
description: Este tópico mostra como converter um arquivo PDF para outros formatos de arquivo como EPUB, LaTeX, Texto, XPS etc usando Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Converter PDF para EPUB

{{% alert color="success" %}}
**Tente converter PDF para EPUB online**

Aspose.PDF para Python apresenta a você o aplicativo online gratuito ["PDF para EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Conversão PDF para EPUB com Aplicativo Gratuito](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Publicação Eletrônica">EPUB</abbr>** é um padrão de e-book livre e aberto do Fórum Internacional de Publicação Digital (IDPF).
 Arquivos têm a extensão .epub.  
EPUB é projetado para conteúdo redimensionável, o que significa que um leitor de EPUB pode otimizar o texto para um dispositivo de exibição específico. EPUB também suporta conteúdo com layout fixo. O formato é destinado como um formato único que editoras e casas de conversão podem usar internamente, bem como para distribuição e venda. Ele substitui o padrão Open eBook.

Aspose.PDF para Python também suporta o recurso de converter documentos PDF para o formato EPUB. O Aspose.PDF para Python tem uma classe chamada 'EpubSaveOptions' que pode ser usada como o segundo argumento para o método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods), para gerar um arquivo EPUB.  
Por favor, tente usar o seguinte trecho de código para cumprir esse requisito com Python.

```python

from asposepdf import Api

# inicializar licença
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# Converter para Epub
documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.epub"
doc.save(documentOutName, Api.SaveFormat.Epub)
```

## Converter PDF para LaTeX/TeX

**Aspose.PDF para Python via Java** suporta a conversão de PDF para LaTeX/TeX. O formato de arquivo LaTeX é um formato de arquivo de texto com a marcação especial e usado no sistema de preparação de documentos baseado em TeX para composição de alta qualidade.

{{% alert color="success" %}}
**Tente converter PDF para LaTeX/TeX online**

Aspose.PDF para Python apresenta a você o aplicativo online gratuito ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), onde você pode tentar investigar a funcionalidade e a qualidade com que trabalha.

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Para converter arquivos PDF para TeX, Aspose.PDF possui a classe [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/latexsaveoptions/) que fornece a propriedade OutDirectoryPath para salvar imagens temporárias durante o processo de conversão.

O snippet de código a seguir mostra o processo de conversão de arquivos PDF para o formato TEX com Python.

```python
from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.tex"
doc.save(documentOutName, Api.SaveFormat.TeX)
```

## Converter PDF para Texto

**Aspose.PDF para Python** suporta converter todo o documento PDF e página única para um arquivo de Texto.

### Converter documento PDF para arquivo de Texto

Você pode converter um documento PDF para um arquivo TXT usando a classe 'TextDevice'.

O seguinte trecho de código explica como extrair os textos de todas as páginas.

```python

from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_text"
# Abrir documento PDF
document = Api.Document(input_pdf)

device = Device.TextDevice()

for i in range(0, document.getPages.size):
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.txt"
    # Converter uma página específica e salvar como arquivo de texto
    device.process(document.getPages.getPage(i + 1), imageFileName)
```


{{% alert color="success" %}}

**Tente converter Converter PDF para Texto online**

Aspose.PDF para Python apresenta a você o aplicativo online gratuito ["PDF para Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), onde você pode tentar investigar a funcionalidade e qualidade com que funciona.

[![Aspose.PDF Conversão PDF para Texto com Aplicativo Gratuito](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Converter PDF para XPS

**Aspose.PDF para Python** oferece a possibilidade de converter arquivos PDF para o formato <abbr title="XML Paper Specification">XPS</abbr>. Vamos tentar usar o trecho de código apresentado para converter arquivos PDF para o formato XPS com Python.

{{% alert color="success" %}}
**Tente converter PDF para XPS online**

Aspose.PDF para Python apresenta a você o aplicativo online gratuito ["PDF para XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), onde você pode tentar investigar a funcionalidade e qualidade com que funciona.

[![Aspose.PDF Conversão PDF para XPS com Aplicativo Gratuito](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

O tipo de arquivo XPS está principalmente associado à Especificação de Documento XML pela Microsoft Corporation. A Especificação de Documento XML (XPS), anteriormente com o codinome Metro e subsumindo o conceito de marketing Next Generation Print Path (NGPP), é a iniciativa da Microsoft para integrar a criação e visualização de documentos no sistema operacional Windows.

Para converter arquivos PDF para XPS, o Aspose.PDF possui a classe [XpsSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/xpssaveoptions/) que é usada como o segundo argumento do método [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) para gerar o arquivo XPS.

O trecho de código a seguir mostra o processo de conversão de um arquivo PDF para o formato XPS.

```python

from asposepdf import Api

documentName = "../../testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "../../testout/out.xps"
doc.save(documentOutName, Api.SaveFormat.Xps)

```