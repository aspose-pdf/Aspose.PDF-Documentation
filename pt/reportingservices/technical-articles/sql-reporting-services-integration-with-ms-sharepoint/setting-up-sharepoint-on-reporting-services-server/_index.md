---
title: Configurando o SharePoint no servidor Reporting Services
linktitle: Configurando o SharePoint no servidor Reporting Services
type: docs
weight: 30
url: /pt/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Agora precisamos executar etapas semelhantes às que fizemos para o SharePoint WFE. A primeira coisa é passar pela instalação dos pré-requisitos do uisites e, quando isso terminar, iniciar a configuração do SharePoint.

{{% /alert %}}

Para a configuração, escolho Farm de Servidores e uma instalação completa para corresponder à minha SharePoint Box, pois não quero uma instalação standalone para o SharePoint.

## Configuração do SharePoint

{{% alert color="primary" %}}

**No Assistente de Configuração do SharePoint, queremos conectar a uma farm existente.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Image1:- Assistente de configuração do SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Em seguida, apontaremos para o banco de dados SharePoint_Config que nossa fazenda está usando. Se você não souber onde ele está, pode descobrir através do Central Admin em Configurações do Sistema -> Gerenciar Servidores nesta fazenda.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Image2:- Especificar configurações de banco de dados**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Image3:- Assistente de configuração do SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Uma vez que o assistente terminou, isso é tudo que precisamos fazer na caixa do Report Server por enquanto. Voltando para a URL do ReportServer, veremos outro erro, mas isso ocorre porque ainda não o configuramos através do Central Administrator.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Image4:- Erro do servidor de relatório**
{{% /alert %}}

