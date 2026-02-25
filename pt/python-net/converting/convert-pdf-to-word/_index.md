---
title: Converter PDF para documentos Microsoft Word em Python
linktitle: Converter PDF para Word
type: docs
weight: 10
url: /pt/python-net/convert-pdf-to-word/
lastmod: "2025-09-27"
description: Aprenda como converter documentos PDF para o formato Word em Python usando Aspose.PDF para fácil edição de documentos.
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como converter PDF para Word em Python
Abstract: Este artigo fornece um guia abrangente sobre como converter arquivos PDF para formatos Microsoft Word (DOC e DOCX) usando Python, especificamente utilizando a biblioteca Aspose.PDF. Ele descreve as vantagens de converter PDFs em documentos Word editáveis, permitindo uma manipulação de conteúdo mais fácil, como texto, tabelas e imagens. O artigo detalha o processo de conversão de PDF para DOC (formato Word 97-2003) e DOCX, com trechos de código demonstrando essas conversões em Python. O processo envolve a criação de um objeto `Document` a partir do PDF e sua gravação no formato desejado usando o método `save()` e a enumeração `SaveFormat`. Além disso, apresenta a classe `DocSaveOptions`, que permite maior personalização do processo de conversão, como a especificação de modos de reconhecimento. O artigo também destaca aplicações online fornecidas pelo Aspose.PDF para testar a qualidade e a funcionalidade da conversão. O conteúdo inclui uma visão estruturada e links para as seções correspondentes a cada formato.
---

## Converter PDF para DOC

Uma das funcionalidades mais populares é a conversão de PDF para DOC do Microsoft Word, que facilita o gerenciamento de conteúdo. **Aspose.PDF for Python via .NET** permite converter arquivos PDF não apenas para DOC, mas também para formato DOCX, de maneira fácil e eficiente.

A classe [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) fornece diversas propriedades que aprimoram o processo de conversão de arquivos PDF para o formato DOC. Entre essas propriedades, Mode permite especificar o modo de reconhecimento para o conteúdo PDF. Você pode especificar qualquer valor da enumeração RecognitionMode para esta propriedade. Cada um desses valores tem benefícios e limitações específicas:

Etapas: Converter PDF para DOC em Python

1. Carregue o PDF em um objeto 'ap.Document'.
1. Crie uma instância de 'DocSaveOptions'.
1. Defina a propriedade format como 'DocFormat.DOC' para garantir que a saída esteja no formato .doc (formato Word antigo).
1. Salve o PDF como um documento Word usando as opções de salvamento especificadas.
1. Exiba uma mensagem de confirmação.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Tente converter PDF para DOC online**

Aspose.PDF for Python apresenta a você um aplicativo online gratuito ["PDF para DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), onde você pode experimentar a funcionalidade e a qualidade que ele oferece.

[![Converter PDF para DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Converter PDF para DOCX

A API Aspose.PDF for Python permite ler e converter documentos PDF para DOCX usando Python via .NET. DOCX é um formato conhecido para documentos Microsoft Word cujo estrutura foi alterada de binário puro para uma combinação de arquivos XML e binários. Arquivos docx podem ser abertos com o Word 2007 e versões posteriores, mas não com as versões mais antigas do MS Word que suportam extensões de arquivo DOC.

O trecho de código Python a seguir mostra o processo de conversão de um arquivo PDF para o formato DOCX.

Etapas: Converter PDF para DOCX em Python

1. Carregue o PDF de origem usando 'ap.Document'.
1. Crie uma instância de 'DocSaveOptions'.
1. Defina a propriedade format como 'DocFormat.DOC_X' para gerar um arquivo .docx (formato Word moderno).
1. Salve o PDF como um arquivo DOCX com as opções de salvamento configuradas.
1. Exiba uma mensagem de confirmação após a conversão.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC_X
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

A classe [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) possui uma propriedade chamada Format que permite especificar o formato do documento resultante, ou seja, DOC ou DOCX. Para converter um arquivo PDF para o formato DOCX, forneça o valor Docx da enumeração DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Tente converter PDF para DOCX online**

Aspose.PDF for Python apresenta a você um aplicativo online gratuito ["PDF para Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), onde você pode experimentar a funcionalidade e a qualidade que ele oferece.

[![Conversão Aspose.PDF PDF para Word - App Gratuito](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

