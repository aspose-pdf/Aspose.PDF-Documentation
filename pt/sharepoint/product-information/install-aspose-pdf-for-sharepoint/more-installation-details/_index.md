---
title: Mais detalhes de instalação
linktitle: Mais detalhes de instalação
type: docs
weight: 30
url: /pt/sharepoint/more-installation-details/
lastmod: "2020-12-16"
description: Mais informações sobre a instalação da API PDF SharePoint explicam como implantá-la, ativá-la e desativá-la em conjuntos de sites.
---

## Implantação

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint executa as seguintes ações durante a implantação:**
- Instale Aspose.PDF.SharePoint.dll no Global Assembly Cache e adicione a entrada SafeControl ao arquivo web.config.
- Instale o manifesto do recurso e outros arquivos necessários nos diretórios apropriados.
- Cadastre o recurso no banco de dados do SharePoint e disponibilize-o para ativação no escopo do recurso.

{{% /alert %}}

## Ativação

{{% alert color="primary" %}}

**Aspose.PDF para SharePoint é empacotado como um recurso de nível de site (conjunto de sites) e pode ser ativado e desativado em conjuntos de sites.**

{{% /alert %}}

{{% alert color="primary" %}}

Durante a ativação, o recurso faz algumas alterações no diretório virtual do aplicativo Web pai do conjunto de sites: Adicione a página de configurações de conversão ao arquivo de mapa do site. Copie os arquivos de recursos necessários para a pasta App_GlobalResources no diretório virtual.

{{% /alert %}}

