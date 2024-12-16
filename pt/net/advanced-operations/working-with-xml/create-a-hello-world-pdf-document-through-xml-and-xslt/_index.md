---
title: Criando PDF a partir de XML usando XSLT
linktitle: Criar PDF a partir de XML usando XSLT
type: docs
weight: 10
url: /pt/net/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: Biblioteca C# fornece a capacidade de converter um arquivo XML em documento PDF, exigindo que o arquivo XML de entrada siga o Esquema Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Criando PDF a partir de XML usando XSLT",
    "alternativeHeadline": "Como criar PDF a partir de XML usando XSLT",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, c#, criar pdf xml, pdf com xslt",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/create-a-hello-world-pdf-document-through-xml-and-xslt/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-a-hello-world-pdf-document-through-xml-and-xslt/"
    },
    "dateModified": "2022-02-04",
    "description": "Biblioteca C# fornece a capacidade de converter um arquivo XML em documento PDF, exigindo que o arquivo XML de entrada siga o Esquema Aspose.PDF."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

Às vezes, você pode ter arquivos XML existentes que contêm dados de aplicativos e deseja gerar um relatório PDF usando esses arquivos. Você pode usar XSLT para transformar seu documento XML existente em um documento XML compatível com Aspose.Pdf e, em seguida, gerar um arquivo PDF. Existem 3 etapas para gerar PDF usando XML e XSLT.

Por favor, siga estas etapas para converter um arquivo XML em um documento PDF usando XSLT:

* Crie uma instância da classe PDF que representa um documento PDF
* Se você comprou uma licença, deve também incorporar o código para usar essa licença com a ajuda da classe License no namespace Aspose.Pdf
* Vincule os arquivos XML e XSLT de entrada à instância da classe PDF chamando seu método BindXML
* Salve o XML vinculado com a instância PDF como um documento PDF

## Arquivo XML de Entrada

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Hello World!</Content>
</Contents>
```

## Arquivo XSLT de Entrada

```xml
<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="text()"/>
    <xsl:template match="/Contents">
    <html>
      <Document xmlns="Aspose.Pdf" IsAutoHyphenated="false">
        <PageInfo>
          <DefaultTextState
                            Font = "Helvetica" FontSize="8" LineSpacing="4"/>
          <Margin Left="5cm" Right="5cm" Top="3cm" Bottom="15cm" />
        </PageInfo>
        <Page id="mainSection">
          <TextFragment>
            <TextSegment>
              <xsl:value-of select="Content"/>
            </TextSegment>
          </TextFragment>
        </Page>
      </Document>
    </html>
</xsl:template>
</xsl:stylesheet>
```
{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Working-Document-HelloWorldPDFUsingXmlAndXslt-HelloWorldPDFUsingXmlAndXslt.cs" >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

---
id: start
title: Introdução
sidebar_label: Introdução
slug: /
---

## Bem-vindo

Bem-vindo à documentação do nosso projeto. Este documento fornecerá uma visão geral do projeto e como você pode começar a usá-lo.

## Visão Geral

Nosso projeto é uma poderosa ferramenta que permite aos desenvolvedores criar aplicações de forma rápida e eficiente. Ele vem com uma variedade de recursos que facilitam o desenvolvimento e a manutenção do código.

## Primeiros Passos

Para começar, siga estas etapas:

1. Clone o repositório para sua máquina local.
2. Instale as dependências necessárias usando `npm install`.
3. Inicie o servidor de desenvolvimento com `npm start`.

## Estrutura do Projeto

Nosso projeto possui a seguinte estrutura de diretórios:

- `src/`: Contém o código-fonte da aplicação.
- `public/`: Contém arquivos públicos, como HTML e imagens.
- `config/`: Contém arquivos de configuração.

## Recursos

Aqui estão alguns dos principais recursos do nosso projeto:

- **Desenvolvimento Rápido**: Ferramentas e bibliotecas que aceleram o processo de desenvolvimento.
- **Manutenção Fácil**: Código modular e bem documentado que facilita a manutenção.
- **Alta Performance**: Otimizações para garantir que a aplicação seja rápida e responsiva.

```json
{
  "changefreq": "monthly"
}
```

## Contribuindo

Se você quiser contribuir para o projeto, siga estas diretrizes:

1. Faça um fork do repositório.
2. Crie um branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adicione nova feature'`).
4. Push para o branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

```json
{
  "type": "docs"
}
```

## Suporte

Se você encontrar algum problema ou tiver alguma dúvida, por favor, abra uma issue no GitHub. Nossa equipe estará feliz em ajudar.

Obrigado por usar nosso projeto! Esperamos que ele facilite seu trabalho e ajude você a criar ótimas aplicações.
```
