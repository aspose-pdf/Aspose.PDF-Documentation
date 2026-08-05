---
title: Cómo utilizar Aspose.PDF para demostraciones fuera de línea de JasperReports
linktitle: How to - use Aspose.PDF for JasperReports offline demos
type: docs
weight: 10
url: /es/jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
description: Explore demostraciones sin conexión de Aspose.PDF para JasperReports. Aprenda implementaciones y funciones prácticas de forma práctica.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF para JasperReports incluye una serie de proyectos de demostración para ayudarle a comenzar a exportar informes a formatos PDF desde su aplicación. Las demostraciones son demostraciones estándar de JasperReports que se han modificado para demostrar cómo utilizar nuevos exportadores.

{{% /alert %}}

## Ejecución de Aspose.PDF para demostraciones de JasperReports

Para ejecutar Aspose.PDF para demostraciones de JasperReports:

{{% alert color="primary" %}}

1. Descargue JasperReports desde <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.. Asegúrese de descargar todo el proyecto archivado con el código fuente y las demostraciones, no solo un único JAR.
2. Unpack the archived project to some location on your hard disk, for example C:\.
3. Copy all demo folders from the \demo folder in **Aspose.PDF.JasperReports.zip** to ```<InstallDir>```\jasperreports\demo\samples, where ```<InstallDir>``` is the location you have unpacked JasperReports to. This step is required because the demo build scripts rely on the JasperReports folder structure, otherwise you have to modify build scripts.
4. Copie el archivo **aspose.pdf.jasperreports.jar** de la carpeta \lib en **Aspose.PDF.JasperReports.zip** a ```<InstallDir>```\jasperreports\lib.
5. Descargue la herramienta ANT de <http://ant.apache.org/bindownload.cgi>.
6. Desempaquete la herramienta ANT y configure las variables de entorno como se describe en el manual de la herramienta.
7. Cambie el directorio actual a ```<InstallDir>```\demo\hsqldb y ejecute la siguiente línea de comando:
   servidor de ejecución de hormigas
8. Abra una nueva instancia del símbolo del sistema y cambie el directorio actual a uno de los demos de Aspose.PDF para JasperReports, por ejemplo ```<InstallDir>```\demo\samples\charts.ap.
9. Ejecute los siguientes comandos en la línea de comando:
10. ant javac: para compilar los archivos fuente Java de la aplicación de prueba.
11. compilación ant: para compilar el diseño del informe XML y producir el archivo .jasper
12. relleno de hormiga: para llenar el diseño del informe compilado con datos y producir el archivo .jrprint
13. Ejecute el siguiente comando en la línea de comando:
   ant pdf: para generar un archivo PDF a partir del informe de demostración.
14. Abra uno de los documentos resultantes para verlo, por ejemplo ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf en Adobe Reader u otra aplicación.

{{% /alert %}}

