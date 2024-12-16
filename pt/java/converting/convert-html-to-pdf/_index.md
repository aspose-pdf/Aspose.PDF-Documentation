---
title: Converter arquivo HTML para PDF em Java
linktitle: Converter arquivo HTML para PDF
type: docs
weight: 40
url: /pt/java/convert-html-to-pdf/
lastmod: "2021-11-19"
description: Este tópico mostra como o Aspose.PDF permite converter formatos HTML e MHTML para arquivo PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Visão Geral

Este artigo explica como converter HTML para PDF usando Java. O código é muito simples, basta carregar o HTML na classe Document e salvá-lo como um PDF de saída. Converter MHTML para PDF em Java também é semelhante. Ele abrange os seguintes tópicos:

- [Java HTML para PDF](#convert-html-to-pdf)
- [Java MHTML para PDF](#convert-mhtml-to-pdf)
- [Java Converter HTML para PDF](#convert-html-to-pdf)
- [Java Converter MHTML para PDF](#convert-mhtml-to-pdf)
- [Java PDF de HTML](#convert-html-to-pdf)
- [Java PDF de MHTML](#convert-mhtml-to-pdf)
- [Java HTML para PDF Converter - Como Converter Página da Web para PDF](#convert-html-to-pdf)

- [Java Biblioteca HTML para PDF, API ou Código para Renderizar, Salvar, Gerar ou Criar PDF Programaticamente a partir de HTML](#convert-html-to-pdf)

## Biblioteca Java para Conversão de HTML para PDF

**Aspose.PDF for Java** é uma API de manipulação de PDF que permite converter documentos HTML existentes para PDF de forma contínua. O processo de conversão de HTML para PDF pode ser personalizado de maneira flexível.

## Converter HTML para PDF

O exemplo de código Java a seguir mostra como converter um documento HTML para PDF.

1. Crie uma instância da classe [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. Inicialize o objeto [Document](https://reference.aspose.com/page/java/com.aspose.page/document).
1. Salve o documento PDF de saída chamando o método **Document.save(String)**.

```java
// Abra o documento PDF de origem
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// Instanciar objeto HTML SaveOptions
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// Salve o documento
document.save(DATA_DIR + "MultiPageHTML_out.html", htmlsaveOptions);
```

{{% alert color="success" %}}
**Tente converter HTML para PDF online**

A Aspose apresenta a você a aplicação online gratuita ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de HTML para PDF usando Aplicativo Gratuito](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf) {{% /alert %}}

## Conversão avançada de HTML para PDF

O mecanismo de conversão HTML possui várias opções que nos permitem controlar o processo de conversão.

### Suporte a Consultas de Mídia

1. Crie um [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) HTML.
1. Defina o modo Print ou Screen.
1. Inicialize o [objeto Document](<https://reference.aspose.com/page/java/com.aspose.page/document>).
1. Salve o documento PDF de saída.

Consultas de mídia são uma técnica popular para entregar uma folha de estilo personalizada para diferentes dispositivos. Podemos definir o tipo de dispositivo usando a propriedade [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType).

```java
// Crie um LoadOptions HTML
HtmlLoadOptions options = new HtmlLoadOptions();

// Defina o modo Print ou Screen
options.setHtmlMediaType(HtmlMediaType.Print);

// Inicialize o objeto documento
String htmlFileName = Paths.get(DATA_DIR.toString(), "test.html").toString();
Document document = new Document(htmlFileName, options);

// Salve o documento PDF de saída
document.save(Paths.get(DATA_DIR.toString(), "HTMLtoPDF.pdf").toString());
document.close();
```


### Ativar (desativar) incorporação de fontes

1. Adicione novas [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) Html.
1. Ative/Desative a incorporação de fontes.
1. Salve um novo Documento.

As páginas HTML frequentemente usam fontes (por exemplo, fontes de pasta local, Google Fonts, etc). Podemos também controlar a incorporação de fontes em um documento usando a propriedade [IsEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#isEmbedFonts--).

```java
HtmlLoadOptions options = new HtmlLoadOptions();
// Ativar/Desativar incorporação de fontes
options.setEmbedFonts(true);

Document document = new Document(DATA_DIR + "test_fonts.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();
```

### Gerenciar carregamento de recursos externos

O Motor de Conversão fornece um mecanismo que permite controlar o carregamento de certos recursos associados ao documento HTML.

A classe [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) possui a propriedade [CustomLoaderOfExternalResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#setCustomLoaderOfExternalResources-com.aspose.pdf.LoadOptions.ResourceLoadingStrategy-) com a qual podemos definir o comportamento do carregador de recursos.

```java
HtmlLoadOptions options = new HtmlLoadOptions();

options.setCustomLoaderOfExternalResources(
        new LoadOptions.ResourceLoadingStrategy() {
            public LoadOptions.ResourceLoadingResult invoke(String resourceURI) {
                // Criando recurso de modelo limpo para substituição:
                LoadOptions.ResourceLoadingResult res = new LoadOptions.ResourceLoadingResult(new byte[] {});
                // Retornar array de bytes vazio no caso do servidor i.imgur.com
                if (resourceURI.contains("i.imgur.com")) {
                    return res;
                } else {
                    // Processar recursos com carregador de recursos padrão
                    res.setLoadingCancelled(true);
                    return res;
                }
            }   
});

Document document = new Document(DATA_DIR + "test.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();    
```

## Converter MHTML para PDF

{{% alert color="success" %}}
**Tente converter MHTML para PDF online**


Aspose.PDF for Java apresenta a você o aplicativo online gratuito ["MHTML to PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF MHTML para PDF usando App Gratuito](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="Encapsulamento MIME de documentos HTML agregados">MHTML</abbr>, abreviação de MIME HTML, é um formato de arquivo de arquivo de página da web usado para combinar recursos que geralmente são representados por links externos (como imagens, animações Flash, applets Java e arquivos de áudio) com código HTML em um único arquivo. O conteúdo de um arquivo MHTML é codificado como se fosse uma mensagem de e-mail em HTML, usando o tipo MIME multipart/related.

O próximo trecho de código mostra como converter arquivos MHTML para o formato PDF com Java:

```java
// Crie uma instância de MhtLoadOptions para especificar as opções de carregamento para o
// arquivo MHTML.
MhtLoadOptions options = new MhtLoadOptions();

// Defina o caminho do arquivo MHTML.
String mhtmlFileName = Paths.get(DATA_DIR.toString(), "samplefile.mhtml").toString();

// Carregar o arquivo MHTML em um objeto Document.
Document document = new Document(mhtmlFileName, options);

// Salve o documento como um arquivo PDF.
document.save(Paths.get(DATA_DIR.toString(), "MarkdowntoPDF.pdf").toString());

// Feche o documento.
document.close();
```