---
title: Más detalles de instalación
linktitle: Más detalles de instalación
type: docs
weight: 30
url: /es/sharepoint/more-installation-details/
lastmod: "2026-09-09"
description: Más información sobre la instalación de PDF SharePoint API explica cómo implementarlo, activarlo y desactivarlo en colecciones de sitios.
---

## Implementación

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint realiza las siguientes acciones durante el despliegue:**
- Instale Aspose.PDF.SharePoint.dll en la caché de ensamblados global y agregue la entrada SafeControl al archivo web.config.
- Instale el manifiesto de la característica y otros archivos necesarios en los directorios apropiados.
- Registre la característica en la base de datos de SharePoint y póngala a disposición para la activación en el ámbito de la característica.

{{% /alert %}}

## Activación

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint is packaged as a site (site collection) level feature and can be activated and deactivated on site collections.**

{{% /alert %}}

{{% alert color="primary" %}}

Durante la activación, la característica realiza algunos cambios en el directorio virtual de la aplicación web principal de la colección de sitios: Añadir la página de configuración de conversión al archivo sitemap. Copiar los archivos de recursos necesarios a la carpeta App_GlobalResources en el directorio virtual.

{{% /alert %}}
