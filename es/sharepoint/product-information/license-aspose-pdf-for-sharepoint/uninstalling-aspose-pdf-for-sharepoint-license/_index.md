---
title: Desinstalando la licencia de Aspose.Pdf para SharePoint
linktitle: Desinstalando la licencia de Aspose.Pdf para SharePoint
type: docs
weight: 30
url: /es/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2026-06-18"
description: Por favor, siga los pasos mencionados en este artículo para desinstalar la licencia de PDF SharePoint API.
---

## Pasos de desinstalación

{{% alert color="primary" %}}

Para desinstalar la licencia de Aspose.PDF para SharePoint, por favor utilice los pasos a continuación desde la consola del servidor.

1. Retire la solución de licencia del farm:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Ejecute los trabajos de temporizador administrativos para completar la retractación inmediatamente:

  stsadm.exe -o execadmsvcjobs

3. Espere a que la retractación se complete. Puede usar Central   

  Administración para comprobar si la retractación se completó bajo la Administración Central -> Operaciones -> Gestión de soluciones

4. Elimine la solución del almacén de soluciones de SharePoint:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}
