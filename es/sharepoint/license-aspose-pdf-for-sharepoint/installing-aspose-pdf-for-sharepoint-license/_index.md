---
title: Instalación de Aspose.PDF para licencia de SharePoint
linktitle: Instalación de Aspose.PDF para licencia de SharePoint
type: docs
weight: 10
url: /es/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Una vez que esté satisfecho con su evaluación, puede comprar una licencia para PDF SharePoint API y seguir las instrucciones de instalación para aplicarla.
---

{{% alert color="primary" %}}

Once you are happy with your evaluation, you can [purchase a license](https://purchase.aspose.com/buy). Before purchasing make sure you understand and agree to the license subscription terms.

{{% /alert %}}

{{% alert color="primary" %}}

La licencia se le enviará por correo electrónico una vez que se haya pagado el pedido. La licencia es un archivo .zip que contiene un paquete de solución SharePoint normal.

Este archivo contiene:

- Aspose.PDF.SharePoint.License.wsp

Archivo del paquete de solución de SharePoint. Aspose.PDF para la licencia de SharePoint está empaquetado como una solución de SharePoint para facilitar la implementación/retirada en toda la granja de servidores.

- Léame.txt

Instrucciones de instalación de licencia. La instalación de la licencia se realiza desde la consola del servidor a través de stsadm.exe. Los pasos necesarios para instalar la licencia se detallan a continuación.

**Nota:** Las rutas se omiten para mayor claridad. Es posible que deba agregar la ruta real a stsadm.exe y/o al archivo de solución al ejecutarlos.

1. Ejecute stsadm para agregar la solución al almacén de soluciones de SharePoint:

stsadm.exe -o addsolution -nombre de archivo Aspose.PDF.SharePoint.License.wsp

2. Implemente la solución en todos los servidores de la granja:

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. Ejecute trabajos del temporizador administrativo para completar la implementación de inmediato.

stsadm.exe -o execadmsvcjobs

**Note:** You will receive a warning when running deployment step if Windows SharePoint Services Administration service is not started. Stsadm.exe relies on this service and Windows SharePoint Timer Service to replicate solution data across the farm. If these services are not running on your server farm, you may need to deploy the license at each server.

{{% /alert %}}

