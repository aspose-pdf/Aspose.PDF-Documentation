---
title: Cómo - usar Aspose.Pdf para demostraciones offline de JasperReports
type: docs
weight: 10
url: /es/jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF para JasperReports incluye una serie de proyectos de demostración para ayudarte a comenzar a exportar informes a formatos PDF desde tu aplicación. Las demostraciones son demostraciones estándar de JasperReports que han sido modificadas para demostrar cómo utilizar nuevos exportadores.

{{% /alert %}}
### **Ejecutar demostraciones de Aspose.PDF para JasperReports**
Para ejecutar demostraciones de Aspose.PDF para JasperReports:

{{% alert color="primary" %}}

1. Descargue JasperReports desde <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. Asegúrese de descargar todo el proyecto archivado con el código fuente y las demostraciones, no solo un único JAR.
2. Desempaquete el proyecto archivado en alguna ubicación de su disco duro, por ejemplo C:\.
3. Copie todas las carpetas de demostración desde la carpeta \demo en **Aspose.PDF.JasperReports.zip** a ```<InstallDir>```\jasperreports\demo\samples, donde ```<InstallDir>``` es la ubicación donde ha descomprimido JasperReports. Este paso es necesario porque los scripts de construcción de demostración dependen de la estructura de carpetas de JasperReports, de lo contrario, debe modificar los scripts de construcción.
4. Copie el archivo **aspose.pdf.jasperreports.jar** de la carpeta \lib en **Aspose.PDF.JasperReports.zip** a ```<InstallDir>```\jasperreports\lib.
5. Descargue la herramienta ANT desde <http://ant.apache.org/bindownload.cgi>.
6. Descomprima la herramienta ANT y configure las variables de entorno como se describe en el manual de la herramienta.
7. Cambie el directorio actual a ```<InstallDir>```\demo\hsqldb y ejecute la siguiente línea de comandos:
   ant runServer
8. Abra una nueva instancia de símbolo del sistema y cambie el directorio actual a una de las demostraciones de Aspose.PDF para JasperReports, por ejemplo ```<InstallDir>```\demo\samples\charts.ap.
9. Ejecute los siguientes comandos en la línea de comandos:
10. ant javac – para compilar los archivos fuente de Java de la aplicación de prueba.  
11. ant compile – para compilar el diseño del informe XML y producir el archivo .jasper  
12. ant fill – para llenar el diseño del informe compilado con datos y producir el archivo .jrprint  
13. Ejecute el siguiente comando en la línea de comandos:  
    ant pdf – para producir un archivo PDF a partir del informe de demostración.  
14. Abra uno de los documentos resultantes para ver, por ejemplo, ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf en Adobe Reader u otra aplicación.  

{{% /alert %}}