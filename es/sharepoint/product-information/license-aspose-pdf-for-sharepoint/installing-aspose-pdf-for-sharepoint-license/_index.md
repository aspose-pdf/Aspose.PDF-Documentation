---
title: Instalando la licencia de Aspose.Pdf para SharePoint
linktitle: Instalando la licencia de Aspose.Pdf para SharePoint
type: docs
weight: 10
url: /es/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2026-06-18"
description: Una vez que estés satisfecho con tu evaluación, puedes comprar una licencia para PDF SharePoint API y seguir las instrucciones de instalación para aplicarla.
---

{{% alert color="primary" %}}

Una vez que estés satisfecho con tu evaluación, puedes [comprar una licencia](https://purchase.aspose.com/buy). Antes de comprar, asegúrate de comprender y aceptar los términos de suscripción de la licencia.

{{% /alert %}}

{{% alert color="primary" %}}

La licencia se enviará por correo electrónico después de que se haya pagado el pedido. La licencia es un archivo .zip que contiene un paquete de solución regular de SharePoint.

Este archivo contiene:

- Aspose.PDF.SharePoint.License.wsp

Archivo de paquete de solución de SharePoint. Aspose.PDF for SharePoint License se empaqueta como una solución de SharePoint para facilitar el despliegue/retiro en toda la granja de servidores.

- readme.txt

Instrucciones de instalación de la licencia. La instalación de la licencia se realiza desde la consola del servidor mediante stsadm.exe. Los pasos necesarios para instalar la licencia se indican a continuación.

**Nota:** Las rutas se omiten por claridad. Es posible que necesite agregar la ruta real a stsadm.exe y/o al archivo de solución al ejecutarlos.

1. Ejecute stsadm para agregar la solución al almacén de soluciones de SharePoint:

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. Despliegue la solución en todos los servidores de la granja:

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. Ejecute los trabajos temporizadores administrativos para completar el despliegue inmediatamente.

stsadm.exe -o execadmsvcjobs

**Nota:** Recibirás una advertencia al ejecutar el paso de implementación si el servicio Windows SharePoint Services Administration no está iniciado. Stsadm.exe depende de este servicio y del Windows SharePoint Timer Service para replicar los datos de la solución en toda la granja. Si estos servicios no están ejecutándose en tu granja de servidores, es posible que necesites desplegar la licencia en cada servidor.


{{% /alert %}}
