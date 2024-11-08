---
title: Mais detalhes de instalação
type: docs
weight: 30
url: /pt/sharepoint/more-installation-details/
lastmod: "2020-12-16"
description: Mais informações sobre a instalação do PDF SharePoint API explicam como implantá-lo, ativá-lo e desativá-lo em coleções de sites.
---

## **Implantação**

{{% alert color="primary" %}}

**Aspose.PDF para SharePoint executa as seguintes ações durante a implantação:**
- Instalar Aspose.PDF.SharePoint.dll no Cache de Assemblies Global e adicionar entrada SafeControl ao arquivo web.config.
- Instalar manifesto de recurso e outros arquivos necessários nos diretórios apropriados.
- Registrar o recurso no banco de dados do SharePoint e torná-lo disponível para ativação no escopo do recurso.

{{% /alert %}}


## **Ativação**

{{% alert color="primary" %}}

**Aspose.PDF para SharePoint é empacotado como um recurso de nível de site (coleção de sites) e pode ser ativado e desativado em coleções de sites.**

{{% /alert %}}

{{% alert color="primary" %}}

Durante a ativação, o recurso faz algumas alterações no diretório virtual do aplicativo web pai da coleção de sites: Adiciona página de configurações de conversão ao arquivo de mapa do site.
 Copy necessary resource files to the App_GlobalResources folder in the virtual directory.

{{% /alert %}}