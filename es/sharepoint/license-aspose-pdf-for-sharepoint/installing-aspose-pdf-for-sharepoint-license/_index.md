---
title: Instalando la licencia de Aspose.PDF para SharePoint
linktitle: Instalando la licencia de Aspose.PDF para SharePoint
type: docs
weight: 10
url: /es/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2026-09-09"
description: Una vez que esté satisfecho con su evaluación, puede adquirir una licencia para la API PDF SharePoint y seguir las instrucciones de instalación para aplicarla.
---

{{% alert color="primary" %}}

Una vez que esté satisfecho con su evaluación, puede [purchase a license](https://purchase.aspose.com/buy). Antes de comprar, asegúrese de comprender y aceptar los términos de suscripción de la licencia.

{{% /alert %}}

{{% alert color="primary" %}}

La licencia se enviará por correo electrónico después de que se haya pagado el pedido. La licencia es un archivo .zip que contiene un paquete de solución de SharePoint normal.

Este archivo contiene:

- Aspose.PDF.SharePoint.License.wsp

Archivo de paquete de solución de SharePoint. La licencia de Aspose.PDF for SharePoint se empaqueta como una solución de SharePoint para facilitar la implementación/retiro en toda la granja de servidores.

- readme.txt

Instrucciones de instalación de la licencia. La instalación de la licencia se realiza desde la consola del servidor mediante stsadm.exe. Los pasos necesarios para instalar la licencia se presentan a continuación.

**Note:** Las rutas se omiten por claridad. Es posible que necesite agregar la ruta real a stsadm.exe y/o al archivo de solución al ejecutarlos.

1. Ejecute stsadm para agregar la solución al almacén de soluciones de SharePoint:

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. Implemente la solución en todos los servidores del clúster:

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. Ejecute trabajos administrativos del temporizador para completar el despliegue inmediatamente.

stsadm.exe -o execadmsvcjobs

**Note:** Recibirá una advertencia al ejecutar el paso de despliegue si el servicio de Administración de Windows SharePoint Services no está iniciado. Stsadm.exe depende de este servicio y del Servicio de Temporizador de Windows SharePoint para replicar los datos de la solución en toda la granja. Si estos servicios no se están ejecutando en su granja de servidores, es posible que necesite desplegar la licencia en cada servidor.

{{% /alert %}}
