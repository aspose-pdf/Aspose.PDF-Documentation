---
title: Desinstalando a Licença Aspose.Pdf for SharePoint
linktitle: Desinstalando a Licença Aspose.Pdf for SharePoint
type: docs
weight: 30
url: /pt/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2026-08-07"
description: Por favor, siga as etapas mencionadas neste artigo para desinstalar a Licença PDF SharePoint API.
---

## Etapas de Desinstalação

{{% alert color="primary" %}}

Para desinstalar a licença Aspose.PDF for SharePoint, por favor use as etapas abaixo no console do servidor.

1. Retire a solução de licença da farm:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Execute trabalhos administrativos de timer para concluir a retirada imediatamente:

  stsadm.exe -o execadmsvcjobs

3. Aguarde a conclusão da retirada. Você pode usar Central   

  Administration para verificar se a retirada foi concluída em Central Administration -> Operations -> Solution Management

4. Remova a solução do repositório de soluções do SharePoint:

  stsadm.exe -o deletarsolução -nome Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}
