---
title: Desinstalación de Aspose.PDF para licencia de SharePoint
linktitle: Desinstalación de Aspose.PDF para licencia de SharePoint
type: docs
weight: 30
url: /es/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Siga los pasos mencionados en este artículo para desinstalar la licencia API de PDF SharePoint.
---

## Pasos de desinstalación

{{% alert color="primary" %}}

Para desinstalar Aspose.PDF para la licencia de SharePoint, siga los pasos a continuación desde la consola del servidor.

1. Retirar la solución de licencia de la granja:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Ejecute trabajos del temporizador administrativo para completar la retractación inmediatamente:

  stsadm.exe -o execadmsvcjobs

3. Espere a que se complete la retracción. Puedes usar Central

  Administración para verificar si la retirada se completó en Administración central -> Operaciones -> Gestión de soluciones

4. Elimine la solución del almacén de soluciones de SharePoint:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}

