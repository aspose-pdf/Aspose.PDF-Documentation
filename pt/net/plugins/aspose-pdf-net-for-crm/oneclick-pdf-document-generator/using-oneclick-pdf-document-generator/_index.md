---
title: Usando o Gerador de Documentos PDF OneClick
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/using-oneclick-pdf-document-generator/
description: Aprenda como usar o Gerador de Documentos PDF OneClick da Aspose.PDF no Microsoft Dynamics
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using OneClick PDF Document Generator",
    "alternativeHeadline": "Streamlined PDF Generation in Microsoft Dynamics",
    "abstract": "Desbloqueie a geração de documentos sem costura no Microsoft Dynamics com o Gerador de Documentos PDF OneClick da Aspose.PDF. Este recurso inovador permite que os usuários criem modelos de PDF personalizáveis diretamente dentro do CRM, gerem documentos de forma eficiente com um único clique e integrem facilmente botões OneClick em formulários para acesso simplificado. Aprimore suas capacidades de gerenciamento de dados e melhore a produtividade com esta poderosa ferramenta",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "313",
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
    "url": "/net/using-oneclick-pdf-document-generator/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-oneclick-pdf-document-generator/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Criar Modelo e Adicionar no CRM

- Abra o Word e crie um modelo.
- Insira campos MailMerge para dados provenientes do CRM.

![Inserir campos MailMerge](using-oneclick-pdf-document-generator_1.png)

- Certifique-se de que o nome do campo corresponda exatamente ao campo do CRM.
- Os modelos são específicos para uso com entidades individuais.

![Modelo de Demonstração](using-oneclick-pdf-document-generator_2.png)

- Uma vez que o modelo é criado, abra a entidade de Configuração do PDF OneClick no CRM e crie um novo registro.
- Dê o nome do modelo, selecione a entidade para a qual o modelo é definido e anexe o documento criado na anexação.

![Selecionar Modelo](using-oneclick-pdf-document-generator_3.png)

## Gerar Documento a partir do Botão da Faixa

- Abra o registro onde você deseja gerar o documento. (Certifique-se de que um modelo já esteja anexado na configuração para essa entidade)
- Clique no botão PDF OneClick na faixa.

![Clique no PDF OneClick](using-oneclick-pdf-document-generator_4.png)

- Na janela pop-up: selecione o modelo, nome do arquivo e ação e clique em Gerar.
- Verifique o arquivo baixado ou notas, com base na seleção.

## Configurar Botões OneClick e usá-los

- Para usar o botão OneClick diretamente do formulário, abra a personalização do formulário.
- Insira WebResource onde você deseja adicionar os botões OneClick.
- Selecione OpenButtonPage na WebResource e dê um nome.
- Configure os botões no campo de dados no seguinte exemplo.

![Propriedades da WebResource](using-oneclick-pdf-document-generator_5.png)

- Use uma linha separada para cada botão e use a seguinte sintaxe:
  - Sintaxe: Nome do Modelo |<Ação: Download/Nota>|Nome do Arquivo de Saída
  - Exemplo:Demo|Download|Meu Arquivo Baixado
- Salve e publique a personalização.
- O botão está disponível no formulário.

![O botão está disponível no formulário](using-oneclick-pdf-document-generator_6.png)