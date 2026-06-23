---
title: Mais detalhes da instalação
linktitle: Mais detalhes da instalação
type: docs
weight: 30
url: /pt/sharepoint/more-installation-details/
lastmod: "2026-06-18"
description: Mais informações sobre a instalação da API PDF SharePoint explicam como implantar, ativar e desativar a API nas coleções de sites.
---

## **Implantação**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint executa as seguintes ações durante a implantação:**
- Instale Aspose.PDF.SharePoint.dll no Global Assembly Cache e adicione a entrada SafeControl ao arquivo web.config.
- Instale o manifesto de recurso e outros arquivos necessários nos diretórios apropriados.
- Registre o recurso no banco de dados do SharePoint e torne-o disponível para a ativação no escopo do recurso.

{{% /alert %}}


## **Ativação**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint é empacotado como um recurso de nível de site (coleção de sites) e pode ser ativado e desativado em coleções de sites.**

{{% /alert %}}

{{% alert color="primary" %}}

Durante a ativação, o recurso faz algumas alterações no diretório virtual do aplicativo web pai da coleção de sites: Adicionar a página de configurações de conversão ao arquivo sitemap. Copiar os arquivos de recursos necessários para a pasta App_GlobalResources no diretório virtual.

{{% /alert %}}
