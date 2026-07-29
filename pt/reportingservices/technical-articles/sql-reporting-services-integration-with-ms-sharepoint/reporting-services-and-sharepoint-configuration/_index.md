---
title: Configuração do Reporting Services e do SharePoint
linktitle: Configuração do Reporting Services e do SharePoint
type: docs
weight: 40
url: /pt/reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Agora que o SharePoint está instalado e configurado no servidor RS e o RS está configurado através do Reporting Services Configuration Manager, podemos passar para a configuração dentro do Central Admin. O RS 2008 R2 realmente simplificou esse processo. Antes, tínhamos um processo de 3 etapas que era necessário executar para que isso funcionasse. Agora temos apenas uma etapa.

{{% /alert %}}

{{% alert color="primary" %}}

Queremos ir ao site do Administrador Central e depois às Configurações Gerais de Aplicação. Na parte inferior, veremos Reporting Services.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**Image1**:- diálogo de configuração do SharePoint

Selecione o link "Reporting Services Integration". A tela a seguir será exibida.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)
**Image2**:- Especifique as credenciais de integração do Reporting Services

{{% /alert %}}

## URL do Serviço Web:

**Forneceremos a URL para o Report Server que encontramos no Reporting Services Configuration Manager.**

## Modo de Autenticação:

**Também selecionaremos um modo de autenticação. O link da MSDN a seguir detalha o que são esses modos.
Visão geral de segurança para Reporting Services em modo integrado do SharePoint**

{{% alert color="primary" %}}

**Em resumo, se seu site estiver usando Autenticação de Claims, você sempre usará Autenticação Confiável independentemente do que escolher aqui. Se quiser passar credenciais do Windows, deverá escolher Autenticação do Windows. Para Autenticação Confiável, passaremos o token SPUser e não dependeremos da credencial do Windows. Você também deverá usar Autenticação Confiável se configurou seus sites em Modo Clássico para NTLM e o RS está configurado para NTLM. Kerberos seria necessário para usar Autenticação do Windows e repassá‑la para sua fonte de dados.**

{{% /alert %}}

## Ativar recurso:

{{% alert color="primary" %}}

**Isso dá a você a opção de ativar o Reporting Services em todas as coleções de sites, ou você pode escolher em quais deseja ativá-lo. Isso realmente significa quais sites poderão usar o Reporting Services. Quando terminar, você deverá ver os seguintes resultados**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**Image3:**- Integração bem‑sucedida do Reporting Services com o ambiente SharePoint
{{% /alert %}}

{{% alert color="primary" %}}

Voltando ao URL do ReportServer, devemos ver algo semelhante ao seguinte

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**Image4:**- O Reporting Services está conectado com sucesso ao ambiente SharePoint

**NOTE:** ***Se o seu site SharePoint estiver configurado para SSL, ele não aparecerá nesta lista. É um problema conhecido e não significa que haja um problema. Seus relatórios ainda devem funcionar.***
{{% /alert %}}

{{% alert color="primary" %}}

Agora que integrámos com sucesso ambos os produtos, estamos prontos para usar Reporting Services no SharePoint 2010. Assim como na versão anterior, temos um recurso (ativado quando configuramos a Integração do Reporting Services) na “Site Collection Feature”. Também a instalação adicionou 3 tipos de conteúdo ao nosso site. Na Imagem 7 podemos ver 2 desses tipos de conteúdo adicionados a uma biblioteca de documentos para criar um relatório personalizado usando o, como podemos ver na Image5 abaixo.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)

**Image5:**- Report Builder

O “Reporter Builder” é um controle ActiveX, portanto precisamos baixá‑lo no servidor, como podemos ver na Imagem 6 abaixo.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**Image6:**- Baixe e instale o Report Builder
{{% /alert %}}

{{% alert color="primary" %}}

Depois que o processo de download for concluído, carregue o controle “Report Builder”. Agora estamos prontos para criar nosso primeiro relatório, como mostrado na Image7 abaixo.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- Report Builder – Assistente de criação de novo relatório
{{% /alert %}}

{{% alert color="primary" %}}

Após criar nosso relatório, podemos salvá‑lo na biblioteca de documentos criada para armazenar os relatórios no nosso SharePoint 2010. O outro tipo de conteúdo deve ser usado para criar conexões compartilhadas como fonte de dados e salvá‑las em uma biblioteca de documentos no SharePoint. Podemos criar uma biblioteca de documentos, adicionar esse tipo de conteúdo e, então, ter nossas conexões disponíveis para alterar a fonte de dados dos relatórios.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Integração bem-sucedida do Aspose.PDF for Reporting Services com o MS SharePoint
{{% /alert %}}

