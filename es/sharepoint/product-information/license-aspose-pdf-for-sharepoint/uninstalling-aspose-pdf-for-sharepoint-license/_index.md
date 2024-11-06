---
title: Desinstalar la Licencia de Aspose.Pdf para SharePoint
type: docs
weight: 30
url: es/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Por favor, siga los pasos mencionados en este artículo para desinstalar la licencia de la API de PDF para SharePoint.
---

## Pasos de Desinstalación

{{% alert color="primary" %}}

Para desinstalar la licencia de Aspose.PDF para SharePoint, por favor use los siguientes pasos desde la consola del servidor.

1. Retraer la solución de licencia de la granja:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Ejecutar trabajos de temporizador administrativos para completar la retracción inmediatamente:

  stsadm.exe -o execadmsvcjobs

3. Espere a que se complete la retracción. Puede usar la Administración Central para verificar si la retracción se completó bajo Administración Central -> Operaciones -> Gestión de Soluciones

4. Eliminar la solución de la tienda de soluciones de SharePoint:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}