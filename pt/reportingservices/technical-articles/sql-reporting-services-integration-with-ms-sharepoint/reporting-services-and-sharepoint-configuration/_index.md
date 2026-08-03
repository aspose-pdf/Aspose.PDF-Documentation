---
title: Configuração do Reporting Services e do SharePoint
linktitle: Reporting Services and SharePoint configuration
type: docs
weight: 40
url: /reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Agora que o SharePoint está instalado e configurado no servidor RS e o RS está instalado e configurado por meio do Reporting Services Configuration Manager, podemos passar para a configuração no Central Admin. O RS 2008 R2 realmente simplificou esse processo. Costumávamos ter um processo de três etapas que você precisava executar para que isso funcionasse. Agora só temos um passo.

{{% /alert %}}

{{% alert color="primary" %}}

Queremos ir para o site do Administrador Central e depois para Configurações Gerais do Aplicativo. Na parte inferior, veremos Reporting Services.

![Configuration-step1](reporting-services-and-sharepoint-configuration_1.png)
**Imagem1**: - Caixa de diálogo de configuração do SharePoint

Selecione o link "Integração do Reporting Services". A tela a seguir será exibida.

![Configuration-step2](reporting-services-and-sharepoint-configuration_2.png)
**Imagem2**: - Especifique as credenciais de integração do Reporting Services

{{% /alert %}}

## URL do serviço web:

**Forneceremos a URL do Servidor de Relatórios que encontramos no Reporting Services Configuration Manager.**

## Modo de autenticação:

**Também selecionaremos um modo de autenticação. O link do MSDN a seguir explica detalhadamente o que são.
Visão geral de segurança do Reporting Services no modo integrado do SharePoint**

{{% alert color="primary" %}}

**Resumindo, se o seu site estiver usando autenticação de declarações, você sempre usará autenticação confiável, independentemente do que escolher aqui. Se quiser passar credenciais do Windows, você deverá escolher Autenticação do Windows. Para autenticação confiável, passaremos o token SPUser e não dependeremos da credencial do Windows. Você também desejará usar a autenticação confiável se tiver configurado seus sites no modo clássico para NTLM e o RS estiver configurado para NTLM. O Kerberos seria necessário para usar a autenticação do Windows e transmiti-la para sua fonte de dados.**

{{% /alert %}}

## Ativar recurso:

{{% alert color="primary" %}}

**Isso oferece a opção de ativar o Reporting Services em todos os conjuntos de sites ou você pode escolher em quais deseja ativá-lo. Na verdade, isso significa quais sites poderão usar o Reporting Services. Quando terminar, você deverá ver os seguintes resultados **

![Configuration-step3](reporting-services-and-sharepoint-configuration_3.png)

**Imagem3:**- Integração bem-sucedida do Reporting Services com o ambiente SharePoint
{{% /alert %}}

{{% alert color="primary" %}}

Voltando ao URL ReportServer, devemos ver algo semelhante ao seguinte

![Configuration-step4](reporting-services-and-sharepoint-configuration_4.png)

**Imagem4:**- Reporting Services foi conectado com sucesso ao ambiente SharePoint

**NOTA:** ***Se o seu site SharePoint estiver configurado para SSL, ele não aparecerá nesta lista. É um problema conhecido e não significa que haja um problema. Seus relatórios ainda devem funcionar.***
{{% /alert %}}

{{% alert color="primary" %}}

Agora que integramos ambos os produtos com sucesso, estamos prontos para usar o Reporting Services no SharePoint 2010. Assim como na versão anterior, temos um recurso (ativado quando configuramos a Integração do Reporting Services) no “Site Collection Feature”. Além disso, a instalação adicionou 3 tipos de conteúdo para adicionar ao nosso site. Na Imagem 7 podemos ver 2 deles tipos de conteúdo adicionados em uma biblioteca de documentos para criar um relatório personalizado usando o, como podemos ver na Imagem 5 abaixo.

![Configuration-step5](reporting-services-and-sharepoint-configuration_5.png)

**Imagem5:**- Construtor de Relatórios

O “Reporter Builder” é um controle ActiveX então precisamos baixá-lo através do servidor, como podemos ver na Imagem 6 abaixo.

![Configuration-step6](reporting-services-and-sharepoint-configuration_6.png)

**Imagem6:**- Baixe e instale o Report Builder
{{% /alert %}}

{{% alert color="primary" %}}

Assim que o processo de download for concluído, carregue o controle “Report Builder”. Agora estamos prontos para desenhar nosso primeiro relatório, conforme mostrado na Imagem7 abaixo.

![Configuration-step7](reporting-services-and-sharepoint-configuration_7.png)

**Imagem7:**- Report Builder – Novo assistente de geração de relatórios
{{% /alert %}}

{{% alert color="primary" %}}

Após criar nosso relatório poderíamos salvá-lo na biblioteca de documentos criada para colocar os relatórios em nosso SharePoint 2010. O outro tipo de conteúdo deve ser usado para criar conexão compartilhada como fonte de dados e salvá-los em uma biblioteca de documentos no SharePoint. Podemos criar uma biblioteca de documentos, adicionar este tipo de conteúdo e depois termos nossas conexões disponíveis para alterar a fonte de dados dos relatórios.

![Configuration-step8](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Integração bem-sucedida de Aspose.PDF para Reporting Services com MS SharePoint
{{% /alert %}}

