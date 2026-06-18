---
title: Más detalles de instalación
linktitle: Más detalles de instalación
type: docs
weight: 30
url: /es/sharepoint/more-installation-details/
lastmod: "2026-06-18"
description: Más información sobre la instalación de PDF SharePoint API explica cómo desplegar, activar y desactivar en colecciones de sitios.
---

## **Despliegue**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint realiza las siguientes acciones durante el despliegue:**
- Instale Aspose.PDF.SharePoint.dll en la Caché de ensamblados global y agregue la entrada SafeControl al archivo web.config.
- Instale el manifiesto de la función y otros archivos necesarios en los directorios apropiados.
- Registre la característica en la base de datos de SharePoint y hágala disponible para la activación en el alcance de la característica.

{{% /alert %}}


## **Activación**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint se empaqueta como una característica a nivel de sitio (colección de sitios) y puede activarse y desactivarse en colecciones de sitios.**

{{% /alert %}}

{{% alert color="primary" %}}

Durante la activación, la característica realiza algunos cambios en el directorio virtual de la aplicación web principal de la colección de sitios: Añadir la página de configuración de conversión al archivo sitemap. Copiar los archivos de recursos necesarios a la carpeta App_GlobalResources en el directorio virtual.

{{% /alert %}}
