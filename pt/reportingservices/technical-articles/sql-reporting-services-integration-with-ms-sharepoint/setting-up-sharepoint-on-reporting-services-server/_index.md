---
title: Configurando o SharePoint no Servidor de Serviços de Relatório
type: docs
weight: 30
url: pt/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Agora precisamos executar etapas semelhantes às que fizemos para o WFE do SharePoint. A primeira coisa é passar pela instalação dos Pré-requisitos e, uma vez concluída, iniciar a configuração do SharePoint.

{{% /alert %}}

Para a configuração, escolho Server Farm e uma instalação completa para corresponder à minha caixa do SharePoint, pois não quero uma instalação autônoma para o SharePoint.

## Configuração do SharePoint

{{% alert color="primary" %}}

**No Assistente de Configuração do SharePoint, queremos nos conectar a uma farm existente.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Imagem1:- Assistente de configuração do SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Em seguida, apontaremos para o banco de dados SharePoint_Config que nossa farm está usando. 

**Se você não sabe onde está, pode descobrir através do Central Admin em Configurações do Sistema -> Gerenciar Servidores nesta fazenda.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Imagem2:- Especificar configurações de configuração do banco de dados**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Imagem3:- Assistente de configuração do SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Uma vez que o assistente esteja concluído, isso é tudo o que precisamos fazer na Caixa do Servidor de Relatórios por enquanto. Voltando para a URL do ReportServer, veremos outro erro, mas isso é porque não o configuramos através do Administrador Central.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Imagem4:- Erro do servidor de relatórios**
{{% /alert %}}