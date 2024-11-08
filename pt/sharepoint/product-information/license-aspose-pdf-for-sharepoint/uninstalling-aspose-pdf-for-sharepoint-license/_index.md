---
title: Desinstalando a Licença do Aspose.Pdf para SharePoint
type: docs
weight: 30
url: /pt/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Siga os passos mencionados neste artigo para desinstalar a Licença da API PDF SharePoint.
---

## Etapas de Desinstalação

{{% alert color="primary" %}}

Para desinstalar a licença do Aspose.PDF para SharePoint, use os passos abaixo a partir do console do servidor.

1. Retire a solução de licença da farm:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Execute trabalhos de timer administrativos para completar a retração imediatamente:

  stsadm.exe -o execadmsvcjobs

3. Aguarde a conclusão da retração. Você pode usar a Administração Central   

  para verificar se a retração foi concluída em Administração Central -> Operações -> Gerenciamento de Soluções

4. Remova a solução da loja de soluções do SharePoint:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}