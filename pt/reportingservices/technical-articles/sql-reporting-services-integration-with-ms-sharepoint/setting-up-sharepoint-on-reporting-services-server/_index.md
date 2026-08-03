---
title: Configurando o SharePoint no Reporting Services Server
linktitle: Setting up SharePoint on Reporting Services Server
type: docs
weight: 30
url: /reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Agora precisamos executar etapas semelhantes às que fizemos para o WFE do SharePoint. A primeira coisa é passar pela instalação dos pré-requisitos e, quando terminar, iniciar a configuração do SharePoint.

{{% /alert %}}

Para a configuração, escolho Server Farm e uma instalação completa para corresponder ao meu SharePoint Box, pois não quero uma instalação autônoma para o SharePoint.

## Configuração do SharePoint

{{% alert color="primary" %}}

**No Assistente de Configuração do SharePoint, queremos nos conectar a um farm existente.**

![Assistente de configuração do SharePoint](setting-up-sharepoint-on-reporting-services-server_1.png)

**Imagem1:- Assistente de configuração do SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Em seguida, apontaremos para o banco de dados SharePoint_Config que nosso farm está usando. Se você não sabe onde fica, você pode descobrir através do Central Admin em Configurações do Sistema -> Servidores Gerenciadores neste farm.**

![Banco de dados de configuração do SharePoint](setting-up-sharepoint-on-reporting-services-server_2.png)

**Imagem2:- Especifique as configurações do banco de dados**

![Assistente de configuração do SharePoint](setting-up-sharepoint-on-reporting-services-server_3.png)

**Imagem3:- Assistente de configuração do SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Depois que o assistente estiver concluído, isso é tudo que precisamos fazer na Caixa do Servidor de Relatórios por enquanto. Voltando à URL do ReportServer, veremos outro erro, mas é porque não o configuramos através do Administrador Central.**

![Erro de configuração do SharePoint](setting-up-sharepoint-on-reporting-services-server_4.png)

**Imagem4:- Reportar erro do servidor**
{{% /alert %}}
