---
title: Más detalles de instalación
linktitle: Más detalles de instalación
type: docs
weight: 30
url: /es/sharepoint/more-installation-details/
lastmod: "2020-12-16"
description: Más información sobre la instalación de PDF SharePoint API explica cómo implementarla, activarla y desactivarla en las colecciones de sitios.
---

## Despliegue

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint realiza las siguientes acciones durante la implementación:**

- Instale Aspose.PDF.SharePoint.dll en la caché de ensamblados global y agregue la entrada SafeControl al archivo web.config.
- Instale el manifiesto de funciones y otros archivos necesarios en los directorios apropiados.
- Registre la función en la base de datos de SharePoint y póngala a disposición para la activación en el alcance de la función.

{{% /alert %}}

## Activación

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint está empaquetado como una característica a nivel de sitio (colección de sitios) y se puede activar y desactivar en colecciones de sitios.**

{{% /alert %}}

{{% alert color="primary" %}}

Durante la activación, la función realiza algunos cambios en el directorio virtual de la aplicación web principal de la colección de sitios: Agregar la página de configuración de conversión al archivo de mapa del sitio. Copie los archivos de recursos necesarios a la carpeta App_GlobalResources en el directorio virtual.

{{% /alert %}}

