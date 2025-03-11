---
title: Módulo de Importação de PDF do Umbraco
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/umbraco-pdf-import-module/
description: Aprenda como instalar e usar o Módulo de Importação de PDF do Umbraco
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Umbraco PDF Import Module",
    "alternativeHeadline": "Umbraco Module Simplifies PDF Content Import Process",
    "abstract": "O Módulo de Importação de PDF do Umbraco permite que os desenvolvedores importem conteúdo PDF em seus sites Umbraco sem a necessidade de software adicional. Este poderoso complemento de código aberto simplifica o manuseio de documentos, fornecendo uma interface amigável para buscar e exibir conteúdos PDF instantaneamente, aumentando a eficiência da gestão de conteúdo em aplicações .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "950",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/umbraco-pdf-import-module/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/umbraco-pdf-import-module/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Introdução

**Aspose.PDF for .NET** é um componente de criação e manipulação de documentos PDF que permite que suas aplicações .NET leiam, escrevam e manipulem documentos PDF existentes sem usar o Adobe Acrobat. Ele também permite que você crie formulários e gerencie campos de formulário incorporados em um documento PDF.

**Aspose.PDF for .NET** é acessível e oferece uma incrível variedade de recursos, incluindo opções de compressão de PDF; criação e manipulação de tabelas; suporte para objetos gráficos; funcionalidade extensa de hyperlinks; controles de segurança avançados; manipulação de fontes personalizadas; integração com fontes de dados; adicionar ou remover marcadores; criar índice; adicionar, atualizar, excluir anexos e anotações; importar ou exportar dados de formulários PDF; adicionar, substituir ou remover texto e imagens; dividir, concatenar, extrair ou inserir páginas; transformar páginas em imagem; imprimir documentos PDF e muito mais.

### **Recursos do Módulo**

A Importação de PDF do Umbraco é um complemento de código aberto da [Aspose](http://www.aspose.com/) que permite que os desenvolvedores obtenham/leiam conteúdos de qualquer documento PDF sem exigir nenhum outro software. Este complemento demonstra o poderoso recurso de importação fornecido pelo [Aspose.PDF](https://products.aspose.com/pdf/net/). Ele adiciona um controle simples de navegador de arquivos e um botão **Importar do PDF** na página onde o complemento é adicionado. Ao clicar no botão, o conteúdo do documento é buscado do arquivo e exibido na tela imediatamente.

## Requisitos do Sistema e Plataformas Suportadas

### **Requisitos do Sistema**

Para configurar o módulo Aspose .NET Pdf Import para Umbraco, você precisa atender aos seguintes requisitos:

- Umbraco 6.0+.

Sinta-se à vontade para nos contatar se desejar instalar este módulo em outras versões do Umbraco.

### **Plataformas Suportadas**

O módulo é suportado em todas as versões de

- Umbraco rodando em ASP.NET 4.0.

## Download

Você pode baixar o Aspose .NET Pdf Import para Umbraco de um dos seguintes locais

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/releases).
- [Sourceforge](https://sourceforge.net/projects/asposeumbraco/files/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/downloads).
- [Umbraco](https://our.umbraco.com/packages/developer-tools/import-from-pdf-using-asposepdf/).

## Instalando

Uma vez baixado, siga estas etapas para instalar este pacote em seu site Umbraco:

1. Faça login na seção **Desenvolvedor** do Umbraco, por exemplo <http://www.myblog.com/umbraco/>.
1. No menu, expanda a pasta **Pacotes**.
   A partir daqui, há duas maneiras de instalar um pacote: selecione **Instalar pacote local** ou navegue pelo **Repositório de Pacotes do Umbraco.**.
1. Se você instalar **pacote local**, não descompacte o pacote, mas carregue o zip no Umbraco.
1. Siga as instruções na tela.

**Nota:** Você pode receber um erro de ‘Comprimento máximo da solicitação excedido’ ao instalar. Você pode corrigir facilmente esse problema atualizando o valor de ‘maxRequestLength’ no seu arquivo web.config do Umbraco.

```xml
  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
```

## Usando

Depois de instalar o macro, é muito simples começar a usá-lo em seu site:

1. Certifique-se de que você está logado na seção **Desenvolvedor** do Umbraco, por exemplo <http://www.myblog.com/umbraco/>.
1. Clique em **Configurações** na lista de seções no canto inferior esquerdo da tela.
1. Expanda o nó **Templates** e selecione o template ao qual você deseja adicionar o macro, por exemplo, Postagem de Blog.
1. Selecione a posição no template selecionado onde você deseja o botão.
1. Clique em **Inserir Macro** na faixa superior.
1. Em **Escolher um macro**, selecione o macro instalado e clique em **OK**.

Você adicionou com sucesso o template. Um botão intitulado **Importar do PDF** agora aparece em todas as páginas criadas usando este template. Qualquer pessoa pode simplesmente clicar no botão e importar o conteúdo de um documento PDF.

## Demonstração em Vídeo

Por favor, confira [o vídeo](https://www.youtube.com/watch?v=zmZTJ86B25E) abaixo para ver o módulo em ação.

## Suporte, Extensão e Contribuição

### Suporte

Desde os primeiros dias da Aspose, sabíamos que apenas oferecer bons produtos aos nossos clientes não seria suficiente. Também precisávamos fornecer um bom serviço. Nós somos desenvolvedores e entendemos como é frustrante quando um problema técnico ou uma peculiaridade no software impede que você faça o que precisa. Estamos aqui para resolver problemas, não para criá-los.

É por isso que oferecemos suporte gratuito. Qualquer pessoa que use nosso produto, seja comprando ou usando uma avaliação, merece nossa total atenção e respeito.

Você pode registrar quaisquer problemas ou sugestões relacionadas aos Módulos Aspose.PDF .NET para Umbraco usando qualquer uma das seguintes plataformas:

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/issues).
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/tickets/?source=navbar).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/issues?status=new&status=open).

### Estender e Contribuir

Aspose .NET PDF Import para Umbraco é de código aberto e seu código-fonte está disponível nos principais sites de codificação social listados abaixo. Os desenvolvedores são incentivados a baixar o código-fonte e estender a funcionalidade conforme suas próprias necessidades.

#### Código Fonte

Você pode obter o código-fonte mais recente de um dos seguintes locais

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco).
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/code/ci/master/tree/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/src).

#### Como configurar o código-fonte

Você precisa ter o seguinte instalado para abrir e estender o código-fonte

- Visual Studio 2010 ou superior.

Siga estas etapas simples para começar

1. Baixe/Clone o código-fonte.
1. Abra o Visual Studio 2010 e escolha **Arquivo** > **Abrir Projeto**.
1. Navegue até o código-fonte mais recente que você baixou e abra **Aspose.Import from PDF.sln**.