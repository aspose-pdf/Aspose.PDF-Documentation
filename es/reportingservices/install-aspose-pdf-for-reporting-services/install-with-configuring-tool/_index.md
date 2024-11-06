---
title: Instalar con la Herramienta de Configuración
type: docs
weight: 30
url: es/reportingservices/install-with-configuring-tool/
lastmod: "2021-06-05"
---

La Herramienta de Configuración de Aspose.Pdf para Reporting Services puede ayudarte a configurar la extensión Aspose.Pdf para Reporting Services para cualquiera de las versiones de Report Server (RS) compatibles. Actualmente soporta RS2016, RS2017, RS2019, RS2022 y Power BI Report Server. La Herramienta de Configuración requiere .NET Framework 4.8.

Si deseas instalar la extensión y registrarla con el Report Server, selecciona el tipo de acción 'Register'. Para desregistrar y desinstalar la extensión, selecciona el tipo de acción 'Unregister'.

![todo:image_alt_text](install-with-configuring-tool_1.png)

**Los siguientes pasos describen cómo usarla en detalle:**

1. Ingresa o busca la ruta del archivo DLL para la extensión Aspose.Pdf para Reporting Services;
1. Selecciona el tipo de acción correspondiente: Register o Unregister;
1. Seleccione la pestaña correspondiente a la versión del Report Server que desea configurar. Asegúrese de haber seleccionado el archivo DLL que está destinado para su versión de RS. Si la versión solicitada del producto no está instalada en la máquina, la herramienta de configuración le informará con consejos. Si está configurando la extensión para la instancia nombrada RS2016 (no la predeterminada 'MSSQLSERVER'), por favor ingrese el nombre de la instancia personalizada y luego presione el botón 'Actualizar'.
1. Asegúrese de que las rutas y nombres de los archivos de configuración mostrados en los cuadros de texto inferiores sean correctos. Si no lo son, puede presionar el botón 'Actualizar' para intentar encontrar la instancia de RS nuevamente, o puede buscarlos manualmente.
1. Presione el botón 'Config'. La herramienta ahora intentará realizar la configuración solicitada y le informará si la configuración es exitosa o no.