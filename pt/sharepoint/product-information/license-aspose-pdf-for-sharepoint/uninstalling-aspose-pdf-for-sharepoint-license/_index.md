---
title: Desinstalando a Licença Aspose.Pdf para SharePoint
linktitle: Desinstalando a Licença Aspose.Pdf para SharePoint
type: docs
weight: 30
url: /pt/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2026-06-18"
description: Por favor, siga as etapas mencionadas neste artigo para desinstalar a Licença PDF SharePoint API.
---

## Etapas de Desinstalação

{{% alert color="primary" %}}

Para desinstalar a licença Aspose.PDF para SharePoint, por favor use as etapas abaixo no console do servidor.

1. Retire a solução de licença da farm:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Execute trabalhos de temporizador administrativos para concluir a retração imediatamente:

  stsadm.exe -o execadmsvcjobs

3. Aguarde a conclusão da retração. Você pode usar Central   

  Administração para verificar se a retração foi concluída em Administração Central -\u003E Operações -\u003E Gerenciamento de Soluções

4. Remova a solução do repositório de soluções do SharePoint:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}
