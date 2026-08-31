---
title: Mais detalhes de instalação
linktitle: Mais detalhes de instalação
type: docs
weight: 30
url: /pt/sharepoint/more-installation-details/
lastmod: "2026-08-31"
description: Mais informações sobre a instalação da API PDF SharePoint explicam como implantar, ativar e desativar a mesma nas coleções de sites.
---

## Implantação

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint executa as seguintes ações durante a implantação:**
- Instale Aspose.PDF.SharePoint.dll no Global Assembly Cache e adicione a entrada SafeControl ao arquivo web.config.
- Instale o manifesto da funcionalidade e outros arquivos necessários nos diretórios apropriados.
- Registre a funcionalidade no banco de dados do SharePoint e torne-a disponível para ativação no escopo da funcionalidade.

{{% /alert %}}

## Ativação

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint é empacotado como uma funcionalidade de nível de site (coleção de sites) e pode ser ativado e desativado em coleções de sites.**

{{% /alert %}}

{{% alert color="primary" %}}

Durante a ativação, a funcionalidade faz algumas alterações no diretório virtual da aplicação web pai da coleção de sites: Adicionar a página de configurações de conversão ao arquivo de mapa do site. Copiar os arquivos de recursos necessários para a pasta App_GlobalResources no diretório virtual.

{{% /alert %}}
