---
title: Más detalles de instalación
type: docs
weight: 30
url: es/sharepoint/more-installation-details/
lastmod: "2020-12-16"
description: Más información sobre la instalación de PDF SharePoint API explica cómo desplegar, activar y desactivar en colecciones de sitios.
---

## **Despliegue**

{{% alert color="primary" %}}

**Aspose.PDF para SharePoint realiza las siguientes acciones durante el despliegue:**
- Instalar Aspose.PDF.SharePoint.dll en la Caché de Ensamblado Global y agregar una entrada SafeControl al archivo web.config.
- Instalar el manifiesto de características y otros archivos necesarios en los directorios apropiados.
- Registrar la característica en la base de datos de SharePoint y hacerla disponible para la activación en el ámbito de la característica.

{{% /alert %}}


## **Activación**

{{% alert color="primary" %}}

**Aspose.PDF para SharePoint está empaquetado como una característica a nivel de sitio (colección de sitios) y puede ser activado y desactivado en colecciones de sitios.**

{{% /alert %}}

{{% alert color="primary" %}}

Durante la activación, la característica realiza algunos cambios en el directorio virtual de la aplicación web principal de la colección de sitios: Agregar página de configuración de conversión al archivo del mapa del sitio.
 Copia los archivos de recursos necesarios en la carpeta App_GlobalResources en el directorio virtual.

{{% /alert %}}