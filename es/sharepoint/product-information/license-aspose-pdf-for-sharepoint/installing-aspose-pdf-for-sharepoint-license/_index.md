---
title: Instalación de la Licencia de Aspose.Pdf para SharePoint
type: docs
weight: 10
url: es/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Una vez que esté satisfecho con su evaluación, puede comprar una licencia para la API de PDF SharePoint y seguir las instrucciones de instalación para aplicarla.
---

{{% alert color="primary" %}}

Una vez que esté satisfecho con su evaluación, puede [comprar una licencia](https://purchase.aspose.com/buy). Antes de comprar, asegúrese de entender y aceptar los términos de suscripción de la licencia.

{{% /alert %}}

{{% alert color="primary" %}}

La licencia se le enviará por correo electrónico después de que se haya pagado el pedido. La licencia es un archivo .zip que contiene un paquete de solución regular de SharePoint.
{{% /alert %}}

Este archivo contiene:

- Aspose.PDF.SharePoint.License.wsp

Archivo de paquete de solución de SharePoint. La Licencia de Aspose.PDF para SharePoint está empaquetada como una solución de SharePoint para facilitar el despliegue/retiro a través de la granja de servidores.

- readme.txt

Instrucciones de instalación de la licencia.
 La instalación de la licencia se realiza desde la consola del servidor a través de stsadm.exe. Los pasos necesarios para instalar la licencia se detallan a continuación.

**Nota:** Las rutas se omiten para mayor claridad. Es posible que necesites agregar la ruta real a stsadm.exe y/o al archivo de solución al ejecutarlos.

1. Ejecuta stsadm para agregar la solución al almacén de soluciones de SharePoint:

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. Despliega la solución en todos los servidores de la granja:

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. Ejecuta trabajos de temporizador administrativos para completar la implementación inmediatamente.

stsadm.exe -o execadmsvcjobs

**Nota:** Recibirás una advertencia al ejecutar el paso de implementación si el servicio de Administración de Servicios de Windows SharePoint no está iniciado. Stsadm.exe depende de este servicio y del Servicio de Temporizador de Windows SharePoint para replicar los datos de la solución en toda la granja. Si estos servicios no están en funcionamiento en tu granja de servidores, es posible que necesites implementar la licencia en cada servidor.