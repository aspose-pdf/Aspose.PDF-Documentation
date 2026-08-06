---
title: Desinstalando Aspose.PDF para licença do SharePoint
linktitle: Desinstalando Aspose.PDF para licença do SharePoint
type: docs
weight: 30
url: /pt/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Siga as etapas mencionadas neste artigo para desinstalar a licença da API do PDF SharePoint.
---

## Uninstallation Steps

{{% alert color="primary" %}}

Para desinstalar a licença Aspose.PDF para SharePoint, siga as etapas abaixo no console do servidor.

1. Retire a solução de licença do farm:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Execute administrative timer jobs to complete the retraction immediately:

  stsadm.exe -o execadmsvcjobs

3. Aguarde a conclusão da retração. Você pode usar Central

  Administração para verificar se a retirada foi concluída em Administração Central -> Operações -> Gerenciamento de Soluções

4. Remova a solução do armazenamento de soluções do SharePoint:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}

