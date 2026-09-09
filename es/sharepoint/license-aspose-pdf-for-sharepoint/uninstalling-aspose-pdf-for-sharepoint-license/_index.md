---
title: Desinstalando la licencia de Aspose.PDF for SharePoint
linktitle: Desinstalando la licencia de Aspose.PDF for SharePoint
type: docs
weight: 30
url: /es/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2026-09-09"
description: Por favor, siga los pasos mencionados en este artículo para desinstalar la licencia PDF SharePoint API.
---

## Pasos de desinstalación

{{% alert color="primary" %}}

Para desinstalar la licencia de Aspose.PDF for SharePoint, por favor use los pasos a continuación desde la consola del servidor.

1. Retire la solución de licencia del farm:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Ejecute trabajos de temporizador administrativos para completar la retractación inmediatamente:

  stsadm.exe -o execadmsvcjobs

3. Espere a que la retractación se complete. Puede usar Central

  Administration para comprobar si la retractación se completó bajo Administración Central -> Operaciones -> Gestión de soluciones

4. Elimine la solución del almacén de soluciones de SharePoint:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}
